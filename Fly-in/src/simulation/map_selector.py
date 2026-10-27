from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from src.Parsers.map_parser import MapParser


def map_pick() -> dict[str, list[Path]]:

    folder_links: dict[str, list[Path]] = {}

    path_links = [
        folder for folder in Path("maps").iterdir()
        if folder.is_dir()
    ]

    for folder in path_links:
        folder_links[folder.name] = list(folder.glob("*.txt"))

    return folder_links


def show_window() -> str:

    qapp = QApplication([])
    qDiffPick = QComboBox()
    qmapPick = QComboBox()
    qwidgt = QWidget()
    layout = QVBoxLayout()
    qwidgt.setLayout(layout)

    folder_links = map_pick() # from folders

    update_maps = lambda mp:(
        qmapPick.clear(),
        qmapPick.addItems([l.name for l in folder_links[mp]]),
        qmapPick.show()
    )

    qmapPick.hide()

    qDiffPick.addItems(list(folder_links.keys()))
    qDiffPick.setFixedWidth(240)
    qmapPick.setFixedWidth(240)
    qDiffPick.currentTextChanged.connect
    qDiffPick.setCurrentIndex(-1)
    qwidgt.resize(650, 650)
    qwidgt.setWindowOpacity(0.75)

    title = QLabel("Pick your battle")
    title.setStyleSheet("font-size: 35px; font-weight: bold; color: white;")

    qwidgt.setObjectName("mainWindow")
    qwidgt.setStyleSheet("""
        QWidget#mainWindow {
            border-image: url("drone.jpg") 0 0 0 0 stretch stretch;
        }
    """)

    layout.addStretch()
    layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter)
    layout.addSpacing(10)
    layout.addWidget(qDiffPick, alignment=Qt.AlignmentFlag.AlignHCenter)
    qDiffPick.currentTextChanged.connect(update_maps)
    layout.addWidget(qmapPick, alignment=Qt.AlignmentFlag.AlignHCenter)
    layout.addStretch()

    qwidgt.show()
    qapp.exec()

    def on_map_selected(filename: str) -> None:
        path = Path("maps") / qDiffPick.currentText() / filename
        parser = MapParser(str(path))
        parser.parse_drone()
        parser.parse_hub()

    qmapPick.textActivated.connect(on_map_selected)



show_window()