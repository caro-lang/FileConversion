# -*- coding: utf-8 -*-
import os
import sys
import fnmatch
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QSizePolicy,QFileDialog, QTextEdit, QAbstractItemView, QMessageBox
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont
# from startPoint import mainFunc


# Main Class that holds User Interface Objects
class Ui_MainWindow(object):
    # Main window setup
    def setupUi(self, mainWindow):
        layout = QGridLayout()
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setLayout(layout)
        self.centralwidget.setMinimumSize(QtCore.QSize(650, 580))
        self.centralwidget.setObjectName("centralwidget")
        mainWindow.setCentralWidget(self.centralwidget)

        self.widget = QtWidgets.QWidget(self.centralwidget)
   #     self.widget.setGeometry(QtCore.QRect(30, 10, 591, 571))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_2 = QtWidgets.QLabel(self.widget)
    #    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
     #   sizePolicy.setHorizontalStretch(0)
      #  sizePolicy.setVerticalStretch(0)
       # sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
    #    self.label_2.setSizePolicy(sizePolicy)
   #     self.label_2.setMinimumSize(QtCore.QSize(180, 25))
     #   font = QtGui.QFont()
      #  font.setFamily("Helvetica")
       # font.setBold(True)
        # font.setWeight(75)
       # font.setStrikeOut(False)
       # font.setKerning(True)

       # self.label_2.setFont(font)
       # self.label_2.setScaledContents(True)
     #   self.label_2.setPixelSize(16)

        self.label_2.setObjectName("label_2")
        layout.addWidget(self.label_2,0, 0)

        self.listWidget = ListBoxWidget()
        #  self.listbox_view = ListBoxWidget(self)
        #  self.listWidget = QtWidgets.QListWidget(self.widget)
    #    self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
   #     self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
     #   self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setObjectName("listWidget")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)

        #addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0)
        #layout.setColumnStretch(3,3)
        layout.addWidget(self.listWidget, 1, 0, 3, 2)

        self.pushButton_1 = QPushButton('Datei hoochladen')
        layout.addWidget(self.pushButton_1, 1, 2)
        self.pushButton_2 = QPushButton('Ordner hoochladen')
        layout.addWidget(self.pushButton_2, 2, 2)
        self.pushButton_3 = QPushButton('Datei(en) löschen')
        self.pushButton_4 = QPushButton('Datei(en) löschen')
        self.pushButton_5 = QPushButton('Datei(en) löschen')
        layout.addWidget(self.pushButton_3, 3, 2)
        layout.addWidget(self.pushButton_4, 4, 0)
        layout.addWidget(self.pushButton_5, 4, 1)

        self.outputWidget = QtWidgets.QTextEdit(readOnly=True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.outputWidget.setSizePolicy(sizePolicy)
        self.outputWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.outputWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.outputWidget.setObjectName("outputWidget")
        layout.addWidget(self.outputWidget, 5, 0, 1, 2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_2.setText(_translate("MainWindow", "Beteiligte Dokumente"))
     #   self.pushButton.setText(_translate("MainWindow", "Konvertieren"))
      #  self.pushButton_2.setText(_translate("MainWindow", "löschen"))
        self.pushButton_3.setText(_translate("MainWindow", "Datei hoochladen"))
        #self.pushButton_4.setText(_translate("MainWindow", "Ordner hochladen"))

      #  self.pushButton_2.setShortcut(_translate("Form", "Backspace"))



#DRAG & DROP
class ListBoxWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            super(ListBoxWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            #event.ignore()
            super(ListBoxWidget, self).dragMoveEvent(event)

        #Drag&Drop
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                print(url)
                cases = [".pdf", ".csv", ".doc", ".docx", "/"]
               # self.filterCases(cases)
                for case in cases :
                    print(case)
                    if(case=="/"):
                        for dir in os.listdir(str(url.toLocalFile())):
                            if dir.endswith(('.pdf', '.csv', '.doc', '.docx')):
                                links.append(str(url.toLocalFile()) + dir)
                        break

                    if case.casefold() in url.toString():
                        links.append(str(url.toLocalFile()))
                        break
            self.addItems(links)
        else:
            #event.ignore()
            event.setDropAction(QtCore.Qt.MoveAction)
            super(ListBoxWidget, self).dropEvent(event)


class Stream(QtCore.QObject):
    """Redirects console output to text widget."""
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class GenMast(QMainWindow):
    """Main application window."""

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.process.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()

    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)


class GridDemo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        global positions, value, position, values

        values = [  '1', '2', '3',
                    '4', '5', '6',
                    '7', '8', '9'   ]

        positions = [(r, c) for r in range(3) for c in range(3)]

        layoutGrid = QGridLayout()
        self.setLayout(layoutGrid)

        self.buttons = {}

        for position, value in zip(positions, values):
            # print('Coordinate: ' + str(positions) + ' with value of '+ str(value))
            self.buttons[position[0], position[1]] = QPushButton(value)
            self.buttons[position[0], position[1]].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.buttons[position[0], position[1]].resizeEvent = self.resizeText
            layoutGrid.addWidget(self.buttons[position[0], position[1]], *position) # widget, position --> row index, column index


    def resizeText(self, event):
        defaultSize = 9
        for position, value in zip(positions, values):
            if self.rect().width() // 40> defaultSize:
                f = QFont('', self.rect().width() // 40)
            else:
                f = QFont('', defaultSize)

            self.buttons[position[0], position[1]].setFont(f)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
