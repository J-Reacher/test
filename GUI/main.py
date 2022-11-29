import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setup_ui(self.main_win)
        self.uic.xinchao_BT.clicked.connect(self.show_txt)
        self.uic.tambiet_BT.clicked.connect(self.main_win.close)

    def show(self):
        self.main_win.show()

    def show_txt(self):
        self.uic.test_LB.setText("HELLO ! ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
