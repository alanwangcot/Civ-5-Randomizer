from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from WordOutline import WordOutline
from Misc import MY_FONT

class SelectionButton(QPushButton):
    def __init__(self, text):
        super().__init__()

        self.setFixedSize(200, 80)
        self.setFont(QFont(MY_FONT, 20))
        # set font color to black
        self.setStyleSheet("color: black")
        outline_effect = WordOutline()
        self.setGraphicsEffect(outline_effect)
        self.setText(text)
        
