# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'look.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 425)
        MainWindow.setStyleSheet("/* STYLE DES QMESSAGEBOX --------------------------- */\n"
"QMessageBox {\n"
"    background-color: #333333;    \n"
"}\n"
"/* --------------------------------------------- */")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.txtInput = QtWidgets.QTextEdit(self.centralwidget)
        self.txtInput.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.txtInput.setCursorWidth(1)
        self.txtInput.setObjectName("txtInput")
        self.gridLayout.addWidget(self.txtInput, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnZoomIn = QtWidgets.QPushButton(self.centralwidget)
        self.btnZoomIn.setObjectName("btnZoomIn")
        self.horizontalLayout_2.addWidget(self.btnZoomIn)
        self.btnZoomOut = QtWidgets.QPushButton(self.centralwidget)
        self.btnZoomOut.setObjectName("btnZoomOut")
        self.horizontalLayout_2.addWidget(self.btnZoomOut)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as_file = QtWidgets.QAction(MainWindow)
        self.actionSave_as_file.setObjectName("actionSave_as_file")
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave_as_file)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txtInput.setDocumentTitle(_translate("MainWindow", "HTML Code"))
        self.txtInput.setPlaceholderText(_translate("MainWindow", "HTML EDITOR"))
        self.btnZoomIn.setText(_translate("MainWindow", "Zoom In"))
        self.btnZoomOut.setText(_translate("MainWindow", "Zoom Out"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_as_file.setText(_translate("MainWindow", "Save as file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

