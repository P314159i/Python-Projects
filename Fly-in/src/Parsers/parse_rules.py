from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum

class Zones(str, Enum):
    NORMAL = "normaal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "Priority"


class Parsemodes(BaseModel):
    start:str = Field(min_length=1, pattern=r"^[^\s-]+$")
    end: str = Field(min_length=1, pattern="r^[^\s-]+$")
    num: int = Field(ge=1)
    zone: Zones | None = None
    color: str | None = None
