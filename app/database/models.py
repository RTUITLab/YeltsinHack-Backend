import uuid

from datetime import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import DataBase


class Camera(DataBase):
    __tablename__ = "camera"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True)

    areas = relationship("Area")
    stats = relationship("CameraStats")


class Point(DataBase):
    __tablename__ = "point"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    x = Column(Float)
    y = Column(Float)
    area_uuid = Column(UUID(as_uuid=True), ForeignKey("area.uuid"))
    camera_stats_uuid = Column(UUID(as_uuid=True), ForeignKey("camera_stats.uuid"))


class Area(DataBase):
    __tablename__ = "area"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    camera_uuid = Column(UUID(as_uuid=True), ForeignKey("camera.uuid"))

    points = relationship("Point")
    stats = relationship("AreaStats")


class AreaStats(DataBase):
    __tablename__ = "area_stats"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    area_uuid = Column(UUID(as_uuid=True), ForeignKey("area.uuid"))
    time = Column(DateTime, default=datetime.now)
    count = Column(Float)


class CameraStats(DataBase):
    __tablename__ = "camera_stats"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    camera_uuid = Column(UUID(as_uuid=True), ForeignKey("camera.uuid"))
    time = Column(DateTime, default=datetime.now)

    points = relationship("Point")
