import pytest


@pytest.mark.asyncio
async def test_user_repo_add_and_get_user(user_repo, dummy_user):
    await user_repo.add(dummy_user)
    user = await user_repo.get(dummy_user.telegram_id)

    assert user.telegram_id == dummy_user.telegram_id, f"{user.telegram_id=}"
    assert user.name == dummy_user.name, f"{user.name}"


@pytest.mark.asyncio
async def test_user_repo_update_user_name(user_repo, dummy_user):
    await user_repo.add(dummy_user)
    updated = await user_repo.update(dummy_user.telegram_id, {"name": "Updated Name"})

    assert updated.name == "Updated Name", f"{updated.name=}"
    assert updated.telegram_id == dummy_user.telegram_id, f"{updated.telegram_id=}"


@pytest.mark.asyncio
async def test_user_repo_delete_user(user_repo, dummy_user):
    await user_repo.add(dummy_user)

    deleted = await user_repo.delete(dummy_user.telegram_id)
    assert deleted.telegram_id == dummy_user.telegram_id, f"{deleted.telegram_id=}"

    with pytest.raises(KeyError):
        await user_repo.delete(dummy_user.telegram_id)
