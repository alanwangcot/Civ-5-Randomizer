from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class WordOutline(QGraphicsDropShadowEffect):
    def __init__(self):
        super().__init__()
        self.setBlurRadius(20)
        self.setColor(QColor(0, 0, 0))
        self.setOffset(0, 0)
        