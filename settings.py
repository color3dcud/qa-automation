import os

from pydantic_settings import BaseSettings


class DevSettingDB(BaseSettings):
    host: str = "127.0.0.1"
    port: str = "3307"
    username: str = "root"
    password: str = "0000"
    db_name: str = "vkeducation"


class SettingDB(DevSettingDB):
    host: str = "project_db"
    port: str = "3306"


db_settings = DevSettingDB()
