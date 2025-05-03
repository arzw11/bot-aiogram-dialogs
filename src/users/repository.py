from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    List,
    Optional,
)

from src.bets.entity import Bet
from src.tournaments.entity import Tournament
from src.users.entity import User


class BaseUserRepository(ABC):
    @abstractmethod
    async def add(self, user: User) -> None:
        ...

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    async def get_by_telegram_id(self, telegram_id: int) -> Optional[User]:
        ...

    @abstractmethod
    async def get_tournaments(self, user_id: int) -> List[Tournament]:
        ...

    @abstractmethod
    async def get_bets(self, user_id: int) -> List[Bet]:
        ...
