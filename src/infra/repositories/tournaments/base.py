from abc import (
    ABC,
    abstractmethod,
)
from typing import Optional

from src.domain.entities.tournaments import Tournament


class BaseTournamentRepository(ABC):
    @abstractmethod
    async def add(self, tournament: Tournament) -> None:
        ...

    @abstractmethod
    async def get_by_id(self, tournament_id: int) -> Optional[Tournament]:
        ...

    @abstractmethod
    async def update(self, tournament: Tournament) -> bool:
        ...

    @abstractmethod
    async def delete(self, tournament_id: int) -> bool:
        ...
