from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    List,
    Optional,
)

from src.bets.entity import Bet


class BaseBetRepository(ABC):
    @abstractmethod
    async def add(self, bet: Bet) -> None:
        ...

    @abstractmethod
    async def get_by_id(self, bet_id: int) -> Optional[Bet]:
        ...

    @abstractmethod
    async def get_all_by_user_id(self, user_id: int) -> List[Bet]:
        ...

    @abstractmethod
    async def get_all_by_tournament_id(self, tournament_id: int) -> List[Bet]:
        ...

    @abstractmethod
    async def update(self, bet: Bet) -> Bet:
        ...

    @abstractmethod
    async def delete(self, bet_id: int) -> bool:
        ...
