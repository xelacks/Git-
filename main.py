import sys
import random
from PyQt6 import QtWidgets, uic, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.canvas = Canvas(self.canvasWidget)
        self.canvasWidget.setLayout(QtWidgets.QVBoxLayout())
        self.canvasWidget.layout().addWidget(self.canvas)

        self.generateButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.canvas.width() - diameter)
        y = random.randint(0, self.canvas.height() - diameter)
        self.canvas.add_circle(x, y, diameter)


class Canvas(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

        for x, y, diameter in self.circles:
            painter.setBrush(QtGui.QColor(255, 255, 0))
            painter.drawEllipse(x, y, diameter, diameter)

    def add_circle(self, x, y, diameter):
        self.circles.append((x, y, diameter))
        self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())