from pathlib import Path
from .map_parser import MapParser
from PySide6.QtWidgets import QComboBox


def map_pick() -> dict[str, list[Path]]:

    folder_links: dict[str, list[Path]] = {}

    path_links = [
        folder for folder in Path("maps").iterdir()
        if folder.is_dir()
    ]

    for folder in path_links:
        folder_links[folder.name] = list(folder.glob("*.txt"))

    return folder_links


def on_map_selected(qDiffPick: QComboBox, filename: str) -> str:
    path = Path("maps") / qDiffPick / filename
    parser = MapParser(str(path))
    parser.parse_drone()
    parser.parse_hub()
    print(parser.num, parser.start_hub, parser.end_hub)
    return path
