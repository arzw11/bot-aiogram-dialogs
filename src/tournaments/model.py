from __future__ import annotations

from typing import List

from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.common.models import TimedBaseModel


class Tournament(TimedBaseModel):
    __tablename__ = "tournament"

    title: Mapped[str] = mapped_column(String, nullable=False)
    bank: Mapped[int] = mapped_column(Integer, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    bets: Mapped[List["Bet"]] = relationship(back_populates="tournament") # noqa
    user: Mapped["User"] = relationship(back_populates="tournaments") # noqa

    def __str__(self):
        return self.title
