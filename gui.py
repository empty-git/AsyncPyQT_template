from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MessagesBoard = QtWidgets.QTextEdit(self.centralwidget)
        self.MessagesBoard.setGeometry(QtCore.QRect(200, 160, 381, 281))
        self.MessagesBoard.setObjectName("MessagesBoard")
        self.messageInput = QtWidgets.QLineEdit(self.centralwidget)
        self.messageInput.setGeometry(QtCore.QRect(200, 60, 381, 41))
        self.messageInput.setObjectName("messageInput")
        self.AppendTextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AppendTextBtn.setGeometry(QtCore.QRect(330, 110, 151, 41))
        self.AppendTextBtn.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background:orange;\n"
"font-size:22px;\n"
"}\n"
"QPushButton:hover{\n"
"color:black;\n"
"}")
        self.AppendTextBtn.setObjectName("AppendTextBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AppendTextBtn.setText(_translate("MainWindow", "Append text"))
