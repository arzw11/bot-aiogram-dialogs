from dataclasses import dataclass
from typing import (
    List,
    Optional,
)


@dataclass
class User:
    user_id: int
    telegram_id: int
    name: Optional[str]
    tournaments: Optional[List["Tournament"]] # noqa
    bets: Optional[List["Bet"]] # noqa
