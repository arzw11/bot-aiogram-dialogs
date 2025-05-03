from common.models import TimedBaseModel
from sqlalchemy import (
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class User(TimedBaseModel):
    telegram_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(length=70), nullable=True)

    def __str__(self):
        return self.telegram_id
