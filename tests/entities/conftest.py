import pytest

from src.users.entity import User


@pytest.fixture
def dummy_user():
    return User(user_id=1, telegram_id=12345, name="Test User", tournaments=[], bets=[])
