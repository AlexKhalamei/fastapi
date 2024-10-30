from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.models import create_tables, delete_tables
from app.routes.router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('The table was deleted')
    await create_tables()
    print('The table was created')
    yield
    print('Off')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
