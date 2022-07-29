import sys

from PySide6 import QtWidgets

from src.calculator import Calculator

app = QtWidgets.QApplication([])

window = Calculator()
window.show()

sys.exit(app.exec())
