from pydantic import BaseModel, Field, PositiveInt, StrictStr
from datetime import date

"""
Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
заказа.
"""

__all__ = (
    'Order',
    'CreateOrder',
)


class OrderField:
    id = Field(description="Product id", example=1)
    user_id = Field(description='User id', example=2)
    goods_id = Field(description='Product id', example=1)
    order_date = Field(description='Date of order', example='2023-06-06')
    status = Field(description="Status of order", example='Created')


class Order(BaseModel):
    id: PositiveInt = OrderField.id
    user_id: PositiveInt = OrderField.user_id
    goods_id: PositiveInt = OrderField.goods_id
    order_date: date = OrderField.order_date
    status: StrictStr = OrderField.status


class CreateOrder(BaseModel):
    user_id: PositiveInt = OrderField.user_id
    goods_id: PositiveInt = OrderField.goods_id
    order_date: date = OrderField.order_date
    status: StrictStr = OrderField.status
