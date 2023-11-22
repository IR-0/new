import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUI('UI.ui', self)
        self.fl = False

    def paintEvent(self, event):
        if self.fl:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.fl = False

    def draw_flag(self, qp):
        self.fl = True
        x, y = randint(0, 400), randint(0, 300)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, randint(10, 50), randint(10, 50))
        qp.update()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())