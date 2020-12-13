# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'person_talk.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(537, 479)
        Dialog.setStyleSheet("border-image: url(:/pre/cat4.jpg);")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(3, 4, 531, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.D_person_name = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.D_person_name.sizePolicy().hasHeightForWidth())
        self.D_person_name.setSizePolicy(sizePolicy)
        self.D_person_name.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.D_person_name.setFont(font)
        self.D_person_name.setStyleSheet("border-image: url(:/pre/32.png);")
        self.D_person_name.setAlignment(QtCore.Qt.AlignCenter)
        self.D_person_name.setObjectName("D_person_name")
        self.horizontalLayout.addWidget(self.D_person_name)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.D_input_text = QtWidgets.QTextEdit(self.layoutWidget)
        self.D_input_text.setStyleSheet("border-image: url(:/pre/guo.png);")
        self.D_input_text.setObjectName("D_input_text")
        self.horizontalLayout_3.addWidget(self.D_input_text)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.S_input_tag = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S_input_tag.sizePolicy().hasHeightForWidth())
        self.S_input_tag.setSizePolicy(sizePolicy)
        self.S_input_tag.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.S_input_tag.setFont(font)
        self.S_input_tag.setStyleSheet("border-image: url(:/pre/32.png);")
        self.S_input_tag.setObjectName("S_input_tag")
        self.horizontalLayout_2.addWidget(self.S_input_tag)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.D_input = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.D_input.sizePolicy().hasHeightForWidth())
        self.D_input.setSizePolicy(sizePolicy)
        self.D_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.D_input.setStyleSheet("border-image: url(:/pre/30.png);")
        self.D_input.setObjectName("D_input")
        self.horizontalLayout_2.addWidget(self.D_input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.D_person_name.setText(_translate("Dialog", "用户名："))
        self.S_input_tag.setText(_translate("Dialog", " 请输入："))
import images.picture_rc
