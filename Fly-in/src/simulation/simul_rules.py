from pydantic import BaseModel, Field, model_validator, ValidationError


class Drone(BaseModel):
    name: str = Field()
    current_hub: str
    path: list[str]

    @property
    def next_hub(self) -> str | None:
        position = self.path.index(self.current_hub)
        if position + 1 >= len(self.path):
            return None
        return self.path[position + 1]

    @property
    def start(self) -> str:
        return self.path[0]

    @property
    def end(self) -> str:
        return self.path[-1]
