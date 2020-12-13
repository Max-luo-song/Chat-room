from PyQt5.Qt import *
from ui_person_list import Ui_Dialog

class Person_list(QWidget, Ui_Dialog):

    person_list_red_signal = pyqtSignal()
    person_list_bule_signal = pyqtSignal()
    person_list_purple_signal = pyqtSignal()
    person_list_back_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def person_list_red_function(self):
        self.people_list_red_signal.emit()

    def person_list_blue_function(self):
        self.people_list_bule_signal.emit()

    def person_list_purple_function(self):
        self.people_list_purple_signal.emit()

    def person_list_back_function(self):
        self.people_list_back_signal.emit()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Person_list()
    window.show()

    sys.exit(app.exec_())
