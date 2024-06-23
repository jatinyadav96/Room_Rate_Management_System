from typing import List

from sqlalchemy.orm import Session

from app.repositories.room_rate_queries import RoomRateQueries
from app.schemas.room_rate import RoomRate, RoomRateCreate, RoomRateUpdate
from app.services.rate_strategies import DiscountRateStrategy, DefaultRateStrategy


class RoomRateService:
    def __init__(self, db: Session):
        self.queries = RoomRateQueries(db)

    def create_room_rate(self, room_rate_data: RoomRateCreate) -> RoomRate:
        return self.queries.create(room_rate_data)

    def update_room_rate(self, room_id: int, room_rate_data: RoomRateUpdate) -> RoomRate:
        return self.queries.update(room_id, room_rate_data)

    def delete_room_rate(self, room_id: int):
        return self.queries.delete(room_id)

    def get_room_rate(self, room_id: int):
        return self.queries.get_room_rate_by_id(room_id)

    def list_room_rates(self, skip: int = 0, limit: int = 10):
        return self.queries.list_all(skip, limit)

    def get_final_rate(self, room_rate_id: int, date: str) -> float:
        room_rate = self.get_room_rate(room_rate_id)
        overridden_rate = self.queries.get_overridden_room_rate_by_date(room_rate_id, date)
        discounts = self.queries.get_discounts_by_room_rate_id(room_rate_id)

        if overridden_rate:
            strategy = DiscountRateStrategy()
        else:
            strategy = DefaultRateStrategy() if not discounts else DiscountRateStrategy()

        return strategy.calculate_rate(room_rate, overridden_rate, discounts)

    def list_final_rates(self, room_id: int, start_date: str, end_date: str) -> List[dict]:
        room_rate = self.get_room_rate(room_id)
        result = []
        for date in self.date_range(start_date, end_date):
            final_rate = self.get_final_rate(room_rate.room_id, date)
            result.append({
                "room_rate_id": room_rate.room_id,
                "date": date,
                "final_rate": final_rate
            })
        return result

    def date_range(self, start_date: str, end_date: str) -> List[str]:
        from datetime import datetime, timedelta
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        delta = end - start
        return [(start + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]
