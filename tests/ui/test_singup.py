import pytest
from src.user import User


@pytest.fixture
def specific_sign_up_user_fixture():
    yield 42


def test_signup_initial(specific_sign_up_user_fixture):
    assert specific_sign_up_user_fixture == 42


def test_signup_final_negative(user_fixture):
    assert user_fixture.get('name') == 'aaaaaautomation_test_removein_30_days_non_existing_user'


def test_signup_final_positive(user_fixture):
    assert user_fixture.get('name') == User.username
