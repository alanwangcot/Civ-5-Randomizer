from PyQt6.QtWidgets import QDialog, QGridLayout, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
from Cards import CivCard
from PyQt6.QtCore import pyqtSignal, Qt
from WordOutline import WordOutline
from Misc import MY_FONT, resource_path

class ResultsDialog(QDialog):
    confirmed_signal = pyqtSignal()
    def __init__(self, num_civs, num_players, civs, datetime, seed):
        super().__init__()

        self.setWindowTitle('随机结果')
        self.setWindowIcon(QIcon(resource_path("assets/icons/civ.png")))

        layout = QGridLayout()
        datetime_label = QLabel("生成时间：" + datetime)
        datetime_label.setFont(QFont(MY_FONT, 7))
        datetime_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(datetime_label, 0, 0)
        seed_label = QLabel("种子：" + str(seed))
        seed_label.setFont(QFont(MY_FONT, 7))
        seed_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(seed_label, 0, 1)

        if (num_players == 10):
            for i in range(0, 5):
                player_label = QLabel("玩家" + str(i + 1))
                player_label.setFont(QFont(MY_FONT, 20))
                outline_effect = WordOutline()
                player_label.setGraphicsEffect(outline_effect)
                layout.addWidget(player_label, i + 1, 0)
                curr_civs = civs[i]
                for j in range(num_civs):
                    civ_icon = resource_path("assets/icons/" + curr_civs[j] + ".png")
                    civ_card = CivCard(curr_civs[j], civ_icon)
                    layout.addWidget(civ_card, i + 1, j + 1)
            for i in range(5, 10):
                player_label = QLabel("玩家" + str(i + 1))
                player_label.setFont(QFont(MY_FONT, 20))
                outline_effect = WordOutline()
                player_label.setGraphicsEffect(outline_effect)
                layout.addWidget(player_label, i - 4, num_civs + 2)
                curr_civs = civs[i]
                for j in range(num_civs):
                    civ_icon = resource_path("assets/icons/" + curr_civs[j] + ".png")
                    civ_card = CivCard(curr_civs[j], civ_icon)
                    layout.addWidget(civ_card, i - 4, j + num_civs + 3)
        else:
            for i in range(num_players):
                player_label = QLabel("玩家" + str(i + 1))
                player_label.setFont(QFont(MY_FONT, 20))
                # player_label.setFlat(True)
                outline_effect = WordOutline()
                player_label.setGraphicsEffect(outline_effect)
                layout.addWidget(player_label, i + 1, 0)
                curr_civs = civs[i]
                for j in range(num_civs):
                    civ_icon = resource_path("assets/icons/" + curr_civs[j] + ".png")
                    civ_card = CivCard(curr_civs[j], civ_icon)
                    layout.addWidget(civ_card, i + 1, j + 1)
        button = QPushButton("确定")
        button.clicked.connect(self.ConfirmClicked)
        layout.addWidget(button, num_players + 2, int(num_civs / 2))
        self.setLayout(layout)
        

    def ConfirmClicked(self):
        self.confirmed_signal.emit()
        self.close()
        