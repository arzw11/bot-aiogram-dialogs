from typing import (
    List,
    Optional,
)

from sqlalchemy import (
    func,
    insert,
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.bets.converters import bet_to_entity
from src.bets.entity import Bet as BetEntity
from src.tournaments.converters import tournament_to_entity
from src.tournaments.entity import Tournament as TournamentEntity
from src.users.converters import user_to_entity
from src.users.entity import User as UserEntity
from src.users.model import User as UserModel
from src.users.repository import BaseUserRepository


class SQLUserRepository(BaseUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, user: UserEntity) -> None:
        stmt = insert(UserModel).values(
            telegram_id=user.telegram_id,
            name=user.name,
        )

        await self._session.execute(stmt)
        await self._session.commit()

    async def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(stmt)
        user = result.scalar_one_or_none()

        if user:
            return user_to_entity(user=user)

        return None

    async def get_by_telegram_id(self, telegram_id: int) -> Optional[UserEntity]:
        stmt = select(UserModel).where(UserModel.telegram_id == telegram_id)
        result = await self._session.execute(stmt)
        user = result.scalar_one_or_none()

        if user:
            return user_to_entity(user=user)

        return None

    async def get_tournaments(self, user_id: int) -> Optional[List[TournamentEntity]]:
        stmt = (
            select(UserModel)
            .options(joinedload(UserModel.tournaments))
            .where(UserModel.id == user_id)
        )
        result = await self._session.execute(stmt)
        user = result.unique().scalar_one_or_none()
        if user:
            return [tournament_to_entity(tournament) for tournament in user.tournaments]

        return None

    async def get_bets(self, user_id: int) -> Optional[List[BetEntity]]:
        stmt = (
            select(UserModel)
            .options(joinedload(UserModel.bets))
            .where(UserModel.id == user_id)
        )
        result = await self._session.execute(stmt)
        user = result.unique().scalar_one_or_none()

        if user:
            return [bet_to_entity(bet) for bet in user.bets]

        return None

    async def count_users(self) -> int:
        stmt = select(func.count(UserModel.id)).select_from(UserModel)
        result = await self._session.execute(stmt)

        return result.scalar_one()
