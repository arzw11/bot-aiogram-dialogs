from src.bets.entity import Bet
from src.tournaments.entity import Tournament


def test_user_creation(dummy_user):
    assert dummy_user.user_id == 1, f"{dummy_user.user_id=}"
    assert dummy_user.telegram_id == 12345, f"{dummy_user.telegram_id=}"
    assert dummy_user.name == "Test User", f"{dummy_user.name=}"
    assert dummy_user.tournaments == [], f"{dummy_user.tournaments=}"
    assert dummy_user.bets == [], f"{dummy_user.bets=}"


def test_user_with_tournaments(dummy_user):
    tournament = Tournament(
        tournament_id=1,
        title="Test Tournament",
        bank=1000,
        user=dummy_user,
        bets=[],
    )

    dummy_user.tournaments.append(tournament)

    assert len(dummy_user.tournaments) == 1, f"{len(dummy_user.tournaments)=}"
    assert dummy_user.tournaments[0].title == "Test Tournament", f"{dummy_user.tournaments[0].title=}"
    assert dummy_user.tournaments[0].bank == 1000, f"{dummy_user.tournaments[0].bank=}"


def test_user_with_bets(dummy_user):
    bet = Bet(
        bet_id=1,
        user=dummy_user,
        tournament=None,
        amount=100,
        odds=2.5,
        result="win",
        payout=250,
    )

    dummy_user.bets.append(bet)

    assert len(dummy_user.bets) == 1, f"{len(dummy_user.bets)=}"
    assert dummy_user.bets[0].amount == 100, f"{dummy_user.bets[0].amount=}"
    assert dummy_user.bets[0].odds == 2.5, f"{dummy_user.bets[0].odds=}"


def test_user_update_name(dummy_user):
    dummy_user.name = "Updated User"

    assert dummy_user.name == "Updated User", f"{dummy_user.name=}"


def test_user_empty_tournaments(dummy_user):
    assert dummy_user.tournaments == [], f"{dummy_user.tournaments=}"


def test_user_empty_bets(dummy_user):
    assert dummy_user.bets == [], f"{dummy_user.bets=}"
