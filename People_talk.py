from PyQt5.Qt import *
from ui_people_talk import Ui_Dialog

class People_talk(QWidget, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = People_talk()
    window.show()

    sys.exit(app.exec_())