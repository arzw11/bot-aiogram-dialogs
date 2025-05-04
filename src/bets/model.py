from __future__ import annotations

from typing import Optional

from sqlalchemy import (
    Enum,
    Float,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.bets.entity import BetResult
from src.common.models import TimedBaseModel


class Bet(TimedBaseModel):
    __tablename__ = "bet"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    tournament_id: Mapped[int] = mapped_column(
        ForeignKey("tournament.id", ondelete="NO ACTION"), nullable=True, default=None,
    )
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    odds: Mapped[float] = mapped_column(Float, nullable=False)
    result: Mapped[BetResult] = mapped_column(Enum(BetResult), nullable=False)

    user: Mapped["User"] = relationship(back_populates="bets") # noqa
    tournament: Mapped[Optional["Tournament"]] = relationship(back_populates="bets") # noqa
