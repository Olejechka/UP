import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox,QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.backdimg = "forest.png"
        self.theme_color = '#6d912d'
        self.mainscreen()
        self.selected_index = 0
        self.pm=True


    def mainscreen(self):
        self.clear_window()
        self.setWindowTitle('JSoku')
        self.setGeometry(0, 0, 1920, 1080)

        self.background_label = QtWidgets.QLabel(self)
        self.background_label.setPixmap(QtGui.QPixmap(self.backdimg))
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.show()

        self.button1 = QtWidgets.QPushButton('Играть', self)
        self.button1.setGeometry(150, 150, 200, 70)
        self.button1.setStyleSheet(
            'color:' + self.theme_color + ';border: 2px solid ' + self.theme_color + ';font-size: 20px; border-radius: 15px;')
        self.button1.show()

        self.button2 = QPushButton('Настройки', self)
        self.button2.setGeometry(150, 250, 200, 70)
        self.button2.setStyleSheet(
            'color:' + self.theme_color + ';border: 2px solid ' + self.theme_color + ';font-size: 20px; border-radius: 15px;')
        self.button2.clicked.connect(self.settings_screen)
        self.button2.show()

        self.button3 = QPushButton('Выход', self)
        self.button3.setStyleSheet(
            'color:' + self.theme_color + ';border: 2px solid ' + self.theme_color + ';font-size: 20px; border-radius: 15px;')
        self.button3.setGeometry(150, 350, 200, 70)
        self.button3.clicked.connect(quit)
        self.button3.show()

    def settings_screen(self):
        self.clear_window()

        self.background_label = QtWidgets.QLabel(self)
        self.background_label.setPixmap(QtGui.QPixmap(self.backdimg))
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.show()

        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(150, 100, 200, 30)
        self.combo_box.addItem("Лес")
        self.combo_box.addItem("Сакура")
        self.combo_box.addItem("Зима")
        self.combo_box.addItem("Океан")
        self.combo_box.setCurrentIndex(self.selected_index)
        self.combo_box.currentIndexChanged.connect(self.changeStyle)
        self.combo_box.show()
        self.combo_box.setStyleSheet(
            "QComboBox { border-radius: 10px; background-color: rgba(255,255,255,128); color: " + self.theme_color + "; font-size: 20px; border: 2px solid " + self.theme_color + "; } " +
            "QComboBox QAbstractItemView { border-radius: 0px; background-color: #ffffff; color: " + self.theme_color + "; font-size: 20px; border: 2px solid " + self.theme_color + "; }")

        self.button4 = QPushButton('Назад', self)
        self.button4.setStyleSheet(
            'color:' + self.theme_color + ';border: 2px solid ' + self.theme_color + ';font-size: 20px; border-radius: 15px;')
        self.button4.setGeometry(150, 350, 200, 70)
        self.button4.clicked.connect(self.mainscreen)
        self.button4.show()

        self.checkbox = QCheckBox('         Звуки           ', self)
        self.checkbox.setGeometry(150, 20, 200, 30)
        self.checkbox.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: rgba(255,255,255,128); color: "+ self.theme_color + "; font-size: 20px; border: 2px solid "+ self.theme_color+"} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.pm else '#ffffff'))
        self.checkbox.setChecked(self.pm)
        self.checkbox.stateChanged.connect(self.checkbox_changed)
        self.checkbox.show()

    def checkbox_changed(self, state):
        self.pm = state == 2
        self.checkbox.setStyleSheet(
            "QCheckBox { border-radius: 15px; background-color: rgba(255,255,255,128); color:  "+ self.theme_color + "; font-size: 20px; border: 2px solid "+ self.theme_color+"} "
            "QCheckBox::indicator { border-radius: 6px; background-color: %s; border: 1px solid rgba(255,255,255,0) }" % (
                self.theme_color if self.pm else '#ffffff'))

    def changeStyle(self, index):
        if index == 0:
            self.theme_color = '#6d912d'
            self.backdimg = 'forest.png'
        elif index == 1:
            self.theme_color = '#ff98d0'
            self.backdimg = 'sakura.png'
        elif index == 2:
            self.theme_color = 'cyan'
            self.backdimg = 'whinter.png'
        elif index == 3:
            self.theme_color = 'blue'

        self.selected_index = index

        self.settings_screen()

    def clear_window(self):
        for widget in self.findChildren(QtWidgets.QWidget):
            widget.deleteLater()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())