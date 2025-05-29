from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    user_id: int
    telegram_id: int
    name: Optional[str]
