import allure
from sqlalchemy import select

from mysql.client import MysqlClient
from mysql.models.test_user_model import TestUserModel


class ProjectDB(MysqlClient):

    TABLES = {
        "test_user": TestUserModel
    }

    @allure.step('Получение данных из БД')
    def get_table_data(self, table, **filters):
        table_model = self.TABLES[table]

        with allure.step(f'Получение данных из таблицы {table_model.__tablename__}, фильтры = {filters}'):
            stmt = select(table_model).filter_by(**filters)
            return self.session.scalar(stmt)
