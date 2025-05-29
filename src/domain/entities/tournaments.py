from dataclasses import (
    dataclass,
    field,
)
from typing import (
    List,
    Optional,
)

from src.domain.entities.bets import (
    Bet,
    BetResult,
)


@dataclass(frozen=True)
class Tournament:
    tournament_id: int
    title: str
    bank: int

    user_id: int
    bets: Optional[List[Bet]]

    bet_count: int = field(default=0)
    win_count: int = field(default=0)
    loss_count: int = field(default=0)
    final_balance: int = field(default=0)

    @classmethod
    def from_bets(
        cls,
        tournament_id: int,
        title: str,
        bank: int,
        user_id: int,
        bets: Optional[List[Bet]],
    ) -> "Tournament":
        final_balance = bank
        bet_count = 0
        win_count = 0
        loss_count = 0

        if bets:
            bet_count = len(bets)
            for bet in bets:
                final_balance += (bet.payout - bet.amount)

                if bet.result == BetResult.WIN:
                    win_count += 1
                else:
                    loss_count += 1

        return cls(
            tournament_id=tournament_id,
            title=title,
            bank=bank,
            user_id=user_id,
            bets=bets,
            bet_count=bet_count,
            win_count=win_count,
            loss_count=loss_count,
            final_balance=final_balance,
        )

    @property
    def profit(self) -> int:
        return self.final_balance - self.bank

    @property
    def roi(self) -> float:
        if self.bank == 0:
            return 0.0
        return (self.profit / self.bank) * 100
