import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
)


class TimedBaseModel(DeclarativeBase):
    intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

    created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
    updated_at = Annotated[
        datetime.datetime, mapped_column(
            server_default=text("TIMEZONE('utc', now())"),
            onupdate=datetime.datetime.utcnow,
        ),
    ]
