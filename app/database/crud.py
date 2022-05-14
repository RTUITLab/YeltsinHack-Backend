from uuid import UUID
from sqlalchemy.orm import Session

from app.database import models, schemas


def create_area(db: Session, area: schemas.AreaCreate):
    area_db = models.Area(name=area.name)
    db.add(area_db)
    db.flush()
    for poin in area.points:
        point_db = models.Point(area_id=area_db.uuid, **poin.dict())
        db.add(point_db)
        db.flush()
    db.commit()


def get_areas(db: Session, uuid: UUID = None):
    query = db.query(models.Area)
    if uuid:
        query = query.filter_by(uuid=uuid)
    return query.all()
