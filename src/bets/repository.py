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
    def add(self, bet: Bet):
        ...

    @abstractmethod
    def get_bet(self, bet_id: int) -> Bet:
        ...

    @abstractmethod
    def get_list_bets_by_user_id(self, user_id: int) -> List[Bet]:
        ...

    @abstractmethod
    def update_bet(self, bet_id: int, data: dict) -> Optional[Bet]:
        ...

    @abstractmethod
    def delete(self, bet_id: int) -> Optional[Bet]:
        ...
