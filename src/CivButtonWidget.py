from PyQt6.QtWidgets import QWidget, QCheckBox, QVBoxLayout, QLabel
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont
from WordOutline import WordOutline
from Misc import MY_FONT


class CivButtonWidget(QWidget):

    checked_name = pyqtSignal(str)
    def __init__(self, text, icon_path, parent=None):
        super().__init__()

        self.icon_path = icon_path
        self.text = text

        self.checkbox = QCheckBox(text, self)
        self.checkbox.setFont(QFont(MY_FONT, 12))

        outline_effect = WordOutline()
        self.checkbox.setGraphicsEffect(outline_effect)
    
        
        self.checkbox.stateChanged.connect(self.updateState)
        

        self.icon_label = ClickableLabel()
        icon_pixmap = QPixmap(icon_path)
        icon_pixmap = icon_pixmap.scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio)
        if (text == "巴西" or text == "印尼" or text == "肖松尼" or text == "亚述" or text == "波兰" or text == "威尼斯" or text == "祖鲁" or text == "葡萄牙" or text == "摩洛哥"):
            icon_pixmap = icon_pixmap.scaled(36, 36, Qt.AspectRatioMode.KeepAspectRatio)
        self.icon_label.setPixmap(icon_pixmap)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_label.clicked.connect(self.handleLabelClick)
        
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if (text == "巴西" or text == "印尼" or text == "肖松尼" or text == "亚述" or text == "波兰" or text == "威尼斯" or text == "祖鲁" or text == "葡萄牙" or text == "摩洛哥"):
            self.layout.addSpacing(10)
        # self.layout.addWidget(self.background_label)
        self.layout.addWidget(self.icon_label)
        if (text == "巴西" or text == "印尼" or text == "肖松尼" or text == "亚述" or text == "波兰" or text == "威尼斯" or text == "祖鲁" or text == "葡萄牙" or text == "摩洛哥"):
            self.layout.addSpacing(5)
        self.layout.addWidget(self.checkbox)
        self.setLayout(self.layout)

    def handleLabelClick(self):
        print('1')
        if(self.checkbox.isChecked()):
            print('2')
            self.checkbox.setChecked(False)
        else:
            print('3')
            self.checkbox.setChecked(True)

    def updateState(self, state):
        if not hasattr(self, 'original_pixmap'):
            self.original_pixmap = self.icon_label.pixmap()

        if state == 2: # for some reason Qt.CheckState.Checked doesn't work here
            # Grey out the icon when checked
            opacity = 0.5

        elif state == 0: # same as above
            opacity = 1


        if hasattr(self, 'original_pixmap') and not self.original_pixmap.isNull():
            new_pixmap = self.original_pixmap.copy()  # Create a copy of the original pixmap
            painter = QPainter(new_pixmap)
            painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
            painter.fillRect(new_pixmap.rect(), QColor(0, 0, 0, int(255 * (1 - opacity))))  # Set the alpha (transparency) value
            painter.end()

            # Set the modified pixmap to the icon_label
            self.icon_label.setPixmap(new_pixmap)
        
        self.checked_name.emit(self.text)

class ClickableLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)