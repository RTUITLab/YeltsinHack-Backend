import uuid

from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import DataBase


class Point(DataBase):
    __tablename__ = "point"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    x = Column(Float)
    y = Column(Float)
    area_id = Column(UUID(as_uuid=True), ForeignKey("area.uuid"))


class Area(DataBase):
    __tablename__ = "area"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)

    points = relationship("Point")
