from src.bets.converters import bet_to_entity
from src.tournaments.entity import Tournament as TournamentEntity
from src.tournaments.model import Tournament as TournamentModel


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
