import pytest


@pytest.mark.asyncio
async def test_bet_repo_add_and_get_bet_by_id(bet_repo, bets):
    test_bet = bets[0]
    await bet_repo.add(
        bet=test_bet,
    )
    bet = await bet_repo.get_by_id(bet_id=test_bet.bet_id)

    assert len(bet_repo._bets) == 1, f"{len(bet_repo._bets)=}"
    assert bet == test_bet, f"{bet=}"
    assert bet.user_id == test_bet.user_id, f"{bet.user_id=}"
    assert bet.payout == test_bet.payout, f"{bet.payout=}"


@pytest.mark.asyncio
async def test_bet_repo_get_all_by_user_id(bet_repo, bets):
    for bet in bets:
        await bet_repo.add(bet=bet)

    bets = await bet_repo.get_all_by_user_id(user_id=1)
    sum_payouts = sum(bet.payout for bet in bets)

    assert len(bet_repo._bets) == 3, f"{len(bet_repo._bets)=}"
    assert type(bets) is list, f"{type(bets)=}"
    assert len(bets) == 2, f"{len(bets)=}"
    assert sum_payouts == 1500, f"{sum_payouts=}"


@pytest.mark.asyncio
async def test_bet_repo_get_all_by_tournament_id(bet_repo, bets):
    for bet in bets:
        await bet_repo.add(bet=bet)

    bets = await bet_repo.get_all_by_tournament_id(tournament_id=2)

    assert len(bet_repo._bets) == 3, f"{len(bet_repo._bets)=}"
    assert len(bets) == 2, f"{len(bets)=}"
    assert bets[0].tournament_id == 2, f"{bets[0].tournament_id=}"


@pytest.mark.asyncio
async def test_bet_repo_update(bet_repo, bets):
    bet1 = bets[0]
    bet2 = bets[1]

    await bet_repo.add(bet=bet1)
    updated_bet = await bet_repo.update(bet=bet2)

    assert updated_bet, f"{updated_bet=}"


@pytest.mark.asyncio
async def test_bet_repo_delete(bet_repo, bets):
    for bet in bets:
        await bet_repo.add(bet=bet)

    assert len(bet_repo._bets) == 3, f"{len(bet_repo._bets)=}"

    deleted_bet1 = await bet_repo.delete(bet_id=1)
    deleted_bet2 = await bet_repo.delete(bet_id=100)

    assert len(bet_repo._bets) == 2, f"{len(bet_repo._bets)=}"
    assert deleted_bet1 != deleted_bet2, f"{deleted_bet1=}"
    assert deleted_bet1, f"{deleted_bet1=}"
    assert not deleted_bet2, f"{deleted_bet2=}"
