from abc import (
    ABC,
    abstractmethod,
)
from typing import Optional

from src.users.entity import User


class UserBaseRepository(ABC):
    @abstractmethod
    async def add(self, user: User):
        ...

    @abstractmethod
    async def get(self, telegram_id: int) -> Optional[User]:
        ...

    @abstractmethod
    async def update(self, telegram_id: int, data: dict) -> User:
        ...

    @abstractmethod
    async def delete(self, telegram_id: int) -> Optional[User]:
        ...
