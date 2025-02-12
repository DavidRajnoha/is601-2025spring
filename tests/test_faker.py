"""Testing that the faker module is working as expected."""
from faker import Faker


def test_faker_basic():
    faker = Faker()
    name = faker.name()
    assert name, "Name should not be empty"
    assert isinstance(name, str), "Name should be a string"


def test_fake_email():
    faker = Faker()
    email = faker.email()
    assert email, "Email should not be empty"
    assert isinstance(email, str), "Email should be a string"
    assert "@" in email, "Email should contain '@'"

def test_faker_locale():
    faker = Faker('cs_CZ')
    female_name = faker.name_female()
    assert female_name, "Name should not be empty"
    assert isinstance(female_name, str), "Name should be a string"
    assert female_name[-1] == "á", "Female czech name should end with 'á'"