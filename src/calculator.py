from functools import partial

from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QGridLayout


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.setWindowTitle('Calculator')

        self.grid_layout = QGridLayout(self)

        self.operation = QLineEdit()
        self.result = QLineEdit('0')

        self.btn_0 = QPushButton('0')
        self.btn_1 = QPushButton('1')
        self.btn_2 = QPushButton('2')
        self.btn_3 = QPushButton('3')
        self.btn_4 = QPushButton('4')
        self.btn_5 = QPushButton('5')
        self.btn_6 = QPushButton('6')
        self.btn_7 = QPushButton('7')
        self.btn_8 = QPushButton('8')
        self.btn_9 = QPushButton('9')

        self.btn_dot = QPushButton('.')
        self.btn_plus = QPushButton('+')
        self.btn_minus = QPushButton('-')
        self.btn_multiply = QPushButton('*')
        self.btn_divide = QPushButton('/')
        self.btn_equal = QPushButton('=')
        self.btn_clear = QPushButton('C')

        self.grid_layout.addWidget(self.operation, 0, 0, 1, 4)
        self.grid_layout.addWidget(self.result, 1, 0, 1, 4)
        self.grid_layout.addWidget(self.btn_clear, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.btn_divide, 2, 3, 1, 1)
        self.grid_layout.addWidget(self.btn_7, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.btn_8, 3, 1, 1, 1)
        self.grid_layout.addWidget(self.btn_9, 3, 2, 1, 1)
        self.grid_layout.addWidget(self.btn_multiply, 3, 3, 1, 1)
        self.grid_layout.addWidget(self.btn_4, 4, 0, 1, 1)
        self.grid_layout.addWidget(self.btn_5, 4, 1, 1, 1)
        self.grid_layout.addWidget(self.btn_6, 4, 2, 1, 1)
        self.grid_layout.addWidget(self.btn_minus, 4, 3, 1, 1)
        self.grid_layout.addWidget(self.btn_1, 5, 0, 1, 1)
        self.grid_layout.addWidget(self.btn_2, 5, 1, 1, 1)
        self.grid_layout.addWidget(self.btn_3, 5, 2, 1, 1)
        self.grid_layout.addWidget(self.btn_plus, 5, 3, 1, 1)
        self.grid_layout.addWidget(self.btn_0, 6, 1, 1, 1)
        self.grid_layout.addWidget(self.btn_dot, 6, 2, 1, 1)
        self.grid_layout.addWidget(self.btn_equal, 6, 3, 1, 1)

        self.btn_digits = []

        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedSize(64, 64)
                if widget.text().isdigit():
                    self.btn_digits.append(widget)
                    widget.clicked.connect(partial(self.btn_number_pressed, widget.text()))

        self.btn_equal.clicked.connect(self.calculate_operation)
        self.btn_clear.clicked.connect(self.reset)
        self.btn_plus.clicked.connect(partial(self.btn_operation_pressed, self.btn_plus.text()))
        self.btn_minus.clicked.connect(partial(self.btn_operation_pressed, self.btn_minus.text()))
        self.btn_multiply.clicked.connect(partial(self.btn_operation_pressed, self.btn_multiply.text()))
        self.btn_divide.clicked.connect(partial(self.btn_operation_pressed, self.btn_divide.text()))

    def btn_number_pressed(self, btn):
        result_txt = str(self.result.text())
        self.result.setText(btn) if result_txt == '0' else self.result.setText(result_txt + btn)

    def btn_operation_pressed(self, operation):
        self.operation.setText(self.operation.text() + self.result.text() + operation)
        self.result.setText('0')

    def reset(self):
        self.operation.setText('')
        self.result.setText('0')

    def calculate_operation(self):
        self.operation.setText(self.operation.text() + self.result.text())
        result_operation = eval(str(self.operation.text()))
        self.result.setText(str(result_operation))
