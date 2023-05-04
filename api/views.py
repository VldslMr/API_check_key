import logging

from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.orm import Session

from api.database import Keys, SessionLocal
from api.search_value import search_value

root_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


logging.basicConfig(level=logging.DEBUG)


@root_router.post(path='/on_publish')
async def check_key(response: Response,
                    request: Request,
                    db: Session = Depends(get_db)):
    body_request = await request.body()
    logging.info(f'{body_request}, type: {type(body_request)}')
    request_key = search_value(body_request, 'name')
    logging.info(f'{request_key}, type: {type(request_key)}')
    db_key = db.query(Keys).filter(Keys.key == request_key).one_or_none()
    response.status_code = 200 if db_key else 404
