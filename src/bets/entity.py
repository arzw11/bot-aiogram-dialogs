from dataclasses import dataclass
from enum import Enum
from typing import Optional


class BetResult(Enum):
    WIN = "win"
    LOSS = "loss"


@dataclass(frozen=True)
class Bet:
    bet_id: int
    user_id: int
    tournament_id: Optional[int] # noqa
    amount: int
    odds: float
    result: BetResult
    payout: int

    @classmethod
    def from_result(
        cls,
        bet_id: int,
        user_id: int,
        tournament_id: Optional[int],
        amount: int,
        odds: float,
        result: BetResult,
    ) -> "Bet":
        payout = int(amount * odds) if result == BetResult.WIN else 0

        return cls(
            bet_id=bet_id,
            user_id=user_id,
            tournament_id=tournament_id,
            amount=amount,
            odds=odds,
            result=result,
            payout=payout,
        )
