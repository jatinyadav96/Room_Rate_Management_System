from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.v1.deps import get_overridden_room_rate_service
from app.schemas.overridden_room_rate import OverriddenRoomRate, OverriddenRoomRateCreate, OverriddenRoomRateUpdate
from app.services.overridden_room_rates_service import OverriddenRoomRateService

router = APIRouter()


@router.post("/overridden_room_rates/", response_model=OverriddenRoomRate)
def create_overridden_room_rate(overridden_room_rate_create: OverriddenRoomRateCreate,
                                service: OverriddenRoomRateService = Depends(get_overridden_room_rate_service)):
    return service.create(overridden_room_rate_create)


@router.get("/overridden_room_rates/{id}", response_model=OverriddenRoomRate)
def read_overridden_room_rate(id: int, service: OverriddenRoomRateService = Depends(get_overridden_room_rate_service)):
    overridden_room_rate = service.get_by_id(id)
    if not overridden_room_rate:
        raise HTTPException(status_code=404, detail="Overridden room rate not found")
    return overridden_room_rate


@router.put("/overridden_room_rates/{id}", response_model=OverriddenRoomRate)
def update_overridden_room_rate(id: int, overridden_room_rate_update: OverriddenRoomRateUpdate,
                                service: OverriddenRoomRateService = Depends(get_overridden_room_rate_service)):
    overridden_room_rate = service.update(id, overridden_room_rate_update)
    if not overridden_room_rate:
        raise HTTPException(status_code=404, detail="Overridden room rate not found")
    return overridden_room_rate


@router.delete("/overridden_room_rates/{id}", response_model=OverriddenRoomRate)
def delete_overridden_room_rate(id: int,
                                service: OverriddenRoomRateService = Depends(get_overridden_room_rate_service)):
    overridden_room_rate = service.delete(id)
    if not overridden_room_rate:
        raise HTTPException(status_code=404, detail="Overridden room rate not found")
    return overridden_room_rate
