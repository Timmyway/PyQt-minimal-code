#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QDesktopWidget
# Built-in module :
import sys

# Look is generated module by pyuic, if you don't need it, 
# just remove it and and look.Ui_MainWindow that App inherits
import look

class App(QtWidgets.QMainWindow, look.Ui_MainWindow):
    def __init__(self, parent=None, title='Snippet: PyQt5 minimal code'):
        super(App, self).__init__(parent)        
        self.setupUi(self) #if using pyuic
        self.title = title
        # A label to say hello !
        self.label = QLabel('Hello world')
        # Create a main widget, then create and set a main grid layout to it
        self.mainWidget = QWidget()
        self.gMainLayout = QGridLayout()
        self.mainWidget.setLayout(self.gMainLayout)
        # Set the main widget as central widget for our application
        self.setCentralWidget(self.mainWidget)
        # The following config method helps us to set all default behaviours
        self.config()

    def config(self):        
        self.gMainLayout.addWidget(self.label, 0, 0)
        # Set application title -----------------------------------------------
        self.setWindowTitle(self.title)
        # ---- Size and position of Mainwindow --------------------------------
        self.center_mainwindow()

    def center_mainwindow(self, w=600, h=300):
        self.resize(w,h)
        size_window = self.geometry()
        # cp is the Center Point of user screen. Ex: if 600x300 so cp = 300,150
        cp = QDesktopWidget().availableGeometry().center() 
        # x = center point - width's half | x = center point - height's half
        position = QPoint(cp.x() - w // 2, cp.y() - h // 2)
        self.move(position)
        
def main(): 
    app = QtWidgets.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()