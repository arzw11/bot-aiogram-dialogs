from dataclasses import asdict

from src.bets.entity import Bet as BetEntity
from src.bets.model import Bet as BetModel


def bet_to_entity(bet: BetModel) -> BetEntity:
    return BetEntity.from_result(
        bet_id=bet.id,
        user_id=bet.user_id,
        tournament_id=bet.tournament_id,
        amount=bet.amount,
        odds=bet.odds,
        result=bet.result,
    )


def bet_from_entity(entity: BetEntity) -> BetModel:
    return BetModel(
        id=entity.bet_id,
        user_id=entity.user_id,
        tournament_id=entity.tournament_id,
        amount=entity.amount,
        odds=entity.odds,
        result=entity.result,
    )


def bet_to_dict_without_bet_id_and_payout(entity: BetEntity) -> dict:
    bet_dict = asdict(entity)
    del bet_dict["bet_id"]
    del bet_dict["payout"]

    return bet_dict
