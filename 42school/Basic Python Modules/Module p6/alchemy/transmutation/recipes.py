from alchemy import *
from elements import create_fire

def lead_to_gold() -> str:

    created_fire: str = create_fire()
    created_air: str = create_air()
    created_strength_potion: str = strength_potion()

    return (f"\n\n✨ Recipe transmuting Lead to Gold:\n\n\n"
            f" ⚗️   brew        {created_air} &\n"
            f"                  {created_strength_potion}\n"
            f"\n ⚗️   mixed with  {created_fire}\n\n"
            "\n\n    · · ─ ·☽𖤓☾· ─ · ·-    \n\n")
