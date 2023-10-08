from PyQt6.QtWidgets import QDialog, QGridLayout, QPushButton, QWidget
from PyQt6.QtGui import QIcon, QFont
from CivCard import CivCard
from PyQt6.QtCore import pyqtSignal
from WordOutline import WordOutline
from Misc import MY_FONT, resource_path

class ResultsDialog(QDialog):
    confirmed_signal = pyqtSignal()
    def __init__(self, num_civs, num_players, civs):
        super().__init__()

        self.setWindowTitle('随机结果')
        self.setWindowIcon(QIcon(resource_path("assets/icons/civ.png")))



        layout = QGridLayout()
        for i in range(num_players):
            player_label = QPushButton("玩家" + str(i + 1))
            player_label.setFont(QFont(MY_FONT, 20))
            player_label.setFlat(True)
            outline_effect = WordOutline()
            player_label.setGraphicsEffect(outline_effect)
            layout.addWidget(player_label, i, 0)
            curr_civs = civs[i]
            for j in range(num_civs):
                civ_icon = resource_path("assets/icons/" + curr_civs[j] + ".png")
                civ_card = CivCard(curr_civs[j], civ_icon)
                layout.addWidget(civ_card, i, j + 1)
        button = QPushButton("确定")
        button.clicked.connect(self.ConfirmClicked)
        layout.addWidget(button, num_players + 1, int(num_civs / 2))
        self.setLayout(layout)
        

    def ConfirmClicked(self):
        self.confirmed_signal.emit()
        self.close()
        