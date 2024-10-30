from fastapi import APIRouter
from typing import Annotated
from fastapi.params import Depends

from app.repository.repository import TaskRepository
from app.schemas.schemas import STaskAdd, STaskGet, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"task_id": task_id}


@router.get("")
async def get_tasks() -> list[STaskGet]:
    tasks = await TaskRepository.find_all()
    return tasks
