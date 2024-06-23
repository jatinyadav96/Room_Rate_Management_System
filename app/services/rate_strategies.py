from abc import ABC, abstractmethod
from typing import Optional, List
from app.models.room_rate import RoomRate, OverriddenRoomRate, Discount


class RateStrategy(ABC):
    @abstractmethod
    def calculate_rate(self, room_rate: RoomRate, overridden_rate: Optional[OverriddenRoomRate],
                       discounts: Optional[List[Discount]]) -> float:
        pass


class DefaultRateStrategy(RateStrategy):
    def calculate_rate(self, room_rate: RoomRate, overridden_rate: Optional[OverriddenRoomRate],
                       discounts: Optional[List[Discount]]) -> float:
        return room_rate.default_rate


class OverriddenRateStrategy(RateStrategy):
    def calculate_rate(self, room_rate: RoomRate, overridden_rate: Optional[OverriddenRoomRate],
                       discounts: Optional[List[Discount]]) -> float:
        return overridden_rate.overridden_rate if overridden_rate else room_rate.default_rate


class DiscountRateStrategy(RateStrategy):
    def calculate_rate(self, room_rate: RoomRate, overridden_rate: Optional[OverriddenRoomRate],
                       discounts: Optional[List[Discount]]) -> float:
        base_rate = overridden_rate.overridden_rate if overridden_rate else room_rate.default_rate
        if discounts:
            highest_discount = max(discount.discount_value for discount in discounts)
            return base_rate - highest_discount
        return base_rate
