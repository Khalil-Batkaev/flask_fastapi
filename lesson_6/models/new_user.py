from pydantic import BaseModel, Field, EmailStr, PositiveInt, StrictStr, SecretStr

"""
Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
"""

__all__ = (
    'User',
    'CreateUser',
)


class UserField:
    id = Field(description="User id", example=1)
    first_name = Field(description='User name', example='Ivan')
    last_name = Field(description='User surname', example='Ivanov')
    email = Field(description='User email', example='ivan_2000@test.ru')
    password = Field(description='User password', example='qwerty')


class User(BaseModel):
    id: PositiveInt = UserField.id
    first_name: StrictStr = UserField.first_name
    last_name: StrictStr = UserField.last_name
    email: EmailStr = UserField.email
    password: SecretStr = UserField.password


class CreateUser(BaseModel):
    first_name: StrictStr = UserField.first_name
    last_name: StrictStr = UserField.last_name
    email: EmailStr = UserField.email
    password: StrictStr = UserField.password
