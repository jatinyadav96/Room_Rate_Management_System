from typing import List

from fastapi import APIRouter
from fastapi import Depends, HTTPException

from app.api.v1.deps import get_room_rate_service
from app.schemas.room_rate import RoomRate, RoomRateCreate, RoomRateUpdate
from app.services.room_rate_service import RoomRateService

router = APIRouter()


@router.post("/room_rates/", response_model=RoomRate)
def create_room_rate(room_rate: RoomRateCreate, service: RoomRateService = Depends(get_room_rate_service)):
    try:
        return service.create_room_rate(room_rate)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/room_rates/{room_id}", response_model=RoomRate)
def update_room_rate(room_id: int, room_rate: RoomRateUpdate,
                     service: RoomRateService = Depends(get_room_rate_service)):
    try:
        return service.update_room_rate(room_id, room_rate)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/room_rates/{room_id}", response_model=RoomRate)
def delete_room_rate(room_id: int, service: RoomRateService = Depends(get_room_rate_service)):
    try:
        return service.delete_room_rate(room_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/room_rates/{room_id}", response_model=RoomRate)
def get_room_rate(room_id: int, service: RoomRateService = Depends(get_room_rate_service)):
    room_rate = service.get_room_rate(room_id)
    if not room_rate:
        raise HTTPException(status_code=404, detail="RoomRate not found")
    return room_rate

#
# @router.get("/room_rates/", response_model=List[RoomRate])
# def list_room_rates(skip: int = 0, limit: int = 10, service: RoomRateService = Depends(get_room_rate_service)):
#     return service.list_room_rates(skip, limit)


@router.get("/room_rates/{room_id}/", response_model=List[dict])
def list_final_room_rates(room_id: int, start_date: str, end_date: str,
                          service: RoomRateService = Depends(get_room_rate_service)):
    return service.list_final_rates(room_id, start_date, end_date)
