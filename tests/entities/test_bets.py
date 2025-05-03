
from src.bets.entity import (
    Bet,
    BetResult,
)


def test_bet_win_payout():
    bet = Bet.from_result(
        bet_id=1,
        user_id=100,
        tournament_id=200,
        amount=100,
        odds=2.5,
        result=BetResult.WIN,
    )

    assert bet.payout == 250, f"{bet.payout=}"
    assert bet.result == BetResult.WIN, f"{bet.result=}"
    assert bet.user_id == 100, f"{bet.user_id=}"
    assert bet.tournament_id == 200, f"{bet.tournament_id=}"


def test_bet_loss_payout():
    bet = Bet.from_result(
        bet_id=2,
        user_id=101,
        tournament_id=201,
        amount=100,
        odds=2.0,
        result=BetResult.LOSS,
    )

    assert bet.payout == 0, f"{bet.payout=}"
    assert bet.result == BetResult.LOSS, f"{bet.result=}"


def test_zero_odds_win():
    bet = Bet.from_result(
        bet_id=3,
        user_id=102,
        tournament_id=202,
        amount=100,
        odds=0.0,
        result=BetResult.WIN,
    )

    assert bet.payout == 0, f"{bet.payout=}"
    assert bet.odds == 0.0, f"{bet.odds=}"


def test_zero_amount_win():
    bet = Bet.from_result(
        bet_id=4,
        user_id=103,
        tournament_id=203,
        amount=0,
        odds=2.0,
        result=BetResult.WIN,
    )

    assert bet.payout == 0, f"{bet.payout=}"
    assert bet.amount == 0, f"{bet.amount=}"


def test_none_tournament_id():
    bet = Bet.from_result(
        bet_id=5,
        user_id=104,
        tournament_id=None,
        amount=50,
        odds=3.0,
        result=BetResult.WIN,
    )

    assert bet.tournament_id is None, f"{bet.tournament_id=}"
    assert bet.payout == 150, f"{bet.payout=}"
