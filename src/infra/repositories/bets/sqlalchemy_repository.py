from typing import (
    List,
    Optional,
)

from sqlalchemy import (
    delete,
    func,
    insert,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.converters.bets import (
    bet_to_dict_without_bet_id_and_payout,
    bet_to_entity,
)
from src.domain.entities.bets import Bet as BetEntity
from src.infra.database.models.bets import Bet as BetModel
from src.infra.repositories.bets.base import BaseBetRepository


class SQLBetRepository(BaseBetRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, bet: BetEntity) -> None:
        stmt = insert(BetModel).values(
            user_id=bet.user_id,
            tournament_id=bet.tournament_id,
            amount=bet.amount,
            odds=bet.odds,
            result=bet.result,
        )

        await self._session.execute(stmt)
        await self._session.commit()

    async def get_by_id(self, bet_id: int) -> Optional[BetEntity]:
        stmt = select(BetModel).where(BetModel.id == bet_id)
        result = await self._session.execute(stmt)

        bet = result.scalar_one_or_none()

        if bet:
            return bet_to_entity(bet=bet)

        return None

    async def get_all_by_user_id(self, user_id: int) -> Optional[List[BetEntity]]:
        stmt = select(BetModel).where(BetModel.user_id == user_id)
        result = await self._session.execute(stmt)

        bets = result.scalars().all()

        if bets:
            return [bet_to_entity(bet) for bet in bets]

        return None

    async def get_all_by_tournament_id(self, tournament_id: int) -> Optional[List[BetEntity]]:
        stmt = select(BetModel).where(BetModel.tournament_id == tournament_id)
        result = await self._session.execute(stmt)

        bets = result.scalars().all()

        if bets:
            return [bet_to_entity(bet) for bet in bets]

        return None

    async def update(self, bet: BetEntity) -> bool:
        stmt = update(BetModel).values(**bet_to_dict_without_bet_id_and_payout(bet)).where(BetModel.id == bet.bet_id)
        result = await self._session.execute(stmt)
        await self._session.commit()

        return result.rowcount > 0

    async def delete(self, bet_id: int) -> bool:
        stmt = delete(BetModel).where(BetModel.id == bet_id)
        result = await self._session.execute(stmt)
        await self._session.commit()

        return result.rowcount > 0

    async def count_bets(self) -> int:
        stmt = select(func.count(BetModel.id)).select_from(BetModel)
        result = await self._session.execute(stmt)

        return result.scalar_one()
