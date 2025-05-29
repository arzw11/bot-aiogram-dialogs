from src.domain.entities.bets import (
    Bet,
    BetResult,
)
from src.domain.entities.tournaments import Tournament


def make_bet(bet_id, user_id, tournament_id, amount, odds, result):
    payout = int(amount * odds) if result == BetResult.WIN else 0
    return Bet(
        bet_id=bet_id,
        user_id=user_id,
        tournament_id=tournament_id,
        amount=amount,
        odds=odds,
        result=result,
        payout=payout,
    )


def test_tournament_without_bets():
    tournament = Tournament.from_bets(
        tournament_id=1,
        title="No Bets Yet",
        bank=1000,
        user_id=42,
        bets=None,
    )

    assert tournament.bet_count == 0, f"{tournament.bet_count=}"
    assert tournament.win_count == 0, f"{tournament.win_count=}"
    assert tournament.loss_count == 0, f"{tournament.loss_count=}"
    assert tournament.final_balance == 1000, f"{tournament.final_balance=}"
    assert tournament.profit == 0, f"{tournament.profit=}"
    assert tournament.roi == 0.0, f"{tournament.roi=}"


def test_tournament_all_wins():
    bets = [
        make_bet(1, 1, 1, 100, 2.0, BetResult.WIN),
        make_bet(2, 1, 1, 200, 1.5, BetResult.WIN),
    ]

    tournament = Tournament.from_bets(
        tournament_id=1,
        title="All Wins",
        bank=1000,
        user_id=1,
        bets=bets,
    )

    assert tournament.bet_count == 2, f"{tournament.bet_count=}"
    assert tournament.win_count == 2, f"{tournament.win_count=}"
    assert tournament.loss_count == 0, f"{tournament.loss_count=}"
    assert tournament.final_balance == 1000 + (200 - 100) + (300 - 200), f"{tournament.final_balance=}"
    assert tournament.profit == 200, f"{tournament.profit=}"
    assert tournament.roi == 20.0, f"{tournament.roi=}"


def test_tournament_all_losses():
    bets = [
        make_bet(3, 2, 1, 100, 2.0, BetResult.LOSS),
        make_bet(4, 2, 1, 50, 1.5, BetResult.LOSS),
    ]

    tournament = Tournament.from_bets(
        tournament_id=2,
        title="All Losses",
        bank=500,
        user_id=2,
        bets=bets,
    )

    assert tournament.bet_count == 2, f"{tournament.bet_count=}"
    assert tournament.win_count == 0, f"{tournament.win_count=}"
    assert tournament.loss_count == 2, f"{tournament.loss_count=}"
    assert tournament.final_balance == 500 - 100 - 50, f"{tournament.final_balance=}"
    assert tournament.profit == -150, f"{tournament.profit=}"
    assert tournament.roi == -30.0, f"{tournament.roi=}"


def test_tournament_mixed_results():
    bets = [
        make_bet(5, 3, 1, 100, 2.0, BetResult.WIN),   # +100
        make_bet(6, 3, 1, 50, 1.5, BetResult.LOSS),   # -50
    ]

    tournament = Tournament.from_bets(
        tournament_id=3,
        title="Mixed",
        bank=800,
        user_id=3,
        bets=bets,
    )

    assert tournament.bet_count == 2, f"{tournament.bet_count=}"
    assert tournament.win_count == 1, f"{tournament.win_count=}"
    assert tournament.loss_count == 1, f"{tournament.loss_count=}"
    assert tournament.final_balance == 800 + 100 - 50, f"{tournament.final_balance=}"
    assert tournament.profit == 50, f"{tournament.profit=}"
    assert round(tournament.roi, 2) == 6.25, f"{round(tournament.roi, 2)=}"


def test_tournament_with_zero_bank():
    bets = [
        make_bet(7, 4, 1, 100, 2.0, BetResult.WIN),
        make_bet(8, 4, 1, 50, 2.0, BetResult.LOSS),
    ]

    tournament = Tournament.from_bets(
        tournament_id=4,
        title="Zero Bank",
        bank=0,
        user_id=4,
        bets=bets,
    )

    assert tournament.final_balance == 0 + 100 - 50, f"{tournament.final_balance=}"
    assert tournament.profit == 50, f"{tournament.profit=}"
    assert tournament.roi == 0.0, f"{tournament.roi=}"
