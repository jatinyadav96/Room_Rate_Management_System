from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.discount_room_rate_service import DiscountRoomRateService
from app.services.discount_service import DiscountService
from app.services.overridden_room_rates_service import OverriddenRoomRateService
from app.services.room_rate_service import RoomRateService


def get_room_rate_service(db: Session = Depends(get_db)) -> RoomRateService:
    return RoomRateService(db)


def get_overridden_room_rate_service(db: Session = Depends(get_db)):
    return OverriddenRoomRateService(db)


def get_discount_service(db: Session = Depends(get_db)):
    return DiscountService(db)


def get_discount_room_rate_service(db: Session = Depends(get_db)) -> DiscountRoomRateService:
    return DiscountRoomRateService(db)
