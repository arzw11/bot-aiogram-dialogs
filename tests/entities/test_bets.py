
from src.bets.entity import (
    Bet,
    BetResult,
)


def test_bet_from_win(dummy_user):
    bet = Bet.from_result(
        bet_id=1,
        user=dummy_user,
        tournament=None,
        amount=100,
        odds=3,
        result=BetResult.WIN,
    )

    assert bet.payout == 300, f"{bet.payout=} "
    assert bet.result == BetResult.WIN, f"{bet.result=} "
    assert bet.user == dummy_user, f"{bet.user=} "
    assert bet.odds == 3, f"{bet.odds=} "


def test_bet_from_loss(dummy_user):
    bet = Bet.from_result(
        bet_id=222,
        user=dummy_user,
        tournament=None,
        amount=1000,
        odds=1.5,
        result=BetResult.LOSS,
    )

    assert bet.payout == 0, f"{bet.payout=} "
    assert bet.result == BetResult.LOSS, f"{bet.result=} "
    assert bet.user == dummy_user, f"{bet.user=} "
    assert bet.odds == 1.5, f"{bet.odds=} "
