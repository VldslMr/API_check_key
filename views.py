from urllib.parse import urlparse

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from database import Keys, SessionLocal

root_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@root_router.post(path='/on_play')
def check_key(url, response: Response, db: Session = Depends(get_db),):
    key_url = urlparse(url).path.split('/')[-1]
    db_key = db.query(Keys).filter(Keys.key == key_url).one_or_none()
    response.status_code = 200 if db_key else 404
