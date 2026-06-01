import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled_1 import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Подключаем события
        self.input1.textChanged.connect(self.calculate)
        self.input2.textChanged.connect(self.calculate)

    def calculate(self):
        try:
            num1 = float(self.input1.text())
        except:
            num1 = 0

        try:
            num2 = float(self.input2.text())
        except:
            num2 = 0

        result = num1 + num2
        self.resultLabel.setText(f"Сумма: {result}")


app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())