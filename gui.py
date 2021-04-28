# -*- coding: utf-8 -*-
import os
import sys
import fnmatch
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTextEdit, QAbstractItemView
from PyQt5.QtCore import Qt, QUrl
#from startPoint import mainFunc


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




#DRAG & DROP
class ListBoxWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
     #   self.resize(100, 100)

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



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 630)
        MainWindow.setMinimumSize(QtCore.QSize(650, 630))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 1260))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

        #sys.stdout = Stream(newText=self.onUpdateText)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(650, 580))
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 591, 571))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # start entfernen
        spacerItem3 = QtWidgets.QSpacerItem(600, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addSpacerItem(spacerItem3)

        self.label_2 = QtWidgets.QLabel(self.widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
      #  sizePolicy.setHorizontalStretch(0)
       # sizePolicy.setVerticalStretch(0)
      #  sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(180, 25))
        self.label_2.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
        # font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)

        self.label_2.setFont(font)
       # self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)


        # Liste
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
     #  self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        #self.verticalLayout

        self.listWidget = ListBoxWidget()
        #  self.listbox_view = ListBoxWidget(self)
        #  self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
    #    self.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
    #    self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
    #    self.listWidget.setAcceptDrops(True)
        self.listWidget.setObjectName("listWidget")

        self.horizontalLayout_5.addWidget(self.listWidget)
        #   self.verticalLayout.addLayout(self.horizontalLayout)

        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.horizontalLayout_5.addItem(spacerItem3)

        self.verticalLayout2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout2.setSpacing(1)
        self.verticalLayout2.setObjectName("verticalLayout2")

        # Datei Upload
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPixelSize(13)
       # font.setFamily("Helvetica")
        font.setBold(True)
        # font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(232, 230, 234);\n"
                                        "border-color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout2.addWidget(self.pushButton_3)
        # self.verticalLayout.addLayout(self.horizontalLayout)

        # Ordner Upload
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPixelSize(13)
    #    font.setFamily("Helvetica")
        font.setBold(True)
        # font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(232, 230, 234);\n"
                                        "border-color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout2.addWidget(self.pushButton_4)


        # Löschen
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
       # self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPixelSize(13)
       # font.setFamily("Helvetica")
        font.setBold(True)
        # font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(232, 230, 234);\n"
                                        "border-color: rgb(0, 0, 0);")
        #self.pushButton_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout2.addWidget(self.pushButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout2.addItem(spacerItem5)
        self.horizontalLayout_5.addLayout(self.verticalLayout2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)




        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Konvertierung
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())

        spacerItem4 = QtWidgets.QSpacerItem(200, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem4)

        #Links vom Konvertierungsbutton
        spacerItem8 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
       # self.verticalLayout.addLayout(self.horizontalLayout)

        #Konvertierungsbutton
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPixelSize(13)
      #  font.setFamily("Helvetica")
        font.setBold(True)
        # font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(232, 230, 234);\n"
                                      "border-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        #Rechts vom Konvertierungsbutton
        spacerItem4 = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        spacerItem4 = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem4)

        self.horizontalLayout7 = QtWidgets.QHBoxLayout()
       # sizePolicy
        #self.horizontalLayout7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout7.setContentsMargins(-1, 1, 200,30)
        self.horizontalLayout7.setObjectName("horizontalLayout7")
        # Create the text output widget.
        # Hier START neuer QTextEdit
        self.outputWidget = QtWidgets.QTextEdit(readOnly=True)
        self.outputWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.outputWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.outputWidget.setObjectName("outputWidget")
        self.outputWidget.setFixedHeight(30)
        self.horizontalLayout7.addWidget(self.outputWidget)
        self.verticalLayout.addLayout(self.horizontalLayout7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_2.setText(_translate("MainWindow", "Beteiligte Dokumente"))
        self.pushButton.setText(_translate("MainWindow", "Konvertieren"))
        self.pushButton_2.setText(_translate("MainWindow", "löschen"))
        self.pushButton_3.setText(_translate("MainWindow", "Datei hoochladen"))
        self.pushButton_4.setText(_translate("MainWindow", "Ordner hochladen"))

        self.pushButton_2.setShortcut(_translate("Form", "Backspace"))

        self.pushButton.clicked.connect(self.convert)
        self.pushButton_2.clicked.connect(self.remove)
        self.pushButton_3.clicked.connect(self.uploadFile)
        self.pushButton_4.clicked.connect(self.uploadDir)


    def uploadFile(self):
        filter= "(*.DOC *.DOCX *.CSV *.PDF *.doc *.docx *.csv *.pdf */)"
       # filter= "(Pdf Dateien(.pdf);; Text files (.txt);;XML files (*.xml))"
        fnames = QFileDialog.getOpenFileNames(None, "Window name", QtCore.QDir.rootPath(), filter)
       # if dir.endswith(('.pdf', '.csv', '.doc', '.docx')):
        fnames= list(fnames)
        for fname in fnames[0]:
            if fname:
                self.listWidget.addItem(str(fname))

    def uploadDir(self):
        # filter= "(*.DOC *.DOCX *.CSV *.PDF *.doc *.docx *.csv *.pdf */)"
        # filter= "(Pdf Dateien(.pdf);; Text files (.txt);;XML files (*.xml))"
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select project folder:', '', QtWidgets.QFileDialog.ShowDirsOnly)
        print(type(dir_))
        for file in os.listdir(dir_):
            print(dir_)
            if file.endswith(('.pdf', '.csv', '.doc', '.docx')):
                self.listWidget.addItem(dir_ + '/' + file)



    def remove(self):
        for SelectedItem in self.listWidget.selectedItems():
            print(SelectedItem.text(), " wurde gelöscht")
            self.listWidget.takeItem(self.listWidget.row(SelectedItem))

    def convert(self):
        self.file_save()
        print("Konvertieren startet")
        textDataList = []
        for i in range(0, self.listWidget.count()):
            print(self.listWidget.item(i).text())
            textDataList.append(self.listWidget.item(i).text())
        #mainFunc(textDataList)
        print(textDataList)


    def file_save(self):
        file_handler = QFileDialog(None, '', QtCore.QDir.rootPath(), '')
        #Das ist der Zielort
        self.zielort = file_handler.getExistingDirectoryUrl()
        self.zielort=self.zielort.toString()
        print(self.zielort)
      #  return file_tuple[0]

    def clicked(self, text):
        #self.label.setText(text)
        #self.label.adjustSize()
        print(text)

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.outputWidget.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.outputWidget.setTextCursor(cursor)
  #      self.process.ensureCursorVisible()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
