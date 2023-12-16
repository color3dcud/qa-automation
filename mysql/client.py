import allure
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from settings import db_settings


class MysqlClient:

    def __init__(self, db_name, user, password):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = '127.0.0.1'
        self.port = db_settings.port

        self.connection = None
        self.engine = None
        self.session: Session | None = None

    @allure.step('Подключение к БД')
    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        self.engine = create_engine(url)
        self.connection = self.engine.connect()
        session = sessionmaker(bind=self.engine)
        self.session = session()
