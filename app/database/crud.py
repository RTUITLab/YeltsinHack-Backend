from uuid import UUID
from sqlalchemy.orm import Session

from app.database import models, schemas


def create_area(db: Session, area: schemas.AreaCreate):
    area_db = models.Area(name=area.name, camera_uuid=area.camera_uuid)
    db.add(area_db)
    db.flush()
    for point in area.points:
        point_db = models.Point(area_uuid=area_db.uuid, **point.dict())
        db.add(point_db)
        db.flush()
    db.commit()


def get_areas(db: Session, uuid: UUID = None, camera_uuid: UUID = None):
    query = db.query(models.Area)
    if camera_uuid:
        query = query.filter_by(uuid=camera_uuid)
    if uuid:
        query = query.filter_by(uuid=uuid)
    return query.all()


def create_camera(db: Session, camera: schemas.CameraCreate):
    camera_db = models.Camera(**camera.dict())
    db.add(camera_db)
    db.commit()


def get_cameras(db: Session, uuid: UUID = None):
    query = db.query(models.Camera)
    if uuid:
        query = query.filter_by(uuid=uuid)
    return query.all()
