import pytest

from src.domain.entities.bets import Bet as BetEntity
from src.infra.database.models.bets import Bet as BetModel
from src.domain.entities.tournaments import Tournament as TournamentEntity
from src.infra.database.models.tournaments import Tournament as TournamentModel
from src.domain.entities.users import User as UserEntity
from src.infra.database.models.users import User as UserModel


@pytest.fixture
def bet_model():
    return BetModel(
        id=1,
        user_id=123,
        tournament_id=456,
        amount=100,
        odds=2.5,
        result="win",
    )


@pytest.fixture
def bet_entity():
    return BetEntity(
        bet_id=1,
        user_id=123,
        tournament_id=456,
        amount=100,
        odds=2.5,
        result="win",
        payout=250,
    )


@pytest.fixture
def tournament_model(bet_model: BetModel) -> TournamentModel:
    return TournamentModel(
        id=10,
        title="Champions League",
        bank=500,
        user_id=123,
        bets=[bet_model],
    )


@pytest.fixture
def tournament_entity(bet_entity: BetEntity) -> TournamentEntity:
    return TournamentEntity.from_bets(
        tournament_id=10,
        title="Champions League",
        bank=500,
        user_id=123,
        bets=[bet_entity],
    )


@pytest.fixture
def user_model() -> UserModel:
    return UserModel(id=1, telegram_id=123456, name="John Doe")


@pytest.fixture
def user_entity() -> UserEntity:
    return UserEntity(user_id=1, telegram_id=123456, name="John Doe")
