from typing import List

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from src.domain.entities.bets import (
    Bet as BetEntity,
    BetResult,
)
from src.domain.entities.tournaments import Tournament as TournamentEntity
from src.domain.entities.users import User as UserEntity
from src.infra.database.models.base import TimedBaseModel as Base
from src.infra.repositories.bets.sqlalchemy_repository import SQLBetRepository
from src.infra.repositories.tournaments.sqlalchemy_repository import SQLTournamentRepository
from src.infra.repositories.users.sqlalchemy_repository import SQLUserRepository


DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def async_engine():
    return create_async_engine(DATABASE_URL, echo=False, future=True)


@pytest_asyncio.fixture(scope="session")
async def initialized_engine(async_engine):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield async_engine
    await async_engine.dispose()


@pytest_asyncio.fixture
async def async_session(initialized_engine):
    async_session_maker = async_sessionmaker(initialized_engine, expire_on_commit=False)
    async with async_session_maker() as session:
        yield session


@pytest_asyncio.fixture
async def user_repo(async_session) -> SQLUserRepository:
    return SQLUserRepository(session=async_session)


@pytest_asyncio.fixture
async def bet_repo(async_session) -> SQLBetRepository:
    return SQLBetRepository(session=async_session)


@pytest_asyncio.fixture
async def tournament_repo(async_session) -> SQLTournamentRepository:
    return SQLTournamentRepository(session=async_session)


@pytest.fixture
def user_entity() -> UserEntity:
    return UserEntity(
        user_id=1,
        telegram_id=123121,
        name="John Doe",
    )


@pytest.fixture
def list_bet_entities() -> List[BetEntity]:
    return [
        BetEntity.from_result(
            bet_id=1,
            user_id=1,
            tournament_id=1,
            amount=1000,
            odds=1.5,
            result=BetResult.WIN,
        ),
        BetEntity.from_result(
            bet_id=2,
            user_id=1,
            tournament_id=1,
            amount=1500,
            odds=1.5,
            result=BetResult.LOSS,
        ),
        BetEntity.from_result(
            bet_id=3,
            user_id=1,
            tournament_id=2,
            amount=500,
            odds=2,
            result=BetResult.WIN,
        ),
    ]


@pytest.fixture
def list_tournament_entities():
    return [
        TournamentEntity.from_bets(
            tournament_id=1,
            title="Champions League",
            bank=1000,
            user_id=1,
            bets=[
                BetEntity.from_result(
                    bet_id=1,
                    user_id=1,
                    tournament_id=1,
                    amount=1000,
                    odds=1.5,
                    result=BetResult.WIN,
                ),
                BetEntity.from_result(
                    bet_id=2,
                    user_id=1,
                    tournament_id=1,
                    amount=1500,
                    odds=1.5,
                    result=BetResult.LOSS,
                ),
            ],
        ),
        TournamentEntity.from_bets(
            tournament_id=2,
            title="EXAMPLE",
            bank=100000,
            user_id=1,
            bets=None,
        ),
    ]
