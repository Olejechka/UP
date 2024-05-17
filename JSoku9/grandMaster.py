import sys
from random import randint
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLineEdit, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCheckBox, QComboBox

def butcr(text, s, sx, sy, x, y, color, action):
    button = QPushButton(text, s)
    button.setGeometry(sx, sy, x, y)
    button.setStyleSheet(
        f'color: white; border: 3px solid {color}; background-color: {color}; font-size: 20px; border-radius: 30px;')
    button.clicked.connect(action)
    button.show()
    return button

def sbutcr(text, s, sx, sy, x, y, color, action):
    button = QPushButton(text, s)
    button.setGeometry(sx, sy, x, y)
    button.setStyleSheet(
        f'color: {color}; border: 3px solid white; background-color: white; font-size: 20px; border-radius: 30px;')
    button.clicked.connect(action)
    button.show()
    return button

def lbcr(text, s, sx, sy, x, y, size, color, weight):
    label = QLabel(text, s)
    label.setGeometry(sx, sy, x, y)
    label.setStyleSheet(
        f'color: {color}; font-size: {size}px; background-color: rgba(255,255,255,0); border-radius: 15px; font-weight: {weight}')
    label.show()
    return label

def bck(img, s, width, height):
    background_label = QLabel(s)
    background_label.setPixmap(QtGui.QPixmap(img))
    background_label.setGeometry(0, 0, width, height)
    background_label.show()
    return background_label

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.backdimg = "whinter.png"
        self.theme_color = '#4472C4'
        self.mainscreen()
        self.selected_index = 0
        self.pm = True
        self.flscr = True
        self.counter = True
        self.timer = True
        self.help = True
        self.diff = 0
        self.errct = 0

        if self.flscr:
            self.showFullScreen()

    def mainscreen(self):
        self.clear_window()
        self.setWindowTitle('JSoku')
        self.setGeometry(0, 0, 1920, 1080)

        bck(self.backdimg, self, self.width(), self.height())
        self.lable0 = lbcr("JSoku", self, 740, 100, 440, 130, 150, self.theme_color, "bold")
        self.button0 = sbutcr("Начать игру", self, 860, 350, 200, 70, self.theme_color, self.prestart)
        self.button1 = butcr("Настройки", self, 860, 450, 200, 70, self.theme_color, self.settings_screen)
        self.button1 = butcr("Рекорды", self, 860, 550, 200, 70, self.theme_color, self.recordscr)
        self.button2 = butcr("Выход", self, 860, 650, 200, 70, self.theme_color, quit)

    def settings_screen(self):
        self.clear_window()
        bck(self.backdimg, self, self.width(), self.height())

        self.lable1_0 = lbcr("Выбор темы:", self, 860, 100, 380, 100, 25, self.theme_color, "none")
        self.lable1_1 = lbcr("Прочее:", self, 860, 240, 380, 100, 25, self.theme_color, "none")
        self.button1_0 = butcr("Назад", self, 1200, 500, 100, 70, self.theme_color, self.mainscreen)

        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(860, 180, 200, 30)
        self.combo_box.addItem("Зима")
        self.combo_box.addItem("Сакура")
        self.combo_box.addItem("Лес")
        self.combo_box.setCurrentIndex(self.selected_index)
        self.combo_box.currentIndexChanged.connect(self.changeStyle)
        self.combo_box.show()
        self.combo_box.setStyleSheet(
            "QComboBox { border-radius: 10px; background-color: rgba(255,255,255,128); color: " + self.theme_color + "; font-size: 20px; border: 2px solid " + self.theme_color + "; } " +
            "QComboBox QAbstractItemView { border-radius: 0px; background-color: #ffffff; color: " + self.theme_color + "; font-size: 20px; border: 2px solid " + self.theme_color + "; }")

        self.checkbox1 = QCheckBox('         Звуки           ', self)
        self.checkbox1.setGeometry(860, 320, 200, 30)
        self.checkbox1.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: " + self.theme_color + "; color: white; font-size: 20px; border: 2px solid " + self.theme_color + "} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.pm else '#ffffff'))
        self.checkbox1.setChecked(self.pm)
        self.checkbox1.stateChanged.connect(self.checkbox_changed)
        self.checkbox1.show()

        self.checkbox = QCheckBox('  Полный экран      ', self)
        self.checkbox.setGeometry(860, 380, 200, 30)
        self.checkbox.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: " + self.theme_color + "; color: white; font-size: 20px; border: 2px solid " + self.theme_color + "} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.flscr else '#ffffff'))
        self.checkbox.setChecked(self.flscr)
        self.checkbox.stateChanged.connect(self.checkbox_changed1)
        self.checkbox.show()

    def recordscr(self):
        self.clear_window()
        bck(self.backdimg, self, self.width(), self.height())

        self.lable1_1 = lbcr("ВАШИ РЕКОРДЫ:", self, 860, 100, 380, 100, 25, self.theme_color, "bold")
        self.lable1_1 = lbcr("_________________________________", self, 700, 120, 600, 100, 25, self.theme_color, "bold")
        self.button2_0 = butcr("Назад", self, 1200, 900, 100, 70, self.theme_color, self.mainscreen)

    def prestart(self):
        self.clear_window()
        bck(self.backdimg, self, self.width(), self.height())

        self.checkbox2_0 = QCheckBox('         Таймер           ', self)
        self.checkbox2_0.setGeometry(860, 320, 200, 30)
        self.checkbox2_0.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: " + self.theme_color + "; color: white; font-size: 20px; border: 2px solid " + self.theme_color + "} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.timer else '#ffffff'))
        self.checkbox2_0.setChecked(self.timer)
        self.checkbox2_0.stateChanged.connect(self.checkbox_changed2)
        self.checkbox2_0.show()

        self.checkbox2_1 = QCheckBox('        Подсказки      ', self)
        self.checkbox2_1.setGeometry(860, 360, 200, 30)
        self.checkbox2_1.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: " + self.theme_color + "; color: white; font-size: 20px; border: 2px solid " + self.theme_color + "} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.help else '#ffffff'))
        self.checkbox2_1.setChecked(self.help)
        self.checkbox2_1.stateChanged.connect(self.checkbox_changed3)


        self.checkbox2_1.show()

        self.checkbox2_2 = QCheckBox('  Счетчик ошибок      ', self)
        self.checkbox2_2.setGeometry(860, 400, 200, 30)
        self.checkbox2_2.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: " + self.theme_color + "; color: white; font-size: 20px; border: 2px solid " + self.theme_color + "} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.counter else '#ffffff'))
        self.checkbox2_2.setChecked(self.counter)
        self.checkbox2_2.stateChanged.connect(self.checkbox_changed4)
        self.checkbox2_2.show()

        self.combo_box1 = QComboBox(self)
        self.combo_box1.setGeometry(860, 180, 200, 30)
        self.combo_box1.addItem("Лёгкий")
        self.combo_box1.addItem("Средний")
        self.combo_box1.addItem("Эксперт")
        self.combo_box1.setCurrentIndex(self.diff)
        self.combo_box1.currentIndexChanged.connect(self.changeStyle1)
        self.combo_box1.show()
        self.combo_box1.setStyleSheet(
            "QComboBox { border-radius: 10px; background-color: rgba(255,255,255,128); color: " + self.theme_color + "; font-size: 20px; border: 2px solid " + self.theme_color + "; } " +
            "QComboBox QAbstractItemView { border-radius: 0px; background-color: #ffffff; color: " + self.theme_color + "; font-size: 20px; border: 2px solid " + self.theme_color + "; }")

        self.button3_0 = butcr("Назад", self, 1200, 900, 100, 70, self.theme_color, self.mainscreen)
        self.button3_1 = sbutcr("Начать игру", self, 860, 500, 200, 70, self.theme_color, self.game)

    def game(self):
        self.clear_window()
        bck(self.backdimg, self, self.width(), self.height())

        if self.counter:
            self.lable2_0 = lbcr(f'Ошибки: {self.errct}/3', self, 860, 100, 380, 100, 25, self.theme_color, "bold")
        if self.help:
            self.button4_0 = butcr("Открыть клетку", self, 1100, 110, 200, 70, self.theme_color, self.mainscreen)

        # Setting up the Sudoku grid
        self.sudoku_grid = SudokuGrid(self)
        self.sudoku_grid.setGeometry(400, 200, 600, 600)
        self.sudoku_grid.show()

    # Functions
    def checkbox_changed(self, state):
        self.pm = state == 2
        self.checkbox1.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: " + self.theme_color + "; color: white; font-size: 20px; border: 2px solid " + self.theme_color + "} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.pm else '#ffffff'))

    def checkbox_changed1(self, state):
        self.flscr = state
        if state == 2:
            self.showFullScreen()
        else:
            self.showNormal()
        self.checkbox.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: " + self.theme_color + "; color: white; font-size: 20px; border: 2px solid " + self.theme_color + "} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.flscr else '#ffffff'))

    def checkbox_changed2(self, state):
        self.timer = state
        self.checkbox2_0.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: " + self.theme_color + "; color: white; font-size: 20px; border: 2px solid " + self.theme_color + "} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.timer else '#ffffff'))

    def checkbox_changed3(self, state):
        self.help = state
        self.checkbox2_1.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: " + self.theme_color + "; color: white; font-size: 20px; border: 2px solid " + self.theme_color + "} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.help else '#ffffff'))

    def checkbox_changed4(self, state):
        self.counter = state
        self.checkbox2_2.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: " + self.theme_color + "; color: white; font-size: 20px; border: 2px solid " + self.theme_color + "} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.counter else '#ffffff'))

    def changeStyle(self, index):
        if index == 0:
            self.theme_color = '#4472C4'
            self.backdimg = 'whinter.png'
        elif index == 1:
            self.theme_color = '#ff98d0'
            self.backdimg = 'sakura.png'
        if index == 2:
            self.theme_color = '#6d912d'
            self.backdimg = 'forest.png'

    def changeStyle1(self, index):
        self.diff = index

    def clear_window(self):
        for widget in self.findChildren(QWidget):
            widget.deleteLater()

class SudokuGrid(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.setLayout(self.grid)
        self.create_sudoku_grid()

    def create_sudoku_grid(self):
        for row in range(9):
            for col in range(9):
                cell = QLineEdit()
                cell.setFixedSize(60, 60)
                cell.setAlignment(QtCore.Qt.AlignCenter)
                cell.setFont(QtGui.QFont('Arial', 18))
                cell.setStyleSheet("border: 1px solid black;")
                self.grid.addWidget(cell, row, col)
                if (row // 3 + col // 3) % 2 == 0:
                    cell.setStyleSheet("background-color: #f0f0f0; border: 1px solid black;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
