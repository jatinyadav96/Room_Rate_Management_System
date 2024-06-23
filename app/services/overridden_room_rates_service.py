from typing import Optional, Type

from sqlalchemy.orm import Session

from app.repositories.overridden_room_rate_queries import OverriddenRoomRateQueries
from app.schemas.overridden_room_rate import OverriddenRoomRateCreate, OverriddenRoomRateUpdate, OverriddenRoomRate


class OverriddenRoomRateService:
    def __init__(self, db: Session):
        self.queries = OverriddenRoomRateQueries(db)

    def create(self, overridden_room_rate_create: OverriddenRoomRateCreate) -> OverriddenRoomRate:
        return self.queries.create(overridden_room_rate_create)

    def get_by_id(self, id: int) -> Type[OverriddenRoomRate]:
        return self.queries.get_by_id(id)

    def update(self, id: int, overridden_room_rate_update: OverriddenRoomRateUpdate) -> Optional[OverriddenRoomRate]:
        return self.queries.update(id, overridden_room_rate_update)

    def delete(self, id: int) -> Optional[OverriddenRoomRate]:
        return self.queries.delete(id)
