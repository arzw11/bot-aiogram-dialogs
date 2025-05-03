from abc import (
    ABC,
    abstractmethod,
)
from typing import Optional

from src.tournaments.entity import Tournament


class BaseTournamentRepository(ABC):
    @abstractmethod
    async def add(self, tournament: Tournament) -> None:
        ...

    @abstractmethod
    async def get_by_id(self, tournament_id: int) -> Optional[Tournament]:
        ...

    @abstractmethod
    async def update(self, tournament: Tournament) -> Tournament:
        ...

    @abstractmethod
    async def delete(self, tournament_id: int) -> bool:
        ...
