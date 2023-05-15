import uvicorn
from fastapi import FastAPI

from api.database import Base, engine
from api.views import root_router
from api.settings import Settings


Base.metadata.create_all(bind=engine)

app = FastAPI()

settings = Settings()

app.include_router(root_router)


if __name__ == '__main__':
    uvicorn.run(app, host=settings.host, port=settings.port)
