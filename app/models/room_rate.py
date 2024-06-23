from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.core.database import Base


class RoomRate(Base):
    __tablename__ = "room_rates"
    room_id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String(255), index=True)
    default_rate = Column(DECIMAL(10, 2))


class OverriddenRoomRate(Base):
    __tablename__ = "overridden_room_rates"
    id = Column(Integer, primary_key=True, index=True)
    room_rate_id = Column(Integer, ForeignKey("room_rates.room_id"))
    overridden_rate = Column(DECIMAL(10, 2))
    stay_date = Column(Date)
    room_rate = relationship("RoomRate")


class Discount(Base):
    __tablename__ = "discounts"
    discount_id = Column(Integer, primary_key=True, index=True)
    discount_name = Column(String(255), index=True)
    discount_type = Column(String(100), index=True)
    discount_value = Column(DECIMAL(10, 2))


class DiscountRoomRate(Base):
    __tablename__ = "discount_room_rates"
    id = Column(Integer, primary_key=True, index=True)
    room_rate_id = Column(Integer, ForeignKey("room_rates.room_id"))
    discount_id = Column(Integer, ForeignKey("discounts.discount_id"))
    room_rate = relationship("RoomRate")
    discount = relationship("Discount")
