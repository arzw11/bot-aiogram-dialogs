from typing import (
    Dict,
    List,
    Optional,
)

import pytest

from src.bets.entity import (
    Bet,
    BetResult,
)
from src.tournaments.entity import Tournament
from src.tournaments.repository import BaseTournamentRepository
from src.users.entity import User
from src.users.repository import UserBaseRepository


class FakeUserRepository(UserBaseRepository):
    def __init__(self):
        self._users: Dict[int, User] = {}

    async def add(self, user: User):
        self._users[user.telegram_id] = user

    async def get(self, telegram_id: int) -> Optional[User]:
        return self._users.get(telegram_id)

    async def update(self, telegram_id: int, data: dict) -> User:
        user = self._users[telegram_id]
        updated_user = User(
            user_id=user.user_id,
            telegram_id=user.telegram_id,
            name=data.get("name", user.name),
            tournaments=data.get("tournaments", user.tournaments),
            bets=data.get("bets", user.bets),
        )
        self._users[telegram_id] = updated_user

        return updated_user

    async def delete(self, telegram_id: int) -> Optional[User]:
        return self._users.pop(telegram_id)


class FakeBetRepository:
    def __init__(self):
        self._bets: Dict[int, Bet] = {}

    async def add(self, bet: Bet):
        self._bets[bet.bet_id] = bet

    async def get_bet(self, bet_id: int) -> Bet:
        return self._bets[bet_id]

    async def get_list_bets_by_user_id(self, user_id: int) -> List[Bet]:
        return [b for b in self._bets.values() if b.user.user_id == user_id]

    async def update_bet(self, bet_id: int, data: dict) -> Optional[Bet]:
        bet = self._bets[bet_id]
        updated = Bet(
            bet_id=bet.bet_id,
            user=bet.user,
            tournament=data.get("tournament", bet.tournament),
            amount=data.get("amount", bet.amount),
            odds=data.get("odds", bet.odds),
            result=data.get("result", bet.result),
            payout=data.get("payout", bet.payout),
        )
        self._bets[bet_id] = updated
        return updated

    async def delete(self, bet_id: int) -> Optional[Bet]:
        return self._bets.pop(bet_id)


class FakeTournamentRepository(BaseTournamentRepository):
    def __init__(self):
        self._tournaments: Dict[int, Tournament] = {}

    async def add(self, tournament: Tournament):
        self._tournaments[tournament.tournament_id] = tournament

    async def get_tournament(self, tournament_id: int) -> Tournament:
        return self._tournaments[tournament_id]

    async def get_list_tournaments_by_user(self, user_id: int) -> List[Tournament]:
        return [t for t in self._tournaments.values() if t.user.user_id == user_id]

    async def update_tournament(self, tournament_id: int, data: dict) -> Optional[Tournament]:
        tournament = self._tournaments[tournament_id]
        updated_tournament = Tournament.from_bets(
            tournament_id=tournament.tournament_id,
            title=data.get("title", tournament.title),
            bank=data.get("bank", tournament.bank),
            user=tournament.user,
            bets=data.get("bets", tournament.bets),
        )
        self._tournaments[tournament_id] = updated_tournament
        return updated_tournament

    async def delete_tournament(self, tournament_id: int) -> Optional[Tournament]:
        return self._tournaments.pop(tournament_id)


@pytest.fixture
def dummy_user():
    return User(
        user_id=1,
        telegram_id=12345,
        name="Test User",
        tournaments=[],
        bets=[],
    )


@pytest.fixture
def dummy_bet(dummy_user):
    return Bet.from_result(
        bet_id=1,
        user=dummy_user,
        tournament=None,
        amount=100,
        odds=2.0,
        result=BetResult.WIN,
    )


@pytest.fixture
def dummy_tournament(dummy_user, dummy_bet):
    return Tournament.from_bets(
        tournament_id=1,
        title="Test Tournament",
        bank=1000,
        user=dummy_user,
        bets=[dummy_bet],
    )


@pytest.fixture
def user_repo():
    return FakeUserRepository()


@pytest.fixture
def bet_repo():
    return FakeBetRepository()


@pytest.fixture
def tournament_repo():
    return FakeTournamentRepository()
