from . import create_air, create_earth
from elements import create_fire, create_water

created_earth_element: str = create_earth()
created_air_element: str = create_air()
created_fire_element: str = create_fire()
created_water_element: str = create_water()


def healing_potion() -> str:

    return (".☘︎ ݁˖Healing potion brewed with "
            f"'{created_earth_element}' &"
            f"'{created_air_element}'")


def strength_potion() -> str:

    return ("⚕ Strength potion brewed with "
            f"'{created_fire_element}' &"
            f"'{created_water_element}'")
