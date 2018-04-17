# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyQtpractice\NewWin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 461)
        MainWindow.setFixedSize(681, 461)
        MainWindow.setWindowIcon(QtGui.QIcon(".\p9.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 160, 571, 251))
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setTextColor(QtGui.QColor('red'))
        self.textBrowser.setPlaceholderText("测试结果将会显示在这..")
        self.ping_button = QtWidgets.QPushButton(self.centralwidget)
        self.ping_button.setGeometry(QtCore.QRect(440, 50, 75, 23))
        self.ping_button.setObjectName("ping_button")
        self.tracert_button = QtWidgets.QPushButton(self.centralwidget)
        self.tracert_button.setGeometry(QtCore.QRect(440, 100, 75, 23))
        self.tracert_button.setObjectName("tracert_button")
        self.telnet_button = QtWidgets.QPushButton(self.centralwidget)
        self.telnet_button.setGeometry(QtCore.QRect(560, 50, 75, 23))
        self.telnet_button.setObjectName("telnet_button")
        self.ipaddress_button = QtWidgets.QPushButton(self.centralwidget)
        self.ipaddress_button.setGeometry(QtCore.QRect(560, 100, 75, 23))
        self.ipaddress_button.setObjectName("ipaddress_button")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 20, 291, 131))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ip = QtWidgets.QLineEdit(self.widget)
        self.ip.setObjectName("ip")
        self.ip.setPlaceholderText(' IP或者域名')
        self.gridLayout.addWidget(self.ip, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.port = QtWidgets.QLineEdit(self.widget)
        self.port.setObjectName("port")
        self.port.setPlaceholderText(' 0~65535')
        self.gridLayout.addWidget(self.port, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 23))
        self.menubar.setObjectName("menubar")
        #fileMenu = self.menubar
        #fileMenu.addMenu('帮助(&H)')
        #fileMenu.addAction(self.close())
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IP测试工具 beta:1.0.1"))
        self.ping_button.setText(_translate("MainWindow", "ping测试"))
        self.tracert_button.setText(_translate("MainWindow", "tracert测试"))
        self.telnet_button.setText(_translate("MainWindow", "telnet测试"))
        self.ipaddress_button.setText(_translate("MainWindow", "IP地址查询"))
        self.label.setText(_translate("MainWindow", "IP地址"))
        self.label_2.setText(_translate("MainWindow", "端口号"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

