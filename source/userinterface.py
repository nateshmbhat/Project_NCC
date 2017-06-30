# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userinterface.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1078, 825)
        MainWindow.setMinimumSize(QtCore.QSize(704, 599))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Documents/CODES/ncc/code/new/Icons/ncc1.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color:rgb(255, 254, 252)"))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setProperty("toolTipDuration", 0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mytab = QtGui.QTabWidget(self.centralwidget)
        self.mytab.setEnabled(True)
        self.mytab.setMinimumSize(QtCore.QSize(0, 599))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mytab.setFont(font)
        self.mytab.setMouseTracking(True)
        self.mytab.setStyleSheet(_fromUtf8(""))
        self.mytab.setTabShape(QtGui.QTabWidget.Rounded)
        self.mytab.setDocumentMode(False)
        self.mytab.setTabsClosable(False)
        self.mytab.setMovable(False)
        self.mytab.setProperty("tabBarAutoHide", False)
        self.mytab.setObjectName(_fromUtf8("mytab"))
        self.Enrol = QtGui.QWidget()
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Enrol.setFont(font)
        self.Enrol.setStyleSheet(_fromUtf8("#Enrol{\n"
"    background-image: url(:/icons/image-blur.png);\n"
"background-position:center;\n"
"}"))
        self.Enrol.setObjectName(_fromUtf8("Enrol"))
        self.gridLayout = QtGui.QGridLayout(self.Enrol)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.searchFrame = QtGui.QFrame(self.Enrol)
        self.searchFrame.setMinimumSize(QtCore.QSize(0, 45))
        self.searchFrame.setStyleSheet(_fromUtf8("#searchFrame{\n"
"background-color:transparent;\n"
"}"))
        self.searchFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.searchFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.searchFrame.setObjectName(_fromUtf8("searchFrame"))
        self.searchbyfieldLineEdit = QtGui.QLineEdit(self.searchFrame)
        self.searchbyfieldLineEdit.setGeometry(QtCore.QRect(0, 0, 251, 26))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchbyfieldLineEdit.sizePolicy().hasHeightForWidth())
        self.searchbyfieldLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.searchbyfieldLineEdit.setFont(font)
        self.searchbyfieldLineEdit.setStyleSheet(_fromUtf8("border-radius:2px;\n"
"font-size:20px;\n"
"width:230;"))
        self.searchbyfieldLineEdit.setText(_fromUtf8(""))
        self.searchbyfieldLineEdit.setObjectName(_fromUtf8("searchbyfieldLineEdit"))
        self.searchPushButton = QtGui.QPushButton(self.searchFrame)
        self.searchPushButton.setGeometry(QtCore.QRect(250, 0, 91, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchPushButton.sizePolicy().hasHeightForWidth())
        self.searchPushButton.setSizePolicy(sizePolicy)
        self.searchPushButton.setMinimumSize(QtCore.QSize(0, 8))
        self.searchPushButton.setMaximumSize(QtCore.QSize(16777215, 27))
        self.searchPushButton.setAutoFillBackground(False)
        self.searchPushButton.setStyleSheet(_fromUtf8("#searchPushButton\n"
"{\n"
"    -moz-box-shadow:inset 0px 1px 0px 0px #54a3f7;\n"
"    -webkit-box-shadow:inset 0px 1px 0px 0px #54a3f7;\n"
"    box-shadow:inset 0px 1px 0px 0px #54a3f7;\n"
"    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #007dc1), color-stop(1, #0061a7));\n"
"    background:-moz-linear-gradient(top, #007dc1 5%, #0061a7 100%);\n"
"    background:-webkit-linear-gradient(top, #007dc1 5%, #0061a7 100%);\n"
"    background:-o-linear-gradient(top, #007dc1 5%, #0061a7 100%);\n"
"    background:-ms-linear-gradient(top, #007dc1 5%, #0061a7 100%);\n"
"    background:linear-gradient(to bottom, #007dc1 5%, #0061a7 100%);\n"
"    background-color:#007dc1;\n"
"    -moz-border-radius:13px;\n"
"    -webkit-border-radius:13px;;\n"
"    border:1px solid #124d77;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:georgia;\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"    text-shadow:0px 1px 0px #154682;\n"
"}\n"
"\n"
"#searchPushButton:hover\n"
"{\n"
"    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #0061a7), color-stop(1, #007dc1));\n"
"    background:-moz-linear-gradient(top, #0061a7 5%, #007dc1 100%);\n"
"    background:-webkit-linear-gradient(top, #0061a7 5%, #007dc1 100%);\n"
"    background:-o-linear-gradient(top, #0061a7 5%, #007dc1 100%);\n"
"    background:-ms-linear-gradient(top, #0061a7 5%, #007dc1 100%);\n"
"    background:linear-gradient(to bottom, #0061a7 5%, #007dc1 100%);\n"
"    background-color:#0061a7;\n"
"}\n"
""))
        self.searchPushButton.setCheckable(False)
        self.searchPushButton.setAutoDefault(False)
        self.searchPushButton.setDefault(False)
        self.searchPushButton.setObjectName(_fromUtf8("searchPushButton"))
        self.enrolmentnumRadioButton = QtGui.QRadioButton(self.searchFrame)
        self.enrolmentnumRadioButton.setGeometry(QtCore.QRect(0, 30, 141, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enrolmentnumRadioButton.sizePolicy().hasHeightForWidth())
        self.enrolmentnumRadioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.enrolmentnumRadioButton.setFont(font)
        self.enrolmentnumRadioButton.setStyleSheet(_fromUtf8("#enrolmentnumRadioButton\n"
"{\n"
"background-color:transparent;\n"
"color:white;\n"
"font-family:georgia;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"#enrolmentnumRadioButton:hover\n"
"{\n"
"background-color:transparent;\n"
"color:yellow;\n"
"font-family:georgia;\n"
"font-weight:bold;\n"
"}\n"
""))
        self.enrolmentnumRadioButton.setChecked(True)
        self.enrolmentnumRadioButton.setObjectName(_fromUtf8("enrolmentnumRadioButton"))
        self.aadhaarnumRadioButton = QtGui.QRadioButton(self.searchFrame)
        self.aadhaarnumRadioButton.setGeometry(QtCore.QRect(170, 30, 131, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aadhaarnumRadioButton.sizePolicy().hasHeightForWidth())
        self.aadhaarnumRadioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.aadhaarnumRadioButton.setFont(font)
        self.aadhaarnumRadioButton.setStyleSheet(_fromUtf8("#aadhaarnumRadioButton\n"
"{\n"
"background-color:transparent;\n"
"color:white;\n"
"font-family:georgia;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"#aadhaarnumRadioButton:hover\n"
"{\n"
"background-color:transparent;\n"
"color:yellow;\n"
"font-family:georgia;\n"
"font-weight:bold;\n"
"}\n"
""))
        self.aadhaarnumRadioButton.setObjectName(_fromUtf8("aadhaarnumRadioButton"))
        self.gridLayout.addWidget(self.searchFrame, 1, 0, 1, 1)
        self.enroltitleLabel = QtGui.QLabel(self.Enrol)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enroltitleLabel.sizePolicy().hasHeightForWidth())
        self.enroltitleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.enroltitleLabel.setFont(font)
        self.enroltitleLabel.setMouseTracking(True)
        self.enroltitleLabel.setStyleSheet(_fromUtf8("background-image:url(:/icons/graywood.png) ;\n"
"background-position:center;\n"
"font-size:30px;\n"
"color:white;\n"
"border-radius:5px;\n"
"border-width:3px;\n"
"border-color:green;\n"
"border-style:dotted;\n"
"text-decoration:underlined;\n"
"text-shadow:0 1px 0 rgb(204,204,204) , 0 2px 0 rgb(201,201,201) , 0 3px 0 rgb(187,187,187) , 0 4px 0 rgb(185,185,185) , 0 5px 0 rgb(170,170,170) , 0 6px 1px rgba(0,0,0,0.0980392) , 0 0 5px rgba(0,0,0,0.0980392) , 0 1px 3px rgba(0,0,0,0.298039) , 0 3px 5px rgba(0,0,0,0.2) , 0 5px 10px rgba(0,0,0,0.247059) , 0 10px 10px rgba(0,0,0,0.2) , 0 20px 20px rgba(0,0,0,0.14902) ;"))
        self.enroltitleLabel.setObjectName(_fromUtf8("enroltitleLabel"))
        self.gridLayout.addWidget(self.enroltitleLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.submitPushButton = QtGui.QPushButton(self.Enrol)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitPushButton.sizePolicy().hasHeightForWidth())
        self.submitPushButton.setSizePolicy(sizePolicy)
        self.submitPushButton.setMinimumSize(QtCore.QSize(600, 0))
        self.submitPushButton.setMaximumSize(QtCore.QSize(500, 16777215))
        self.submitPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitPushButton.setStyleSheet(_fromUtf8("\n"
"#submitPushButton{\n"
"color:white;\n"
"font-size:30px;\n"
"font-family:georgia;\n"
"width:80px;\n"
"height:40px;\n"
"border-style:dashed;\n"
"border-color:black;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255))\n"
"}\n"
"\n"
"#submitPushButton:hover\n"
"{\n"
"color:black;\n"
"font-size:30px;\n"
"font-family:georgia;\n"
"width:80px;\n"
"height:40px;\n"
"border-style:dotted;\n"
"border-color:black;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255))\n"
"}\n"
"\n"
""))
        self.submitPushButton.setCheckable(False)
        self.submitPushButton.setDefault(False)
        self.submitPushButton.setFlat(False)
        self.submitPushButton.setObjectName(_fromUtf8("submitPushButton"))
        self.horizontalLayout_6.addWidget(self.submitPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.Enrol)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet(_fromUtf8("#scrollArea{\n"
"background-color:transparent;\n"
"border-radius:100px;\n"
"}\n"
""))
        self.scrollArea.setFrameShape(QtGui.QFrame.WinPanel)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Raised)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -789, 1019, 1378))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet(_fromUtf8("#scrollAreaWidgetContents{\n"
"background-color:transparent;\n"
"}\n"
""))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(600, 0))
        self.line.setStyleSheet(_fromUtf8("width:10px;"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 6, 0, 1, 1)
        self.bankdetailsLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.bankdetailsLabel.setFont(font)
        self.bankdetailsLabel.setAcceptDrops(False)
        self.bankdetailsLabel.setAutoFillBackground(False)
        self.bankdetailsLabel.setStyleSheet(_fromUtf8("\n"
"#bankdetailsLabel{\n"
"font-size:25px;\n"
"background-color:transparent;\n"
"color:yellow;\n"
"border-width:2px;\n"
"border-color:black;\n"
"border-style:groove;\n"
"margin-bottom:5px;\n"
"}\n"
"\n"
"#bankdetailsLabel:hover\n"
"{\n"
"font-size:25px;\n"
"background-color:transparent;\n"
"color:purple;\n"
"border-width:2px;\n"
"border-color:yellow;\n"
"border-style:groove;\n"
"margin-bottom:5px;\n"
"\n"
"\n"
"}"))
        self.bankdetailsLabel.setObjectName(_fromUtf8("bankdetailsLabel"))
        self.gridLayout_3.addWidget(self.bankdetailsLabel, 8, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 10, 0, 1, 1)
        self.ncclogoLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ncclogoLabel.sizePolicy().hasHeightForWidth())
        self.ncclogoLabel.setSizePolicy(sizePolicy)
        self.ncclogoLabel.setMaximumSize(QtCore.QSize(300, 330))
        self.ncclogoLabel.setSizeIncrement(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ncclogoLabel.setFont(font)
        self.ncclogoLabel.setStyleSheet(_fromUtf8("background-size:10px;\n"
"font-size:50%;\n"
"background-color:transparent;"))
        self.ncclogoLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.ncclogoLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.ncclogoLabel.setText(_fromUtf8(""))
        self.ncclogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ncc2.png")))
        self.ncclogoLabel.setScaledContents(True)
        self.ncclogoLabel.setObjectName(_fromUtf8("ncclogoLabel"))
        self.gridLayout_3.addWidget(self.ncclogoLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_2 = QtGui.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(600, 0))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 13, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 7, 0, 1, 1)
        self.enrolformFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.enrolformFrame.setStyleSheet(_fromUtf8("\n"
"#enrolformFrame{\n"
"font-family:georgia;\n"
"font-weight:bold;\n"
"margin:2px;\n"
"background-color:transparent;\n"
"border-radius:15px;\n"
"\n"
"}\n"
"\n"
""))
        self.enrolformFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.enrolformFrame.setObjectName(_fromUtf8("enrolformFrame"))
        self.Enrol_form = QtGui.QFormLayout(self.enrolformFrame)
        self.Enrol_form.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.Enrol_form.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.Enrol_form.setRowWrapPolicy(QtGui.QFormLayout.DontWrapRows)
        self.Enrol_form.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Enrol_form.setContentsMargins(10, -1, 10, -1)
        self.Enrol_form.setHorizontalSpacing(9)
        self.Enrol_form.setVerticalSpacing(10)
        self.Enrol_form.setObjectName(_fromUtf8("Enrol_form"))
        self.enrolmentnumLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.enrolmentnumLabel.setFont(font)
        self.enrolmentnumLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.enrolmentnumLabel.setObjectName(_fromUtf8("enrolmentnumLabel"))
        self.Enrol_form.setWidget(0, QtGui.QFormLayout.LabelRole, self.enrolmentnumLabel)
        self.enrolmentnumLineEdit = QtGui.QLineEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enrolmentnumLineEdit.setFont(font)
        self.enrolmentnumLineEdit.setStyleSheet(_fromUtf8(""))
        self.enrolmentnumLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.enrolmentnumLineEdit.setText(_fromUtf8(""))
        self.enrolmentnumLineEdit.setObjectName(_fromUtf8("enrolmentnumLineEdit"))
        self.Enrol_form.setWidget(0, QtGui.QFormLayout.FieldRole, self.enrolmentnumLineEdit)
        self.rankLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.rankLabel.setFont(font)
        self.rankLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.rankLabel.setObjectName(_fromUtf8("rankLabel"))
        self.Enrol_form.setWidget(2, QtGui.QFormLayout.LabelRole, self.rankLabel)
        self.rankComboBox = QtGui.QComboBox(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rankComboBox.setFont(font)
        self.rankComboBox.setEditable(False)
        self.rankComboBox.setFrame(False)
        self.rankComboBox.setObjectName(_fromUtf8("rankComboBox"))
        self.rankComboBox.addItem(_fromUtf8(""))
        self.rankComboBox.addItem(_fromUtf8(""))
        self.rankComboBox.addItem(_fromUtf8(""))
        self.rankComboBox.addItem(_fromUtf8(""))
        self.rankComboBox.addItem(_fromUtf8(""))
        self.rankComboBox.addItem(_fromUtf8(""))
        self.rankComboBox.addItem(_fromUtf8(""))
        self.Enrol_form.setWidget(2, QtGui.QFormLayout.FieldRole, self.rankComboBox)
        self.aadhaarLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.aadhaarLabel.setFont(font)
        self.aadhaarLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.aadhaarLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.aadhaarLabel.setTextFormat(QtCore.Qt.PlainText)
        self.aadhaarLabel.setObjectName(_fromUtf8("aadhaarLabel"))
        self.Enrol_form.setWidget(3, QtGui.QFormLayout.LabelRole, self.aadhaarLabel)
        self.aadhaarLineEdit = QtGui.QLineEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aadhaarLineEdit.setFont(font)
        self.aadhaarLineEdit.setMouseTracking(True)
        self.aadhaarLineEdit.setAcceptDrops(True)
        self.aadhaarLineEdit.setStyleSheet(_fromUtf8(""))
        self.aadhaarLineEdit.setText(_fromUtf8(""))
        self.aadhaarLineEdit.setFrame(True)
        self.aadhaarLineEdit.setObjectName(_fromUtf8("aadhaarLineEdit"))
        self.Enrol_form.setWidget(3, QtGui.QFormLayout.FieldRole, self.aadhaarLineEdit)
        self.fullnameLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fullnameLabel.setFont(font)
        self.fullnameLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.fullnameLabel.setObjectName(_fromUtf8("fullnameLabel"))
        self.Enrol_form.setWidget(5, QtGui.QFormLayout.LabelRole, self.fullnameLabel)
        self.fullnameLineEdit = QtGui.QLineEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fullnameLineEdit.setFont(font)
        self.fullnameLineEdit.setStyleSheet(_fromUtf8("b"))
        self.fullnameLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.fullnameLineEdit.setText(_fromUtf8(""))
        self.fullnameLineEdit.setObjectName(_fromUtf8("fullnameLineEdit"))
        self.Enrol_form.setWidget(5, QtGui.QFormLayout.FieldRole, self.fullnameLineEdit)
        self.fathernameLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fathernameLabel.setFont(font)
        self.fathernameLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.fathernameLabel.setObjectName(_fromUtf8("fathernameLabel"))
        self.Enrol_form.setWidget(6, QtGui.QFormLayout.LabelRole, self.fathernameLabel)
        self.fathernameLineEdit = QtGui.QLineEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fathernameLineEdit.setFont(font)
        self.fathernameLineEdit.setStyleSheet(_fromUtf8("b"))
        self.fathernameLineEdit.setObjectName(_fromUtf8("fathernameLineEdit"))
        self.Enrol_form.setWidget(6, QtGui.QFormLayout.FieldRole, self.fathernameLineEdit)
        self.mothernameLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mothernameLabel.setFont(font)
        self.mothernameLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.mothernameLabel.setObjectName(_fromUtf8("mothernameLabel"))
        self.Enrol_form.setWidget(7, QtGui.QFormLayout.LabelRole, self.mothernameLabel)
        self.mothernameLineEdit = QtGui.QLineEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mothernameLineEdit.setFont(font)
        self.mothernameLineEdit.setStyleSheet(_fromUtf8("b"))
        self.mothernameLineEdit.setObjectName(_fromUtf8("mothernameLineEdit"))
        self.Enrol_form.setWidget(7, QtGui.QFormLayout.FieldRole, self.mothernameLineEdit)
        self.sexLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.sexLabel.setFont(font)
        self.sexLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.sexLabel.setObjectName(_fromUtf8("sexLabel"))
        self.Enrol_form.setWidget(8, QtGui.QFormLayout.LabelRole, self.sexLabel)
        self.sexComboBox = QtGui.QComboBox(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sexComboBox.setFont(font)
        self.sexComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sexComboBox.setStyleSheet(_fromUtf8("width:100px;"))
        self.sexComboBox.setIconSize(QtCore.QSize(16, 16))
        self.sexComboBox.setFrame(False)
        self.sexComboBox.setObjectName(_fromUtf8("sexComboBox"))
        self.sexComboBox.addItem(_fromUtf8(""))
        self.sexComboBox.addItem(_fromUtf8(""))
        self.Enrol_form.setWidget(8, QtGui.QFormLayout.FieldRole, self.sexComboBox)
        self.dateofbirthLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.dateofbirthLabel.setFont(font)
        self.dateofbirthLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.dateofbirthLabel.setObjectName(_fromUtf8("dateofbirthLabel"))
        self.Enrol_form.setWidget(11, QtGui.QFormLayout.LabelRole, self.dateofbirthLabel)
        self.dateofbirthDateEdit = QtGui.QDateEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateofbirthDateEdit.setFont(font)
        self.dateofbirthDateEdit.setFrame(True)
        self.dateofbirthDateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.dateofbirthDateEdit.setDate(QtCore.QDate(2000, 1, 1))
        self.dateofbirthDateEdit.setCalendarPopup(True)
        self.dateofbirthDateEdit.setObjectName(_fromUtf8("dateofbirthDateEdit"))
        self.Enrol_form.setWidget(11, QtGui.QFormLayout.FieldRole, self.dateofbirthDateEdit)
        self.addressLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.addressLabel.setFont(font)
        self.addressLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.Enrol_form.setWidget(13, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.addressTextEdit = QtGui.QTextEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addressTextEdit.setFont(font)
        self.addressTextEdit.setStyleSheet(_fromUtf8("border-radius:5px;"))
        self.addressTextEdit.setObjectName(_fromUtf8("addressTextEdit"))
        self.Enrol_form.setWidget(13, QtGui.QFormLayout.FieldRole, self.addressTextEdit)
        self.emailLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.emailLabel.setFont(font)
        self.emailLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.Enrol_form.setWidget(14, QtGui.QFormLayout.LabelRole, self.emailLabel)
        self.emailLineEdit = QtGui.QLineEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setStyleSheet(_fromUtf8(""))
        self.emailLineEdit.setText(_fromUtf8(""))
        self.emailLineEdit.setObjectName(_fromUtf8("emailLineEdit"))
        self.Enrol_form.setWidget(14, QtGui.QFormLayout.FieldRole, self.emailLineEdit)
        self.mobileLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mobileLabel.setFont(font)
        self.mobileLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.mobileLabel.setObjectName(_fromUtf8("mobileLabel"))
        self.Enrol_form.setWidget(15, QtGui.QFormLayout.LabelRole, self.mobileLabel)
        self.mobileLineEdit = QtGui.QLineEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mobileLineEdit.setFont(font)
        self.mobileLineEdit.setStyleSheet(_fromUtf8(""))
        self.mobileLineEdit.setObjectName(_fromUtf8("mobileLineEdit"))
        self.Enrol_form.setWidget(15, QtGui.QFormLayout.FieldRole, self.mobileLineEdit)
        self.bloodgroupLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bloodgroupLabel.setFont(font)
        self.bloodgroupLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.bloodgroupLabel.setObjectName(_fromUtf8("bloodgroupLabel"))
        self.Enrol_form.setWidget(16, QtGui.QFormLayout.LabelRole, self.bloodgroupLabel)
        self.bloodgroupComboBox = QtGui.QComboBox(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bloodgroupComboBox.setFont(font)
        self.bloodgroupComboBox.setAutoFillBackground(False)
        self.bloodgroupComboBox.setStyleSheet(_fromUtf8("height:25px;width:25%;"))
        self.bloodgroupComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.bloodgroupComboBox.setFrame(False)
        self.bloodgroupComboBox.setObjectName(_fromUtf8("bloodgroupComboBox"))
        self.bloodgroupComboBox.addItem(_fromUtf8(""))
        self.bloodgroupComboBox.addItem(_fromUtf8(""))
        self.bloodgroupComboBox.addItem(_fromUtf8(""))
        self.bloodgroupComboBox.addItem(_fromUtf8(""))
        self.bloodgroupComboBox.addItem(_fromUtf8(""))
        self.bloodgroupComboBox.addItem(_fromUtf8(""))
        self.bloodgroupComboBox.addItem(_fromUtf8(""))
        self.bloodgroupComboBox.addItem(_fromUtf8(""))
        self.Enrol_form.setWidget(16, QtGui.QFormLayout.FieldRole, self.bloodgroupComboBox)
        self.gridLayout_3.addWidget(self.enrolformFrame, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.bankformFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bankformFrame.setFont(font)
        self.bankformFrame.setStyleSheet(_fromUtf8("\n"
"#bankformFrame\n"
"{font-weight:bold;\n"
"background-color:transparent;;\n"
"border-radius:10px;\n"
"}"))
        self.bankformFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bankformFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.bankformFrame.setObjectName(_fromUtf8("bankformFrame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.bankformFrame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.banknameLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.banknameLineEdit.setFont(font)
        self.banknameLineEdit.setStyleSheet(_fromUtf8("b"))
        self.banknameLineEdit.setObjectName(_fromUtf8("banknameLineEdit"))
        self.gridLayout_2.addWidget(self.banknameLineEdit, 0, 1, 1, 1)
        self.ifsccodeLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ifsccodeLineEdit.setFont(font)
        self.ifsccodeLineEdit.setStyleSheet(_fromUtf8("b"))
        self.ifsccodeLineEdit.setObjectName(_fromUtf8("ifsccodeLineEdit"))
        self.gridLayout_2.addWidget(self.ifsccodeLineEdit, 5, 1, 1, 1)
        self.accountnameLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.accountnameLabel.setFont(font)
        self.accountnameLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.accountnameLabel.setOpenExternalLinks(False)
        self.accountnameLabel.setObjectName(_fromUtf8("accountnameLabel"))
        self.gridLayout_2.addWidget(self.accountnameLabel, 3, 0, 1, 1)
        self.accountnameLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.accountnameLineEdit.setFont(font)
        self.accountnameLineEdit.setStyleSheet(_fromUtf8("b"))
        self.accountnameLineEdit.setObjectName(_fromUtf8("accountnameLineEdit"))
        self.gridLayout_2.addWidget(self.accountnameLineEdit, 3, 1, 1, 1)
        self.accountnumLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.accountnumLabel.setFont(font)
        self.accountnumLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.accountnumLabel.setOpenExternalLinks(False)
        self.accountnumLabel.setObjectName(_fromUtf8("accountnumLabel"))
        self.gridLayout_2.addWidget(self.accountnumLabel, 4, 0, 1, 1)
        self.ifsccodeLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ifsccodeLabel.setFont(font)
        self.ifsccodeLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.ifsccodeLabel.setOpenExternalLinks(False)
        self.ifsccodeLabel.setObjectName(_fromUtf8("ifsccodeLabel"))
        self.gridLayout_2.addWidget(self.ifsccodeLabel, 5, 0, 1, 1)
        self.accountnumLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.accountnumLineEdit.setFont(font)
        self.accountnumLineEdit.setStyleSheet(_fromUtf8("b"))
        self.accountnumLineEdit.setObjectName(_fromUtf8("accountnumLineEdit"))
        self.gridLayout_2.addWidget(self.accountnumLineEdit, 4, 1, 1, 1)
        self.banknameLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.banknameLabel.setFont(font)
        self.banknameLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.banknameLabel.setOpenExternalLinks(False)
        self.banknameLabel.setObjectName(_fromUtf8("banknameLabel"))
        self.gridLayout_2.addWidget(self.banknameLabel, 0, 0, 1, 1)
        self.bankbranchLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bankbranchLabel.setFont(font)
        self.bankbranchLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.bankbranchLabel.setOpenExternalLinks(False)
        self.bankbranchLabel.setObjectName(_fromUtf8("bankbranchLabel"))
        self.gridLayout_2.addWidget(self.bankbranchLabel, 2, 0, 1, 1)
        self.bankbranchLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bankbranchLineEdit.setFont(font)
        self.bankbranchLineEdit.setStyleSheet(_fromUtf8("b"))
        self.bankbranchLineEdit.setObjectName(_fromUtf8("bankbranchLineEdit"))
        self.gridLayout_2.addWidget(self.bankbranchLineEdit, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.bankformFrame, 9, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.instFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.instFrame.setStyleSheet(_fromUtf8("#instFrame\n"
"{\n"
"width:500px;\n"
"border-radius:10px;\n"
"background-color:transparent;\n"
"}"))
        self.instFrame.setObjectName(_fromUtf8("instFrame"))
        self.gridLayout_4 = QtGui.QGridLayout(self.instFrame)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.unitLineEdit = QtGui.QLineEdit(self.instFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.unitLineEdit.setFont(font)
        self.unitLineEdit.setStyleSheet(_fromUtf8("b"))
        self.unitLineEdit.setObjectName(_fromUtf8("unitLineEdit"))
        self.gridLayout_4.addWidget(self.unitLineEdit, 1, 4, 1, 1)
        self.institutionLabel = QtGui.QLabel(self.instFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.institutionLabel.setFont(font)
        self.institutionLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.institutionLabel.setObjectName(_fromUtf8("institutionLabel"))
        self.gridLayout_4.addWidget(self.institutionLabel, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.instFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 1, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 6, 1, 1)
        self.institutionComboBox = QtGui.QComboBox(self.instFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.institutionComboBox.setFont(font)
        self.institutionComboBox.setObjectName(_fromUtf8("institutionComboBox"))
        self.institutionComboBox.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.institutionComboBox, 0, 4, 1, 1)
        self.gridLayout_3.addWidget(self.instFrame, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../Documents/CODES/ncc/Pictures/Screenshots/Screenshot (113).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mytab.addTab(self.Enrol, icon1, _fromUtf8(""))
        self.Query = QtGui.QWidget()
        self.Query.setStyleSheet(_fromUtf8("\n"
"#Query{    \n"
"    background-image:url(:/icons/simple_grad.png);\n"
"    background-position:center;\n"
"}"))
        self.Query.setObjectName(_fromUtf8("Query"))
        self.gridLayout_5 = QtGui.QGridLayout(self.Query)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.widget = QtGui.QWidget(self.Query)
        self.widget.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.checkboxFrame = QtGui.QFrame(self.widget)
        self.checkboxFrame.setMinimumSize(QtCore.QSize(0, 80))
        self.checkboxFrame.setSizeIncrement(QtCore.QSize(0, 4))
        self.checkboxFrame.setStyleSheet(_fromUtf8("font-size:100%;"))
        self.checkboxFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.checkboxFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.checkboxFrame.setObjectName(_fromUtf8("checkboxFrame"))
        self.gridLayout_7 = QtGui.QGridLayout(self.checkboxFrame)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.selectallCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        self.selectallCheckBox.setStyleSheet(_fromUtf8("#selectallCheckBox{\n"
"font: 75 16pt \"Caladea\";\n"
"color:rgb(255, 170, 0);\n"
"font-weight:bold;\n"
"}\n"
"\n"
"#selectallCheckBox:hover{\n"
"font: 75 12pt \"Georgia\";\n"
"color:rgb(255, 148, 241);\n"
"font-weight:bold;\n"
"\n"
"}"))
        self.selectallCheckBox.setObjectName(_fromUtf8("selectallCheckBox"))
        self.gridLayout_7.addWidget(self.selectallCheckBox, 0, 0, 1, 1)
        self.enrolmentCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.enrolmentCheckBox.setFont(font)
        self.enrolmentCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enrolmentCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox{\n"
"color:white;\n"
"font: 75 13pt \"Cambria\";\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover\n"
"{\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
""))
        self.enrolmentCheckBox.setObjectName(_fromUtf8("enrolmentCheckBox"))
        self.gridLayout_7.addWidget(self.enrolmentCheckBox, 0, 1, 1, 1)
        self.rankCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rankCheckBox.setFont(font)
        self.rankCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rankCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    color:yellow;\n"
"    font: 75 16pt \"Cambria\";\n"
"    text-decoration: underline;\n"
"}"))
        self.rankCheckBox.setObjectName(_fromUtf8("rankCheckBox"))
        self.gridLayout_7.addWidget(self.rankCheckBox, 0, 2, 1, 1)
        self.sfnameCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.sfnameCheckBox.setFont(font)
        self.sfnameCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sfnameCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.sfnameCheckBox.setObjectName(_fromUtf8("sfnameCheckBox"))
        self.gridLayout_7.addWidget(self.sfnameCheckBox, 0, 3, 1, 1)
        self.ffnameCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ffnameCheckBox.setFont(font)
        self.ffnameCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ffnameCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.ffnameCheckBox.setObjectName(_fromUtf8("ffnameCheckBox"))
        self.gridLayout_7.addWidget(self.ffnameCheckBox, 0, 4, 1, 1)
        self.mfnameCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.mfnameCheckBox.setFont(font)
        self.mfnameCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mfnameCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.mfnameCheckBox.setObjectName(_fromUtf8("mfnameCheckBox"))
        self.gridLayout_7.addWidget(self.mfnameCheckBox, 0, 5, 1, 1)
        self.sexCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.sexCheckBox.setFont(font)
        self.sexCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sexCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.sexCheckBox.setObjectName(_fromUtf8("sexCheckBox"))
        self.gridLayout_7.addWidget(self.sexCheckBox, 0, 6, 1, 1)
        self.bloodgroupCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bloodgroupCheckBox.setFont(font)
        self.bloodgroupCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.bloodgroupCheckBox.setObjectName(_fromUtf8("bloodgroupCheckBox"))
        self.gridLayout_7.addWidget(self.bloodgroupCheckBox, 0, 7, 1, 1)
        self.mobileCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.mobileCheckBox.setFont(font)
        self.mobileCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.mobileCheckBox.setObjectName(_fromUtf8("mobileCheckBox"))
        self.gridLayout_7.addWidget(self.mobileCheckBox, 0, 8, 1, 1)
        self.emailCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.emailCheckBox.setFont(font)
        self.emailCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.emailCheckBox.setObjectName(_fromUtf8("emailCheckBox"))
        self.gridLayout_7.addWidget(self.emailCheckBox, 0, 9, 1, 1)
        self.dateofbirthCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.dateofbirthCheckBox.setFont(font)
        self.dateofbirthCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateofbirthCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.dateofbirthCheckBox.setObjectName(_fromUtf8("dateofbirthCheckBox"))
        self.gridLayout_7.addWidget(self.dateofbirthCheckBox, 1, 0, 1, 1)
        self.aadhaarCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.aadhaarCheckBox.setFont(font)
        self.aadhaarCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aadhaarCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover\n"
"{\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
""))
        self.aadhaarCheckBox.setObjectName(_fromUtf8("aadhaarCheckBox"))
        self.gridLayout_7.addWidget(self.aadhaarCheckBox, 1, 1, 1, 1)
        self.institutionCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.institutionCheckBox.setFont(font)
        self.institutionCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.institutionCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
""))
        self.institutionCheckBox.setObjectName(_fromUtf8("institutionCheckBox"))
        self.gridLayout_7.addWidget(self.institutionCheckBox, 1, 2, 1, 1)
        self.unitCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.unitCheckBox.setFont(font)
        self.unitCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.unitCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.unitCheckBox.setTristate(False)
        self.unitCheckBox.setObjectName(_fromUtf8("unitCheckBox"))
        self.gridLayout_7.addWidget(self.unitCheckBox, 1, 3, 1, 1)
        self.banknameCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.banknameCheckBox.setFont(font)
        self.banknameCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.banknameCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
"\n"
"#banknameCheckBox:checked\n"
"{    \n"
"font-color:black;\n"
"    \n"
"}"))
        self.banknameCheckBox.setChecked(False)
        self.banknameCheckBox.setObjectName(_fromUtf8("banknameCheckBox"))
        self.gridLayout_7.addWidget(self.banknameCheckBox, 1, 4, 1, 1)
        self.bankbranchCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bankbranchCheckBox.setFont(font)
        self.bankbranchCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bankbranchCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox, #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox:hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.bankbranchCheckBox.setObjectName(_fromUtf8("bankbranchCheckBox"))
        self.gridLayout_7.addWidget(self.bankbranchCheckBox, 1, 5, 1, 1)
        self.accountnameCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.accountnameCheckBox.setFont(font)
        self.accountnameCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.accountnameCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.accountnameCheckBox.setObjectName(_fromUtf8("accountnameCheckBox"))
        self.gridLayout_7.addWidget(self.accountnameCheckBox, 1, 6, 1, 1)
        self.accountnumCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.accountnumCheckBox.setFont(font)
        self.accountnumCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckBox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckBox:hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.accountnumCheckBox.setObjectName(_fromUtf8("accountnumCheckBox"))
        self.gridLayout_7.addWidget(self.accountnumCheckBox, 1, 7, 1, 1)
        self.addressCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addressCheckBox.setFont(font)
        self.addressCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addressCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.addressCheckBox.setObjectName(_fromUtf8("addressCheckBox"))
        self.gridLayout_7.addWidget(self.addressCheckBox, 1, 8, 1, 1)
        self.ifsccodeCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("cambria"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ifsccodeCheckBox.setFont(font)
        self.ifsccodeCheckBox.setStyleSheet(_fromUtf8("#enrolmentCheckBox,#aadhaarCheckBox,#rankCheckBox,#sfnameCheckBox,#ffnameCheckBox,#mfnameCheckBox,#sexCheckBox,#bloodgroupCheckBox,#emailCheckBox,#mobileCheckBox,#addressCheckBox,#dateofbirthCheckBox,#institutionCheckBox,#unitCheckBox,#banknameCheckBox,#bankbranchCheckBox , #accountnameCheckBox, #accountnumCheckbox , #ifsccodeCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrolmentCheckBox:hover,#aadhaarCheckBox:hover,#rankCheckBox:hover,#sfnameCheckBox:hover,#ffnameCheckBox:hover,#mfnameCheckBox:hover,#sexCheckBox:hover,#bloodgroupCheckBox:hover,#emailCheckBox:hover,#mobileCheckBox:hover,#addressCheckBox:hover,#dateofbirthCheckBox:hover,#institutionCheckBox:hover,#unitCheckBox:hover,#banknameCheckBox:hover,#bankbranchCheckBox :hover, #accountnameCheckBox:hover, #accountnumCheckbox :hover, #ifsccodeCheckBox:hover{\n"
"    text-decoration:underline;\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}"))
        self.ifsccodeCheckBox.setObjectName(_fromUtf8("ifsccodeCheckBox"))
        self.gridLayout_7.addWidget(self.ifsccodeCheckBox, 1, 9, 1, 1)
        self.verticalLayout_4.addWidget(self.checkboxFrame)
        self.frame = QtGui.QFrame(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        self.frame.setFont(font)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.conditionsentrylabel = QtGui.QLabel(self.frame)
        self.conditionsentrylabel.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 169, 203, 252), stop:1 rgba(255, 77, 127, 248));\n"
"color:black;\n"
"font: 14pt \"Georgia\";\n"
"padding:15px;\n"
""))
        self.conditionsentrylabel.setObjectName(_fromUtf8("conditionsentrylabel"))
        self.verticalLayout_3.addWidget(self.conditionsentrylabel)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.andcondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.andcondition.setFont(font)
        self.andcondition.setStyleSheet(_fromUtf8("#andcondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"georgia\";\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:120%;\n"
"}\n"
"\n"
"#andcondition:hover\n"
"{color:rgb(255,255,255);\n"
"padding-left:18px;\n"
"padding-right:22px;\n"
"font: 75 15pt \"georgia\";\n"
"border-style:groove;\n"
"border-color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.602, y1:0.392364, x2:0, y2:1, stop:0 rgba(254, 77, 0, 255), stop:1 rgba(122, 255, 73, 255));\n"
"border-width:3px;\n"
"height:25px;\n"
"width:120%;\n"
"}"))
        self.andcondition.setObjectName(_fromUtf8("andcondition"))
        self.horizontalLayout_5.addWidget(self.andcondition)
        self.orcondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.orcondition.setFont(font)
        self.orcondition.setStyleSheet(_fromUtf8("#orcondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"georgia\";\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:120%;\n"
"}\n"
"\n"
"#orcondition:hover\n"
"{color:rgb(255,255,255);\n"
"padding-left:18px;\n"
"padding-right:22px;\n"
"font: 75 15pt \"georgia\";\n"
"border-style:groove;\n"
"border-color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.602, y1:0.392364, x2:0, y2:1, stop:0 rgba(254, 77, 0, 255), stop:1 rgba(122, 255, 73, 255));\n"
"border-width:3px;\n"
"height:25px;\n"
"width:120%;\n"
"}"))
        self.orcondition.setObjectName(_fromUtf8("orcondition"))
        self.horizontalLayout_5.addWidget(self.orcondition)
        self.openbracecondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.openbracecondition.setFont(font)
        self.openbracecondition.setStyleSheet(_fromUtf8("#openbracecondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:120%;\n"
"}\n"
"\n"
"#openbracecondition:hover\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"background-color: rgb(255, 170, 0);\n"
"width:120%;\n"
"border-width:3px;\n"
"height:25px;\n"
"}"))
        self.openbracecondition.setObjectName(_fromUtf8("openbracecondition"))
        self.horizontalLayout_5.addWidget(self.openbracecondition)
        self.closebracecondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.closebracecondition.setFont(font)
        self.closebracecondition.setStyleSheet(_fromUtf8("#closebracecondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:120%;;\n"
"}\n"
"\n"
"#closebracecondition:hover\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"background-color: rgb(255, 170, 0);\n"
"width:120%;\n"
"border-width:3px;\n"
"height:25px;\n"
"}"))
        self.closebracecondition.setObjectName(_fromUtf8("closebracecondition"))
        self.horizontalLayout_5.addWidget(self.closebracecondition)
        self.equalscondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.equalscondition.setFont(font)
        self.equalscondition.setStyleSheet(_fromUtf8("#equalscondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:120%;\n"
"}\n"
"\n"
"#equalscondition:hover\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"background-color: rgb(255, 170, 0);\n"
"width:120%;\n"
"border-width:3px;\n"
"height:25px;\n"
"}"))
        self.equalscondition.setObjectName(_fromUtf8("equalscondition"))
        self.horizontalLayout_5.addWidget(self.equalscondition)
        self.greatercondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.greatercondition.setFont(font)
        self.greatercondition.setStyleSheet(_fromUtf8("#greatercondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:120%;\n"
"}\n"
"\n"
"#greatercondition:hover\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"background-color: rgb(255, 170, 0);\n"
"width:120%;\n"
"border-width:3px;\n"
"height:25px;\n"
"}"))
        self.greatercondition.setObjectName(_fromUtf8("greatercondition"))
        self.horizontalLayout_5.addWidget(self.greatercondition)
        self.lessercondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lessercondition.setFont(font)
        self.lessercondition.setStyleSheet(_fromUtf8("#lessercondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:120%;\n"
"}\n"
"\n"
"#lessercondition:hover\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"background-color: rgb(255, 170, 0);\n"
"width:120%;\n"
"border-width:3px;\n"
"height:25px;\n"
"}"))
        self.lessercondition.setObjectName(_fromUtf8("lessercondition"))
        self.horizontalLayout_5.addWidget(self.lessercondition)
        self.backcondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.backcondition.setFont(font)
        self.backcondition.setStyleSheet(_fromUtf8("#backcondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"georgia\";\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:120%;\n"
"margin:5px;\n"
"}\n"
"\n"
"#backcondition:hover\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:18px;\n"
"padding-right:22px;\n"
"font: 75 15pt \"georgia\";\n"
"border-style:groove;\n"
"border-color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.012, y1:0.755818, x2:0.641818, y2:0.392, stop:0 rgba(230, 255, 0, 255), stop:1 rgba(85, 104, 255, 255));\n"
"border-width:3px;\n"
"height:25px;\n"
"width:120%;\n"
"}"))
        self.backcondition.setObjectName(_fromUtf8("backcondition"))
        self.horizontalLayout_5.addWidget(self.backcondition)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.conditionlistcombobox = QtGui.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.conditionlistcombobox.setFont(font)
        self.conditionlistcombobox.setStyleSheet(_fromUtf8("#conditionlistcombobox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 12pt \"georgia\";\n"
"width:100%;\n"
"height:30px;\n"
"}\n"
"#conditionlistcombobox:hover{\n"
"    color:darkblue;\n"
"    background-color:  rgb(255, 219, 194);\n"
"    font: 14pt \"georgia\";\n"
"}"))
        self.conditionlistcombobox.setObjectName(_fromUtf8("conditionlistcombobox"))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.conditionlistcombobox)
        self.valuelineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.valuelineEdit.setFont(font)
        self.valuelineEdit.setStyleSheet(_fromUtf8("#valuelineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    width:100%;\n"
"height:30px;\n"
"}\n"
"#valuelineEdit:hover{\n"
"    color:rgb(0, 85, 255);\n"
"    background-color:rgb(214, 214, 214);\n"
"    font: 14pt \"georgia\";\n"
"}"))
        self.valuelineEdit.setObjectName(_fromUtf8("valuelineEdit"))
        self.horizontalLayout_3.addWidget(self.valuelineEdit)
        self.insertcondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.insertcondition.setFont(font)
        self.insertcondition.setStyleSheet(_fromUtf8("#insertcondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"georgia\";\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:10px;\n"
"width:120%;\n"
"}\n"
"\n"
"#insertcondition:hover\n"
"{\n"
"color:white;\n"
"padding-left:18px;\n"
"padding-right:22px;\n"
"font: 75 14pt \"georgia\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:reflect, x1:0.284, y1:0, x2:0.675, y2:0, stop:0 rgba(71, 68, 230, 255), stop:1 rgba(78, 212, 223, 255));\n"
"width:120%;\n"
"}"))
        self.insertcondition.setObjectName(_fromUtf8("insertcondition"))
        self.horizontalLayout_3.addWidget(self.insertcondition)
        self.clearcondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.clearcondition.setFont(font)
        self.clearcondition.setStyleSheet(_fromUtf8("#clearcondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"georgia\";\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:10px;\n"
"width:120%;\n"
"}\n"
"\n"
"#clearcondition:hover\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:18px;\n"
"padding-right:22px;\n"
"font: 75 14pt \"georgia\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 234), stop:0.05 rgba(14, 8, 73, 255), stop:0.119318 rgba(28, 17, 145, 254), stop:0.477273 rgba(126, 14, 81, 237), stop:0.744318 rgba(234, 11, 11, 246), stop:0.79 rgba(244, 70, 5, 245), stop:0.86 rgba(255, 136, 0, 248), stop:0.935 rgba(239, 236, 55, 250));\n"
"width:120%;\n"
"}"))
        self.clearcondition.setObjectName(_fromUtf8("clearcondition"))
        self.horizontalLayout_3.addWidget(self.clearcondition)
        self.querycondition = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.querycondition.setFont(font)
        self.querycondition.setStyleSheet(_fromUtf8("#querycondition{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 12pt \"georgia\";\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:3px;\n"
"height:30px;\n"
"border-radius:10px;\n"
"width:120%;\n"
"}\n"
"\n"
"#querycondition:hover\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:18px;\n"
"padding-right:22px;\n"
"font: 75 15pt \"georgia\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 24, 230), stop:0.085 rgba(2, 79, 0, 255), stop:0.221591 rgba(50, 147, 22, 255), stop:0.275 rgba(165, 142, 70, 255), stop:0.431818 rgba(243, 100, 79, 255), stop:0.573864 rgba(135, 95, 80, 255), stop:0.667 rgba(137, 97, 255, 255), stop:0.818182 rgba(160, 255, 244, 255), stop:0.885 rgba(193, 222, 185, 255), stop:1 rgba(93, 128, 0, 255));\n"
"width:130%;\n"
"}"))
        self.querycondition.setObjectName(_fromUtf8("querycondition"))
        self.horizontalLayout_3.addWidget(self.querycondition)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.webView = QtWebKit.QWebView(self.frame)
        self.webView.setAcceptDrops(True)
        self.webView.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_3.addWidget(self.webView)
        self.verticalLayout_4.addWidget(self.frame)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../Documents/CODES/ncc/Pictures/Screenshots/Screenshot (107).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mytab.addTab(self.Query, icon2, _fromUtf8(""))
        self.Forms = QtGui.QWidget()
        self.Forms.setStyleSheet(_fromUtf8("#Forms{\n"
"    background-image: url(:/icons/green_grad.png);\n"
"background-position:center;\n"
"\n"
"}"))
        self.Forms.setObjectName(_fromUtf8("Forms"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.Forms)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_2 = QtGui.QLabel(self.Forms)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("background-color:transparent;\n"
"font-size:50px;\n"
"color:blue;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.comboBox = QtGui.QComboBox(self.Forms)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(12, _fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.comboBox, QtCore.Qt.AlignHCenter)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem11)
        self.label_3 = QtGui.QLabel(self.Forms)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("font-size:25px;\n"
"background-color:transparent;\n"
"color:black;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3, QtCore.Qt.AlignHCenter)
        self.entryBox = QtGui.QTextEdit(self.Forms)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Caladea"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.entryBox.setFont(font)
        self.entryBox.setStyleSheet(_fromUtf8("background-image: url(:/icons/images-7.jpg);\n"
"border-radius:10px;\n"
"border-width:2px;\n"
"border-style:groove;\n"
"color:black;\n"
"width:40%;"))
        self.entryBox.setObjectName(_fromUtf8("entryBox"))
        self.verticalLayout_5.addWidget(self.entryBox)
        self.webView_2 = QtWebKit.QWebView(self.Forms)
        self.webView_2.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.webView_2.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView_2.setObjectName(_fromUtf8("webView_2"))
        self.verticalLayout_5.addWidget(self.webView_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.generate_excell_sheetPushButton = QtGui.QPushButton(self.Forms)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.generate_excell_sheetPushButton.setFont(font)
        self.generate_excell_sheetPushButton.setStyleSheet(_fromUtf8("\n"
"#Button_1{\n"
"background-color: rgb(255, 255, 255);\n"
"    border-color: rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"height:50px;\n"
"font-size:25px;\n"
"color:rgb(85, 170, 255);\n"
"}\n"
"#Button_1:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"border-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"height:50px;\n"
"color:rgb(255, 255, 255);\n"
"font-size:30px;\n"
"padding-top:-10px;\n"
"}\n"
""))
        self.generate_excell_sheetPushButton.setObjectName(_fromUtf8("generate_excell_sheetPushButton"))
        self.horizontalLayout_2.addWidget(self.generate_excell_sheetPushButton)
        self.open_in_pdfPushButton = QtGui.QPushButton(self.Forms)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.open_in_pdfPushButton.setFont(font)
        self.open_in_pdfPushButton.setStyleSheet(_fromUtf8("\n"
"#Button_2{\n"
"background-color: rgb(255, 255, 255);\n"
"    border-color: rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"height:50px;\n"
"font-size:25px;\n"
"color:rgb(85, 170, 255);\n"
"}\n"
"#Button_2:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"border-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"height:50px;\n"
"color:rgb(255, 255, 255);\n"
"font-size:30px;\n"
"padding-top:-10px;\n"
"}\n"
""))
        self.open_in_pdfPushButton.setObjectName(_fromUtf8("open_in_pdfPushButton"))
        self.horizontalLayout_2.addWidget(self.open_in_pdfPushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.mytab.addTab(self.Forms, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.mytab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mytab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NCC", None))
        self.searchbyfieldLineEdit.setPlaceholderText(_translate("MainWindow", "Search by", None))
        self.searchPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to search</p></body></html>", None))
        self.searchPushButton.setText(_translate("MainWindow", "Search", None))
        self.enrolmentnumRadioButton.setText(_translate("MainWindow", "Enrolment No.", None))
        self.aadhaarnumRadioButton.setText(_translate("MainWindow", "Aadhaar No.", None))
        self.enroltitleLabel.setText(_translate("MainWindow", "Enrolment Form", None))
        self.submitPushButton.setText(_translate("MainWindow", "Submit", None))
        self.bankdetailsLabel.setText(_translate("MainWindow", "Bank Details", None))
        self.enrolmentnumLabel.setToolTip(_translate("MainWindow", "Mandatory field", None))
        self.enrolmentnumLabel.setText(_translate("MainWindow", "<html><head/><body><p>Enrolment No.  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:red;\">*</span></p></body></html>", None))
        self.rankLabel.setText(_translate("MainWindow", "Rank", None))
        self.rankComboBox.setItemText(0, _translate("MainWindow", "Cadet (CDT)", None))
        self.rankComboBox.setItemText(1, _translate("MainWindow", "Lance Corporal (LCPL)", None))
        self.rankComboBox.setItemText(2, _translate("MainWindow", "Corporal (CPL)", None))
        self.rankComboBox.setItemText(3, _translate("MainWindow", "Sergent (SGT)", None))
        self.rankComboBox.setItemText(4, _translate("MainWindow", "Company Sergent Major (CSM)", None))
        self.rankComboBox.setItemText(5, _translate("MainWindow", "Junior Under Officer (JUO)", None))
        self.rankComboBox.setItemText(6, _translate("MainWindow", "Senior Under Officer (SUO)", None))
        self.aadhaarLabel.setText(_translate("MainWindow", "Aadhaar No.", None))
        self.aadhaarLineEdit.setPlaceholderText(_translate("MainWindow", "12 digit Aadhaar number", None))
        self.fullnameLabel.setText(_translate("MainWindow", "<html><head/><body><p>Full Name  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.fathernameLabel.setText(_translate("MainWindow", "<html><head/><body><p>Father\'s Name  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.mothernameLabel.setText(_translate("MainWindow", "<html><head/><body><p>Mother\'s Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.sexLabel.setText(_translate("MainWindow", "Sex", None))
        self.sexComboBox.setItemText(0, _translate("MainWindow", "Male", None))
        self.sexComboBox.setItemText(1, _translate("MainWindow", "Female", None))
        self.dateofbirthLabel.setText(_translate("MainWindow", "Date of Birth", None))
        self.dateofbirthDateEdit.setDisplayFormat(_translate("MainWindow", "dd/MMM/yyyy", None))
        self.addressLabel.setText(_translate("MainWindow", "<html><head/><body><p>Residential Address &nbsp;&nbsp;<span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.emailLabel.setText(_translate("MainWindow", "Email", None))
        self.mobileLabel.setText(_translate("MainWindow", "Mobile", None))
        self.mobileLineEdit.setPlaceholderText(_translate("MainWindow", "10 digit Mobile number", None))
        self.bloodgroupLabel.setText(_translate("MainWindow", "Blood Group", None))
        self.bloodgroupComboBox.setItemText(0, _translate("MainWindow", "O+", None))
        self.bloodgroupComboBox.setItemText(1, _translate("MainWindow", "O-", None))
        self.bloodgroupComboBox.setItemText(2, _translate("MainWindow", "A+", None))
        self.bloodgroupComboBox.setItemText(3, _translate("MainWindow", "A-", None))
        self.bloodgroupComboBox.setItemText(4, _translate("MainWindow", "B+", None))
        self.bloodgroupComboBox.setItemText(5, _translate("MainWindow", "B-", None))
        self.bloodgroupComboBox.setItemText(6, _translate("MainWindow", "AB+", None))
        self.bloodgroupComboBox.setItemText(7, _translate("MainWindow", "AB-", None))
        self.accountnameLabel.setText(_translate("MainWindow", "Account name", None))
        self.accountnumLabel.setText(_translate("MainWindow", "Account No.", None))
        self.ifsccodeLabel.setText(_translate("MainWindow", "IFSC code", None))
        self.banknameLabel.setText(_translate("MainWindow", "Bank Name", None))
        self.bankbranchLabel.setText(_translate("MainWindow", "Branch", None))
        self.unitLineEdit.setText(_translate("MainWindow", "4kar", None))
        self.institutionLabel.setText(_translate("MainWindow", "<html><head/><body><p>Institution &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:#ff0000;\"> </span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Unit &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:#ff0000;\"> *</span></p></body></html>", None))
        self.institutionComboBox.setItemText(0, _translate("MainWindow", "Sarvodaya PU College", None))
        self.mytab.setTabText(self.mytab.indexOf(self.Enrol), _translate("MainWindow", "Enrolment form", None))
        self.mytab.setTabToolTip(self.mytab.indexOf(self.Enrol), _translate("MainWindow", "Enrolment form for NCC", None))
        self.selectallCheckBox.setText(_translate("MainWindow", "Select All", None))
        self.enrolmentCheckBox.setText(_translate("MainWindow", "Enrolment", None))
        self.rankCheckBox.setText(_translate("MainWindow", "Rank", None))
        self.sfnameCheckBox.setText(_translate("MainWindow", "Student Name", None))
        self.ffnameCheckBox.setText(_translate("MainWindow", "Father Name", None))
        self.mfnameCheckBox.setText(_translate("MainWindow", "Mother Name", None))
        self.sexCheckBox.setText(_translate("MainWindow", "Sex", None))
        self.bloodgroupCheckBox.setText(_translate("MainWindow", "Blood Group", None))
        self.mobileCheckBox.setText(_translate("MainWindow", "Mobile", None))
        self.emailCheckBox.setText(_translate("MainWindow", "E-mail", None))
        self.dateofbirthCheckBox.setText(_translate("MainWindow", "Date of Birth", None))
        self.aadhaarCheckBox.setText(_translate("MainWindow", "Aadhaar", None))
        self.institutionCheckBox.setText(_translate("MainWindow", "Institution", None))
        self.unitCheckBox.setText(_translate("MainWindow", "Unit", None))
        self.banknameCheckBox.setText(_translate("MainWindow", "Bank Name", None))
        self.bankbranchCheckBox.setText(_translate("MainWindow", "Branch Name", None))
        self.accountnameCheckBox.setText(_translate("MainWindow", "Account Name", None))
        self.accountnumCheckBox.setText(_translate("MainWindow", "Account Num", None))
        self.addressCheckBox.setText(_translate("MainWindow", "Address", None))
        self.ifsccodeCheckBox.setText(_translate("MainWindow", "IFSC Code", None))
        self.andcondition.setText(_translate("MainWindow", "AND", None))
        self.orcondition.setText(_translate("MainWindow", "OR", None))
        self.openbracecondition.setText(_translate("MainWindow", "(", None))
        self.closebracecondition.setText(_translate("MainWindow", ")", None))
        self.equalscondition.setText(_translate("MainWindow", "=", None))
        self.greatercondition.setText(_translate("MainWindow", ">", None))
        self.lessercondition.setText(_translate("MainWindow", "<", None))
        self.backcondition.setText(_translate("MainWindow", "Back", None))
        self.conditionlistcombobox.setItemText(0, _translate("MainWindow", "Select", None))
        self.conditionlistcombobox.setItemText(1, _translate("MainWindow", "Enrolment_no", None))
        self.conditionlistcombobox.setItemText(2, _translate("MainWindow", "Aadhar", None))
        self.conditionlistcombobox.setItemText(3, _translate("MainWindow", "Rank", None))
        self.conditionlistcombobox.setItemText(4, _translate("MainWindow", "Student_name", None))
        self.conditionlistcombobox.setItemText(5, _translate("MainWindow", "Fathers_name", None))
        self.conditionlistcombobox.setItemText(6, _translate("MainWindow", "Mothers_name", None))
        self.conditionlistcombobox.setItemText(7, _translate("MainWindow", "Sex", None))
        self.conditionlistcombobox.setItemText(8, _translate("MainWindow", "Blood_group", None))
        self.conditionlistcombobox.setItemText(9, _translate("MainWindow", "G_mail", None))
        self.conditionlistcombobox.setItemText(10, _translate("MainWindow", "Mobile", None))
        self.conditionlistcombobox.setItemText(11, _translate("MainWindow", "Address", None))
        self.conditionlistcombobox.setItemText(12, _translate("MainWindow", "Date_of_birth", None))
        self.conditionlistcombobox.setItemText(13, _translate("MainWindow", "Institution", None))
        self.conditionlistcombobox.setItemText(14, _translate("MainWindow", "Units", None))
        self.conditionlistcombobox.setItemText(15, _translate("MainWindow", "Bank_name", None))
        self.conditionlistcombobox.setItemText(16, _translate("MainWindow", "Branch_name", None))
        self.conditionlistcombobox.setItemText(17, _translate("MainWindow", "Account_name", None))
        self.conditionlistcombobox.setItemText(18, _translate("MainWindow", "Account_number", None))
        self.conditionlistcombobox.setItemText(19, _translate("MainWindow", "IFSC_code", None))
        self.insertcondition.setText(_translate("MainWindow", "Insert", None))
        self.clearcondition.setText(_translate("MainWindow", "Clear", None))
        self.querycondition.setText(_translate("MainWindow", "Query", None))
        self.mytab.setTabText(self.mytab.indexOf(self.Query), _translate("MainWindow", "Query", None))
        self.mytab.setTabToolTip(self.mytab.indexOf(self.Query), _translate("MainWindow", "Do YOGA everyday", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Choose your Form</p></body></html>", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "-Select", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cadet details", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Yoga day", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Enrollment Nominal roll", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "Camp Nominal roll", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "Scholarship NR", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "A certe NR for high school JDJW", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "B certe NR SDSW", None))
        self.comboBox.setItemText(8, _translate("MainWindow", "C certe NR SDSW", None))
        self.comboBox.setItemText(9, _translate("MainWindow", "Speciman signature of cadets", None))
        self.comboBox.setItemText(10, _translate("MainWindow", "TADA to cadets camps", None))
        self.comboBox.setItemText(11, _translate("MainWindow", "TADA to cadets for exam", None))
        self.label_3.setText(_translate("MainWindow", "Enter Enrollment numbers", None))
        self.generate_excell_sheetPushButton.setText(_translate("MainWindow", "Generate Excell sheet", None))
        self.open_in_pdfPushButton.setText(_translate("MainWindow", "Open in pdf", None))
        self.mytab.setTabText(self.mytab.indexOf(self.Forms), _translate("MainWindow", "Forms", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

