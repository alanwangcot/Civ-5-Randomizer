from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel, QSpacerItem, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon, QFont
from Misc import resource_path, MY_FONT
from WordOutline import WordOutline
from Cards import WonderCard

class WonderDialog(QDialog):
    confirmed_signal = pyqtSignal()
    def __init__(self, num_players:int, wonders:list):
        super().__init__()

        self.setWindowTitle("随机奇迹")
        self.setWindowIcon(QIcon(resource_path("assets/icons/civ.png")))

        layout = QGridLayout()
        for i in range(num_players):
            player_label = QLabel("玩家" + str(i + 1))
            player_label.setFont(QFont(MY_FONT, 20))
            # player_label.setFlat(True)
            outline_effect = WordOutline()
            player_label.setGraphicsEffect(outline_effect)
            layout.addWidget(player_label, i, 0)
            curr_wonders = wonders[i]
            for j in range(3):
                wonder_icon = resource_path("assets/wonders/" + curr_wonders[j] + ".png")
                wonder_card = WonderCard(curr_wonders[j], wonder_icon)
                layout.addWidget(wonder_card, i, j + 1)
        button = QPushButton("确定")
        button.clicked.connect(self.ConfirmClicked)
        layout.addWidget(button, num_players + 1, 1)
        self.setLayout(layout)

    def ConfirmClicked(self):
        self.confirmed_signal.emit()
        self.close()