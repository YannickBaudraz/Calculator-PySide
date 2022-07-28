import sys

from PySide6 import QtWidgets

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget()
window.setWindowTitle('Calculator')
window.show()

sys.exit(app.exec())
