import pytest

from src.bets.entity import (
    Bet,
    BetResult,
)
from src.tournaments.entity import Tournament


def test_tournament_from_bets_with_wins(dummy_user):
    bets = [
        Bet.from_result(
            bet_id=1,
            user=dummy_user,
            tournament=None,
            amount=100,
            odds=2.0,
            result=BetResult.WIN,
        ),
        Bet.from_result(
            bet_id=2,
            user=dummy_user,
            tournament=None,
            amount=50,
            odds=3.0,
            result=BetResult.WIN,
        ),
    ]

    tournament = Tournament.from_bets(
        tournament_id=1,
        title="Winning Tournament",
        bank=500,
        user=dummy_user,
        bets=bets,
    )

    assert tournament.bet_count == 2, f"{tournament.bet_count=}"
    assert tournament.win_count == 2, f"{tournament.win_count=}"
    assert tournament.loss_count == 0, f"{tournament.loss_count=}"
    assert tournament.final_balance == 500 + (200 - 100) + (150 - 50), f"{tournament.final_balance=}"
    assert tournament.profit == 200, f"{tournament.profit=}"
    assert tournament.roi == 40.0, f"{tournament.roi=}"


def test_tournament_from_bets_with_losses(dummy_user):
    bets = [
        Bet.from_result(
            bet_id=1,
            user=dummy_user,
            tournament=None,
            amount=100,
            odds=2.0,
            result=BetResult.LOSS,
        ),
        Bet.from_result(
            bet_id=2,
            user=dummy_user,
            tournament=None,
            amount=50,
            odds=3.0,
            result=BetResult.LOSS,
        ),
    ]

    tournament = Tournament.from_bets(
        tournament_id=2,
        title="Losing Tournament",
        bank=500,
        user=dummy_user,
        bets=bets,
    )

    assert tournament.bet_count == 2, f"{tournament.bet_count=}"
    assert tournament.win_count == 0, f"{tournament.win_count=}"
    assert tournament.loss_count == 2, f"{tournament.loss_count=}"
    assert tournament.final_balance == 500 - 100 - 50, f"{tournament.final_balance=}"
    assert tournament.profit == -150, f"{tournament.profit=}"
    assert tournament.roi == -30.0, f"{tournament.roi=}"


def test_tournament_from_bets_mixed(dummy_user):
    bets = [
        Bet.from_result(
            bet_id=1,
            user=dummy_user,
            tournament=None,
            amount=100,
            odds=2.0,
            result=BetResult.WIN,
        ),
        Bet.from_result(
            bet_id=2,
            user=dummy_user,
            tournament=None,
            amount=50,
            odds=2.0,
            result=BetResult.LOSS,
        ),
    ]

    tournament = Tournament.from_bets(
        tournament_id=3,
        title="Mixed Tournament",
        bank=300,
        user=dummy_user,
        bets=bets,
    )

    assert tournament.bet_count == 2, f"{tournament.bet_count=}"
    assert tournament.win_count == 1, f"{tournament.win_count=}"
    assert tournament.loss_count == 1, f"{tournament.loss_count=}"
    assert tournament.final_balance == 300 + (200 - 100) - 50, f"{tournament.final_balance=}"
    assert tournament.profit == 50, f"{tournament.profit=}"
    assert tournament.roi == pytest.approx(16.67, 0.1), f"{tournament.roi=}"
