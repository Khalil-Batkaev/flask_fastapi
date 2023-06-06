from datetime import date
from pydantic import BaseModel, Field, EmailStr, PositiveInt, StrictStr, SecretStr, StrictBool

"""
Каждая задача должна содержать поля "название", "описание" и "статус" (выполнена/не выполнена).
"""

__all__ = (
    'Task',
    'CreateTask',
)


class TaskField:
    id = Field(description="Task id", example=1)
    title = Field(description="Title of task", example='Go work!')
    description = Field(description="Description of task", example='Do anything')
    status = Field(description="Status of task", example=False)


class Task(BaseModel):
    id: PositiveInt = TaskField.id
    title: StrictStr = TaskField.title
    description: StrictStr = TaskField.description
    status: StrictBool = TaskField.status


class CreateTask(BaseModel):
    title: StrictStr = TaskField.title
    description: StrictStr = TaskField.description
    status: StrictBool = TaskField.status
