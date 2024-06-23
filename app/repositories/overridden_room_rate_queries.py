from typing import List
from typing import Type

from sqlalchemy.orm import Session

from app.core.exception import EntityNotFound
from app.models.room_rate import OverriddenRoomRate
from app.schemas import overridden_room_rate as schemas


class OverriddenRoomRateQueries:
    def __init__(self, db: Session):
        self.db = db

    def create(self, overridden_room_rates: schemas.OverriddenRoomRateCreate):
        db_overridden_room_rates = OverriddenRoomRate(**overridden_room_rates.dict())
        self.db.add(db_overridden_room_rates)
        self.db.commit()
        self.db.refresh(db_overridden_room_rates)
        return db_overridden_room_rates

    def update(self, id: int, overridden_room_rates: schemas.OverriddenRoomRateUpdate):
        db_overridden_room_rates = self.db.query(OverriddenRoomRate).filter(OverriddenRoomRate.id == id).first()
        if db_overridden_room_rates is None:
            return None
        for key, value in overridden_room_rates.dict(exclude_unset=True).items():
            setattr(db_overridden_room_rates, key, value)
        self.db.commit()
        self.db.refresh(db_overridden_room_rates)
        return db_overridden_room_rates

    def delete(self, id: int):
        db_overridden_room_rates = self.db.query(OverriddenRoomRate).filter(OverriddenRoomRate.id == id).first()
        if db_overridden_room_rates is None:
            raise ValueError("RoomRate not found")
        self.db.delete(db_overridden_room_rates)
        self.db.commit()
        return db_overridden_room_rates

    def get_by_id(self, id: int) -> Type[schemas.OverriddenRoomRate]:
        res = self.db.query(OverriddenRoomRate).filter(OverriddenRoomRate.id == id).first()
        if not res:
            raise EntityNotFound(
                entity="RoomRate", pk_id_name=str(id)
            )
        return res

    def list_all(self, skip: int = 0, limit: int = 10) -> List[Type[schemas.OverriddenRoomRate]]:
        return self.db.query(OverriddenRoomRate).offset(skip).limit(limit).all()
