from src.infra.converters.tournaments import (
    tournament_from_entity,
    tournament_to_entity,
)


def test_tournament_to_entity(tournament_model, tournament_entity):
    converted = tournament_to_entity(tournament_model)

    assert converted.tournament_id == tournament_entity.tournament_id, f"{converted.tournament_id=}"
    assert converted.title == tournament_entity.title, f"{converted.title=}"
    assert converted.user_id == tournament_entity.user_id, f"{converted.user_id=}"
    assert converted.bank == tournament_entity.bank, f"{converted.bank=}"
    assert len(converted.bets or []) == 1, f"{len(converted.bets or [])=}"
    assert converted.bets[0].bet_id == tournament_entity.bets[0].bet_id, f"{converted.bets[0].bet_id=}"


def test_tournament_from_entity(tournament_entity, tournament_model):
    converted = tournament_from_entity(tournament_entity)

    assert converted.id == tournament_model.id, f"{converted.id=}"
    assert converted.title == tournament_model.title, f"{converted.title=}"
    assert converted.user_id == tournament_model.user_id, f"{converted.user_id=}"
