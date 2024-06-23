from datetime import date

from pydantic import BaseModel


class OverriddenRoomRateBase(BaseModel):
    room_rate_id: int
    overridden_rate: float
    stay_date: date


class OverriddenRoomRateCreate(OverriddenRoomRateBase):
    pass


class OverriddenRoomRateUpdate(OverriddenRoomRateBase):
    pass


class OverriddenRoomRate(OverriddenRoomRateBase):
    id: int

    class Config:
        orm_mode = True
