import  sys
from    PyQt5.QtWidgets import QApplication, QMainWindow
from    GDND_python import Ui_MainWindow

class   MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.zo_pushButton.clicked.connect(self.addtext)
        self.uic.out_pushButton_5.clicked.connect(self.main_win.close)#()

    def show(self):
        self.main_win.show()

    def addtext(self):
        the_hoc_depchoai = "ho va ten: "+self.uic.ho_textEdit.toPlainText() + " "+self.uic.ten_textEdit_2.toPlainText()
        self.uic.ket_qua_label.setText(the_hoc_depchoai)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())