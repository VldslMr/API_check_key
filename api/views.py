import logging

from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.orm import Session

from api.database import get_db, Keys

root_router = APIRouter()


logging.basicConfig(level=logging.DEBUG)


@root_router.post(path='/on_publish')
async def on_publish(response: Response,
                     request: Request,
                     db: Session = Depends(get_db)):
    form_data = await request.form()
    logging.info(f'{form_data}, type: {type(form_data)}')
    request_key = form_data.get('name')
    logging.info(f'{request_key}, type: {type(request_key)}')
    db_key = db.query(Keys).filter(Keys.key == request_key).one_or_none()
    response.status_code = 200 if db_key else 404
