from abc import (
    ABC,
    abstractmethod,
)

from src.users.enitity import BaseUser


class UserBaseRepository(ABC):
    @abstractmethod
    async def add(self, user: BaseUser):
        ...

    @abstractmethod
    async def get(self, telegram_id: str) -> BaseUser:
        ...

    @abstractmethod
    async def update(self, telegram_id: str, data: dict) -> BaseUser:
        ...

    @abstractmethod
    async def delete(self, telegram_id: str) -> BaseUser:
        ...
