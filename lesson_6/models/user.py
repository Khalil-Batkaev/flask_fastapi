from datetime import date
from pydantic import BaseModel, Field, EmailStr, PositiveInt, StrictStr, SecretStr, StrictBool

"""
Пользователь должен иметь следующие поля:
○ ID (автоматически генерируется при создании пользователя)
○ username:
○ password:
○ Имя (строка, не менее 2 символов)
○ Фамилия (строка, не менее 2 символов)
○ Дата рождения (строка в формате "YYYY-MM-DD")
○ Email (строка, валидный email)
○ Адрес (строка, не менее 5 символов)
"""

__all__ = (
    'User',
    'CreateUser',
)


class UserField:
    id = Field(description="User id", example=1)
    username = Field(description="User login", example='ivan2000')
    password = Field(description='User password', example='qwerty')
    first_name = Field(description='User name', min_length=2, example='Ivan')
    last_name = Field(description='User surname', min_length=2, example='Ivanov')
    birth_date = Field(description='User birth date', example='2000-10-05')
    email = Field(description='User email', example='ivan_2000@test.ru')
    address = Field(description='User address', min_length=5, example='Victory str, 5')


class User(BaseModel):
    id: PositiveInt = UserField.id
    username: StrictStr = UserField.username
    password: SecretStr = UserField.password
    first_name: StrictStr = UserField.first_name
    last_name: StrictStr = UserField.last_name
    birth_date: date = UserField.birth_date
    email: EmailStr = UserField.email
    address: StrictStr = UserField.address


class CreateUser(BaseModel):
    username: StrictStr = UserField.username
    password: StrictStr = UserField.password
    first_name: StrictStr = UserField.first_name
    last_name: StrictStr = UserField.last_name
    birth_date: date = UserField.birth_date
    email: EmailStr = UserField.email
    address: StrictStr = UserField.address
