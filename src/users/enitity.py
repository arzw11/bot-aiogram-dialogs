from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseUser:
    user_id: int
    telegram_id: int
    name: Optional[str]
    tournaments: Optional[dict]
    bets: Optional[list]
