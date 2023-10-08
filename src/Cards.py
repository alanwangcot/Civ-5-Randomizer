from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from WordOutline import WordOutline
from Misc import MY_FONT

class CivCard(QWidget):
    def __init__(self, text, icon_path, parent=None):
        super().__init__()

        self.icon_path = icon_path
        self.text = text

        self.icon_label = QLabel()
        icon_pixmap = QPixmap(icon_path)
        icon_pixmap = icon_pixmap.scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio)
        if (text == "巴西" or text == "印尼" or text == "肖松尼" or text == "亚述" or text == "波兰" or text == "威尼斯" or text == "祖鲁" or text == "葡萄牙" or text == "摩洛哥"):
            icon_pixmap = icon_pixmap.scaled(28, 28, Qt.AspectRatioMode.KeepAspectRatio)
        self.icon_label.setPixmap(icon_pixmap)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel(text)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont(MY_FONT, 16))
        outline_effect = WordOutline()
        self.label.setGraphicsEffect(outline_effect)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.icon_label)
        layout.addWidget(self.label)

        self.setLayout(layout)

class WonderCard(QWidget):
        def __init__(self, text, icon_path, parent=None):
            super().__init__()

            self.icon_path = icon_path
            self.text = text

            self.icon_label = QLabel()
            icon_pixmap = QPixmap(icon_path)
            icon_pixmap = icon_pixmap.scaled(36, 36, Qt.AspectRatioMode.KeepAspectRatio)
            self.icon_label.setPixmap(icon_pixmap)
            self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.label = QLabel(text)
            self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.label.setFont(QFont(MY_FONT, 20))
            outline_effect = WordOutline()
            self.label.setGraphicsEffect(outline_effect)

            layout = QVBoxLayout()
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(self.icon_label)
            layout.addWidget(self.label)

            self.setLayout(layout)