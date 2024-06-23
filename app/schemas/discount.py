from pydantic import BaseModel


class DiscountBase(BaseModel):
    discount_name: str
    discount_type: str
    discount_value: float


class DiscountCreate(DiscountBase):
    pass


class DiscountUpdate(DiscountBase):
    pass


class Discount(DiscountBase):
    discount_id: int

    class Config:
        orm_mode = True
