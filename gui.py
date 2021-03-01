# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QAbstractItemView
from PyQt5.QtCore import Qt, QUrl


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

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                print(url)
                cases = [".pdf", ".csv", ".doc", ".docx"]
                for case in cases :
                    print(case)
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
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

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

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
       # font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        #self.lineEdit.setStyleSheet()
        #("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Block</span></p></body></html>"))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())

        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
        #font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)

        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = ListBoxWidget()
      #  self.listbox_view = ListBoxWidget(self)
      #  self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setObjectName("listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())

        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        #font.setPointSize(16)
        font.setFamily("Helvetica")
        font.setBold(True)
        #font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(232, 230, 234);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
       # font.setPointSize(16)
        font.setFamily("Helvetica")
        font.setBold(True)
        #font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(232, 230, 234);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        #font.setPointSize(16)
        font.setFamily("Helvetica")
        font.setBold(True)
       # font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(232, 230, 234);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
    #    self.menubar = QtWidgets.QMenuBar(MainWindow)
    #    self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 22))
    #    self.menubar.setObjectName("menubar")
    #    MainWindow.setMenuBar(self.menubar)
       # self.statusbar = QtWidgets.QStatusBar(MainWindow)
       # self.statusbar.setObjectName("statusbar")
       # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Block</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Block"))
        #self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Beteiligte Dokumente</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Beteiligte Dokumente"))
        self.pushButton.setText(_translate("MainWindow", "Konvertieren"))
        self.pushButton_2.setText(_translate("MainWindow", "Alles löschen"))
        self.pushButton_3.setText(_translate("MainWindow", "Upload"))

        self.pushButton.setText(_translate("MainWindow", "Konvertieren"))
        self.pushButton.clicked.connect(self.convert)

        #remove Button
        self.pushButton_2.setText(_translate("MainWindow", "Löschen"))
        self.pushButton_2.setShortcut(_translate("Form", "Backspace"))
        self.pushButton_2.clicked.connect(self.remove)

        #Upload Button
        self.pushButton_3.setText(_translate("MainWindow", "Upload"))
        self.pushButton_3.clicked.connect(self.pushButton_handler)

    def pushButton_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        filter= "(*.DOC *.DOCX *.CSV *.PDF)"
        fname = QFileDialog.getOpenFileName(None, "Window name", "", filter)
        self.listWidget.addItem(fname[0])

    def remove(self):
        for SelectedItem in self.listWidget.selectedItems():
            self.listWidget.takeItem(self.listWidget.row(SelectedItem))

    def convert(self):
        self.lineEdit.text()
        print(self.lineEdit.text())

    def clicked(self, text):
        #self.label.setText(text)
        #self.label.adjustSize()
        print(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
