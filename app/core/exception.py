import logging
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from urllib.request import Request
from starlette.responses import JSONResponse


@dataclass
class EntityNotFound(Exception):
    entity: str
    pk_id_name: Optional[str]


@dataclass
class DatabaseError(Exception):
    message: str


@dataclass
class SQLParamArgNotFoundError(Exception):
    message: str


async def entity_not_found_exception_handler(request: Request, ex: EntityNotFound):
    message = f"Entity {ex.entity} with pk_id_name {ex.pk_id_name} is not found"
    logging.error(f"{message}")

    return JSONResponse(
        status_code=404,
        content={"message": message},
    )
