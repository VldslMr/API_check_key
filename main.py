import uvicorn
from fastapi import FastAPI

from api.database import Base, engine
from api.views import root_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(root_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
