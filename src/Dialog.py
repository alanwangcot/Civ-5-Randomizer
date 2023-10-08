from PyQt6.QtWidgets import QDialog, QGridLayout, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, pyqtSignal
from Misc import MY_FONT, resource_path


class Dialog(QDialog):

    dialog_confirmed = pyqtSignal()
    def __init__(self, text):
        super().__init__()

        self.setWindowTitle('错误！')
        self.setWindowIcon(QIcon(resource_path("assets/icons/civ.png")))
        self.setFixedSize(300,100)
        dialog_label = QLabel(text)
        dialog_label.setFont(QFont(MY_FONT,12))
        dialog_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dialog_layout = QGridLayout()
        dialog_layout.addWidget(dialog_label, 0, 0)

        button = QPushButton("确定")
        button.setFont(QFont(MY_FONT, 12))
        button.clicked.connect(self.confirmDialog)
        dialog_layout.addWidget(button, 1, 0)

        self.setLayout(dialog_layout)

    def confirmDialog(self):
        self.dialog_confirmed.emit()
        self.close()