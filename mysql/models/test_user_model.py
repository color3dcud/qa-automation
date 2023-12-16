import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, DATETIME, SMALLINT

from mysql.models.base_model import BaseModel


class TestUserModel(BaseModel):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(VARCHAR(255), default=None)
    surname: Mapped[str] = mapped_column(VARCHAR(255), default=None)
    middle_name: Mapped[Optional[str]] = mapped_column(VARCHAR(255), default=None)
    username: Mapped[str] = mapped_column(VARCHAR(16), default=None, unique=True)
    password: Mapped[str] = mapped_column(VARCHAR(255), default=None)
    email: Mapped[str] = mapped_column(VARCHAR(64), default=None, unique=True)
    access: Mapped[int] = mapped_column(SMALLINT, default=None)
    active: Mapped[int] = mapped_column(SMALLINT, default=None)
    start_active_time: Mapped[datetime.datetime] = mapped_column(DATETIME, default=None)



