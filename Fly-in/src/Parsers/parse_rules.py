from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum

class Zones(str, Enum):
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"

class Hubs(BaseModel):
    name: str = Field(min_length=1, pattern=r"^[^\s-]+$")
    x: int
    y: int
    zone: Zones = Zones.NORMAL
    color: str | None = None
    max_drones: int = Field(default=1, ge=1)

class Num(BaseModel):
    num: int = Field(ge=1)
