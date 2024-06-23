from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.discount_room_rate import DiscountRoomRate, DiscountRoomRateCreate, DiscountRoomRateUpdate
from app.services.discount_room_rate_service import DiscountRoomRateService
from app.api.v1.deps import get_discount_room_rate_service

router = APIRouter()


@router.post("/discount_room_rates/", response_model=DiscountRoomRate)
def create_discount_room_rate(discount_room_rate_create: DiscountRoomRateCreate,
                              service: DiscountRoomRateService = Depends(get_discount_room_rate_service)):
    return service.create(discount_room_rate_create)


@router.get("/discount_room_rates/{id}", response_model=DiscountRoomRate)
def read_discount_room_rate(id: int, service: DiscountRoomRateService = Depends(get_discount_room_rate_service)):
    discount_room_rate = service.get_by_id(id)
    if not discount_room_rate:
        raise HTTPException(status_code=404, detail="Discount room rate not found")
    return discount_room_rate


@router.put("/discount_room_rates/{id}", response_model=DiscountRoomRate)
def update_discount_room_rate(id: int, discount_room_rate_update: DiscountRoomRateUpdate,
                              service: DiscountRoomRateService = Depends(get_discount_room_rate_service)):
    discount_room_rate = service.update(id, discount_room_rate_update)
    if not discount_room_rate:
        raise HTTPException(status_code=404, detail="Discount room rate not found")
    return discount_room_rate


@router.delete("/discount_room_rates/{id}", response_model=DiscountRoomRate)
def delete_discount_room_rate(id: int, service: DiscountRoomRateService = Depends(get_discount_room_rate_service)):
    discount_room_rate = service.delete(id)
    if not discount_room_rate:
        raise HTTPException(status_code=404, detail="Discount room rate not found")
    return discount_room_rate
