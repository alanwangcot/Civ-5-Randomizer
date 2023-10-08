import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QSpacerItem, QVBoxLayout
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

        self.checkboxes = []
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
        self.list_players = DropdownList("玩家数量", ["2", "3", "4", "5", "6", "7", "8", '9', '10'])
        self.list_civs = DropdownList("文明数量", ["1", "2", "3", "4", "5", "6", "7", "8"])
        self.layout.addWidget(self.list_players, 4, 7)
        self.layout.addWidget(self.list_civs, 4, 6)
        self.list_players.index_changed.connect(self.handlePlayerNum)
        self.list_civs.index_changed.connect(self.handleCivNum)

        spacer = QSpacerItem(100, 100)
        self.layout.addItem(spacer, 5, 0)

        ban_info_label= QLabel("勾选禁用")
        ban_info_label.setToolTip("恭喜你发现了彩蛋~ ( ˘ ³˘)♥")
        # ban_info_label2 = QLabel("禁用文明")

        ban_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # system default font, size 20
        ban_info_label.setFont(QFont(MY_FONT, 20))
        # ban_info_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # ban_info_label2.setFont(QFont(MY_FONT, 20))
        outline_effect1 = WordOutline()
        outline_effect2 = WordOutline()
        ban_info_label.setGraphicsEffect(outline_effect1)
        # ban_info_label2.setGraphicsEffect(outline_effect2)

        self.layout.addWidget(ban_info_label, 4, 5)
        # self.layout.addWidget(ban_info_label2, 4, 5)


    def handleChecked(self, checked_name):
        if (checked_name in self.civs.CIV_LIST):
            self.civs.CIV_LIST.remove(checked_name)
            # print(len(self.civs.CIV_LIST))
        else:
            self.civs.CIV_LIST.append(checked_name)
            # print(len(self.civs.CIV_LIST))

    def createButtons(self):
        row = 0
        col = 0
        civs_copy = self.civs.CIV_LIST.copy()
        
        for civ in civs_copy:
            checkbox = CivButtonWidget(civ, resource_path(f"assets/icons/{civ}.png"), self)
            self.layout.addWidget(checkbox, row, col)
            
            checkbox.checked_name.connect(self.handleChecked)
            # 默认禁用4禁
            if civ == "威尼斯" or civ == "匈" or civ == "西班牙" or civ == "肖松尼" or civ == "巴比伦":
                checkbox.checkbox.setChecked(True)
            # 默认禁用二级文明
            if civ == "中国" or civ == "波兰" or civ == "阿拉伯" or civ == "俄罗斯" or civ == "英格兰" or civ == "埃及" or civ == "玛雅" or civ == "朝鲜" or civ == "蒙古":
                checkbox.checkbox.setChecked(True)
                
            col += 1
            if (col > 9):
                row += 1
                col = 0
            self.checkboxes.append(checkbox)
    
    def createSelectionButton(self):
        selection_button = SelectionButton("摇一摇！")
        selection_button.setToolTip("随机生成文明")
        wonders_button = SelectionButton("随机奇迹")
        wonders_button.setToolTip("随机生成奇迹，人数最多8人，每人最多一个前期奇迹")
        selection_button.clicked.connect(self.rollCivs)
        wonders_button.clicked.connect(self.rollWonders)
        self.layout.addWidget(wonders_button, 5, 8)
        self.layout.addWidget(selection_button, 4, 8)

        # if windows
        if sys.platform.startswith('win'):
            font = QFont(MY_FONT, 10)
        else:
            font = QFont(MY_FONT, 14)

        # 一键禁用/解禁一级/二级文明/全部
        god_layout = QVBoxLayout()
        self.ban_god_button = SelectionButton("禁/解禁④🈲")
        self.ban_god_button.setFixedSize(100, 50)
        self.ban_god_button.setFont(font)
        self.ban_god_button.setToolTip("按一次全解禁，再按一次全禁。别连续点太多次不然程序会卡死。")
        self.ban_god_button.clicked.connect(self.unbanGod)
        self.ban_second_button = SelectionButton("禁/解禁二级")
        self.ban_second_button.setToolTip("按一次全解禁，再按一次全禁。别连续点太多次不然程序会卡死。")
        self.ban_second_button.setFixedSize(100, 50)
        self.ban_second_button.setFont(font)
        self.ban_second_button.clicked.connect(self.unbanSecond)
        unban_all_button = SelectionButton("解禁全部")
        unban_all_button.setToolTip("直接解禁全部文明")
        unban_all_button.setFixedSize(100, 50)
        unban_all_button.setFont(font)
        unban_all_button.clicked.connect(self.unbanAll)
        self.layout.addWidget(self.ban_god_button, 5, 5)
        self.layout.addWidget(self.ban_second_button, 5, 6)
        self.layout.addWidget(unban_all_button, 5, 7)
    
    def banGod(self):
        for i in range(1,5):
            self.checkboxes[i].checkbox.setChecked(True)
        self.ban_god_button.clicked.connect(self.unbanGod)

    def unbanGod(self):
        for i in range(1,5):
            self.checkboxes[i].checkbox.setChecked(False)
        self.ban_god_button.clicked.connect(self.banGod)
            
    def banSecond(self):
        indexes = [5, 15, 17, 19, 24, 26, 29, 32, 37]
        for i in indexes:
            self.checkboxes[i].checkbox.setChecked(True)
        self.ban_second_button.clicked.connect(self.unbanSecond)

    def unbanSecond(self):
        indexes = [5, 15, 17, 19, 24, 26, 29, 32, 37]
        for i in indexes:
            self.checkboxes[i].checkbox.setChecked(False)
        self.ban_second_button.clicked.connect(self.banSecond)

    def unbanAll(self):
        for checkbox in self.checkboxes:
            checkbox.checkbox.setChecked(False)

    def rollWonders(self):
        if (self.num_players > 8):
            dialog = Dialog("玩家数量过多！(最多8人)！奇迹不够啦！")
            dialog.exec()
            return
        print("rolling wonders with following params: ")
        print("num players: ", self.num_players)
        rolled_wonders = self.wonders.randomize(self.num_players)
        print("rolled wonders: ", rolled_wonders)
        dialog = WonderDialog(self.num_players, rolled_wonders[1:], rolled_wonders[0][1], rolled_wonders[0][0])
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
        dialog = ResultsDialog(self.num_civs, self.num_players, rolled_civs[1:], rolled_civs[0][1], rolled_civs[0][0])
        dialog.confirmed_signal.connect(self.show)
        self.hide()
        dialog.exec()


    def handlePlayerNum(self, num):

        print("selected player num: ", num)
        if (num > self.num_players):
            if (num * self.num_civs > len(self.civs.CIV_LIST)):
                self.list_players.comboBox.setCurrentIndex(self.num_players - 2)
                dialog = Dialog("玩家数量过多！文明数量不足！")
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
                dialog = Dialog("每个玩家文明数量过多！文明数量不足！")
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