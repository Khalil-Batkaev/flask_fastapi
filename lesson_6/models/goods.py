from pydantic import BaseModel, Field, PositiveInt, StrictStr

"""
Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
"""

__all__ = (
    'Goods',
    'CreateGoods',
)


class GoodsField:
    id = Field(description="Product id", example=1)
    title = Field(description='Product name', example='MacBook')
    description = Field(description="Description of product", example='Laptop')
    price = Field(description='Price of product', example=999.90)


class Goods(BaseModel):
    id: PositiveInt = GoodsField.id
    title: StrictStr = GoodsField.title
    description: StrictStr = GoodsField.description
    price: float = GoodsField.price


class CreateGoods(BaseModel):
    title: StrictStr = GoodsField.title
    description: StrictStr = GoodsField.description
    price: float = GoodsField.price
