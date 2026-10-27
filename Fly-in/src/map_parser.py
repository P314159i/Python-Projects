from pathlib import Path

def map_pick() -> str:

    from pathlib import Path

    folder_links: dict[str, list[Path]] = {}

    path_links = [
        folder for folder in Path("../maps").iterdir()
        if folder.is_dir()
    ]

    for folder in path_links:
        folder_links[folder.name] = list(folder.glob("*.txt"))

    for folder, files in folder_links.items():
        for file in files:
            print(file.name)


map_pick()
