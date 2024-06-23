from pydantic import BaseModel


class DiscountRoomRateBase(BaseModel):
    room_rate_id: int
    discount_id: int


class DiscountRoomRateCreate(DiscountRoomRateBase):
    pass


class DiscountRoomRateUpdate(DiscountRoomRateBase):
    pass


class DiscountRoomRate(DiscountRoomRateBase):
    id: int

    class Config:
        orm_mode = True
