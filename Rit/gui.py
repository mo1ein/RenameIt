import os
import sys
import time
import PyQt5
import argparse
import PIL.Image
import PIL.ExifTags
from datetime import datetime
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QMessageBox
from Rit.Rit import Rename

#for resolation of 4k displays
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

#gui class 
class Ui_MainWindow(Rename):

    def __init__(self) :
        super().__init__()
        self.filename = []
        self.time_format = ""
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 499)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setGeometry(QtCore.QRect(170, 40, 321, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        #Browse button
        self.Browse.setFont(font)
        self.Browse.setMouseTracking(True)
        self.Browse.setObjectName("Browse")
        #ProgressBar 
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(170, 410, 321, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #ComboBox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 80, 321, 31))
        self.comboBox.setObjectName("comboBox")
        for Items in range(5) : self.comboBox.addItem("")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(220, 120, 221, 171))
        self.log.setObjectName("log")
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(280, 300, 111, 81))
        self.Enter.setObjectName("Enter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 16))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rit"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.Browse.clicked.connect(self.choose)
        self.label.setText(_translate("MainWindow", "File Path :"))
        #ComboBox Items
        self.comboBox.setItemText(0, _translate("MainWindow", 'YYYY-MM-DD  ->   2020-02-10 (default)'))
        self.comboBox.setItemText(1, _translate("MainWindow", 'YYYY-MM-DD  ->  2020-Feb-25'))
        self.comboBox.setItemText(2, _translate("MainWindow", 'YYYY-MM-DD  ->  2020-Februery-25'))
        self.comboBox.setItemText(3, _translate("MainWindow", 'DD MM DD HH:MM:SS YYYY -> Fri 30 Mar 2020 12:11:14 AM.jpg'))

        self.label_2.setText(_translate("MainWindow", "Time Format :"))
        self.Enter.setText(_translate("MainWindow", "Rit!"))
        self.Enter.clicked.connect(self.showDialog)
        #default item in combobox
        self.comboBox.setCurrentIndex(0)
        self.time_format = '%F' 
        print ("Format:: ",self.comboBox.currentIndex())
        self.comboBox.currentIndexChanged.connect(self.selectFormat)

    def choose (self):
        self.log.clear()
        files = QFileDialog.getOpenFileNames() #TODO some detail works
        self.filename = files[0]
        for i in self.filename : 
            name = os.path.split(i)[1]
            self.log.append(name)

    def selectFormat(self,i):
        print ("Items in the list are :")
        print ("Format:: ",self.comboBox.currentIndex())
        
        if self.comboBox.currentIndex() == 0 :
            self.time_format = '%F' 

        elif self.comboBox.currentIndex() == 1 :
            self.time_format = '%Y-%b-%d'

        elif self.comboBox.currentIndex() == 2 :
            self.time_format = '%Y-%B-%d'

        elif self.comboBox.currentIndex() == 3 :
            self.time_format = '%c'

        elif self.comboBox.currentIndex() == 4 :
            self.time_format = '%Y-%m-%d-%H:%M'

    
    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are You Sure to Rit files ?")
        msgBox.setWindowTitle("Warning!")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.buttonClicked.connect(self.msgButtonClick)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            r = Rename()
            r.path = self.filename
            r.format = self.time_format
            r.Rit()
            self.progressBar.setVisible(True)
            print('Yes clicked')
            #demo progressBar #TODO fix it
            while self.progressBar.value()<100 :
                self.progressBar.setValue(self.progressBar.value()+1)
            self.progressBar.setVisible(False)
            self.alert()

 
    def alert (self ) :
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('%s Files Renamed :)'%len(self.filename))
        msgBox.setWindowTitle("Alert")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.buttonClicked.connect(self.msgButtonClick)
        returnValue = msgBox.exec()

       
    def msgButtonClick(self,i):
       print("Button clicked is:",i.text())
       print( self.progressBar.value())


def main():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()

