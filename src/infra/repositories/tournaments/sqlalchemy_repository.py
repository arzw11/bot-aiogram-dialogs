from typing import Optional

from sqlalchemy import (
    delete,
    func,
    insert,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.infra.converters.tournaments import (
    tournament_to_dict,
    tournament_to_entity,
)
from src.domain.entities.tournaments import Tournament as TournamentEntity
from src.infra.database.models.tournaments import Tournament as TournamentModel
from src.infra.repositories.tournaments.base import BaseTournamentRepository


class SQLTournamentRepository(BaseTournamentRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, tournament: TournamentEntity) -> None:
        stmt = insert(TournamentModel).values(
            title=tournament.title,
            bank=tournament.bank,
            user_id=tournament.user_id,
        )
        await self._session.execute(stmt)
        await self._session.commit()

    async def get_by_id(self, tournament_id: int) -> Optional[TournamentEntity]:
        stmt = (
            select(TournamentModel)
            .options(joinedload(TournamentModel.bets))  # Загрузить связанные ставки
            .where(TournamentModel.id == tournament_id)
        )
        result = await self._session.execute(stmt)

        tournament = result.unique().scalar_one_or_none()
        if tournament:
            return tournament_to_entity(tournament=tournament)

        return None

    async def update(self, tournament: TournamentEntity) -> bool:
        stmt = update(TournamentModel).values(**tournament_to_dict(tournament))
        result = await self._session.execute(stmt)
        await self._session.commit()

        return result.rowcount > 0

    async def delete(self, tournament_id: int) -> bool:
        stmt = delete(TournamentModel).where(TournamentModel.id == tournament_id)
        result = await self._session.execute(stmt)
        await self._session.commit()

        return result.rowcount > 0

    async def count_tournaments(self) -> int:
        stmt = select(func.count(TournamentModel.id)).select_from(TournamentModel)
        result = await self._session.execute(stmt)

        return result.scalar_one()
