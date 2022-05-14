from fastapi import APIRouter, Depends, Response


from ..database import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/stats",
    tags=["Stats"]
)


# @router.get("", response_model=List[schemas.Area])
# async def get_areas(
#     uuid: UUID = None,
#     camera_uuid: UUID = None,
#     db=Depends(get_db)
# ):
#     areas = crud.get_areas(db, uuid, camera_uuid)
#     if not areas:
#         raise HTTPException(status_code=404, detail="No areas")
#     return areas


@router.post("")
async def create_stats(
    stats: schemas.StatsCreate,
    db=Depends(get_db)
):
    crud.create_stats(db, stats)
    return Response(status_code=204)
