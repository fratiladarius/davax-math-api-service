from datetime import datetime

from pydantic import BaseModel, Field


class RequestEntry(BaseModel):
    id: int | None = None
    op_type: str
    input_args: list[int]
    result: int
    timestamp: datetime = Field(default_factory=datetime.now)
