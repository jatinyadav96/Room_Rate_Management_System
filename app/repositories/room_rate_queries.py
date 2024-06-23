from typing import List, Optional
from typing import Type

from sqlalchemy.orm import Session

from app.core.exception import EntityNotFound
from app.models.room_rate import RoomRate as RoomRateORM, OverriddenRoomRate, Discount, DiscountRoomRate
from app.schemas import room_rate as schemas


class RoomRateQueries:
    def __init__(self, db: Session):
        self.db = db

    def create(self, room_rate: schemas.RoomRateCreate):
        db_room_rate = RoomRateORM(room_name=room_rate.room_name, default_rate=room_rate.default_rate)
        self.db.add(db_room_rate)
        self.db.commit()
        self.db.refresh(db_room_rate)
        return db_room_rate

    def update(self, room_id: int, room_rate: schemas.RoomRateUpdate):
        db_room_rate = self.db.query(RoomRateORM).filter(RoomRateORM.room_id == room_id).first()
        if db_room_rate is None:
            raise EntityNotFound(
                entity="RoomRate", pk_id_name=str(room_id)
            )
        for key, value in room_rate.dict(exclude_unset=True).items():
            setattr(db_room_rate, key, value)
        self.db.commit()
        self.db.refresh(db_room_rate)
        return db_room_rate

    def delete(self, room_id: int):
        db_room_rate = self.db.query(RoomRateORM).filter(RoomRateORM.room_id == room_id).first()
        if db_room_rate is None:
            raise EntityNotFound(
                entity="RoomRate", pk_id_name=str(room_id)
            )
        self.db.delete(db_room_rate)
        self.db.commit()
        return db_room_rate

    def get_room_rate_by_id(self, room_id: int) -> Type[schemas.RoomRate]:
        res = self.db.query(RoomRateORM).filter(RoomRateORM.room_id == room_id).first()
        if not res:
            raise EntityNotFound(
                entity="RoomRate", pk_id_name=str(room_id)
            )
        return res

    def list_all(self, skip: int = 0, limit: int = 10) -> List[Type[schemas.RoomRate]]:
        return self.db.query(RoomRateORM).offset(skip).limit(limit).all()

    def get_overridden_room_rate_by_date(self, room_rate_id: int, date: str) -> Optional[OverriddenRoomRate]:
        return self.db.query(OverriddenRoomRate).filter(
            OverriddenRoomRate.room_rate_id == room_rate_id,
            OverriddenRoomRate.stay_date == date
        ).first()

    def get_discounts_by_room_rate_id(self, room_rate_id: int) -> List[Discount]:
        return self.db.query(Discount).join(
            DiscountRoomRate, DiscountRoomRate.discount_id == Discount.discount_id
        ).filter(DiscountRoomRate.room_rate_id == room_rate_id).all()
