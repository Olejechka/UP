from random import randint
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys





def application(): #добавить класс для окна
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('Jsoku test')
    window.setGeometry(750,250,500,700)


#титульная ст
    text1 = QtWidgets.QLabel(window)
    text1.setText("Jsoku")
    text1.move(235,100)
    #text1.setFixedSize(100, 10)
    text1.adjustSize()

#кнопки ТС
    btnTs1 = QtWidgets.QPushButton(window)
    btnTs1.move(150, 150)
    btnTs1.setText('Играть')
    btnTs1.setFixedSize(200, 70)
    btnTs1.clicked.connect(seconscr)
    #btnTs1.adjustSize()

    btnTs2 = QtWidgets.QPushButton(window)
    btnTs2.move(150, 250)
    btnTs2.setText('Пустышка для настроек')
    btnTs2.setFixedSize(200, 70)

    btnTs3 = QtWidgets.QPushButton(window)
    btnTs3.move(150, 350)
    btnTs3.setText('Пустышка для выхода')
    btnTs3.setFixedSize(200, 70)

    btnTs4 = QtWidgets.QPushButton(window)
    btnTs4.move(470, 10)
    btnTs4.setText('⚙')
    btnTs4.setFixedSize(20, 21)

    window.show()
    sys.exit(app.exec_())


def seconscr():
    print('settings menu are butted')


if __name__ == '__main__':
    application()