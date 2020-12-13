from PyQt5.Qt import *
from ui_logic import Ui_Dialog

class Logic(QWidget, Ui_Dialog):

    logic_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def logic_signal_function(self):
        self.logic_signal.emit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Logic()
    window.show()
    sys.exit(app.exec_())
