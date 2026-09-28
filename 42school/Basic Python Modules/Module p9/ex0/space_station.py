from datetime import datetime
from pydantic import BaseModel, Field, ValidationError

# pydentic model class, a data model class, sets rules for instances
class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0) # ge: <=
    last_maintenance: datetime # last maintencnace date & time
    station_is_operational: bool = True
    optional_notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-09-28T12:00:00",
    )
    