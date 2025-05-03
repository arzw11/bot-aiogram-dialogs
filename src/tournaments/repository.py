from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    List,
    Optional,
)

from src.tournaments.entity import Tournament


class BaseTournamentRepository(ABC):
    @abstractmethod
    async def add(self, tournament: Tournament):
        ...

    @abstractmethod
    async def get_tournament(self, tournament_id: int) -> Tournament:
        ...

    @abstractmethod
    async def get_list_tournaments_by_user(self, user_id: int) -> List[Tournament]:
        ...

    @abstractmethod
    async def update_tournament(self, tournament_id: int, data: dict) -> Optional[Tournament]:
        ...

    @abstractmethod
    async def delete_tournament(self, tournament_id: int) -> Optional[Tournament]:
        ...
