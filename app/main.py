from fastapi import FastAPI

from app.api.v1.routers import room_rate, discount, overridden_room_rate, discount_room_rate
from app.core.exception import entity_not_found_exception_handler, EntityNotFound

app = FastAPI()

app.include_router(room_rate.router, prefix="/api/v1", tags=["room_rates"])
app.include_router(discount.router, prefix="/api/v1", tags=["discount"])
app.include_router(overridden_room_rate.router, prefix="/api/v1", tags=["overridden_room_rate"])
app.include_router(discount_room_rate.router, prefix="/api/v1", tags=["discount_room_rate"])

app.add_exception_handler(EntityNotFound, entity_not_found_exception_handler)


@app.on_event("startup")
async def startup():
    from app.core.database import database
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    from app.core.database import database
    await database.disconnect()
