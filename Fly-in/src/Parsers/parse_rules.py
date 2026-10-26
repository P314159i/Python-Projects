from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum

class Zones(str, Enum):
    NORMAL = "normaal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "Priority"


class Parsemodes(BaseModel):
    start = Field(min_length=1, pattern=r"^[^\s-]+$")
    end = Field(min_length=1, pattern="r^[^\s-]+$")
    num = Field(ge=2)
    zone = Zones | None
    color = str | None
