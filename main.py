import sys
import random
from PyQt6 import QtWidgets, QtGui


class Canvas(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)

    def add_circle(self, x, y, diameter, color):
        self.circles.append((x, y, diameter, color))
        self.update()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        layout = QtWidgets.QVBoxLayout(central_widget)

        self.generateButton = QtWidgets.QPushButton("Generate Circle", self)
        layout.addWidget(self.generateButton)

        self.canvas = Canvas(self)
        layout.addWidget(self.canvas)

        self.generateButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.canvas.width() - diameter)
        y = random.randint(0, self.canvas.height() - diameter)

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        color = QtGui.QColor(red, green, blue)

        self.canvas.add_circle(x, y, diameter, color)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
