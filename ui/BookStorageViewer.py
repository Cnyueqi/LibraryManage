# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookStorageViewer.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qdarkstyle
import db


class Ui_BookStorageViewer(object):
    def setupUi(self, BookStorageViewer):
        BookStorageViewer.setObjectName("BookStorageViewer")
        BookStorageViewer.setWindowModality(QtCore.Qt.WindowModal)
        BookStorageViewer.resize(750, 422)
        BookStorageViewer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(BookStorageViewer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Hlayout1 = QtWidgets.QHBoxLayout()
        self.Hlayout1.setObjectName("Hlayout1")
        self.searchEdit = QtWidgets.QLineEdit(BookStorageViewer)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.searchEdit.setFont(font)
        self.searchEdit.setObjectName("searchEdit")
        self.Hlayout1.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(BookStorageViewer)
        self.searchButton.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.searchButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/syx/.designer/images/search.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.searchButton.setIcon(icon)
        self.searchButton.setObjectName("searchButton")
        self.Hlayout1.addWidget(self.searchButton)
        self.comboBox = QtWidgets.QComboBox(BookStorageViewer)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 32))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.Hlayout1.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.Hlayout1)
        self.tableWidget = QtWidgets.QTableWidget(BookStorageViewer)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalWidget = QtWidgets.QWidget(BookStorageViewer)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.horizontalWidget)
        self.widget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget.setObjectName("widget")
        self.Hlayout = QtWidgets.QHBoxLayout(self.widget)
        self.Hlayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.Hlayout.setObjectName("Hlayout")
        self.jumpToLabel = QtWidgets.QLabel(self.widget)
        self.jumpToLabel.setObjectName("jumpToLabel")
        self.Hlayout.addWidget(self.jumpToLabel)
        self.pageEdit = QtWidgets.QLineEdit(self.widget)
        self.pageEdit.setMaximumSize(QtCore.QSize(32, 16777215))
        self.pageEdit.setObjectName("pageEdit")
        self.Hlayout.addWidget(self.pageEdit)
        self.pageLabel = QtWidgets.QLabel(self.widget)
        self.pageLabel.setObjectName("pageLabel")
        self.Hlayout.addWidget(self.pageLabel)
        self.jumpToButton = QtWidgets.QPushButton(self.widget)
        self.jumpToButton.setObjectName("jumpToButton")
        self.Hlayout.addWidget(self.jumpToButton)
        self.prevButton = QtWidgets.QPushButton(self.widget)
        self.prevButton.setObjectName("prevButton")
        self.Hlayout.addWidget(self.prevButton)
        self.backButton = QtWidgets.QPushButton(self.widget)
        self.backButton.setObjectName("backButton")
        self.Hlayout.addWidget(self.backButton)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.horizontalWidget)

        self.retranslateUi(BookStorageViewer)
        QtCore.QMetaObject.connectSlotsByName(BookStorageViewer)

    def retranslateUi(self, BookStorageViewer):
        _translate = QtCore.QCoreApplication.translate
        BookStorageViewer.setWindowTitle(_translate("BookStorageViewer", "欢迎使用图书馆管理系统"))
        self.searchButton.setText(_translate("BookStorageViewer", "查询"))
        self.comboBox.setItemText(0, _translate("BookStorageViewer", "按书名查询"))
        self.comboBox.setItemText(1, _translate("BookStorageViewer", "按书号查询"))
        self.comboBox.setItemText(2, _translate("BookStorageViewer", "按作者查询"))
        self.comboBox.setItemText(3, _translate("BookStorageViewer", "按分类查询"))
        self.comboBox.setItemText(4, _translate("BookStorageViewer", "按出版社查询"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("BookStorageViewer", "新建行"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("BookStorageViewer", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("BookStorageViewer", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("BookStorageViewer", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("BookStorageViewer", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("BookStorageViewer", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("BookStorageViewer", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("BookStorageViewer", "7"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("BookStorageViewer", "8"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("BookStorageViewer", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BookStorageViewer", "书名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BookStorageViewer", "书号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("BookStorageViewer", "作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("BookStorageViewer", "分类"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("BookStorageViewer", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("BookStorageViewer", "出版时间"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("BookStorageViewer", "库存"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("BookStorageViewer", "剩余可借"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("BookStorageViewer", "总借阅次数"))
        self.jumpToLabel.setText(_translate("BookStorageViewer", "跳转到第"))
        self.pageLabel.setText(_translate("BookStorageViewer", "/5页"))
        self.jumpToButton.setText(_translate("BookStorageViewer", "跳转"))
        self.prevButton.setText(_translate("BookStorageViewer", "前一页"))
        self.backButton.setText(_translate("BookStorageViewer", "后一页"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QWidget()
    ui = Ui_BookStorageViewer()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())