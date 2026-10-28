from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from src.Parsers.map_pick import map_pick, on_map_selected


def window() -> str:

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

    qmapPick.textActivated.connect(
        lambda filename: on_map_selected(qDiffPick.currentText(), filename)
    )

    qwidgt.show()
    qapp.exec()



window()