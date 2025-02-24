"""
Test the CommandHandler class.
"""
# pylint: disable=protected-access
# Used for testing purposes only.
from calculator.command.command_handler import CommandHandler


def test_register_command(mock_command):
    """Test that a command is correctly registered."""
    handler = CommandHandler()
    handler._register("test", mock_command)

    assert "test" in handler._commands
    assert handler._commands["test"] is mock_command


def test_execute_registered_command(mock_command):
    """Test that a registered command executes properly."""
    handler = CommandHandler()
    handler._register("test", mock_command)

    handler.handle("test")
    assert mock_command.executed is True


def test_execute_unregistered_command(capfd):
    """Test that handling an unregistered command prints an error."""
    handler = CommandHandler()

    handler.handle("nonexistent")

    captured = capfd.readouterr()
    assert 'Command "nonexistent" not found' in captured.out


def test_dynamic_command_discovery(mock_command_package, mock_greet_class, mock_exit_class):
    """
    Test that the CommandHandler dynamically discovers and registers commands
    using the mocked package fixture.
    """
    handler = CommandHandler()
    handler.load_commands(mock_command_package)  # Load commands dynamically

    # Ensure the mocked commands were registered
    assert "greet" in handler._commands
    assert "exit" in handler._commands

    # Ensure they are instances of the mocked command classes
    assert isinstance(handler._commands["greet"], mock_greet_class)
    assert isinstance(handler._commands["exit"], mock_exit_class)
