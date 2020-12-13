from PyQt5.Qt import *
from ui_main_call import Ui_Dialog

class Main_call(QWidget, Ui_Dialog):

    main_call_people_talk_signal = pyqtSignal()
    main_call_person_talk_signal = pyqtSignal()
    main_call_back_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def main_call_people_talk_function(self):
        self.main_call_people_talk_signal.emit()

    def main_call_person_talk_function(self):
        self.main_call_person_talk_signal.emit()

    def main_call_back_function(self):
        self.main_call_back_signal.emit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Main_call()
    window.show()

    sys.exit(app.exec_())