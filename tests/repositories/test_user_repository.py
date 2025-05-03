import pytest

from src.bets.entity import (
    Bet,
    BetResult,
)
from src.tournaments.entity import Tournament
from src.users.entity import User


def make_user(user_id: int, telegram_id: int, name: str = "Test") -> User:
    return User(user_id=user_id, telegram_id=telegram_id, name=name)


def make_tournament(tournament_id: int, user_id: int) -> Tournament:
    return Tournament.from_bets(
        tournament_id=tournament_id,
        title="Test Tournament",
        bank=1000,
        user_id=user_id,
        bets=[],
    )


def make_bet(bet_id: int, user_id: int, result: BetResult = BetResult.WIN) -> Bet:
    return Bet.from_result(
        bet_id=bet_id,
        user_id=user_id,
        tournament_id=None,
        amount=100,
        odds=2.0,
        result=result,
    )


@pytest.mark.asyncio
async def test_user_repo_add_and_get_user_by_id_and_telegram(user_repo):
    user = make_user(1, 101)

    await user_repo.add(user)

    assert await user_repo.get_by_id(1) == user, f"{user_repo.get_by_id(1)=}"
    assert await user_repo.get_by_telegram_id(101) == user, f"{user_repo.get_by_telegram_id(101)=}"


@pytest.mark.asyncio
async def test_user_repo_get_tournaments_for_user(user_repo):
    user = make_user(2, 202)
    await user_repo.add(user)

    tournament = make_tournament(10, user_id=2)
    await user_repo.add_tournament_for_user(2, tournament)

    tournaments = await user_repo.get_tournaments(2)
    assert len(tournaments) == 1, f"{len(tournaments)=}"
    assert tournaments[0] == tournament, f"{tournaments[0]=}"


@pytest.mark.asyncio
async def test_user_repo_get_bets_for_user(user_repo):
    user = make_user(3, 303)
    await user_repo.add(user)

    bet = make_bet(20, user_id=3)
    await user_repo.add_bet_for_user(3, bet)

    bets = await user_repo.get_bets(3)
    assert len(bets) == 1, f"{len(bets)=}"
    assert bets[0] == bet, f"{bets[0]=}"


@pytest.mark.asyncio
async def test_user_repo_get_empty_tournaments_and_bets_for_new_user(user_repo):
    user = make_user(4, 404)
    await user_repo.add(user)

    assert await user_repo.get_tournaments(4) == [], f"{await user_repo.get_tournaments(4)=}"
    assert await user_repo.get_bets(4) == [], f"{await user_repo.get_bets(4)=}"


@pytest.mark.asyncio
async def test_user_repo_get_nonexistent_user_returns_none(user_repo):
    assert await user_repo.get_by_id(999) is None, f"{await user_repo.get_by_id(999)=}"
    assert await user_repo.get_by_telegram_id(9999) is None, f"{await user_repo.get_by_telegram_id(9999)=}"
