from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Response
from typing import List


from ..database import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/areas",
    tags=["Areas"]
)


@router.get("", response_model=List[schemas.Area])
async def get_areas(
    uuid: UUID = None,
    camera_uuid: UUID = None,
    db=Depends(get_db)
):
    areas = crud.get_areas(db, uuid, camera_uuid)
    if not areas:
        raise HTTPException(status_code=404, detail="No areas")
    return areas


@router.post("")
async def create_areas(
    area: schemas.AreaCreate,
    db=Depends(get_db)
):
    crud.create_area(db, area)
    return Response(status_code=204)
