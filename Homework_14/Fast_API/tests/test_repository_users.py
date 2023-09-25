import sys
import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session

sys.path.append("C:/Users/PC/Desktop/Fast_API")

from src.database.models import User
from src.repository.users import (
    get_user_by_email, 
    create_user, 
    update_token, 
    confirmed_email
)


class TestYourModule(unittest.TestCase):

    def setUp(self):
        self.session = MagicMock(spec=Session)

#-----------------------------------------------------------------------------------------------------------------------------------
    async def test_get_user_by_email(self):
        # Тест на получение пользователя по email
        email = "test@example.com"
        expected_user = User(email=email)
        self.session.query.return_value.filter.return_value.first.return_value = expected_user
        result = await get_user_by_email(email=email, db=self.session)
        self.assertEqual(result, expected_user)

#-----------------------------------------------------------------------------------------------------------------------------------
    async def test_create_user(self):
        # Тест на создание пользователя
        user_data = {
            'username': 'Pavlo',
            "email": "test@example.com",
            'password': '123456789'
        }
        expected_user = User(**user_data)
        await create_user(body=user_data, db=self.session)
        self.session.add.assert_called_once_with(expected_user)
        self.session.commit.assert_called_once()

#-----------------------------------------------------------------------------------------------------------------------------------
    async def test_update_token(self):
        # Тест на обновление токена пользователя
        user = User()
        token = "new_token"
        await update_token(user=user, token=token, db=self.session)
        self.assertEqual(user.refresh_token, token)
        self.session.commit.assert_called_once()

#-----------------------------------------------------------------------------------------------------------------------------------
    async def test_confirmed_email(self):
        # Тест на подтверждение email пользователя
        email = "test@example.com"
        user = User(email=email)
        self.session.query.return_value.filter.return_value.first.return_value = user
        await confirmed_email(email=email, db=self.session)
        self.assertTrue(user.confirmed)
        self.session.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
