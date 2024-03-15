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
        self.text1.move(165, 50)
        self.text1.setStyleSheet("font-size: 50pt; color: f7dfea;")
        self.text1.adjustSize()
        self.text1.show()

        self.btnTs1 = QtWidgets.QPushButton('Играть', self)
        self.btnTs1.setGeometry(150, 150, 200, 70)
        self.btnTs1.setStyleSheet("QPushButton { border-radius: 35px; background-color: #e090b5; color: #f7dfea; font-size: 20px}")
        self.btnTs1.show()

        self.btnTs2 = QtWidgets.QPushButton('Настройки', self)
        self.btnTs2.setGeometry(150, 250,200, 70)
        self.btnTs2.setStyleSheet("QPushButton { border-radius: 35px; background-color: #e090b5; color: #f7dfea; font-size: 20px}")
        self.btnTs2.clicked.connect(self.second_screen)
        self.btnTs2.show()

        self.btnTs3 = QtWidgets.QPushButton('Выход', self)
        self.btnTs3.setGeometry(150, 350,200, 70)
        self.btnTs3.setStyleSheet("QPushButton { border-radius: 35px; background-color: #e090b5; color: #f7dfea; font-size: 20px}")
        self.btnTs3.clicked.connect(quit)
        self.btnTs3.show()

        self.btnTs4 = QtWidgets.QPushButton('⚙', self)
        self.btnTs4.setGeometry(470, 10,20, 21)
        self.btnTs4.show()

    def second_screen(self):
        print('Settings menu opened')
        self.clear_window()

        self.btns1 = QtWidgets.QPushButton('Разрешение', self)
        self.btns1.setGeometry(150, 150,200, 70)
        self.btns1.setStyleSheet("QPushButton { border-radius: 35px; background-color: #e090b5; color: #f7dfea; font-size: 20px}")
        self.btns1.show()
        self.btns1.clicked.connect(self.screen_size)

        self.btns2 = QtWidgets.QPushButton('Вернуться', self)
        self.btns2.setGeometry(150, 350,200, 70)
        self.btns2.setStyleSheet("QPushButton { border-radius: 35px; background-color: #e090b5; color: #f7dfea; font-size: 20px}")
        self.btns2.show()
        self.btns2.clicked.connect(self.main_screen)

    def screen_size(self):
        self.clear_window()

        self.btnss1 = QtWidgets.QPushButton('500x700', self)
        self.btnss1.setGeometry(150, 150,200, 70)
        self.btnss1.setStyleSheet("QPushButton { border-radius: 35px; background-color: #e090b5; color: #f7dfea; font-size: 20px}")
        self.btnss1.show()
        self.btnss1.clicked.connect(lambda: self.setGeometry(750, 250, 500, 700))

        self.btnss2 = QtWidgets.QPushButton('1280x720', self)
        self.btnss2.setGeometry(150, 250,200, 70)
        self.btnss2.setStyleSheet("QPushButton { border-radius: 35px; background-color: #e090b5; color: #f7dfea; font-size: 20px}")
        self.btnss2.clicked.connect(lambda: self.setGeometry(350, 250, 1280, 720))
        self.btnss2.show()

        self.btnss3 = QtWidgets.QPushButton('Вернуться', self)
        self.btnss3.setGeometry(150, 350,200, 70)
        self.btnss3.setStyleSheet("QPushButton { border-radius: 35px; background-color: #e090b5; color: #f7dfea; font-size: 20px}")
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