"""Integration tests for environment variable loading in the App class."""
import os
import pytest
from calculator.app import App


@pytest.fixture(scope="function")
def clean_environment():
    """Fixture that preserves and restores environment variables."""
    # Store original environment
    original_environ = os.environ.copy()

    # Clear variables that might interfere with testing
    keys_to_clear = []
    for key in os.environ:  # Iterate directly over dictionary
        if key.startswith('CALCULATOR_') or key in ['LOG_LEVEL', 'APP_ENV']:
            keys_to_clear.append(key)

    for key in keys_to_clear:
        if key in os.environ:
            del os.environ[key]

    # Let the test run
    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_environ)


def read_env_file(file_path='.env'):
    """Helper function to read variables from a .env file."""
    env_vars = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, value = line.split('=', 1)
                env_vars[key.strip()] = value.strip().strip("'").strip('"')
    return env_vars


def find_dotenv_file():
    """Find the .env file by looking in common locations."""
    # Try the current directory first
    if os.path.exists('.env'):
        return '.env'

    # Try the project root (assuming tests are in a subdirectory)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    dotenv_path = os.path.join(project_root, '.env')
    if os.path.exists(dotenv_path):
        return dotenv_path

    # If we're running from a deeper directory structure
    parent_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    dotenv_path = os.path.join(parent_root, '.env')
    if os.path.exists(dotenv_path):
        return dotenv_path

    return None


@pytest.mark.usefixtures("clean_environment")
def test_env_vars_loaded_from_file():
    """Test that environment variables from .env file are loaded correctly."""
    # Skip if .env doesn't exist
    dotenv_path = find_dotenv_file()
    if dotenv_path is None:
        pytest.skip(".env file not found")

    # Read expected variables from .env file directly
    expected_env_vars = read_env_file(dotenv_path)
    assert len(expected_env_vars) > 0, "The .env file should contain at least one variable"

    # Before initializing App, environment variables should NOT be present
    for key, value in expected_env_vars.items():  # Use .items() for iteration
        assert key not in os.environ or os.environ[key] != value, \
            f"Environment variable '{key}' was already set before App initialization"

    # Initialize the app, which should load environment variables
    App()

    # After initializing App, environment variables SHOULD be present
    for key, expected_value in expected_env_vars.items():
        actual_value = os.environ.get(key)
        assert actual_value is not None, f"Environment variable '{key}' was not loaded"
        assert actual_value == expected_value, f"Environment variable '{key}' has incorrect value"


@pytest.mark.usefixtures("clean_environment")
def test_custom_env_var_processing():
    """Test that App correctly processes specific environment variables."""
    # Skip if .env doesn't exist
    dotenv_path = find_dotenv_file()
    if dotenv_path is None:
        pytest.skip(".env file not found")

    # Read variables from .env to see what we can test
    env_vars = read_env_file(dotenv_path)
    if len(env_vars) == 0:
        pytest.skip("No environment variables found in .env file")

    # Pick a sample key to verify (customize this based on your app's environment variables)
    sample_keys = [key for key in env_vars  # Iterate directly over dictionary
                  if key.startswith('CALCULATOR_') or key in ['APP_ENV']]

    if not sample_keys:
        pytest.skip("No relevant environment variables found in .env file")

    # Initialize the app
    App()

    # Verify that the environment variables are accessible
    for key in sample_keys:
        assert os.environ.get(key) == env_vars[key], \
            f"Environment variable '{key}' was not correctly loaded"
