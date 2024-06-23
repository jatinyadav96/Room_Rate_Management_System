from pydantic import BaseModel


class RoomRateBase(BaseModel):
    room_name: str
    default_rate: float


class RoomRateCreate(RoomRateBase):
    pass


class RoomRateUpdate(RoomRateBase):
    pass


class RoomRate(RoomRateBase):
    room_id: int

    class Config:
        orm_mode = True
