import sys

from PySide6 import QtWidgets

from calculator_pyside.calculator import Calculator

app = QtWidgets.QApplication([])

window = Calculator()
window.show()

sys.exit(app.exec())
