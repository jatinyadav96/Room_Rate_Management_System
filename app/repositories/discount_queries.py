from typing import List
from typing import Type

from sqlalchemy.orm import Session

from app.core.exception import EntityNotFound
from app.models.room_rate import Discount
from app.schemas import discount as schemas


class DiscountQueries:
    def __init__(self, db: Session):
        self.db = db

    def create(self, discount: schemas.DiscountCreate):
        db_discount = Discount(discount_name=discount.discount_name, discount_type=discount.discount_type,
                               discount_value=discount.discount_value)
        self.db.add(db_discount)
        self.db.commit()
        self.db.refresh(db_discount)
        return db_discount

    def update(self, discount_id: int, discount: schemas.DiscountUpdate):
        db_discount = self.db.query(Discount).filter(Discount.discount_id == discount_id).first()
        if db_discount is None:
            return None
        for key, value in discount.dict(exclude_unset=True).items():
            setattr(db_discount, key, value)
        self.db.commit()
        self.db.refresh(db_discount)
        return db_discount

    def delete(self, discount_id: int):
        db_discount = self.db.query(Discount).filter(Discount.discount_id == discount_id).first()
        if db_discount is None:
            raise ValueError("RoomRate not found")
        self.db.delete(db_discount)
        self.db.commit()
        return db_discount

    def get_by_id(self, discount_id: int) -> Type[schemas.Discount]:
        res = self.db.query(Discount).filter(Discount.discount_id == discount_id).first()
        if not res:
            raise EntityNotFound(
                entity="RoomRate", pk_id_name=str(discount_id)
            )
        return res

    def list_all(self, skip: int = 0, limit: int = 10) -> List[Type[schemas.Discount]]:
        return self.db.query(Discount).offset(skip).limit(limit).all()
