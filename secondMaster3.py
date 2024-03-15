from random import randint
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow






class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Jsoku test 2')
        self.setGeometry(750, 250, 500, 700)

        self.main_screen()

    def main_screen(self):
        self.clear_window()

        self.text1 = QtWidgets.QLabel("Jsoku", self)
        self.text1.move(235, 100)
        self.text1.show()

        self.btnTs1 = QtWidgets.QPushButton('Играть', self)
        self.btnTs1.move(150, 150)
        self.btnTs1.setFixedSize(200, 70)
        self.btnTs1.show()

        self.btnTs2 = QtWidgets.QPushButton('Настройки', self)
        self.btnTs2.move(150, 250)
        self.btnTs2.setFixedSize(200, 70)
        self.btnTs2.clicked.connect(self.second_screen)
        self.btnTs2.show()

        self.btnTs3 = QtWidgets.QPushButton('Выход', self)
        self.btnTs3.move(150, 350)
        self.btnTs3.setFixedSize(200, 70)
        self.btnTs3.clicked.connect(quit)
        self.btnTs3.show()

        self.btnTs4 = QtWidgets.QPushButton('⚙', self)
        self.btnTs4.move(470, 10)
        self.btnTs4.setFixedSize(20, 21)
        self.btnTs4.show()

    def second_screen(self):
        print('Settings menu opened')
        self.clear_window()

        self.btns1 = QtWidgets.QPushButton('Разрешение', self)
        self.btns1.move(150, 150)
        self.btns1.setFixedSize(200, 70)
        self.btns1.show()
        self.btns1.clicked.connect(self.screen_size)

        self.btns2 = QtWidgets.QPushButton('Вернуться', self)
        self.btns2.move(150, 350)
        self.btns2.setFixedSize(200, 70)
        self.btns2.show()
        self.btns2.clicked.connect(self.main_screen)

    def screen_size(self):
        self.clear_window()

        self.btnss1 = QtWidgets.QPushButton('500x700', self)
        self.btnss1.move(150, 150)
        self.btnss1.setFixedSize(200, 70)
        self.btnss1.show()
        self.btnss1.clicked.connect(lambda: self.setGeometry(750, 250, 500, 700))

        self.btnss2 = QtWidgets.QPushButton('1280x720', self)
        self.btnss2.move(150, 250)
        self.btnss2.setFixedSize(200, 70)
        self.btnss2.clicked.connect(lambda: self.setGeometry(350, 250, 1280, 720))
        self.btnss2.show()

        self.btnss3 = QtWidgets.QPushButton('Вернуться', self)
        self.btnss3.move(150, 350)
        self.btnss3.setFixedSize(200, 70)
        self.btnss3.clicked.connect(self.second_screen)
        self.btnss3.show()

    def clear_window(self):
        for widget in self.findChildren(QtWidgets.QWidget):
            widget.deleteLater()



def run_app():
    app = QApplication([])
    window = MainWin()
    window.show()
    app.exec_()

if __name__ == '__main__':
    run_app()