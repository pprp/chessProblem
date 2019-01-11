# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pyqt-workspace\chess\Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChessPlayer(object):
    def setupUi(self, ChessPlayer):
        ChessPlayer.setObjectName("ChessPlayer")
        ChessPlayer.resize(860, 563)
        self.centralWidget = QtWidgets.QWidget(ChessPlayer)
        self.centralWidget.setObjectName("centralWidget")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(600, 0, 20, 641))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lv = QtWidgets.QListView(self.centralWidget)
        self.lv.setGeometry(QtCore.QRect(617, 30, 231, 171))
        self.lv.setObjectName("lv")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 601, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setObjectName("grid")
        self.btn_calc = QtWidgets.QPushButton(self.centralWidget)
        self.btn_calc.setGeometry(QtCore.QRect(747, 360, 71, 31))
        self.btn_calc.setAutoRepeatDelay(300)
        self.btn_calc.setObjectName("btn_calc")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(627, 270, 31, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(738, 270, 32, 32))
        self.label_2.setObjectName("label_2")
        self.lineEdit_row = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_row.setGeometry(QtCore.QRect(667, 270, 61, 31))
        self.lineEdit_row.setObjectName("lineEdit_row")
        self.lineEdit_col = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_col.setGeometry(QtCore.QRect(776, 270, 61, 31))
        self.lineEdit_col.setObjectName("lineEdit_col")
        self.btn_sure = QtWidgets.QPushButton(self.centralWidget)
        self.btn_sure.setGeometry(QtCore.QRect(637, 360, 81, 31))
        self.btn_sure.setObjectName("btn_sure")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(697, 7, 61, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_ans = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_ans.setGeometry(QtCore.QRect(672, 410, 151, 31))
        self.lineEdit_ans.setObjectName("lineEdit_ans")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(627, 410, 31, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(627, 310, 31, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit_num = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_num.setGeometry(QtCore.QRect(667, 310, 61, 31))
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.btn_exit = QtWidgets.QPushButton(self.centralWidget)
        self.btn_exit.setGeometry(QtCore.QRect(640, 500, 191, 41))
        self.btn_exit.setObjectName("btn_exit")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(690, 220, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(630, 220, 51, 21))
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(740, 310, 30, 30))
        self.label_4.setObjectName("label_4")
        self.lineEdit_y = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_y.setGeometry(QtCore.QRect(777, 310, 61, 31))
        self.lineEdit_y.setObjectName("lineEdit_y")
        ChessPlayer.setCentralWidget(self.centralWidget)

        self.retranslateUi(ChessPlayer)
        QtCore.QMetaObject.connectSlotsByName(ChessPlayer)

    def retranslateUi(self, ChessPlayer):
        _translate = QtCore.QCoreApplication.translate
        ChessPlayer.setWindowTitle(_translate("ChessPlayer", "MainWindow"))
        self.btn_calc.setText(_translate("ChessPlayer", "计算"))
        self.label.setText(_translate("ChessPlayer", "行："))
        self.label_2.setText(_translate("ChessPlayer", "列："))
        self.btn_sure.setText(_translate("ChessPlayer", "确认"))
        self.label_3.setText(_translate("ChessPlayer", "系统提供"))
        self.label_5.setText(_translate("ChessPlayer", "out"))
        self.label_6.setText(_translate("ChessPlayer", "棋数："))
        self.btn_exit.setText(_translate("ChessPlayer", "退出"))
        self.label_7.setText(_translate("ChessPlayer", "选择"))
        self.label_4.setText(_translate("ChessPlayer", "Y："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChessPlayer = QtWidgets.QMainWindow()
    ui = Ui_ChessPlayer()
    ui.setupUi(ChessPlayer)
    ChessPlayer.show()
    sys.exit(app.exec_())

