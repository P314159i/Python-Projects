from datetime import datetime
from pydantic import BaseModel, Field, ValidationError

# pydentic model class, a data model class, sets rules for instances
class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0) # ge: >=
    last_maintenance: datetime # last maintencnace date & time
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    station = SpaceStation( # pydentic checks every value
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-09-28T12:00:00",
        is_operational=True
    )
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(
        f"Status: {'Operational' if station.is_operational else 'Offline'}"
    )

    try:
        SpaceStation(
            station_id="BAD001",
            name="Invalid Station",
            crew_size=50,
            power_level=80.0,
            oxygen_level=90.0,
            last_maintenance="2026-09-28T12:00:00"
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
