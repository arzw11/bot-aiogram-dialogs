from typing import (
    Dict,
    List,
    Optional,
)

import pytest

from src.domain.entities.bets import (
    Bet,
    BetResult,
)
from src.infra.repositories.bets.base import BaseBetRepository
from src.domain.entities.tournaments import Tournament
from src.infra.repositories.tournaments.base import BaseTournamentRepository
from src.domain.entities.users import User
from src.infra.repositories.users.base import BaseUserRepository


class FakeBetRepository(BaseBetRepository):
    def __init__(self):
        self._bets: Dict[int, Bet] = {}

    async def add(self, bet: Bet):
        self._bets[bet.bet_id] = bet

    async def get_by_id(self, bet_id: int) -> Optional[Bet]:
        return self._bets.get(bet_id)

    async def get_all_by_user_id(self, user_id: int) -> List[Bet]:
        return [bet for bet in self._bets.values() if bet.user_id == user_id]

    async def get_all_by_tournament_id(self, tournament_id: int) -> List[Bet]:
        return [bet for bet in self._bets.values() if bet.tournament_id and bet.tournament_id == tournament_id]

    async def update(self, bet: Bet) -> bool:
        self._bets[bet.bet_id] = bet
        return True

    async def delete(self, bet_id: int) -> bool:
        if self._bets.get(bet_id):
            del self._bets[bet_id]
            return True

        return False


class FakeTournamentRepository(BaseTournamentRepository):
    def __init__(self):
        self._tournaments: Dict[int, Tournament] = {}

    async def add(self, tournament: Tournament) -> None:
        self._tournaments[tournament.tournament_id] = tournament

    async def get_by_id(self, tournament_id: int) -> Optional[Tournament]:
        return self._tournaments.get(tournament_id)

    async def update(self, tournament: Tournament) -> Tournament:
        self._tournaments[tournament.tournament_id] = tournament
        return tournament

    async def delete(self, tournament_id: int) -> bool:
        if self._tournaments.get(tournament_id):
            del self._tournaments[tournament_id]
            return True

        return False


class FakeUserRepository(BaseUserRepository):
    def __init__(self):
        self._by_id: Dict[int, User] = {}
        self._by_telegram: Dict[int, User] = {}
        self._tournaments_by_user: Dict[int, List[Tournament]] = {}
        self._bets_by_user: Dict[int, List[Bet]] = {}

    async def add(self, user: User) -> None:
        self._by_id[user.user_id] = user
        self._by_telegram[user.telegram_id] = user
        self._tournaments_by_user[user.user_id] = []
        self._bets_by_user[user.user_id] = []

    async def get_by_id(self, user_id: int) -> Optional[User]:
        return self._by_id.get(user_id)

    async def get_by_telegram_id(self, telegram_id: int) -> Optional[User]:
        return self._by_telegram.get(telegram_id)

    async def get_tournaments(self, user_id: int) -> List[Tournament]:
        return self._tournaments_by_user.get(user_id, [])

    async def get_bets(self, user_id: int) -> List[Bet]:
        return self._bets_by_user.get(user_id, [])

    async def add_tournament_for_user(self, user_id: int, tournament: Tournament):
        self._tournaments_by_user.setdefault(user_id, []).append(tournament)

    async def add_bet_for_user(self, user_id: int, bet: Bet):
        self._bets_by_user.setdefault(user_id, []).append(bet)


@pytest.fixture
def bet_repo():
    return FakeBetRepository()


@pytest.fixture
def tournament_repo():
    return FakeTournamentRepository()


@pytest.fixture
def user_repo():
    return FakeUserRepository()


@pytest.fixture
def bets():
    return [
        Bet.from_result(
            bet_id=1,
            user_id=1,
            tournament_id=2,
            amount=1000,
            odds=1.5,
            result=BetResult.WIN,
        ),
        Bet.from_result(
            bet_id=2,
            user_id=1,
            tournament_id=2,
            amount=1500,
            odds=1.5,
            result=BetResult.LOSS,
        ),
        Bet.from_result(
            bet_id=4,
            user_id=3,
            tournament_id=3,
            amount=1000,
            odds=1.5,
            result=BetResult.WIN,
        ),
    ]
