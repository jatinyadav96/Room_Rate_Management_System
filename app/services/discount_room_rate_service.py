from typing import List, Optional, Type
from sqlalchemy.orm import Session
from app.models.room_rate import DiscountRoomRate
from app.repositories.discount_room_rate_queries import DiscountRoomRateQueries
from app.schemas.discount_room_rate import DiscountRoomRateCreate, DiscountRoomRateUpdate


class DiscountRoomRateService:
    def __init__(self, db: Session):
        self.repository = DiscountRoomRateQueries(db)

    def create(self, discount_room_rate: DiscountRoomRateCreate) -> DiscountRoomRate:
        return self.repository.create(discount_room_rate)

    def get_by_id(self, id: int) -> Type[DiscountRoomRate]:
        return self.repository.get_by_id(id)

    def update(self, id: int, discount_room_rate_update: DiscountRoomRateUpdate) -> Optional[DiscountRoomRate]:
        return self.repository.update(id, discount_room_rate_update)

    def delete(self, id: int) -> Optional[DiscountRoomRate]:
        return self.repository.delete(id)
