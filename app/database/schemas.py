from datetime import datetime
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
    area_uuid: UUID or str


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
    camera_uuid: UUID or str


class AreaStatsBase(BaseModel):
    count: float


class AreaStatsCreate(AreaStatsBase):
    area_uuid: UUID


class AreaStats(AreaStatsBase):
    uuid: UUID
    time: datetime

    class Config:
        orm_mode = True


class Area(AreaBase):
    uuid: UUID or str
    points: List[Point]
    stats: List[AreaStats]

    class Config:
        orm_mode = True
# endregion


# region Camera
class CameraBase(BaseModel):
    name: str


class CameraCreate(CameraBase):
    pass


# class CameraStatsBase(BaseModel):
#     camera_uuid: UUID or str


# class CameraStatsCreate(CameraStatsBase):
#     pass


class CameraStats(BaseModel):
    uuid: UUID or str
    time: datetime
    points: List[Point]

    class Config:
        orm_mode = True


class Camera(CameraBase):
    uuid: UUID or str
    areas: List[Area]
    stats: List[CameraStats]

    class Config:
        orm_mode = True
# endregion


class CamStatsCreate(BaseModel):
    uuid: UUID
    points: List[PointBase]


class StatsCreate(BaseModel):
    areas: dict
    camera: List[CamStatsCreate]
