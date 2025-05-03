import pytest


@pytest.mark.asyncio
async def test_bet_repo_add_and_get_bet(bet_repo, dummy_bet):
    await bet_repo.add(dummy_bet)
    fetched = await bet_repo.get_bet(dummy_bet.bet_id)
    assert fetched == dummy_bet, f"{fetched=}"
    assert fetched.payout == 200, f"{fetched.payout=}"


@pytest.mark.asyncio
async def test_bet_repo_get_list_bets_by_user_id(bet_repo, dummy_bet):
    await bet_repo.add(dummy_bet)
    bets = await bet_repo.get_list_bets_by_user_id(dummy_bet.user.user_id)
    assert len(bets) == 1, f"{len(bets)=}"
    assert bets[0].bet_id == dummy_bet.bet_id, f"{bets[0].bet_id=}"


@pytest.mark.asyncio
async def test_bet_repo_update_bet(bet_repo, dummy_bet):
    await bet_repo.add(dummy_bet)
    updated = await bet_repo.update_bet(dummy_bet.bet_id, {"amount": 150, "odds": 1.5, "payout": 225})
    assert updated.amount == 150, f"{updated.amount=}"
    assert updated.odds == 1.5, f"{updated.odds=}"
    assert updated.payout == 225, f"{updated.payout=}"


@pytest.mark.asyncio
async def test_bet_repo_delete_bet(bet_repo, dummy_bet):
    await bet_repo.add(dummy_bet)
    deleted = await bet_repo.delete(dummy_bet.bet_id)
    assert deleted == dummy_bet, f"{deleted=}"
    with pytest.raises(KeyError):
        await bet_repo.get_bet(dummy_bet.bet_id)
