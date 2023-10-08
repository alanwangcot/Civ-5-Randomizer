from PyQt6.QtWidgets import QComboBox, QWidget, QLabel, QVBoxLayout
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import pyqtSignal

from Misc import MY_FONT

class DropdownList(QWidget):

    index_changed = pyqtSignal(int)
    def __init__(self, label_text, options):
        super().__init__()
        self.num_options = len(options)

        self.label = QLabel(label_text)
        self.label.setFont(QFont(MY_FONT, 12))
        outline_effect = QGraphicsDropShadowEffect()
        outline_effect.setBlurRadius(20)
        outline_effect.setColor(QColor(0, 0, 0))
        outline_effect.setOffset(0, 0)
        self.label.setGraphicsEffect(outline_effect)


        self.comboBox = QComboBox()
        self.comboBox.addItems(options)
        self.comboBox.currentIndexChanged.connect(self.onIndexChanged)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.comboBox)
        layout.addSpacing(20)
        self.setLayout(layout)
        self.onIndexChanged(0)

    def onIndexChanged(self, index):
        selected_value = self.comboBox.itemText(index)
        # print(int(selected_value))
        self.index_changed.emit(int(selected_value))

    def changeOptions(self, options:list):
        curr_index = self.comboBox.currentIndex()
        self.comboBox.clear()
        self.comboBox.addItems(options)
        self.comboBox.setCurrentIndex(curr_index)