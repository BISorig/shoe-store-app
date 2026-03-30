from datetime import datetime

from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    article: str = Field(min_length=1)
    status: str = Field(min_length=1)
    pickup_point_id: int
    order_date: datetime
    delivery_date: datetime
    user_id: int
    receipt_code: int


class OrderUpdate(OrderCreate):
    pass
