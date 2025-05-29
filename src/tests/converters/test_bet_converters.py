from src.infra.converters.bets import (
    bet_from_entity,
    bet_to_entity,
)


def test_bet_to_entity(bet_model, bet_entity):
    converted_entity = bet_to_entity(bet_model)

    assert converted_entity.bet_id == bet_entity.bet_id, f"{converted_entity.bet_id=}"
    assert converted_entity.user_id == bet_entity.user_id, f"{converted_entity.user_id=}"
    assert converted_entity.tournament_id == bet_entity.tournament_id, f"{converted_entity.tournament_id=}"
    assert converted_entity.amount == bet_entity.amount, f"{converted_entity.amount=}"
    assert converted_entity.odds == bet_entity.odds, f"{converted_entity.odds=}"
    assert converted_entity.result == bet_entity.result, f"{converted_entity.result=}"


def test_bet_from_entity(bet_entity, bet_model):
    converted_model = bet_from_entity(bet_entity)

    assert converted_model.id == bet_model.id, f"{converted_model.id=}"
    assert converted_model.user_id == bet_model.user_id, f"{converted_model.user_id=}"
    assert converted_model.tournament_id == bet_model.tournament_id, f"{converted_model.tournament_id=}"
    assert converted_model.amount == bet_model.amount, f"{converted_model.amount=}"
    assert converted_model.odds == bet_model.odds, f"{converted_model.odds=}"
    assert converted_model.result == bet_model.result, f"{converted_model.result=}"
