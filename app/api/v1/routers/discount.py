from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.discount import Discount, DiscountCreate, DiscountUpdate
from app.services.discount_service import DiscountService
from app.api.v1.deps import get_discount_service

router = APIRouter()


@router.post("/discounts/", response_model=Discount)
def create_discount(discount_create: DiscountCreate, service: DiscountService = Depends(get_discount_service)):
    return service.create(discount_create)


@router.get("/discounts/{discount_id}", response_model=Discount)
def read_discount(discount_id: int, service: DiscountService = Depends(get_discount_service)):
    discount = service.get_by_id(discount_id)
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return discount


@router.put("/discounts/{discount_id}", response_model=Discount)
def update_discount(discount_id: int, discount_update: DiscountUpdate,
                    service: DiscountService = Depends(get_discount_service)):
    discount = service.update(discount_id, discount_update)
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return discount


@router.delete("/discounts/{discount_id}", response_model=Discount)
def delete_discount(discount_id: int, service: DiscountService = Depends(get_discount_service)):
    discount = service.delete(discount_id)
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return discount
