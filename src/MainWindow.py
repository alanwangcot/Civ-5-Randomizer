import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QSpacerItem
from PyQt6.QtGui import QColor, QPalette, QPixmap, QIcon, QPainter, QFont
from CivButtonWidget import CivButtonWidget
from Civilizations import Civilizations
from DropdownList import DropdownList
from Dialog import Dialog
from PyQt6.QtCore import Qt
from WordOutline import WordOutline
from SelectionButton import SelectionButton
from ResultsDialog import ResultsDialog
from Misc import MY_FONT, resource_path
from Wonders import Wonders
from WonderDialog import WonderDialog




class MainWindow(QMainWindow):

    num_civs: int = 1
    num_players: int = 2
    def __init__(self):
        super().__init__()

        self.civs = Civilizations()
        self.wonders = Wonders()
        # Set dark theme background color
        palette = self.palette()

        palette.setColor(QPalette.ColorRole.WindowText, QColor("white"))
        palette.setColor(QPalette.ColorRole.Button, QColor("#7f0151"))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor("white"))
        self.setPalette(palette)

        self.setWindowTitle("文明5随机文明选择器")
        self.setWindowIcon(QIcon(resource_path("assets/icons/civ.png")))
        self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(1200, 900)

        # Create a central widget with a layout for the background image
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        # Set the background image
        background_image = QPixmap(resource_path("assets/background/background.png"))
        background_image = background_image.scaled(1250, 950, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        painter = QPainter(background_image)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
        painter.fillRect(background_image.rect(), QColor(0, 0, 0, int(255 * (1 - 0.5))))
        painter.end()
        
        background_label = QLabel(self.central_widget)
        background_label.setPixmap(background_image)
        background_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the image
        # background_label.setDisabled(True)  # Hack to make transparent

        
        # Make the label transparent so that it doesn't hide your existing widgets
        background_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        background_label.setAutoFillBackground(True)

        self.layout.addWidget(background_label, 0, 0, -1, -1)  # Add the label to cover the entire window
        self.list_players = DropdownList("玩家数量", ["2", "3", "4", "5", "6", "7", "8"])
        self.list_civs = DropdownList("文明数量", ["1", "2", "3", "4", "5", "6", "7", "8"])
        self.layout.addWidget(self.list_players, 4, 7)
        self.layout.addWidget(self.list_civs, 4, 6)
        self.list_players.index_changed.connect(self.handlePlayerNum)
        self.list_civs.index_changed.connect(self.handleCivNum)

        spacer = QSpacerItem(100, 100)
        self.layout.addItem(spacer, 5, 0)

        ban_info_label1 = QLabel("上方勾选")
        ban_info_label2 = QLabel("禁用文明")

        ban_info_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # system default font, size 20
        ban_info_label1.setFont(QFont(MY_FONT, 20))
        ban_info_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ban_info_label2.setFont(QFont(MY_FONT, 20))
        outline_effect1 = WordOutline()
        outline_effect2 = WordOutline()
        ban_info_label1.setGraphicsEffect(outline_effect1)
        ban_info_label2.setGraphicsEffect(outline_effect2)

        self.layout.addWidget(ban_info_label1, 4, 4)
        self.layout.addWidget(ban_info_label2, 4, 5)

    def handleChecked(self, checked_name):
        if (checked_name in self.civs.CIV_LIST):
            self.civs.CIV_LIST.remove(checked_name)
            print(len(self.civs.CIV_LIST))
        else:
            self.civs.CIV_LIST.append(checked_name)
            print(len(self.civs.CIV_LIST))

    def createButtons(self):
        row = 0
        col = 0
        civs_copy = self.civs.CIV_LIST.copy()
        for civ in civs_copy:
            checkbox = CivButtonWidget(civ, resource_path(f"assets/icons/{civ}.png"), self)
            self.layout.addWidget(checkbox, row, col)
            
            checkbox.checked_name.connect(self.handleChecked)
            if civ == "威尼斯" or civ == "匈" or civ == "西班牙" or civ == "肖松尼" or civ == "巴比伦":
                checkbox.checkbox.setChecked(True)
                pass
            col += 1
            if (col > 9):
                row += 1
                col = 0
    
    def createSelectionButton(self):
        selection_button = SelectionButton("摇一摇！")
        wonders_button = SelectionButton("随机奇迹")
        selection_button.clicked.connect(self.rollCivs)
        wonders_button.clicked.connect(self.rollWonders)
        self.layout.addWidget(wonders_button, 5, 8)
        self.layout.addWidget(selection_button, 4, 8)


    def rollWonders(self):
        print("rolling wonders with following params: ")
        print("num players: ", self.num_players)
        rolled_wonders = self.wonders.randomize(self.num_players)
        print("rolled wonders: ", rolled_wonders)
        dialog = WonderDialog(self.num_players, rolled_wonders)
        dialog.confirmed_signal.connect(self.show)
        self.hide()
        dialog.exec()

    def rollCivs(self):
        print("rolling civs with following params: ")
        print("civs available: ", len(self.civs.CIV_LIST))
        print("num civs: ", self.num_civs)
        print("num players: ", self.num_players)
        rolled_civs = self.civs.randomize(self.num_players, self.num_civs)
        print("rolled civs: ", rolled_civs)
        dialog = ResultsDialog(self.num_civs, self.num_players, rolled_civs)
        dialog.confirmed_signal.connect(self.show)
        self.hide()
        dialog.exec()


    def handlePlayerNum(self, num):

        print("selected player num: ", num)
        if (num > self.num_players):
            if (num * self.num_civs > len(self.civs.CIV_LIST)):
                self.list_players.comboBox.setCurrentIndex(self.num_players - 2)
                dialog = Dialog()
                dialog.exec()
            else:
                self.num_players = num  
        else: 
            self.num_players = num
        print("num players: ", self.num_players)
        print("num civs: ", self.num_civs)


    def handleCivNum(self, num):

        print("selected civ num: ", num)
        if (num > self.num_civs):
            if (num * self.num_players > len(self.civs.CIV_LIST)):
                self.list_civs.comboBox.setCurrentIndex(self.num_civs - 1)
                dialog = Dialog()
                dialog.exec()
            else:
                self.num_civs = num
        else:
            self.num_civs = num
        print("num players: ", self.num_players)
        print("num civs: ", self.num_civs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.createButtons()
    window.createSelectionButton()
    window.show()
    sys.exit(app.exec())