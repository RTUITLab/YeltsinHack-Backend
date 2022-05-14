from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Response
from typing import List


from ..database import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/cameras",
    tags=["Cameras"]
)


@router.get("", response_model=List[schemas.Camera])
async def get_cameras(uuid: UUID = None, db=Depends(get_db)):
    cameras = crud.get_cameras(db, uuid)
    if not cameras:
        raise HTTPException(status_code=404, detail="No cameras")
    return cameras


@router.post("")
async def create_cameras(
    camera: schemas.CameraCreate,
    db=Depends(get_db)
):
    crud.create_camera(db, camera)
    return Response(status_code=204)
