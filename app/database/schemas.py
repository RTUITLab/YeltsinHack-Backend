from typing import List
from pydantic import BaseModel
from uuid import UUID


# region Token
class Token(BaseModel):
    access_token: str
    token_type: str
# endregion


# region Point
class PointBase(BaseModel):
    x: float
    y: float


class PointCreate(PointBase):
    pass


class Point(PointBase):
    uuid: UUID or str

    class Config:
        orm_mode = True
# endregion


# region Area
class AreaBase(BaseModel):
    name: str
    points: List[PointBase]


class AreaCreate(AreaBase):
    pass


class Area(AreaBase):
    uuid: UUID or str
    points: List[Point]

    class Config:
        orm_mode = True
# endregion
