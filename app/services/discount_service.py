from typing import Optional, Type

from sqlalchemy.orm import Session

from app.repositories.discount_queries import DiscountQueries
from app.schemas.discount import Discount, DiscountCreate, DiscountUpdate


class DiscountService:
    def __init__(self, db: Session):
        self.queries = DiscountQueries(db)

    def create(self, discount_create: DiscountCreate) -> Discount:
        return self.queries.create(discount_create)

    def get_by_id(self, id: int) -> Type[Discount]:
        return self.queries.get_by_id(id)

    def update(self, id: int, discount_update: DiscountUpdate) -> Optional[Discount]:
        return self.queries.update(id, discount_update)

    def delete(self, id: int) -> Optional[Discount]:
        return self.queries.delete(id)
