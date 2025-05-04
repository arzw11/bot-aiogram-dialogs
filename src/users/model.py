from __future__ import annotations

from typing import List

from sqlalchemy import (
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.common.models import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = "user"

    telegram_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(length=70), nullable=True)

    tournaments: Mapped[List["Tournament"]] = relationship(back_populates="user") # noqa
    bets: Mapped[List["Bet"]] = relationship(back_populates="user") # noqa

    def __str__(self):
        return self.name
