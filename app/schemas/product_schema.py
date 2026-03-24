from pydantic import BaseModel, Field


class ProductUpdate(BaseModel):
    name: str
    category_id: int
    description: str
    manufacturer_id: int
    supplier_id: int
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)
    image_path: str | None = None
