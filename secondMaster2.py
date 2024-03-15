from random import randint
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys




class mainwin(QMainWindow):
    def __init__(self):
        super(mainwin,self).__init__()
        winf = 500
        wins = 700
        def seconscr():
            print('settings menu are butted')
            self.text1.hide()
            self.btnTs1.hide()
            self.btnTs2.hide()
            self.btnTs3.hide()
            self.btnTs4.hide()

            self.btns1 = QtWidgets.QPushButton(self)
            self.btns1.move(150, 150)
            self.btns1.setText('Разрешение')
            self.btns1.setFixedSize(200, 70)
            self.btns1.show()
            self.btns1.clicked.connect(scrensize)

            self.btns2 = QtWidgets.QPushButton(self)
            self.btns2.move(150, 350)
            self.btns2.setText('Вернуться')
            self.btns2.setFixedSize(200, 70)
            self.btns2.show()
            self.btns2.clicked.connect(back)

        def scrensize():
            self.btns1.hide()
            self.btns2.hide()

            self.btnss1 = QtWidgets.QPushButton(self)
            self.btnss1.move(150, 150)
            self.btnss1.setText('500x700')
            self.btnss1.setFixedSize(200, 70)
            self.btnss1.show()
            self.btnss1.clicked.connect(scchang1)

            self.btnss2 = QtWidgets.QPushButton(self)
            self.btnss2.move(150, 250)
            self.btnss2.setText('1280x720')
            self.btnss2.setFixedSize(200, 70)
            self.btnss2.show()
            self.btnss2.clicked.connect(scchang2)

            self.btnss3 = QtWidgets.QPushButton(self)
            self.btnss3.move(150, 350)
            self.btnss3.setText('Вернуться')
            self.btnss3.setFixedSize(200, 70)
            self.btnss3.show()
            self.btnss3.clicked.connect(scrensize)



        def scchang1():
            self.setGeometry(750, 250, 500, 700)
        def scchang2():
            self.setGeometry(350, 250, 1280, 720)

        def back():
            self.btns2.hide()
            self.btns1.hide()

            self.text1.show()
            self.btnTs1.show()
            self.btnTs2.show()
            self.btnTs3.show()
            self.btnTs4.show()
    #титульная ст

        self.setWindowTitle('Jsoku test 2')
        self.setGeometry(750, 250, winf, wins)

        self.text1 = QtWidgets.QLabel(self)
        self.text1.setText("Jsoku")
        self.text1.move(235,100)
        #text1.setFixedSize(100, 10)
        self.text1.adjustSize()

    #кнопки ТС
        self.btnTs1 = QtWidgets.QPushButton(self)
        self.btnTs1.move(150, 150)
        self.btnTs1.setText('Играть')
        self.btnTs1.setFixedSize(200, 70)
        #self.btnTs1.clicked.connect(seconscr)
        #btnTs1.adjustSize()

        self.btnTs2 = QtWidgets.QPushButton(self)
        self.btnTs2.move(150, 250)
        self.btnTs2.setText('Настройки')
        self.btnTs2.setFixedSize(200, 70)
        self.btnTs2.clicked.connect(seconscr)

        self.btnTs3 = QtWidgets.QPushButton(self)
        self.btnTs3.move(150, 350)
        self.btnTs3.setText('Выход')
        self.btnTs3.setFixedSize(200, 70)
        self.btnTs3.clicked.connect(quit)

        self.btnTs4 = QtWidgets.QPushButton(self)
        self.btnTs4.move(470, 10)
        self.btnTs4.setText('⚙')
        self.btnTs4.setFixedSize(20, 21)


def application():
    app = QApplication(sys.argv)
    window = mainwin()

    window.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    application()