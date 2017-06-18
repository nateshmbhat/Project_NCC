# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt/exa.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NCC_Attendence_Model(object):
    def setupUi(self, NCC_Attendence_Model):
        NCC_Attendence_Model.setObjectName(_fromUtf8("NCC_Attendence_Model"))
        NCC_Attendence_Model.resize(723, 457)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NCC_Attendence_Model.sizePolicy().hasHeightForWidth())
        NCC_Attendence_Model.setSizePolicy(sizePolicy)
        NCC_Attendence_Model.setStyleSheet(_fromUtf8(""))
        self.centralWidget = QtGui.QWidget(NCC_Attendence_Model)
        self.centralWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setStyleSheet(_fromUtf8("background-color: rgb(226, 235, 255);\n"
""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Tab_1 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_1.sizePolicy().hasHeightForWidth())
        self.Tab_1.setSizePolicy(sizePolicy)
        self.Tab_1.setObjectName(_fromUtf8("Tab_1"))
        self.verticalLayoutWidget = QtGui.QWidget(self.Tab_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 701, 321))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(599, 0))
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setStyleSheet(_fromUtf8("background-color: rgb(168, 164, 170);\n"
"background-color: rgb(255, 183, 249);"))
        self.tableWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(8)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 3))
        brush.setStyle(QtCore.Qt.Dense2Pattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.Tab_1)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 0, 1490, 51))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 0);\n"
"font: 75 18pt \"Ubuntu Mono\";\n"
"font: 75 30pt \"Ubuntu Mono\";\n"
"background-color: rgb(60, 43, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.tabWidget.addTab(self.Tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        NCC_Attendence_Model.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(NCC_Attendence_Model)
        self.statusBar.setEnabled(False)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        NCC_Attendence_Model.setStatusBar(self.statusBar)

        self.retranslateUi(NCC_Attendence_Model)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NCC_Attendence_Model)

    def retranslateUi(self, NCC_Attendence_Model):
        NCC_Attendence_Model.setWindowTitle(_translate("NCC_Attendence_Model", "MainWindow", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("NCC_Attendence_Model", "DATE", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("NCC_Attendence_Model", "dsnfdnf", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("NCC_Attendence_Model", "dfsdsdf", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("NCC_Attendence_Model", "dfdf", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("NCC_Attendence_Model", "fdddfsfd", None))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("NCC_Attendence_Model", "sdsdads", None))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("NCC_Attendence_Model", "sdsa", None))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("NCC_Attendence_Model", "sdsdsad", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("NCC_Attendence_Model", "Day 1", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("NCC_Attendence_Model", "Day 2", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("NCC_Attendence_Model", "Day 3", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("NCC_Attendence_Model", "Day 4", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("NCC_Attendence_Model", "Day 5", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("NCC_Attendence_Model", "Day 7", None))
        self.label.setText(_translate("NCC_Attendence_Model", "            Attendence", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_1), _translate("NCC_Attendence_Model", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("NCC_Attendence_Model", "Tab 2", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NCC_Attendence_Model = QtGui.QMainWindow()
    ui = Ui_NCC_Attendence_Model()
    ui.setupUi(NCC_Attendence_Model)
    NCC_Attendence_Model.show()
    sys.exit(app.exec_())

