from typing import Optional, Type

from sqlalchemy.orm import Session

from app.core.exception import EntityNotFound
from app.models.room_rate import DiscountRoomRate
from app.schemas import discount_room_rate as schemas


class DiscountRoomRateQueries:
    def __init__(self, db: Session):
        self.db = db

    def create(self, discount_room_rate: schemas.DiscountRoomRateCreate) -> DiscountRoomRate:
        discount_room_rate = DiscountRoomRate(**discount_room_rate.dict())
        self.db.add(discount_room_rate)
        self.db.commit()
        self.db.refresh(discount_room_rate)
        return discount_room_rate

    def get_by_id(self, id: int) -> Type[DiscountRoomRate]:
        res = self.db.query(DiscountRoomRate).filter(DiscountRoomRate.id == id).first()
        if not res:
            raise EntityNotFound(
                entity="DiscountRoomRate", pk_id_name=str(id)
            )
        return res

    def update(self, id: int, discount_room_rate_update: schemas.DiscountRoomRateUpdate) -> Optional[Type[DiscountRoomRate]]:
        db_discount_room_rate = self.db.query(DiscountRoomRate).filter(DiscountRoomRate.id == id).first()
        if not db_discount_room_rate:
            raise EntityNotFound(
                entity="DiscountRoomRate", pk_id_name=str(id)
            )
        for key, value in discount_room_rate_update.items():
            setattr(db_discount_room_rate, key, value)
        self.db.commit()
        self.db.refresh(db_discount_room_rate)
        return db_discount_room_rate

    def delete(self, id: int) -> Optional[Type[DiscountRoomRate]]:
        db_discount_room_rate = self.db.query(DiscountRoomRate).filter(DiscountRoomRate.id == id).first()
        if not db_discount_room_rate:
            return None
        self.db.delete(db_discount_room_rate)
        self.db.commit()
        return db_discount_room_rate
