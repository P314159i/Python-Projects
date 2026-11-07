from pathlib import Path
from PySide6.QtWidgets import QComboBox


def map_pick() -> dict[str, list[Path]]:
    ''' itterates through folders and finds all .txt maps '''

    folder_links: dict[str, list[Path]] = {}

    path_links = [
        folder for folder in Path("maps").iterdir()
        if folder.is_dir()
    ]

    for folder in path_links: # .name on path: return final part of the path(name)
        folder_links[folder.name] = list(folder.glob("*.txt"))

    return folder_links


def on_map_selected(DiffPick: str, filename: str) -> None:
    ''' gets the selected map (from GUI) and parse it '''

    from .map_parser import MapParser

    path = Path("maps") / DiffPick / filename
    parser = MapParser(str(path))
    parser.parse()

    return parser
