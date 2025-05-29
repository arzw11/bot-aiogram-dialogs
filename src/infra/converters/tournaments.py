from dataclasses import asdict

from src.infra.converters.bets import bet_to_entity
from src.domain.entities.tournaments import Tournament as TournamentEntity
from src.infra.database.models.tournaments import Tournament as TournamentModel


def tournament_to_entity(tournament: TournamentModel) -> TournamentEntity:
    return TournamentEntity.from_bets(
        tournament_id=tournament.id,
        title=tournament.title,
        bank=tournament.bank,
        user_id=tournament.user_id,
        bets=[bet_to_entity(bet) for bet in tournament.bets] if tournament.bets else None,
    )


def tournament_from_entity(entity: TournamentEntity) -> TournamentModel:
    return TournamentModel(
        id=entity.tournament_id,
        title=entity.title,
        user_id=entity.user_id,
    )


def tournament_to_dict(entity: TournamentEntity) -> dict:
    tournament_dict = asdict(entity)

    del tournament_dict["bets"]
    del tournament_dict["tournament_id"]
    del tournament_dict["bet_count"]
    del tournament_dict["win_count"]
    del tournament_dict["loss_count"]
    del tournament_dict["final_balance"]

    return tournament_dict
