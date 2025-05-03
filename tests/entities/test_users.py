from src.users.entity import User


def test_create_user_with_name():
    user = User(
        user_id=1,
        telegram_id=123456789,
        name="John Doe",
    )

    assert user.user_id == 1, f"{user.user_id=}"
    assert user.telegram_id == 123456789, f"{user.telegram_id=}"
    assert user.name == "John Doe", f"{user.name=}"


def test_create_user_without_name():
    user = User(
        user_id=2,
        telegram_id=987654321,
        name=None,
    )

    assert user.name is None, f"{user.name=}"
    assert user.telegram_id == 987654321, f"{user.telegram_id=}"
