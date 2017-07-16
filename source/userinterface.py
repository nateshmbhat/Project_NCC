# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Natesh\Documents\GitHub\Project_NCC\User interface\userinterface1.ui'
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
        MainWindow.resize(1100, 893)
        MainWindow.setMinimumSize(QtCore.QSize(844, 716))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("E:/CODES/ncc/.designer/.designer/.designer/.designer/.designer/Documents/CODES/ncc/code/new/Icons/ncc1.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color:rgb(255, 254, 252)"))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setProperty("toolTipDuration", 0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mytab = QtGui.QTabWidget(self.centralwidget)
        self.mytab.setEnabled(True)
        self.mytab.setMinimumSize(QtCore.QSize(826, 678))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mytab.setFont(font)
        self.mytab.setMouseTracking(True)
        self.mytab.setToolTip(_fromUtf8(""))
        self.mytab.setStyleSheet(_fromUtf8(""))
        self.mytab.setTabShape(QtGui.QTabWidget.Rounded)
        self.mytab.setDocumentMode(False)
        self.mytab.setTabsClosable(False)
        self.mytab.setMovable(True)
        self.mytab.setProperty("tabBarAutoHide", False)
        self.mytab.setObjectName(_fromUtf8("mytab"))
        self.Enrol = QtGui.QWidget()
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Enrol.setFont(font)
        self.Enrol.setStyleSheet(_fromUtf8("#Enrol{\n"
"    background-image:url(:/icons/Grungy Blue HD Wallpaper  Theme Bin - Customization HD Wallpapers ....png);\n"
"\n"
"    background-position:center;\n"
"\n"
"}"))
        self.Enrol.setObjectName(_fromUtf8("Enrol"))
        self.gridLayout = QtGui.QGridLayout(self.Enrol)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
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
        self.submitbuttonFrame = QtGui.QFrame(self.Enrol)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitbuttonFrame.sizePolicy().hasHeightForWidth())
        self.submitbuttonFrame.setSizePolicy(sizePolicy)
        self.submitbuttonFrame.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.submitbuttonFrame.setObjectName(_fromUtf8("submitbuttonFrame"))
        self.gridLayout_11 = QtGui.QGridLayout(self.submitbuttonFrame)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.submitPushButton = QtGui.QPushButton(self.submitbuttonFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitPushButton.sizePolicy().hasHeightForWidth())
        self.submitPushButton.setSizePolicy(sizePolicy)
        self.submitPushButton.setMinimumSize(QtCore.QSize(600, 0))
        self.submitPushButton.setMaximumSize(QtCore.QSize(500, 16777215))
        self.submitPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitPushButton.setStyleSheet(_fromUtf8("#submitPushButton{\n"
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
"\n"
"#submitPushButton:pressed\n"
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
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 200), stop:0.166 rgba(255, 255, 0, 200), stop:0.333 rgba(0, 255, 0, 200), stop:0.5 rgba(0, 255, 255, 200), stop:0.666 rgba(0, 0, 255, 200), stop:0.833 rgba(255, 0, 255, 200), stop:1 rgba(255, 0, 0, 200))\n"
"}\n"
""))
        self.submitPushButton.setCheckable(False)
        self.submitPushButton.setDefault(False)
        self.submitPushButton.setFlat(False)
        self.submitPushButton.setObjectName(_fromUtf8("submitPushButton"))
        self.gridLayout_11.addWidget(self.submitPushButton, 2, 0, 1, 1)
        self.updateentryCheckBox = QtGui.QCheckBox(self.submitbuttonFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.updateentryCheckBox.setFont(font)
        self.updateentryCheckBox.setStyleSheet(_fromUtf8("color:white;"))
        self.updateentryCheckBox.setObjectName(_fromUtf8("updateentryCheckBox"))
        self.gridLayout_11.addWidget(self.updateentryCheckBox, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.submitbuttonFrame, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1041, 1899))
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
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 12, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_10.addWidget(self.pushButton)
        self.horizontalLayout_12.addLayout(self.verticalLayout_10)
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
        self.horizontalLayout_12.addWidget(self.ncclogoLabel)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.selectpicturePushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectpicturePushButton.sizePolicy().hasHeightForWidth())
        self.selectpicturePushButton.setSizePolicy(sizePolicy)
        self.selectpicturePushButton.setMinimumSize(QtCore.QSize(160, 0))
        self.selectpicturePushButton.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectpicturePushButton.setFont(font)
        self.selectpicturePushButton.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0.528409, y1:1, x2:0.494, y2:0, stop:0.0227273 rgba(255, 108, 0, 255), stop:0.857955 rgba(255, 70, 219, 255));\n"
"color:white;"))
        self.selectpicturePushButton.setCheckable(False)
        self.selectpicturePushButton.setChecked(False)
        self.selectpicturePushButton.setAutoDefault(False)
        self.selectpicturePushButton.setDefault(False)
        self.selectpicturePushButton.setFlat(False)
        self.selectpicturePushButton.setObjectName(_fromUtf8("selectpicturePushButton"))
        self.gridLayout_8.addWidget(self.selectpicturePushButton, 3, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_8.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setMaximumSize(QtCore.QSize(130, 23))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_8.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.selectpictureLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.selectpictureLabel.setMinimumSize(QtCore.QSize(160, 170))
        self.selectpictureLabel.setMaximumSize(QtCore.QSize(160, 170))
        self.selectpictureLabel.setStyleSheet(_fromUtf8("border:2px groove white;\n"
"background-color:rgba(213, 213, 213,100)"))
        self.selectpictureLabel.setText(_fromUtf8(""))
        self.selectpictureLabel.setScaledContents(True)
        self.selectpictureLabel.setObjectName(_fromUtf8("selectpictureLabel"))
        self.gridLayout_8.addWidget(self.selectpictureLabel, 2, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_8)
        self.horizontalLayout_12.addLayout(self.verticalLayout_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)
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
        self.gridLayout_3.addWidget(self.line, 10, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 7, 0, 1, 1)
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
        self.institutionLabel = QtGui.QLabel(self.instFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.institutionLabel.setFont(font)
        self.institutionLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.institutionLabel.setObjectName(_fromUtf8("institutionLabel"))
        self.gridLayout_4.addWidget(self.institutionLabel, 0, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 1, 1, 1, 1)
        self.unitLineEdit = QtGui.QLineEdit(self.instFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.unitLineEdit.setFont(font)
        self.unitLineEdit.setStyleSheet(_fromUtf8(""))
        self.unitLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.unitLineEdit.setObjectName(_fromUtf8("unitLineEdit"))
        self.gridLayout_4.addWidget(self.unitLineEdit, 1, 4, 1, 1)
        self.label = QtGui.QLabel(self.instFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 1, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 6, 1, 1)
        self.institutionenrollComboBox = QtGui.QComboBox(self.instFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.institutionenrollComboBox.setFont(font)
        self.institutionenrollComboBox.setObjectName(_fromUtf8("institutionenrollComboBox"))
        self.gridLayout_4.addWidget(self.institutionenrollComboBox, 0, 4, 1, 1)
        self.gridLayout_3.addWidget(self.instFrame, 21, 0, 1, 1, QtCore.Qt.AlignHCenter)
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
        self.enrolmentnumLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.enrolmentnumLabel.setObjectName(_fromUtf8("enrolmentnumLabel"))
        self.Enrol_form.setWidget(0, QtGui.QFormLayout.LabelRole, self.enrolmentnumLabel)
        self.enrolmentnumLineEdit = QtGui.QLineEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enrolmentnumLineEdit.setFont(font)
        self.enrolmentnumLineEdit.setStyleSheet(_fromUtf8("#enrolmentnumLineEdit:focus\n"
"{\n"
"border:2px groove chartreuse;\n"
"\n"
"}"))
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
        self.rankLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.rankLabel.setObjectName(_fromUtf8("rankLabel"))
        self.Enrol_form.setWidget(2, QtGui.QFormLayout.LabelRole, self.rankLabel)
        self.rankComboBox = QtGui.QComboBox(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rankComboBox.setFont(font)
        self.rankComboBox.setStyleSheet(_fromUtf8("#rankComboBox:focus\n"
"{\n"
"border:2px groove chartreuse;\n"
"}"))
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
        self.aadhaarLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.aadhaarLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.aadhaarLabel.setTextFormat(QtCore.Qt.AutoText)
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
        self.aadhaarLineEdit.setStyleSheet(_fromUtf8("#aadhaarLineEdit:focus\n"
"{\n"
"border:2px groove chartreuse;\n"
"}"))
        self.aadhaarLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.aadhaarLineEdit.setText(_fromUtf8(""))
        self.aadhaarLineEdit.setMaxLength(12)
        self.aadhaarLineEdit.setFrame(True)
        self.aadhaarLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.aadhaarLineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.aadhaarLineEdit.setObjectName(_fromUtf8("aadhaarLineEdit"))
        self.Enrol_form.setWidget(3, QtGui.QFormLayout.FieldRole, self.aadhaarLineEdit)
        self.fullnameLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fullnameLabel.setFont(font)
        self.fullnameLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.fullnameLabel.setObjectName(_fromUtf8("fullnameLabel"))
        self.Enrol_form.setWidget(5, QtGui.QFormLayout.LabelRole, self.fullnameLabel)
        self.fullnameLineEdit = QtGui.QLineEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fullnameLineEdit.setFont(font)
        self.fullnameLineEdit.setStyleSheet(_fromUtf8("#fullnameLineEdit:focus\n"
"{\n"
"border:2px groove chartreuse;\n"
"}"))
        self.fullnameLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.fullnameLineEdit.setText(_fromUtf8(""))
        self.fullnameLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fullnameLineEdit.setObjectName(_fromUtf8("fullnameLineEdit"))
        self.Enrol_form.setWidget(5, QtGui.QFormLayout.FieldRole, self.fullnameLineEdit)
        self.fathernameLineEdit = QtGui.QLineEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fathernameLineEdit.setFont(font)
        self.fathernameLineEdit.setStyleSheet(_fromUtf8("b"))
        self.fathernameLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fathernameLineEdit.setObjectName(_fromUtf8("fathernameLineEdit"))
        self.Enrol_form.setWidget(6, QtGui.QFormLayout.FieldRole, self.fathernameLineEdit)
        self.mothernameLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mothernameLabel.setFont(font)
        self.mothernameLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
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
        self.mothernameLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mothernameLineEdit.setObjectName(_fromUtf8("mothernameLineEdit"))
        self.Enrol_form.setWidget(7, QtGui.QFormLayout.FieldRole, self.mothernameLineEdit)
        self.sexLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.sexLabel.setFont(font)
        self.sexLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
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
        self.dateofbirthLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
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
        self.addressLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.Enrol_form.setWidget(13, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.emailLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.emailLabel.setFont(font)
        self.emailLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
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
        self.emailLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.emailLineEdit.setObjectName(_fromUtf8("emailLineEdit"))
        self.Enrol_form.setWidget(14, QtGui.QFormLayout.FieldRole, self.emailLineEdit)
        self.mobileLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mobileLabel.setFont(font)
        self.mobileLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
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
        self.mobileLineEdit.setText(_fromUtf8(""))
        self.mobileLineEdit.setMaxLength(10)
        self.mobileLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mobileLineEdit.setObjectName(_fromUtf8("mobileLineEdit"))
        self.Enrol_form.setWidget(15, QtGui.QFormLayout.FieldRole, self.mobileLineEdit)
        self.bloodgroupLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bloodgroupLabel.setFont(font)
        self.bloodgroupLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.bloodgroupLabel.setObjectName(_fromUtf8("bloodgroupLabel"))
        self.Enrol_form.setWidget(16, QtGui.QFormLayout.LabelRole, self.bloodgroupLabel)
        self.bloodgroupComboBox = QtGui.QComboBox(self.enrolformFrame)
        self.bloodgroupComboBox.setMinimumSize(QtCore.QSize(64, 25))
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
        self.certificateLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.certificateLabel.setFont(font)
        self.certificateLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.certificateLabel.setObjectName(_fromUtf8("certificateLabel"))
        self.Enrol_form.setWidget(18, QtGui.QFormLayout.LabelRole, self.certificateLabel)
        self.campsattendedLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.campsattendedLabel.setFont(font)
        self.campsattendedLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.campsattendedLabel.setObjectName(_fromUtf8("campsattendedLabel"))
        self.Enrol_form.setWidget(20, QtGui.QFormLayout.LabelRole, self.campsattendedLabel)
        self.remarksLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.remarksLabel.setFont(font)
        self.remarksLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.remarksLabel.setObjectName(_fromUtf8("remarksLabel"))
        self.Enrol_form.setWidget(24, QtGui.QFormLayout.LabelRole, self.remarksLabel)
        self.specialachievementsLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.specialachievementsLabel.setFont(font)
        self.specialachievementsLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.specialachievementsLabel.setObjectName(_fromUtf8("specialachievementsLabel"))
        self.Enrol_form.setWidget(22, QtGui.QFormLayout.LabelRole, self.specialachievementsLabel)
        self.extracurricularactivitiesLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.extracurricularactivitiesLabel.setFont(font)
        self.extracurricularactivitiesLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.extracurricularactivitiesLabel.setObjectName(_fromUtf8("extracurricularactivitiesLabel"))
        self.Enrol_form.setWidget(21, QtGui.QFormLayout.LabelRole, self.extracurricularactivitiesLabel)
        self.enroldateLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.enroldateLabel.setFont(font)
        self.enroldateLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.enroldateLabel.setObjectName(_fromUtf8("enroldateLabel"))
        self.Enrol_form.setWidget(23, QtGui.QFormLayout.LabelRole, self.enroldateLabel)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.NullcertRadioButton = QtGui.QRadioButton(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NullcertRadioButton.setFont(font)
        self.NullcertRadioButton.setStyleSheet(_fromUtf8("background-color:transparent;color:white;"))
        self.NullcertRadioButton.setChecked(True)
        self.NullcertRadioButton.setAutoExclusive(True)
        self.NullcertRadioButton.setObjectName(_fromUtf8("NullcertRadioButton"))
        self.horizontalLayout_13.addWidget(self.NullcertRadioButton)
        self.AcertRadioButton = QtGui.QRadioButton(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AcertRadioButton.setFont(font)
        self.AcertRadioButton.setStyleSheet(_fromUtf8("background-color:transparent;color:white;"))
        self.AcertRadioButton.setObjectName(_fromUtf8("AcertRadioButton"))
        self.horizontalLayout_13.addWidget(self.AcertRadioButton)
        self.BcertRadioButton = QtGui.QRadioButton(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BcertRadioButton.setFont(font)
        self.BcertRadioButton.setStyleSheet(_fromUtf8("background-color:transparent;color:white;"))
        self.BcertRadioButton.setObjectName(_fromUtf8("BcertRadioButton"))
        self.horizontalLayout_13.addWidget(self.BcertRadioButton)
        self.CcertRadioButton = QtGui.QRadioButton(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CcertRadioButton.setFont(font)
        self.CcertRadioButton.setStyleSheet(_fromUtf8("background-color:transparent;color:white;"))
        self.CcertRadioButton.setObjectName(_fromUtf8("CcertRadioButton"))
        self.horizontalLayout_13.addWidget(self.CcertRadioButton)
        self.Enrol_form.setLayout(18, QtGui.QFormLayout.FieldRole, self.horizontalLayout_13)
        self.remarksTextEdit = QtGui.QTextEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.remarksTextEdit.setFont(font)
        self.remarksTextEdit.setStyleSheet(_fromUtf8("border-radius:5px;"))
        self.remarksTextEdit.setTabChangesFocus(True)
        self.remarksTextEdit.setObjectName(_fromUtf8("remarksTextEdit"))
        self.Enrol_form.setWidget(24, QtGui.QFormLayout.FieldRole, self.remarksTextEdit)
        self.extraactivitiesTextEdit = QtGui.QTextEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.extraactivitiesTextEdit.setFont(font)
        self.extraactivitiesTextEdit.setStyleSheet(_fromUtf8("border-radius:5px;"))
        self.extraactivitiesTextEdit.setTabChangesFocus(True)
        self.extraactivitiesTextEdit.setObjectName(_fromUtf8("extraactivitiesTextEdit"))
        self.Enrol_form.setWidget(21, QtGui.QFormLayout.FieldRole, self.extraactivitiesTextEdit)
        self.specialachievementsTextEdit = QtGui.QTextEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.specialachievementsTextEdit.setFont(font)
        self.specialachievementsTextEdit.setStyleSheet(_fromUtf8("border-radius:5px;"))
        self.specialachievementsTextEdit.setTabChangesFocus(True)
        self.specialachievementsTextEdit.setObjectName(_fromUtf8("specialachievementsTextEdit"))
        self.Enrol_form.setWidget(22, QtGui.QFormLayout.FieldRole, self.specialachievementsTextEdit)
        self.enroldateDateEdit = QtGui.QDateEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.enroldateDateEdit.setFont(font)
        self.enroldateDateEdit.setCalendarPopup(True)
        self.enroldateDateEdit.setObjectName(_fromUtf8("enroldateDateEdit"))
        self.Enrol_form.setWidget(23, QtGui.QFormLayout.FieldRole, self.enroldateDateEdit)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.NULLCampsCheckBox = QtGui.QCheckBox(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NULLCampsCheckBox.setFont(font)
        self.NULLCampsCheckBox.setStyleSheet(_fromUtf8("background-color:transparent;color:white;"))
        self.NULLCampsCheckBox.setChecked(True)
        self.NULLCampsCheckBox.setAutoExclusive(False)
        self.NULLCampsCheckBox.setObjectName(_fromUtf8("NULLCampsCheckBox"))
        self.horizontalLayout_10.addWidget(self.NULLCampsCheckBox)
        self.NICCheckBox = QtGui.QCheckBox(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NICCheckBox.setFont(font)
        self.NICCheckBox.setStyleSheet(_fromUtf8("background-color:transparent;color:white;"))
        self.NICCheckBox.setObjectName(_fromUtf8("NICCheckBox"))
        self.horizontalLayout_10.addWidget(self.NICCheckBox)
        self.CATCCheckBox = QtGui.QCheckBox(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CATCCheckBox.setFont(font)
        self.CATCCheckBox.setStyleSheet(_fromUtf8("background-color:transparent;color:white;"))
        self.CATCCheckBox.setObjectName(_fromUtf8("CATCCheckBox"))
        self.horizontalLayout_10.addWidget(self.CATCCheckBox)
        self.AACCheckBox = QtGui.QCheckBox(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AACCheckBox.setFont(font)
        self.AACCheckBox.setStyleSheet(_fromUtf8("background-color:transparent;color:white;"))
        self.AACCheckBox.setObjectName(_fromUtf8("AACCheckBox"))
        self.horizontalLayout_10.addWidget(self.AACCheckBox)
        self.Enrol_form.setLayout(20, QtGui.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.fathernameLabel = QtGui.QLabel(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fathernameLabel.setFont(font)
        self.fathernameLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.fathernameLabel.setObjectName(_fromUtf8("fathernameLabel"))
        self.Enrol_form.setWidget(6, QtGui.QFormLayout.LabelRole, self.fathernameLabel)
        self.addressTextEdit = QtGui.QTextEdit(self.enrolformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addressTextEdit.setFont(font)
        self.addressTextEdit.setStyleSheet(_fromUtf8("border-radius:5px;"))
        self.addressTextEdit.setTabChangesFocus(True)
        self.addressTextEdit.setObjectName(_fromUtf8("addressTextEdit"))
        self.Enrol_form.setWidget(13, QtGui.QFormLayout.FieldRole, self.addressTextEdit)
        self.gridLayout_3.addWidget(self.enrolformFrame, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
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
        self.ifsccodeLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ifsccodeLineEdit.setFont(font)
        self.ifsccodeLineEdit.setStyleSheet(_fromUtf8("b"))
        self.ifsccodeLineEdit.setMaxLength(11)
        self.ifsccodeLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ifsccodeLineEdit.setObjectName(_fromUtf8("ifsccodeLineEdit"))
        self.gridLayout_2.addWidget(self.ifsccodeLineEdit, 5, 1, 1, 1)
        self.ifsccodeLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ifsccodeLabel.setFont(font)
        self.ifsccodeLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.ifsccodeLabel.setOpenExternalLinks(False)
        self.ifsccodeLabel.setObjectName(_fromUtf8("ifsccodeLabel"))
        self.gridLayout_2.addWidget(self.ifsccodeLabel, 5, 0, 1, 1)
        self.bankbranchLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bankbranchLabel.setFont(font)
        self.bankbranchLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
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
        self.bankbranchLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bankbranchLineEdit.setObjectName(_fromUtf8("bankbranchLineEdit"))
        self.gridLayout_2.addWidget(self.bankbranchLineEdit, 2, 1, 1, 1)
        self.banknameLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.banknameLineEdit.setFont(font)
        self.banknameLineEdit.setStyleSheet(_fromUtf8("b"))
        self.banknameLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.banknameLineEdit.setObjectName(_fromUtf8("banknameLineEdit"))
        self.gridLayout_2.addWidget(self.banknameLineEdit, 0, 1, 1, 1)
        self.accountnameLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.accountnameLineEdit.setFont(font)
        self.accountnameLineEdit.setStyleSheet(_fromUtf8("b"))
        self.accountnameLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.accountnameLineEdit.setObjectName(_fromUtf8("accountnameLineEdit"))
        self.gridLayout_2.addWidget(self.accountnameLineEdit, 3, 1, 1, 1)
        self.micrLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.micrLabel.setFont(font)
        self.micrLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.micrLabel.setObjectName(_fromUtf8("micrLabel"))
        self.gridLayout_2.addWidget(self.micrLabel, 7, 0, 1, 1)
        self.banknameLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.banknameLabel.setFont(font)
        self.banknameLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.banknameLabel.setOpenExternalLinks(False)
        self.banknameLabel.setObjectName(_fromUtf8("banknameLabel"))
        self.gridLayout_2.addWidget(self.banknameLabel, 0, 0, 1, 1)
        self.accountnumLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.accountnumLabel.setFont(font)
        self.accountnumLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.accountnumLabel.setOpenExternalLinks(False)
        self.accountnumLabel.setObjectName(_fromUtf8("accountnumLabel"))
        self.gridLayout_2.addWidget(self.accountnumLabel, 4, 0, 1, 1)
        self.accountnumLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.accountnumLineEdit.setFont(font)
        self.accountnumLineEdit.setStyleSheet(_fromUtf8("b"))
        self.accountnumLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.accountnumLineEdit.setObjectName(_fromUtf8("accountnumLineEdit"))
        self.gridLayout_2.addWidget(self.accountnumLineEdit, 4, 1, 1, 1)
        self.micrLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.micrLineEdit.setFont(font)
        self.micrLineEdit.setMaxLength(9)
        self.micrLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.micrLineEdit.setObjectName(_fromUtf8("micrLineEdit"))
        self.gridLayout_2.addWidget(self.micrLineEdit, 7, 1, 1, 1)
        self.accountnameLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.accountnameLabel.setFont(font)
        self.accountnameLabel.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.accountnameLabel.setOpenExternalLinks(False)
        self.accountnameLabel.setObjectName(_fromUtf8("accountnameLabel"))
        self.gridLayout_2.addWidget(self.accountnameLabel, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_3.addWidget(self.bankformFrame, 15, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.formFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.formFrame.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.formFrame.setObjectName(_fromUtf8("formFrame"))
        self.gridLayout_10 = QtGui.QGridLayout(self.formFrame)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.vegRadioButton = QtGui.QRadioButton(self.formFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vegRadioButton.sizePolicy().hasHeightForWidth())
        self.vegRadioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.vegRadioButton.setFont(font)
        self.vegRadioButton.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;\n"
"margin-right:300px;"))
        self.vegRadioButton.setChecked(True)
        self.vegRadioButton.setAutoExclusive(True)
        self.vegRadioButton.setObjectName(_fromUtf8("vegRadioButton"))
        self.gridLayout_10.addWidget(self.vegRadioButton, 0, 0, 1, 1)
        self.nonvegRadioButton = QtGui.QRadioButton(self.formFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nonvegRadioButton.sizePolicy().hasHeightForWidth())
        self.nonvegRadioButton.setSizePolicy(sizePolicy)
        self.nonvegRadioButton.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nonvegRadioButton.setFont(font)
        self.nonvegRadioButton.setStyleSheet(_fromUtf8("background-color:transparent;margin:3px;\n"
"color:white;"))
        self.nonvegRadioButton.setObjectName(_fromUtf8("nonvegRadioButton"))
        self.gridLayout_10.addWidget(self.nonvegRadioButton, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.formFrame, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 22, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 13, 0, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 17, 0, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 16, 0, 1, 1)
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
        self.gridLayout_3.addWidget(self.bankdetailsLabel, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
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
        self.gridLayout_3.addWidget(self.line_2, 20, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 1)
        self.searchFrame = QtGui.QFrame(self.Enrol)
        self.searchFrame.setMinimumSize(QtCore.QSize(0, 45))
        self.searchFrame.setStyleSheet(_fromUtf8("#searchFrame{\n"
"background-color:transparent;\n"
"}"))
        self.searchFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.searchFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.searchFrame.setObjectName(_fromUtf8("searchFrame"))
        self.gridLayout_13 = QtGui.QGridLayout(self.searchFrame)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.enrolPushButton = QtGui.QPushButton(self.searchFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enrolPushButton.sizePolicy().hasHeightForWidth())
        self.enrolPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.enrolPushButton.setFont(font)
        self.enrolPushButton.setStyleSheet(_fromUtf8("background-color:rgba(170, 0, 255,200);\n"
"color:yellow;"))
        self.enrolPushButton.setCheckable(True)
        self.enrolPushButton.setChecked(True)
        self.enrolPushButton.setFlat(False)
        self.enrolPushButton.setObjectName(_fromUtf8("enrolPushButton"))
        self.gridLayout_13.addWidget(self.enrolPushButton, 0, 1, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.enrolmentnumRadioButton = QtGui.QRadioButton(self.searchFrame)
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
        self.horizontalLayout_9.addWidget(self.enrolmentnumRadioButton, QtCore.Qt.AlignLeft)
        self.aadhaarnumRadioButton = QtGui.QRadioButton(self.searchFrame)
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
        self.horizontalLayout_9.addWidget(self.aadhaarnumRadioButton, QtCore.Qt.AlignLeft)
        spacerItem11 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.gridLayout_13.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.searchbyfieldLineEdit = QtGui.QLineEdit(self.searchFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchbyfieldLineEdit.sizePolicy().hasHeightForWidth())
        self.searchbyfieldLineEdit.setSizePolicy(sizePolicy)
        self.searchbyfieldLineEdit.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.searchbyfieldLineEdit.setFont(font)
        self.searchbyfieldLineEdit.setStyleSheet(_fromUtf8("border-radius:2px;\n"
"font-size:20px;\n"
""))
        self.searchbyfieldLineEdit.setText(_fromUtf8(""))
        self.searchbyfieldLineEdit.setObjectName(_fromUtf8("searchbyfieldLineEdit"))
        self.horizontalLayout_6.addWidget(self.searchbyfieldLineEdit)
        self.searchPushButton = QtGui.QPushButton(self.searchFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchPushButton.sizePolicy().hasHeightForWidth())
        self.searchPushButton.setSizePolicy(sizePolicy)
        self.searchPushButton.setMinimumSize(QtCore.QSize(100, 8))
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
"\n"
"\n"
"#searchPushButton:pressed\n"
"{\n"
"    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #0061a7), color-stop(1, #007dc1));\n"
"    background:-moz-linear-gradient(top, #0061a7 5%, #007dc1 100%);\n"
"    background:-webkit-linear-gradient(top, #0061a7 5%, #007dc1 100%);\n"
"    background:-o-linear-gradient(top, #0061a7 5%, #007dc1 100%);\n"
"    background:-ms-linear-gradient(top, #0061a7 5%, #007dc1 100%);\n"
"    background:linear-gradient(to bottom, #0061a7 5%, #007dc1 100%);\n"
"    background-color:rgba(3, 50, 120,150);\n"
"}\n"
""))
        self.searchPushButton.setCheckable(False)
        self.searchPushButton.setAutoDefault(False)
        self.searchPushButton.setDefault(False)
        self.searchPushButton.setObjectName(_fromUtf8("searchPushButton"))
        self.horizontalLayout_6.addWidget(self.searchPushButton, QtCore.Qt.AlignLeft)
        spacerItem12 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.gridLayout_13.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem13, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.searchFrame, 1, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("E:/CODES/ncc/.designer/.designer/.designer/.designer/.designer/Documents/CODES/ncc/Pictures/Screenshots/Screenshot (113).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.checkboxFrame.setMinimumSize(QtCore.QSize(0, 100))
        self.checkboxFrame.setSizeIncrement(QtCore.QSize(0, 4))
        self.checkboxFrame.setStyleSheet(_fromUtf8("font-size:100%;"))
        self.checkboxFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.checkboxFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.checkboxFrame.setObjectName(_fromUtf8("checkboxFrame"))
        self.gridLayout_7 = QtGui.QGridLayout(self.checkboxFrame)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.remarksCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        self.remarksCheckBox.setStyleSheet(_fromUtf8("#remarksCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#remarksCheckBox:hover\n"
"{\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
""))
        self.remarksCheckBox.setObjectName(_fromUtf8("remarksCheckBox"))
        self.gridLayout_7.addWidget(self.remarksCheckBox, 3, 1, 1, 1)
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
        self.gridLayout_7.addWidget(self.banknameCheckBox, 1, 3, 1, 1)
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
        self.gridLayout_7.addWidget(self.accountnumCheckBox, 1, 6, 1, 1)
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
        self.gridLayout_7.addWidget(self.addressCheckBox, 1, 2, 1, 1)
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
        self.gridLayout_7.addWidget(self.bankbranchCheckBox, 1, 4, 1, 1)
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
        self.gridLayout_7.addWidget(self.emailCheckBox, 1, 0, 1, 1)
        self.micrCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        self.micrCheckBox.setStyleSheet(_fromUtf8("#micrCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#micrCheckBox:hover\n"
"{\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
""))
        self.micrCheckBox.setObjectName(_fromUtf8("micrCheckBox"))
        self.gridLayout_7.addWidget(self.micrCheckBox, 3, 0, 1, 1)
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
        self.gridLayout_7.addWidget(self.accountnameCheckBox, 1, 5, 1, 1)
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
        self.gridLayout_7.addWidget(self.sfnameCheckBox, 0, 2, 1, 1)
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
        self.gridLayout_7.addWidget(self.mfnameCheckBox, 0, 4, 1, 1)
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
        self.gridLayout_7.addWidget(self.bloodgroupCheckBox, 0, 5, 1, 1)
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
        self.gridLayout_7.addWidget(self.ffnameCheckBox, 0, 6, 1, 1)
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
        self.gridLayout_7.addWidget(self.sexCheckBox, 0, 3, 1, 1)
        self.vegitarianCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        self.vegitarianCheckBox.setStyleSheet(_fromUtf8("#vegitarianCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#vegitarianCheckBox:hover\n"
"{\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
""))
        self.vegitarianCheckBox.setObjectName(_fromUtf8("vegitarianCheckBox"))
        self.gridLayout_7.addWidget(self.vegitarianCheckBox, 3, 2, 1, 1)
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
        self.gridLayout_7.addWidget(self.ifsccodeCheckBox, 3, 3, 1, 1)
        self.enrollDateCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        self.enrollDateCheckBox.setStyleSheet(_fromUtf8("#enrollDateCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#enrollDateCheckBox:hover\n"
"{\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
""))
        self.enrollDateCheckBox.setObjectName(_fromUtf8("enrollDateCheckBox"))
        self.gridLayout_7.addWidget(self.enrollDateCheckBox, 3, 4, 1, 1)
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
        self.gridLayout_7.addWidget(self.unitCheckBox, 3, 5, 1, 1)
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
        self.gridLayout_7.addWidget(self.institutionCheckBox, 3, 6, 1, 1)
        self.extraCurricularActivitiesCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        self.extraCurricularActivitiesCheckBox.setStyleSheet(_fromUtf8("#extraCurricularActivitiesCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#extraCurricularActivitiesCheckBox:hover\n"
"{\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
""))
        self.extraCurricularActivitiesCheckBox.setObjectName(_fromUtf8("extraCurricularActivitiesCheckBox"))
        self.gridLayout_7.addWidget(self.extraCurricularActivitiesCheckBox, 4, 0, 1, 2)
        self.campsAttendedCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        self.campsAttendedCheckBox.setStyleSheet(_fromUtf8("#campsAttendedCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#campsAttendedCheckBox:hover\n"
"{\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
""))
        self.campsAttendedCheckBox.setObjectName(_fromUtf8("campsAttendedCheckBox"))
        self.gridLayout_7.addWidget(self.campsAttendedCheckBox, 4, 2, 1, 1)
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
        self.gridLayout_7.addWidget(self.rankCheckBox, 4, 3, 1, 1)
        self.specialAchievementsCheckBox = QtGui.QCheckBox(self.checkboxFrame)
        self.specialAchievementsCheckBox.setStyleSheet(_fromUtf8("#specialAchievementsCheckBox{\n"
"color:white;\n"
"font:13pt cambria ;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#specialAchievementsCheckBox:hover\n"
"{\n"
"    font:15pt cambria;\n"
"    color:yellow;\n"
"}\n"
""))
        self.specialAchievementsCheckBox.setObjectName(_fromUtf8("specialAchievementsCheckBox"))
        self.gridLayout_7.addWidget(self.specialAchievementsCheckBox, 4, 6, 1, 1)
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
        self.gridLayout_7.addWidget(self.dateofbirthCheckBox, 4, 5, 1, 1)
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
        self.gridLayout_7.addWidget(self.mobileCheckBox, 4, 4, 1, 1)
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
"border-width:2px;\n"
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
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0.602, y1:0.392364, x2:0, y2:1, stop:0 rgba(254, 77, 0, 255), stop:1 rgba(122, 255, 73, 255));\n"
"border-width:2px;\n"
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
"border-width:2px;\n"
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
"border-radius:15px;\n"
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
"border-width:2px;\n"
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
"border-width:2px;\n"
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
"border-width:2px;\n"
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
"border-width:2px;\n"
"height:25px;\n"
"}"))
        self.closebracecondition.setObjectName(_fromUtf8("closebracecondition"))
        self.horizontalLayout_5.addWidget(self.closebracecondition)
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
"border-width:2px;\n"
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
"border-width:2px;\n"
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
"border-width:2px;\n"
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
"border-width:2px;\n"
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
"border-width:2px;\n"
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
"border-radius:15px;\n"
"background-color:qlineargradient(spread:pad, x1:0.012, y1:0.755818, x2:0.641818, y2:0.392, stop:0 rgba(230, 255, 0, 255), stop:1 rgba(85, 104, 255, 255));\n"
"border-width:2px;\n"
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
"width:130%;\n"
"height:30px;\n"
"}\n"
"#conditionlistcombobox:hover{\n"
"    border:1px solid chartreuse;\n"
"    font: 14pt \"georgia\";\n"
"width:130%;\n"
"}"))
        self.conditionlistcombobox.setMaxVisibleItems(25)
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
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.conditionlistcombobox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.conditionlistcombobox)
        self.campsattendedqueryComboBox = QtGui.QComboBox(self.frame)
        self.campsattendedqueryComboBox.setStyleSheet(_fromUtf8("#campsattendedqueryComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 12pt \"georgia\";\n"
"width:130%;\n"
"height:30px;\n"
"}\n"
"#campsattendedqueryComboBox:hover{\n"
"    border:1px solid chartreuse;\n"
"    font: 14pt \"georgia\";\n"
"width:130%;\n"
"}"))
        self.campsattendedqueryComboBox.setObjectName(_fromUtf8("campsattendedqueryComboBox"))
        self.campsattendedqueryComboBox.addItem(_fromUtf8(""))
        self.campsattendedqueryComboBox.addItem(_fromUtf8(""))
        self.campsattendedqueryComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.campsattendedqueryComboBox)
        self.vegitarianqueryComboBox = QtGui.QComboBox(self.frame)
        self.vegitarianqueryComboBox.setStyleSheet(_fromUtf8("#vegitarianqueryComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 12pt \"georgia\";\n"
"width:130%;\n"
"height:30px;\n"
"}\n"
"#vegitarianqueryComboBox:hover{\n"
"    border:1px solid chartreuse;\n"
"    font: 14pt \"georgia\";\n"
"width:130%;\n"
"}"))
        self.vegitarianqueryComboBox.setObjectName(_fromUtf8("vegitarianqueryComboBox"))
        self.vegitarianqueryComboBox.addItem(_fromUtf8(""))
        self.vegitarianqueryComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.vegitarianqueryComboBox)
        self.bloodgroupqueryComboBox = QtGui.QComboBox(self.frame)
        self.bloodgroupqueryComboBox.setStyleSheet(_fromUtf8("#bloodgroupqueryComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 12pt \"georgia\";\n"
"width:130%;\n"
"height:30px;\n"
"}\n"
"#bloodgroupqueryComboBox:hover{\n"
"    border:1px solid chartreuse;\n"
"    font: 14pt \"georgia\";\n"
"width:130%;\n"
"}"))
        self.bloodgroupqueryComboBox.setObjectName(_fromUtf8("bloodgroupqueryComboBox"))
        self.bloodgroupqueryComboBox.addItem(_fromUtf8(""))
        self.bloodgroupqueryComboBox.addItem(_fromUtf8(""))
        self.bloodgroupqueryComboBox.addItem(_fromUtf8(""))
        self.bloodgroupqueryComboBox.addItem(_fromUtf8(""))
        self.bloodgroupqueryComboBox.addItem(_fromUtf8(""))
        self.bloodgroupqueryComboBox.addItem(_fromUtf8(""))
        self.bloodgroupqueryComboBox.addItem(_fromUtf8(""))
        self.bloodgroupqueryComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.bloodgroupqueryComboBox)
        self.certificatequeryComboBox = QtGui.QComboBox(self.frame)
        self.certificatequeryComboBox.setStyleSheet(_fromUtf8("#certificatequeryComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 12pt \"georgia\";\n"
"width:130%;\n"
"height:30px;\n"
"}\n"
"#certificatequeryComboBox:hover{\n"
"    border:1px solid chartreuse;\n"
"    font: 14pt \"georgia\";\n"
"width:130%;\n"
"}"))
        self.certificatequeryComboBox.setObjectName(_fromUtf8("certificatequeryComboBox"))
        self.certificatequeryComboBox.addItem(_fromUtf8(""))
        self.certificatequeryComboBox.addItem(_fromUtf8(""))
        self.certificatequeryComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.certificatequeryComboBox)
        self.institutionqueryComboBox = QtGui.QComboBox(self.frame)
        self.institutionqueryComboBox.setStyleSheet(_fromUtf8("#institutionqueryComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 12pt \"georgia\";\n"
"width:130%;\n"
"height:30px;\n"
"}\n"
"#institutionqueryComboBox:hover{\n"
"        border:1px solid chartreuse;\n"
"    font: 14pt \"georgia\";\n"
"width:130%;\n"
"}"))
        self.institutionqueryComboBox.setObjectName(_fromUtf8("institutionqueryComboBox"))
        self.horizontalLayout_3.addWidget(self.institutionqueryComboBox)
        self.rankqueryComboBox = QtGui.QComboBox(self.frame)
        self.rankqueryComboBox.setStyleSheet(_fromUtf8("#rankqueryComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 12pt \"georgia\";\n"
"width:130%;\n"
"height:30px;\n"
"}\n"
"#rankqueryComboBox:hover{\n"
"    border:1px solid chartreuse;\n"
"    font: 14pt \"georgia\";\n"
"width:130%;\n"
"}"))
        self.rankqueryComboBox.setObjectName(_fromUtf8("rankqueryComboBox"))
        self.rankqueryComboBox.addItem(_fromUtf8(""))
        self.rankqueryComboBox.addItem(_fromUtf8(""))
        self.rankqueryComboBox.addItem(_fromUtf8(""))
        self.rankqueryComboBox.addItem(_fromUtf8(""))
        self.rankqueryComboBox.addItem(_fromUtf8(""))
        self.rankqueryComboBox.addItem(_fromUtf8(""))
        self.rankqueryComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.rankqueryComboBox)
        self.sexqueryComboBox = QtGui.QComboBox(self.frame)
        self.sexqueryComboBox.setStyleSheet(_fromUtf8("#sexqueryComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 12pt \"georgia\";\n"
"width:130%;\n"
"height:30px;\n"
"}\n"
"#sexqueryComboBox:hover{\n"
"    border:1px solid chartreuse;\n"
"    font: 14pt \"georgia\";\n"
"width:130%;\n"
"}"))
        self.sexqueryComboBox.setObjectName(_fromUtf8("sexqueryComboBox"))
        self.sexqueryComboBox.addItem(_fromUtf8(""))
        self.sexqueryComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.sexqueryComboBox)
        self.datequeryDateEdit = QtGui.QDateEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.datequeryDateEdit.setFont(font)
        self.datequeryDateEdit.setStyleSheet(_fromUtf8("#datequeryDateEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 14pt \"georgia\";\n"
"width:130%;\n"
"height:30px;\n"
"}\n"
"#datequeryDateEdit:hover{\n"
"    border:1px solid chartreuse;\n"
"    font: 16pt \"georgia\";\n"
"width:130%;\n"
"}"))
        self.datequeryDateEdit.setObjectName(_fromUtf8("datequeryDateEdit"))
        self.horizontalLayout_3.addWidget(self.datequeryDateEdit)
        self.valuelineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.valuelineEdit.setFont(font)
        self.valuelineEdit.setStyleSheet(_fromUtf8("#valuelineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(85, 0, 0);\n"
"    font: 12pt \"georgia\";\n"
"    font-weight:bold;\n"
"    width:130%;\n"
"height:30px;\n"
"}\n"
"#valuelineEdit:hover{\n"
"    font: 14pt \"georgia\";\n"
"    width:130%;\n"
"}\n"
"\n"
"#valuelineEdit:focus\n"
"{\n"
"    border:1px solid chartreuse;\n"
"\n"
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
"border-width:2px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:130%;\n"
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
"border-radius:15px;\n"
"background-color:qlineargradient(spread:reflect, x1:0.284, y1:0, x2:0.675, y2:0, stop:0 rgba(71, 68, 230, 255), stop:1 rgba(78, 212, 223, 255));\n"
"width:130%;\n"
"}\n"
"\n"
"#insertcondition:pressed\n"
"{\n"
"color:white;\n"
"padding-left:18px;\n"
"padding-right:22px;\n"
"font: 75 14pt \"georgia\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"background-color:qlineargradient(spread:reflect, x1:0.284, y1:0, x2:0.675, y2:0, stop:0 rgba(71, 68, 230, 200), stop:1 rgba(78, 212, 223, 200));\n"
"width:130%;\n"
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
"border-width:2px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:130%;\n"
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
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 234), stop:0.05 rgba(14, 8, 73, 255), stop:0.119318 rgba(28, 17, 145, 254), stop:0.477273 rgba(126, 14, 81, 237), stop:0.744318 rgba(234, 11, 11, 246), stop:0.79 rgba(244, 70, 5, 245), stop:0.86 rgba(255, 136, 0, 248), stop:0.935 rgba(239, 236, 55, 250));\n"
"width:130%;\n"
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
"border-width:2px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:130%;\n"
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
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 24, 200), stop:0.085 rgba(2, 79, 0, 200), stop:0.221591 rgba(50, 147, 22, 200), stop:0.275 rgba(165, 142, 70, 200), stop:0.431818 rgba(243, 100, 79, 200), stop:0.573864 rgba(135, 95, 80, 200), stop:0.667 rgba(137, 97, 255, 200), stop:0.818182 rgba(160, 255, 244, 200), stop:0.885 rgba(193, 222, 185, 200), stop:1 rgba(93, 128, 0, 200));\n"
"width:130%;\n"
"}\n"
"\n"
"#querycondition:pressed\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:18px;\n"
"padding-right:22px;\n"
"font: 75 15pt \"georgia\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 24, 200), stop:0.085 rgba(2, 79, 0, 150), stop:0.221591 rgba(50, 147, 22, 150), stop:0.275 rgba(165, 142, 70, 150), stop:0.431818 rgba(243, 100, 79, 150), stop:0.573864 rgba(135, 95, 80, 150), stop:0.667 rgba(137, 97, 255, 150), stop:0.818182 rgba(160, 255, 244, 150), stop:0.885 rgba(193, 222, 185, 150), stop:1 rgba(93, 128, 0, 150));\n"
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
        self.generateexcelqueryPushButton = QtGui.QPushButton(self.Query)
        self.generateexcelqueryPushButton.setStyleSheet(_fromUtf8("#generateexcelqueryPushButton{\n"
"background-color: rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"font: 75 14pt \"georgia\";\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"border-style:solid;\n"
"border-color: rgb(255, 170, 0);\n"
"border-width:2px;\n"
"height:30px;\n"
"border-radius:15px;\n"
"width:130%;\n"
"}\n"
"\n"
"#generateexcelqueryPushButton:hover\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:18px;\n"
"padding-right:22px;\n"
"font: 75 16pt \"georgia\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 24, 200), stop:0.085 rgba(2, 79, 0, 200), stop:0.221591 rgba(50, 147, 22, 200), stop:0.275 rgba(165, 142, 70, 200), stop:0.431818 rgba(243, 100, 79, 200), stop:0.573864 rgba(135, 95, 80, 200), stop:0.667 rgba(137, 97, 255, 200), stop:0.818182 rgba(160, 255, 244, 200), stop:0.885 rgba(193, 222, 185, 200), stop:1 rgba(93, 128, 0, 200));\n"
"width:130%;\n"
"}\n"
"\n"
"#generateexcelqueryPushButton:pressed\n"
"{\n"
"color:rgb(255,255,255);\n"
"padding-left:18px;\n"
"padding-right:22px;\n"
"font: 75 12pt \"georgia\";\n"
"border-style:solid;\n"
"border-color:rgb(255,255,255);\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 41, 24, 200), stop:0.085 rgba(2, 79, 0, 150), stop:0.221591 rgba(50, 147, 22, 150), stop:0.275 rgba(165, 142, 70, 150), stop:0.431818 rgba(243, 100, 79, 150), stop:0.573864 rgba(135, 95, 80, 150), stop:0.667 rgba(137, 97, 255, 150), stop:0.818182 rgba(160, 255, 244, 150), stop:0.885 rgba(193, 222, 185, 150), stop:1 rgba(93, 128, 0, 150));\n"
"width:130%;\n"
"}"))
        self.generateexcelqueryPushButton.setObjectName(_fromUtf8("generateexcelqueryPushButton"))
        self.gridLayout_5.addWidget(self.generateexcelqueryPushButton, 1, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("E:/CODES/ncc/.designer/.designer/.designer/.designer/.designer/Documents/CODES/ncc/Pictures/Screenshots/Screenshot (107).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mytab.addTab(self.Query, icon2, _fromUtf8(""))
        self.Forms = QtGui.QWidget()
        self.Forms.setStyleSheet(_fromUtf8("#Forms{\n"
"    background-image: url(:/icons/green_grad.png);\n"
"background-position:centre;\n"
"\n"
"}"))
        self.Forms.setObjectName(_fromUtf8("Forms"))
        self.gridLayout_15 = QtGui.QGridLayout(self.Forms)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.formsframe = QtGui.QFrame(self.Forms)
        self.formsframe.setStyleSheet(_fromUtf8("#formsframe{\n"
"background-color:transparent;\n"
"}"))
        self.formsframe.setObjectName(_fromUtf8("formsframe"))
        self.gridLayout_17 = QtGui.QGridLayout(self.formsframe)
        self.gridLayout_17.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.saveExelPushButton = QtGui.QPushButton(self.formsframe)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.saveExelPushButton.setFont(font)
        self.saveExelPushButton.setStyleSheet(_fromUtf8("#saveExelPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"    border-color: rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"height:30px;\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"padding-left:8px;\n"
"padding-right:8px;\n"
"color:rgb(85, 170, 255);\n"
"color:black;\n"
"width:400%;\n"
"}\n"
"#saveExelPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"font-weight:bold;\n"
"border-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"\n"
"padding-left:8px;\n"
"padding-right:8px;\n"
"height:30px;\n"
"color:rgb(255, 255, 255);\n"
"font-size:20px;\n"
"padding-top:-10px;\n"
"width:400%;\n"
"}\n"
""))
        self.saveExelPushButton.setObjectName(_fromUtf8("saveExelPushButton"))
        self.horizontalLayout_14.addWidget(self.saveExelPushButton, QtCore.Qt.AlignHCenter)
        self.updateExelPushButton = QtGui.QPushButton(self.formsframe)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.updateExelPushButton.setFont(font)
        self.updateExelPushButton.setStyleSheet(_fromUtf8("\n"
"#updateExelPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"    border-color: rgb(0, 0, 127);\n"
"border-radius:10px;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"height:30px;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"width:175%;\n"
"color:rgb(85, 170, 255);\n"
"color:black;\n"
"width:400%;\n"
"}\n"
"#updateExelPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"border-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border-width:2px;\n"
"border-style:solid;\n"
"height:30px;\n"
"font-weight:bold;\n"
"color:rgb(255, 255, 255);\n"
"font-size:20px;\n"
"padding-top:-10px;\n"
"width:175%;\n"
"width:400%;\n"
"}\n"
""))
        self.updateExelPushButton.setObjectName(_fromUtf8("updateExelPushButton"))
        self.horizontalLayout_14.addWidget(self.updateExelPushButton, QtCore.Qt.AlignHCenter)
        self.gridLayout_9.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_9, 9, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.formsframe)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("font-size:25px;\n"
"background-color:transparent;\n"
"color:black;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_17.addWidget(self.label_3, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.formsComboBox = QtGui.QComboBox(self.formsframe)
        self.formsComboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.formsComboBox.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Caladea"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.formsComboBox.setFont(font)
        self.formsComboBox.setStyleSheet(_fromUtf8("#formsComboBox{\n"
"border-radius:2px;\n"
"}"))
        self.formsComboBox.setMaxVisibleItems(20)
        self.formsComboBox.setObjectName(_fromUtf8("formsComboBox"))
        self.formsComboBox.addItem(_fromUtf8(""))
        self.formsComboBox.addItem(_fromUtf8(""))
        self.formsComboBox.addItem(_fromUtf8(""))
        self.formsComboBox.addItem(_fromUtf8(""))
        self.formsComboBox.addItem(_fromUtf8(""))
        self.gridLayout_17.addWidget(self.formsComboBox, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.webView_2 = QtWebKit.QWebView(self.formsframe)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Colonna MT"))
        self.webView_2.setFont(font)
        self.webView_2.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.webView_2.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView_2.setObjectName(_fromUtf8("webView_2"))
        self.gridLayout_17.addWidget(self.webView_2, 7, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.formsframe)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Colonna MT"))
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8("background-color:transparent;\n"
"color:blue;"))
        self.label_12.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_17.addWidget(self.label_12, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem14, 4, 0, 1, 1)
        self.entryBox = QtGui.QTextEdit(self.formsframe)
        self.entryBox.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Caladea"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.entryBox.setFont(font)
        self.entryBox.setStyleSheet(_fromUtf8("background-color: rgb(210, 255, 249);\n"
"border-radius:10px;\n"
"border-width:2px;\n"
"border-style:groove;\n"
"color:black;"))
        self.entryBox.setObjectName(_fromUtf8("entryBox"))
        self.gridLayout_17.addWidget(self.entryBox, 5, 0, 1, 2, QtCore.Qt.AlignHCenter)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem15, 8, 0, 1, 1)
        self.gridLayout_15.addWidget(self.formsframe, 0, 0, 1, 1)
        self.mytab.addTab(self.Forms, _fromUtf8(""))
        self.DataEntry = QtGui.QWidget()
        self.DataEntry.setStyleSheet(_fromUtf8("#DataEntry{\n"
"    background-image: url(:/icons/PF2cI1N.png);\n"
"background-position:center;\n"
"background-repeat:none;\n"
"\n"
"}"))
        self.DataEntry.setObjectName(_fromUtf8("DataEntry"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.DataEntry)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.institutionuploaddatacomboBox = QtGui.QComboBox(self.DataEntry)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Caladea"))
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.institutionuploaddatacomboBox.setFont(font)
        self.institutionuploaddatacomboBox.setStyleSheet(_fromUtf8("font-size:20px;\n"
"border-radius:5px;\n"
"padding-left:5px;\n"
"background-image: url(:/icons/close line.png);\n"
"color: rgb(0, 0, 127);"))
        self.institutionuploaddatacomboBox.setMaxVisibleItems(25)
        self.institutionuploaddatacomboBox.setObjectName(_fromUtf8("institutionuploaddatacomboBox"))
        self.institutionuploaddatacomboBox.addItem(_fromUtf8(""))
        self.institutionuploaddatacomboBox.addItem(_fromUtf8(""))
        self.institutionuploaddatacomboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.institutionuploaddatacomboBox)
        self.typecomboBox = QtGui.QComboBox(self.DataEntry)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Caladea"))
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.typecomboBox.setFont(font)
        self.typecomboBox.setStyleSheet(_fromUtf8("font-size:20px;\n"
"border-radius:5px;\n"
"padding-left:5px;\n"
"background-image: url(:/icons/close line.png);\n"
"color: rgb(0, 0, 127);"))
        self.typecomboBox.setMaxVisibleItems(25)
        self.typecomboBox.setObjectName(_fromUtf8("typecomboBox"))
        self.typecomboBox.addItem(_fromUtf8(""))
        self.typecomboBox.addItem(_fromUtf8(""))
        self.typecomboBox.addItem(_fromUtf8(""))
        self.typecomboBox.addItem(_fromUtf8(""))
        self.typecomboBox.addItem(_fromUtf8(""))
        self.typecomboBox.addItem(_fromUtf8(""))
        self.typecomboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.typecomboBox)
        self.openPushButton = QtGui.QPushButton(self.DataEntry)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Caladea"))
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.openPushButton.setFont(font)
        self.openPushButton.setStyleSheet(_fromUtf8("#openPushButton{\n"
"font-size:20px;\n"
"    color: rgb(94, 0, 141);\n"
"color:black;\n"
"    background-color:white;\n"
"border-style:solid;\n"
"    border-color: rgb(104, 0, 156);\n"
"border-width:2px;\n"
"height:24px;\n"
"border-radius:10px;\n"
"}\n"
"#openPushButton:hover{\n"
"font-size:25px;\n"
"    background-color:rgba(94, 0, 141,100);\n"
"border-radius:10px;\n"
"color:white;\n"
"border-style:solid;\n"
"border-color:white;\n"
"border-width:2px;\n"
"height:30px;\n"
"padding-top:-5px;\n"
"}"))
        self.openPushButton.setObjectName(_fromUtf8("openPushButton"))
        self.horizontalLayout_7.addWidget(self.openPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tableWidget = QtGui.QTableWidget(self.DataEntry)
        self.tableWidget.setStyleSheet(_fromUtf8("background-color:rgba(170, 255, 255 , 10)"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.savedataPushButton = QtGui.QPushButton(self.DataEntry)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.savedataPushButton.setFont(font)
        self.savedataPushButton.setStyleSheet(_fromUtf8("#savedataPushButton{\n"
"font-size:20px;\n"
"    color: rgb(94, 0, 141);\n"
"color:black;\n"
"    background-color:white;\n"
"border-style:solid;\n"
"    border-color: rgb(104, 0, 156);\n"
"border-width:2px;\n"
"height:30px;\n"
"border-radius:10px;\n"
"}\n"
"#savedataPushButton:hover{\n"
"font-size:25px;\n"
"    background-color:rgba(94, 0, 141,100);\n"
"border-radius:10px;\n"
"color:white;\n"
"border-style:solid;\n"
"border-color:white;\n"
"border-width:2px;\n"
"height:30px;\n"
"padding-top:-5px;\n"
"}\n"
""))
        self.savedataPushButton.setObjectName(_fromUtf8("savedataPushButton"))
        self.horizontalLayout_8.addWidget(self.savedataPushButton)
        self.save_data_excelPushButton = QtGui.QPushButton(self.DataEntry)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.save_data_excelPushButton.setFont(font)
        self.save_data_excelPushButton.setStyleSheet(_fromUtf8("#save_data_excelPushButton{\n"
"font-size:20px;\n"
"    color: rgb(94, 0, 141);\n"
"color:black;\n"
"    background-color:white;\n"
"border-style:solid;\n"
"    border-color: rgb(104, 0, 156);\n"
"border-width:2px;\n"
"height:30px;\n"
"border-radius:10px;\n"
"}\n"
"#save_data_excelPushButton:hover{\n"
"font-size:25px;\n"
"    background-color:rgba(94, 0, 141,100);\n"
"border-radius:10px;\n"
"color:white;\n"
"border-style:solid;\n"
"border-color:white;\n"
"border-width:2px;\n"
"height:30px;\n"
"padding-top:-5px;\n"
"}\n"
""))
        self.save_data_excelPushButton.setObjectName(_fromUtf8("save_data_excelPushButton"))
        self.horizontalLayout_8.addWidget(self.save_data_excelPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.mytab.addTab(self.DataEntry, _fromUtf8(""))
        self.Settings = QtGui.QWidget()
        self.Settings.setStyleSheet(_fromUtf8("#Settings{\n"
"background-image:url(:/icons/Gradient Wallpaper HD 17 Color hd background hd screensavers hd ....png);\n"
"    selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"background-position:center;\n"
"}"))
        self.Settings.setObjectName(_fromUtf8("Settings"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.Settings)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.SettingsScrollArea = QtGui.QScrollArea(self.Settings)
        self.SettingsScrollArea.setStyleSheet(_fromUtf8("#SettingsScrollArea\n"
"{\n"
"    background-color:transparent;\n"
"}"))
        self.SettingsScrollArea.setWidgetResizable(True)
        self.SettingsScrollArea.setObjectName(_fromUtf8("SettingsScrollArea"))
        self.settingsscrollAreaWidgetContents = QtGui.QWidget()
        self.settingsscrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1039, 1198))
        self.settingsscrollAreaWidgetContents.setStyleSheet(_fromUtf8("#settingsscrollAreaWidgetContents\n"
"{\n"
"    background-color:transparent;\n"
"}"))
        self.settingsscrollAreaWidgetContents.setObjectName(_fromUtf8("settingsscrollAreaWidgetContents"))
        self.gridLayout_14 = QtGui.QGridLayout(self.settingsscrollAreaWidgetContents)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.settingsmainframewidget = QtGui.QWidget(self.settingsscrollAreaWidgetContents)
        self.settingsmainframewidget.setMinimumSize(QtCore.QSize(514, 0))
        self.settingsmainframewidget.setStyleSheet(_fromUtf8("#settingsmainframewidget{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}"))
        self.settingsmainframewidget.setObjectName(_fromUtf8("settingsmainframewidget"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.settingsmainframewidget)
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.frame_2 = QtGui.QFrame(self.settingsmainframewidget)
        self.frame_2.setStyleSheet(_fromUtf8("#frame_2{\n"
"background-color:transparent;\n"
"}"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_16 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.settings_institutionlistLabel = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Caladea"))
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.settings_institutionlistLabel.setFont(font)
        self.settings_institutionlistLabel.setStyleSheet(_fromUtf8("border-image: url(:/icons/image-blur.png);\n"
"color:white;"))
        self.settings_institutionlistLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_institutionlistLabel.setObjectName(_fromUtf8("settings_institutionlistLabel"))
        self.gridLayout_16.addWidget(self.settings_institutionlistLabel, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.settings_instLineEdit = QtGui.QLineEdit(self.frame_2)
        self.settings_instLineEdit.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.settings_instLineEdit.setFont(font)
        self.settings_instLineEdit.setAutoFillBackground(False)
        self.settings_instLineEdit.setObjectName(_fromUtf8("settings_instLineEdit"))
        self.horizontalLayout_4.addWidget(self.settings_instLineEdit)
        self.settings_addPushButton = QtGui.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.settings_addPushButton.setFont(font)
        self.settings_addPushButton.setDefault(False)
        self.settings_addPushButton.setObjectName(_fromUtf8("settings_addPushButton"))
        self.horizontalLayout_4.addWidget(self.settings_addPushButton)
        self.settings_backinstPushButton = QtGui.QPushButton(self.frame_2)
        self.settings_backinstPushButton.setMaximumSize(QtCore.QSize(37, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.settings_backinstPushButton.setFont(font)
        self.settings_backinstPushButton.setObjectName(_fromUtf8("settings_backinstPushButton"))
        self.horizontalLayout_4.addWidget(self.settings_backinstPushButton)
        self.gridLayout_16.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.settings_addinstitutionPushButton = QtGui.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.settings_addinstitutionPushButton.setFont(font)
        self.settings_addinstitutionPushButton.setObjectName(_fromUtf8("settings_addinstitutionPushButton"))
        self.horizontalLayout_2.addWidget(self.settings_addinstitutionPushButton)
        self.removeinstitutionPushButton = QtGui.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.removeinstitutionPushButton.setFont(font)
        self.removeinstitutionPushButton.setObjectName(_fromUtf8("removeinstitutionPushButton"))
        self.horizontalLayout_2.addWidget(self.removeinstitutionPushButton)
        self.gridLayout_16.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.settings_institutionListWidget = QtGui.QListWidget(self.frame_2)
        self.settings_institutionListWidget.setMinimumSize(QtCore.QSize(500, 285))
        self.settings_institutionListWidget.setMaximumSize(QtCore.QSize(16777215, 333))
        self.settings_institutionListWidget.setStyleSheet(_fromUtf8("background-color:rgba(229, 229, 229,200);"))
        self.settings_institutionListWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.settings_institutionListWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.settings_institutionListWidget.setResizeMode(QtGui.QListView.Fixed)
        self.settings_institutionListWidget.setViewMode(QtGui.QListView.ListMode)
        self.settings_institutionListWidget.setUniformItemSizes(True)
        self.settings_institutionListWidget.setObjectName(_fromUtf8("settings_institutionListWidget"))
        self.gridLayout_16.addWidget(self.settings_institutionListWidget, 1, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.gridLayout_14.addWidget(self.settingsmainframewidget, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.formsandfieldsgridwidget = QtGui.QWidget(self.settingsscrollAreaWidgetContents)
        self.formsandfieldsgridwidget.setMinimumSize(QtCore.QSize(0, 600))
        self.formsandfieldsgridwidget.setStyleSheet(_fromUtf8("#formsandfieldsgridwidget\n"
"{\n"
"    background-color:transparent;\n"
"}"))
        self.formsandfieldsgridwidget.setObjectName(_fromUtf8("formsandfieldsgridwidget"))
        self.gridLayout_12 = QtGui.QGridLayout(self.formsandfieldsgridwidget)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.settings_fieldsknownRadioButton = QtGui.QRadioButton(self.formsandfieldsgridwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.settings_fieldsknownRadioButton.setFont(font)
        self.settings_fieldsknownRadioButton.setStyleSheet(_fromUtf8("background-color:transparent;\n"
"color:white;"))
        self.settings_fieldsknownRadioButton.setCheckable(True)
        self.settings_fieldsknownRadioButton.setChecked(False)
        self.settings_fieldsknownRadioButton.setObjectName(_fromUtf8("settings_fieldsknownRadioButton"))
        self.horizontalLayout_16.addWidget(self.settings_fieldsknownRadioButton)
        self.settings_fieldsunknownRadioButton = QtGui.QRadioButton(self.formsandfieldsgridwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.settings_fieldsunknownRadioButton.setFont(font)
        self.settings_fieldsunknownRadioButton.setStyleSheet(_fromUtf8("background-color:transparent;\n"
"color:white;"))
        self.settings_fieldsunknownRadioButton.setCheckable(True)
        self.settings_fieldsunknownRadioButton.setChecked(False)
        self.settings_fieldsunknownRadioButton.setObjectName(_fromUtf8("settings_fieldsunknownRadioButton"))
        self.horizontalLayout_16.addWidget(self.settings_fieldsunknownRadioButton)
        self.settings_addfieldPushButton = QtGui.QPushButton(self.formsandfieldsgridwidget)
        self.settings_addfieldPushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.settings_addfieldPushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gabriola"))
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.settings_addfieldPushButton.setFont(font)
        self.settings_addfieldPushButton.setStyleSheet(_fromUtf8(""))
        self.settings_addfieldPushButton.setObjectName(_fromUtf8("settings_addfieldPushButton"))
        self.horizontalLayout_16.addWidget(self.settings_addfieldPushButton)
        self.settings_removefieldPushButton = QtGui.QPushButton(self.formsandfieldsgridwidget)
        self.settings_removefieldPushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gabriola"))
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.settings_removefieldPushButton.setFont(font)
        self.settings_removefieldPushButton.setObjectName(_fromUtf8("settings_removefieldPushButton"))
        self.horizontalLayout_16.addWidget(self.settings_removefieldPushButton)
        self.gridLayout_12.addLayout(self.horizontalLayout_16, 3, 2, 1, 1)
        self.formsandfieldsLabel = QtGui.QLabel(self.formsandfieldsgridwidget)
        self.formsandfieldsLabel.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Caladea"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.formsandfieldsLabel.setFont(font)
        self.formsandfieldsLabel.setStyleSheet(_fromUtf8("border-image: url(:/icons/image-blur.png);\n"
"color:white;\n"
"margin:2px 8px;\n"
"text-align:center;"))
        self.formsandfieldsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.formsandfieldsLabel.setObjectName(_fromUtf8("formsandfieldsLabel"))
        self.gridLayout_12.addWidget(self.formsandfieldsLabel, 0, 1, 1, 2)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.settings_formsLabel = QtGui.QLabel(self.formsandfieldsgridwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.settings_formsLabel.setFont(font)
        self.settings_formsLabel.setStyleSheet(_fromUtf8("#settings_formsLabel\n"
"{\n"
"background-color:qlineargradient(spread:pad, x1:0.012, y1:0.755818, x2:0.641818, y2:0.392, stop:0 rgba(230, 255, 0, 255), stop:1 rgba(85, 104, 255, 150));\n"
"}\n"
"\n"
"#settings_formsLabel:hover\n"
"{\n"
"    background-color:qlineargradient(spread:pad, x1:0.012, y1:0.755818, x2:0.641818, y2:0.392, stop:0 rgba(85, 104, 255, 255), stop:1 rgba(230, 255, 0, 150));\n"
"}"))
        self.settings_formsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_formsLabel.setObjectName(_fromUtf8("settings_formsLabel"))
        self.verticalLayout_6.addWidget(self.settings_formsLabel)
        self.settings_formsListWidget = QtGui.QListWidget(self.formsandfieldsgridwidget)
        self.settings_formsListWidget.setMinimumSize(QtCore.QSize(400, 300))
        self.settings_formsListWidget.setMaximumSize(QtCore.QSize(475, 16777215))
        self.settings_formsListWidget.setStyleSheet(_fromUtf8("background-color:rgba(229, 229, 229,200);"))
        self.settings_formsListWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.settings_formsListWidget.setWordWrap(True)
        self.settings_formsListWidget.setObjectName(_fromUtf8("settings_formsListWidget"))
        self.verticalLayout_6.addWidget(self.settings_formsListWidget)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.settings_addformLineEdit = QtGui.QLineEdit(self.formsandfieldsgridwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.settings_addformLineEdit.setFont(font)
        self.settings_addformLineEdit.setText(_fromUtf8(""))
        self.settings_addformLineEdit.setObjectName(_fromUtf8("settings_addformLineEdit"))
        self.horizontalLayout_11.addWidget(self.settings_addformLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.setStretch(1, 1)
        self.gridLayout_12.addLayout(self.verticalLayout_6, 1, 1, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.settings_fieldsLabel = QtGui.QLabel(self.formsandfieldsgridwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.settings_fieldsLabel.setFont(font)
        self.settings_fieldsLabel.setStyleSheet(_fromUtf8("#settings_fieldsLabel \n"
"{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(229, 0, 254, 150), stop:1 rgba(122, 255, 73, 255));\n"
"}\n"
"\n"
"#settings_fieldsLabel:hover\n"
"{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.767, y2:0.773, stop:0 rgba(0, 203, 5, 200), stop:1 rgba(255, 77, 127, 150))\n"
"}"))
        self.settings_fieldsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_fieldsLabel.setObjectName(_fromUtf8("settings_fieldsLabel"))
        self.verticalLayout_7.addWidget(self.settings_fieldsLabel)
        self.settings_fieldsListWidget = QtGui.QListWidget(self.formsandfieldsgridwidget)
        self.settings_fieldsListWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.settings_fieldsListWidget.setStyleSheet(_fromUtf8("background-color:rgba(229, 229, 229,200);"))
        self.settings_fieldsListWidget.setAutoScroll(False)
        self.settings_fieldsListWidget.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.settings_fieldsListWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.settings_fieldsListWidget.setMovement(QtGui.QListView.Static)
        self.settings_fieldsListWidget.setWordWrap(True)
        self.settings_fieldsListWidget.setObjectName(_fromUtf8("settings_fieldsListWidget"))
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(65)
        item.setFont(font)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.settings_fieldsListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Caladea"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.settings_fieldsListWidget.addItem(item)
        self.verticalLayout_7.addWidget(self.settings_fieldsListWidget)
        self.settings_addfieldLineEdit = QtGui.QLineEdit(self.formsandfieldsgridwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.settings_addfieldLineEdit.setFont(font)
        self.settings_addfieldLineEdit.setText(_fromUtf8(""))
        self.settings_addfieldLineEdit.setObjectName(_fromUtf8("settings_addfieldLineEdit"))
        self.verticalLayout_7.addWidget(self.settings_addfieldLineEdit)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.settings_fieldsComboBox = QtGui.QComboBox(self.formsandfieldsgridwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_fieldsComboBox.sizePolicy().hasHeightForWidth())
        self.settings_fieldsComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.settings_fieldsComboBox.setFont(font)
        self.settings_fieldsComboBox.setMaxVisibleItems(20)
        self.settings_fieldsComboBox.setObjectName(_fromUtf8("settings_fieldsComboBox"))
        self.horizontalLayout_15.addWidget(self.settings_fieldsComboBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.gridLayout_12.addLayout(self.verticalLayout_7, 1, 2, 1, 1)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.settings_addformPushButton = QtGui.QPushButton(self.formsandfieldsgridwidget)
        self.settings_addformPushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gabriola"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.settings_addformPushButton.setFont(font)
        self.settings_addformPushButton.setObjectName(_fromUtf8("settings_addformPushButton"))
        self.horizontalLayout_17.addWidget(self.settings_addformPushButton)
        self.settings_removeformPushButton = QtGui.QPushButton(self.formsandfieldsgridwidget)
        self.settings_removeformPushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gabriola"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.settings_removeformPushButton.setFont(font)
        self.settings_removeformPushButton.setObjectName(_fromUtf8("settings_removeformPushButton"))
        self.horizontalLayout_17.addWidget(self.settings_removeformPushButton)
        self.gridLayout_12.addLayout(self.horizontalLayout_17, 3, 1, 1, 1)
        self.gridLayout_14.addWidget(self.formsandfieldsgridwidget, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem17, 1, 0, 1, 1)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem18, 3, 0, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem19, 4, 0, 1, 1)
        self.settings_candidopenPushButton = QtGui.QPushButton(self.settingsscrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        self.settings_candidopenPushButton.setFont(font)
        self.settings_candidopenPushButton.setStyleSheet(_fromUtf8("#settings_candidopenPushButton\n"
"{\n"
"border-radius:20px;\n"
"background-color:qlineargradient(spread:pad, x1:0.505682, y1:0, x2:0.477273, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 #6c65d6);\n"
"font-family:georgia;\n"
"color:white;\n"
"border-top:1px solid yellow;\n"
"border-bottom:1px solid black;\n"
"padding:10px 10px;\n"
"}\n"
"#settings_candidopenPushButton:hover\n"
"{\n"
"    color:black;\n"
"    background-color:rgba(0, 170, 255,255);\n"
"\n"
"}\n"
"\n"
"#settings_candidopenPushButton:pressed\n"
"{\n"
"    color:black;\n"
"    background-color:rgba(0, 170, 255,175);\n"
"\n"
"}"))
        self.settings_candidopenPushButton.setObjectName(_fromUtf8("settings_candidopenPushButton"))
        self.gridLayout_14.addWidget(self.settings_candidopenPushButton, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem20, 7, 0, 1, 1)
        self.SettingsScrollArea.setWidget(self.settingsscrollAreaWidgetContents)
        self.verticalLayout_11.addWidget(self.SettingsScrollArea)
        self.mytab.addTab(self.Settings, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.mytab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.selectpictureLabel.setBuddy(self.selectpicturePushButton)
        self.enrolmentnumLabel.setBuddy(self.enrolmentnumLineEdit)
        self.rankLabel.setBuddy(self.rankComboBox)
        self.aadhaarLabel.setBuddy(self.aadhaarLineEdit)
        self.fullnameLabel.setBuddy(self.fullnameLineEdit)
        self.mothernameLabel.setBuddy(self.mothernameLineEdit)
        self.sexLabel.setBuddy(self.sexComboBox)
        self.dateofbirthLabel.setBuddy(self.dateofbirthDateEdit)
        self.fathernameLabel.setBuddy(self.fathernameLineEdit)

        self.retranslateUi(MainWindow)
        self.mytab.setCurrentIndex(3)
        QtCore.QObject.connect(self.searchbyfieldLineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.searchPushButton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.enrolmentnumLineEdit, self.rankComboBox)
        MainWindow.setTabOrder(self.rankComboBox, self.aadhaarLineEdit)
        MainWindow.setTabOrder(self.aadhaarLineEdit, self.fullnameLineEdit)
        MainWindow.setTabOrder(self.fullnameLineEdit, self.fathernameLineEdit)
        MainWindow.setTabOrder(self.fathernameLineEdit, self.mothernameLineEdit)
        MainWindow.setTabOrder(self.mothernameLineEdit, self.sexComboBox)
        MainWindow.setTabOrder(self.sexComboBox, self.dateofbirthDateEdit)
        MainWindow.setTabOrder(self.dateofbirthDateEdit, self.addressTextEdit)
        MainWindow.setTabOrder(self.addressTextEdit, self.emailLineEdit)
        MainWindow.setTabOrder(self.emailLineEdit, self.mobileLineEdit)
        MainWindow.setTabOrder(self.mobileLineEdit, self.bloodgroupComboBox)
        MainWindow.setTabOrder(self.bloodgroupComboBox, self.NullcertRadioButton)
        MainWindow.setTabOrder(self.NullcertRadioButton, self.AcertRadioButton)
        MainWindow.setTabOrder(self.AcertRadioButton, self.BcertRadioButton)
        MainWindow.setTabOrder(self.BcertRadioButton, self.CcertRadioButton)
        MainWindow.setTabOrder(self.CcertRadioButton, self.NULLCampsCheckBox)
        MainWindow.setTabOrder(self.NULLCampsCheckBox, self.NICCheckBox)
        MainWindow.setTabOrder(self.NICCheckBox, self.CATCCheckBox)
        MainWindow.setTabOrder(self.CATCCheckBox, self.AACCheckBox)
        MainWindow.setTabOrder(self.AACCheckBox, self.extraactivitiesTextEdit)
        MainWindow.setTabOrder(self.extraactivitiesTextEdit, self.specialachievementsTextEdit)
        MainWindow.setTabOrder(self.specialachievementsTextEdit, self.enroldateDateEdit)
        MainWindow.setTabOrder(self.enroldateDateEdit, self.remarksTextEdit)
        MainWindow.setTabOrder(self.remarksTextEdit, self.vegRadioButton)
        MainWindow.setTabOrder(self.vegRadioButton, self.nonvegRadioButton)
        MainWindow.setTabOrder(self.nonvegRadioButton, self.banknameLineEdit)
        MainWindow.setTabOrder(self.banknameLineEdit, self.bankbranchLineEdit)
        MainWindow.setTabOrder(self.bankbranchLineEdit, self.accountnameLineEdit)
        MainWindow.setTabOrder(self.accountnameLineEdit, self.accountnumLineEdit)
        MainWindow.setTabOrder(self.accountnumLineEdit, self.ifsccodeLineEdit)
        MainWindow.setTabOrder(self.ifsccodeLineEdit, self.micrLineEdit)
        MainWindow.setTabOrder(self.micrLineEdit, self.institutionenrollComboBox)
        MainWindow.setTabOrder(self.institutionenrollComboBox, self.unitLineEdit)
        MainWindow.setTabOrder(self.unitLineEdit, self.updateentryCheckBox)
        MainWindow.setTabOrder(self.updateentryCheckBox, self.submitPushButton)
        MainWindow.setTabOrder(self.submitPushButton, self.searchbyfieldLineEdit)
        MainWindow.setTabOrder(self.searchbyfieldLineEdit, self.enrolmentnumRadioButton)
        MainWindow.setTabOrder(self.enrolmentnumRadioButton, self.aadhaarnumRadioButton)
        MainWindow.setTabOrder(self.aadhaarnumRadioButton, self.searchPushButton)
        MainWindow.setTabOrder(self.searchPushButton, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.enrolPushButton)
        MainWindow.setTabOrder(self.enrolPushButton, self.selectpicturePushButton)
        MainWindow.setTabOrder(self.selectpicturePushButton, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.mytab)
        MainWindow.setTabOrder(self.mytab, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.SettingsScrollArea)
        MainWindow.setTabOrder(self.SettingsScrollArea, self.selectallCheckBox)
        MainWindow.setTabOrder(self.selectallCheckBox, self.enrolmentCheckBox)
        MainWindow.setTabOrder(self.enrolmentCheckBox, self.sfnameCheckBox)
        MainWindow.setTabOrder(self.sfnameCheckBox, self.sexCheckBox)
        MainWindow.setTabOrder(self.sexCheckBox, self.mfnameCheckBox)
        MainWindow.setTabOrder(self.mfnameCheckBox, self.bloodgroupCheckBox)
        MainWindow.setTabOrder(self.bloodgroupCheckBox, self.ffnameCheckBox)
        MainWindow.setTabOrder(self.ffnameCheckBox, self.emailCheckBox)
        MainWindow.setTabOrder(self.emailCheckBox, self.aadhaarCheckBox)
        MainWindow.setTabOrder(self.aadhaarCheckBox, self.addressCheckBox)
        MainWindow.setTabOrder(self.addressCheckBox, self.banknameCheckBox)
        MainWindow.setTabOrder(self.banknameCheckBox, self.bankbranchCheckBox)
        MainWindow.setTabOrder(self.bankbranchCheckBox, self.accountnameCheckBox)
        MainWindow.setTabOrder(self.accountnameCheckBox, self.accountnumCheckBox)
        MainWindow.setTabOrder(self.accountnumCheckBox, self.micrCheckBox)
        MainWindow.setTabOrder(self.micrCheckBox, self.remarksCheckBox)
        MainWindow.setTabOrder(self.remarksCheckBox, self.vegitarianCheckBox)
        MainWindow.setTabOrder(self.vegitarianCheckBox, self.ifsccodeCheckBox)
        MainWindow.setTabOrder(self.ifsccodeCheckBox, self.enrollDateCheckBox)
        MainWindow.setTabOrder(self.enrollDateCheckBox, self.unitCheckBox)
        MainWindow.setTabOrder(self.unitCheckBox, self.institutionCheckBox)
        MainWindow.setTabOrder(self.institutionCheckBox, self.extraCurricularActivitiesCheckBox)
        MainWindow.setTabOrder(self.extraCurricularActivitiesCheckBox, self.campsAttendedCheckBox)
        MainWindow.setTabOrder(self.campsAttendedCheckBox, self.rankCheckBox)
        MainWindow.setTabOrder(self.rankCheckBox, self.mobileCheckBox)
        MainWindow.setTabOrder(self.mobileCheckBox, self.dateofbirthCheckBox)
        MainWindow.setTabOrder(self.dateofbirthCheckBox, self.specialAchievementsCheckBox)
        MainWindow.setTabOrder(self.specialAchievementsCheckBox, self.andcondition)
        MainWindow.setTabOrder(self.andcondition, self.orcondition)
        MainWindow.setTabOrder(self.orcondition, self.openbracecondition)
        MainWindow.setTabOrder(self.openbracecondition, self.closebracecondition)
        MainWindow.setTabOrder(self.closebracecondition, self.greatercondition)
        MainWindow.setTabOrder(self.greatercondition, self.lessercondition)
        MainWindow.setTabOrder(self.lessercondition, self.backcondition)
        MainWindow.setTabOrder(self.backcondition, self.conditionlistcombobox)
        MainWindow.setTabOrder(self.conditionlistcombobox, self.bloodgroupqueryComboBox)
        MainWindow.setTabOrder(self.bloodgroupqueryComboBox, self.institutionqueryComboBox)
        MainWindow.setTabOrder(self.institutionqueryComboBox, self.rankqueryComboBox)
        MainWindow.setTabOrder(self.rankqueryComboBox, self.sexqueryComboBox)
        MainWindow.setTabOrder(self.sexqueryComboBox, self.datequeryDateEdit)
        MainWindow.setTabOrder(self.datequeryDateEdit, self.valuelineEdit)
        MainWindow.setTabOrder(self.valuelineEdit, self.insertcondition)
        MainWindow.setTabOrder(self.insertcondition, self.clearcondition)
        MainWindow.setTabOrder(self.clearcondition, self.querycondition)
        MainWindow.setTabOrder(self.querycondition, self.webView)
        MainWindow.setTabOrder(self.webView, self.formsComboBox)
        MainWindow.setTabOrder(self.formsComboBox, self.entryBox)
        MainWindow.setTabOrder(self.entryBox, self.saveExelPushButton)
        MainWindow.setTabOrder(self.saveExelPushButton, self.updateExelPushButton)
        MainWindow.setTabOrder(self.updateExelPushButton, self.institutionuploaddatacomboBox)
        MainWindow.setTabOrder(self.institutionuploaddatacomboBox, self.typecomboBox)
        MainWindow.setTabOrder(self.typecomboBox, self.openPushButton)
        MainWindow.setTabOrder(self.openPushButton, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.savedataPushButton)
        MainWindow.setTabOrder(self.savedataPushButton, self.save_data_excelPushButton)
        MainWindow.setTabOrder(self.save_data_excelPushButton, self.settings_institutionListWidget)
        MainWindow.setTabOrder(self.settings_institutionListWidget, self.settings_addinstitutionPushButton)
        MainWindow.setTabOrder(self.settings_addinstitutionPushButton, self.removeinstitutionPushButton)
        MainWindow.setTabOrder(self.removeinstitutionPushButton, self.settings_instLineEdit)
        MainWindow.setTabOrder(self.settings_instLineEdit, self.settings_addPushButton)
        MainWindow.setTabOrder(self.settings_addPushButton, self.settings_backinstPushButton)
        MainWindow.setTabOrder(self.settings_backinstPushButton, self.settings_formsListWidget)
        MainWindow.setTabOrder(self.settings_formsListWidget, self.settings_addformLineEdit)
        MainWindow.setTabOrder(self.settings_addformLineEdit, self.settings_addformPushButton)
        MainWindow.setTabOrder(self.settings_addformPushButton, self.settings_removeformPushButton)
        MainWindow.setTabOrder(self.settings_removeformPushButton, self.settings_fieldsListWidget)
        MainWindow.setTabOrder(self.settings_fieldsListWidget, self.settings_addfieldLineEdit)
        MainWindow.setTabOrder(self.settings_addfieldLineEdit, self.settings_fieldsComboBox)
        MainWindow.setTabOrder(self.settings_fieldsComboBox, self.settings_fieldsknownRadioButton)
        MainWindow.setTabOrder(self.settings_fieldsknownRadioButton, self.settings_fieldsunknownRadioButton)
        MainWindow.setTabOrder(self.settings_fieldsunknownRadioButton, self.settings_addfieldPushButton)
        MainWindow.setTabOrder(self.settings_addfieldPushButton, self.settings_removefieldPushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NCC", None))
        self.enroltitleLabel.setText(_translate("MainWindow", "Enrolment Form", None))
        self.submitPushButton.setText(_translate("MainWindow", "Submit", None))
        self.updateentryCheckBox.setText(_translate("MainWindow", "Update Entry", None))
        self.pushButton.setStyleSheet(_translate("MainWindow", "background-color:transparent;", None))
        self.selectpicturePushButton.setToolTip(_translate("MainWindow", "Select the picture of the candidate", None))
        self.selectpicturePushButton.setText(_translate("MainWindow", "Select Picture", None))
        self.institutionLabel.setText(_translate("MainWindow", "<html><head/><body><p>Institution &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:#ff0000;\"> </span></p></body></html>", None))
        self.unitLineEdit.setText(_translate("MainWindow", "4KAR", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Unit &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:#ff0000;\"> *</span></p></body></html>", None))
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
        self.aadhaarLabel.setText(_translate("MainWindow", "<html><head/><body><p>Aadhaar No.  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:red;\">*</span></p></body></html>", None))
        self.aadhaarLineEdit.setPlaceholderText(_translate("MainWindow", "Enter 12 digit aadhaar number", None))
        self.fullnameLabel.setText(_translate("MainWindow", "<html><head/><body><p>Student Name  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.mothernameLabel.setText(_translate("MainWindow", "<html><head/><body><p>Mother\'s Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.sexLabel.setText(_translate("MainWindow", "Sex", None))
        self.sexComboBox.setItemText(0, _translate("MainWindow", "Male", None))
        self.sexComboBox.setItemText(1, _translate("MainWindow", "Female", None))
        self.dateofbirthLabel.setText(_translate("MainWindow", "Date of Birth", None))
        self.dateofbirthDateEdit.setDisplayFormat(_translate("MainWindow", "dd/MMM/yyyy", None))
        self.addressLabel.setText(_translate("MainWindow", "<html><head/><body><p>Residential Address &nbsp;&nbsp;<span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.emailLabel.setText(_translate("MainWindow", "Email", None))
        self.emailLineEdit.setPlaceholderText(_translate("MainWindow", "example@mail.com", None))
        self.mobileLabel.setText(_translate("MainWindow", "Mobile", None))
        self.mobileLineEdit.setPlaceholderText(_translate("MainWindow", "Enter 10 digit mobile number", None))
        self.bloodgroupLabel.setText(_translate("MainWindow", "Blood Group", None))
        self.bloodgroupComboBox.setItemText(0, _translate("MainWindow", "O+", None))
        self.bloodgroupComboBox.setItemText(1, _translate("MainWindow", "O-", None))
        self.bloodgroupComboBox.setItemText(2, _translate("MainWindow", "A+", None))
        self.bloodgroupComboBox.setItemText(3, _translate("MainWindow", "A-", None))
        self.bloodgroupComboBox.setItemText(4, _translate("MainWindow", "B+", None))
        self.bloodgroupComboBox.setItemText(5, _translate("MainWindow", "B-", None))
        self.bloodgroupComboBox.setItemText(6, _translate("MainWindow", "AB+", None))
        self.bloodgroupComboBox.setItemText(7, _translate("MainWindow", "AB-", None))
        self.certificateLabel.setText(_translate("MainWindow", "Certificate", None))
        self.campsattendedLabel.setText(_translate("MainWindow", "Camps Attended", None))
        self.remarksLabel.setText(_translate("MainWindow", "Remarks", None))
        self.specialachievementsLabel.setText(_translate("MainWindow", "Special Achievements", None))
        self.extracurricularactivitiesLabel.setText(_translate("MainWindow", "Extra Curricular Activities", None))
        self.enroldateLabel.setText(_translate("MainWindow", "Enrol Date", None))
        self.NullcertRadioButton.setText(_translate("MainWindow", "NULL", None))
        self.AcertRadioButton.setText(_translate("MainWindow", "A", None))
        self.BcertRadioButton.setText(_translate("MainWindow", "B", None))
        self.CcertRadioButton.setText(_translate("MainWindow", "C", None))
        self.enroldateDateEdit.setDisplayFormat(_translate("MainWindow", "dd/MMM/yyyy", None))
        self.NULLCampsCheckBox.setText(_translate("MainWindow", "NULL", None))
        self.NICCheckBox.setText(_translate("MainWindow", "NIC", None))
        self.CATCCheckBox.setText(_translate("MainWindow", "CATC", None))
        self.AACCheckBox.setText(_translate("MainWindow", "AAC", None))
        self.fathernameLabel.setText(_translate("MainWindow", "<html><head/><body><p>Father\'s Name  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.ifsccodeLabel.setText(_translate("MainWindow", "IFSC code", None))
        self.bankbranchLabel.setText(_translate("MainWindow", "Branch", None))
        self.micrLabel.setText(_translate("MainWindow", "MICR CODE", None))
        self.banknameLabel.setText(_translate("MainWindow", "Bank Name", None))
        self.accountnumLabel.setText(_translate("MainWindow", "Account No.", None))
        self.accountnameLabel.setText(_translate("MainWindow", "Account name", None))
        self.vegRadioButton.setText(_translate("MainWindow", "Veg", None))
        self.nonvegRadioButton.setText(_translate("MainWindow", "Non-Veg", None))
        self.bankdetailsLabel.setText(_translate("MainWindow", "Bank Details", None))
        self.enrolPushButton.setText(_translate("MainWindow", "Enroll", None))
        self.enrolmentnumRadioButton.setText(_translate("MainWindow", "Enrolment No.", None))
        self.aadhaarnumRadioButton.setText(_translate("MainWindow", "Aadhaar No.", None))
        self.searchbyfieldLineEdit.setPlaceholderText(_translate("MainWindow", "Search by", None))
        self.searchPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to search</p></body></html>", None))
        self.searchPushButton.setText(_translate("MainWindow", "Search", None))
        self.mytab.setTabText(self.mytab.indexOf(self.Enrol), _translate("MainWindow", "Enrolment form", None))
        self.mytab.setTabToolTip(self.mytab.indexOf(self.Enrol), _translate("MainWindow", "Enrolment form", None))
        self.remarksCheckBox.setText(_translate("MainWindow", "Remarks", None))
        self.selectallCheckBox.setText(_translate("MainWindow", "Select All", None))
        self.aadhaarCheckBox.setText(_translate("MainWindow", "Aadhaar", None))
        self.banknameCheckBox.setText(_translate("MainWindow", "Bank Name", None))
        self.accountnumCheckBox.setText(_translate("MainWindow", "Account Num", None))
        self.addressCheckBox.setText(_translate("MainWindow", "Address", None))
        self.bankbranchCheckBox.setText(_translate("MainWindow", "Branch Name", None))
        self.emailCheckBox.setText(_translate("MainWindow", "Email", None))
        self.micrCheckBox.setText(_translate("MainWindow", "MICR", None))
        self.accountnameCheckBox.setText(_translate("MainWindow", "Account Name", None))
        self.enrolmentCheckBox.setText(_translate("MainWindow", "Enrolment", None))
        self.sfnameCheckBox.setText(_translate("MainWindow", "Student Name", None))
        self.mfnameCheckBox.setText(_translate("MainWindow", "Mother Name", None))
        self.bloodgroupCheckBox.setText(_translate("MainWindow", "Blood Group", None))
        self.ffnameCheckBox.setText(_translate("MainWindow", "Father Name", None))
        self.sexCheckBox.setText(_translate("MainWindow", "Sex", None))
        self.vegitarianCheckBox.setText(_translate("MainWindow", "Vegitarian", None))
        self.ifsccodeCheckBox.setText(_translate("MainWindow", "IFSC Code", None))
        self.enrollDateCheckBox.setText(_translate("MainWindow", "Enroll Date", None))
        self.unitCheckBox.setText(_translate("MainWindow", "Unit", None))
        self.institutionCheckBox.setText(_translate("MainWindow", "Institution", None))
        self.extraCurricularActivitiesCheckBox.setText(_translate("MainWindow", "Extra_Curricular_Activities", None))
        self.campsAttendedCheckBox.setText(_translate("MainWindow", "Camps_Attended", None))
        self.rankCheckBox.setText(_translate("MainWindow", "Rank", None))
        self.specialAchievementsCheckBox.setText(_translate("MainWindow", "Special_Achievements", None))
        self.dateofbirthCheckBox.setText(_translate("MainWindow", "Date of Birth", None))
        self.mobileCheckBox.setText(_translate("MainWindow", "Mobile", None))
        self.andcondition.setText(_translate("MainWindow", "AND", None))
        self.orcondition.setText(_translate("MainWindow", "OR", None))
        self.openbracecondition.setText(_translate("MainWindow", "(", None))
        self.closebracecondition.setText(_translate("MainWindow", ")", None))
        self.greatercondition.setText(_translate("MainWindow", ">", None))
        self.lessercondition.setText(_translate("MainWindow", "<", None))
        self.backcondition.setText(_translate("MainWindow", "Back", None))
        self.conditionlistcombobox.setItemText(0, _translate("MainWindow", "Select Fields", None))
        self.conditionlistcombobox.setItemText(1, _translate("MainWindow", "Enrolment_Number", None))
        self.conditionlistcombobox.setItemText(2, _translate("MainWindow", "Rank", None))
        self.conditionlistcombobox.setItemText(3, _translate("MainWindow", "Aadhaar_Number", None))
        self.conditionlistcombobox.setItemText(4, _translate("MainWindow", "Student_Name", None))
        self.conditionlistcombobox.setItemText(5, _translate("MainWindow", "Fathers_Name", None))
        self.conditionlistcombobox.setItemText(6, _translate("MainWindow", "Mothers_Name", None))
        self.conditionlistcombobox.setItemText(7, _translate("MainWindow", "Sex", None))
        self.conditionlistcombobox.setItemText(8, _translate("MainWindow", "Date_Of_Birth", None))
        self.conditionlistcombobox.setItemText(9, _translate("MainWindow", "Address", None))
        self.conditionlistcombobox.setItemText(10, _translate("MainWindow", "Enrol_Date", None))
        self.conditionlistcombobox.setItemText(11, _translate("MainWindow", "Email", None))
        self.conditionlistcombobox.setItemText(12, _translate("MainWindow", "Mobile_Number", None))
        self.conditionlistcombobox.setItemText(13, _translate("MainWindow", "Blood_Group", None))
        self.conditionlistcombobox.setItemText(14, _translate("MainWindow", "Certificate", None))
        self.conditionlistcombobox.setItemText(15, _translate("MainWindow", "Camps_Attended", None))
        self.conditionlistcombobox.setItemText(16, _translate("MainWindow", "Vegitarian", None))
        self.conditionlistcombobox.setItemText(17, _translate("MainWindow", "Bank_Name", None))
        self.conditionlistcombobox.setItemText(18, _translate("MainWindow", "Branch", None))
        self.conditionlistcombobox.setItemText(19, _translate("MainWindow", "Account_Name", None))
        self.conditionlistcombobox.setItemText(20, _translate("MainWindow", "Account_Number", None))
        self.conditionlistcombobox.setItemText(21, _translate("MainWindow", "IFSC_Code", None))
        self.conditionlistcombobox.setItemText(22, _translate("MainWindow", "Institution", None))
        self.conditionlistcombobox.setItemText(23, _translate("MainWindow", "Unit", None))
        self.campsattendedqueryComboBox.setItemText(0, _translate("MainWindow", "NIC", None))
        self.campsattendedqueryComboBox.setItemText(1, _translate("MainWindow", "AAC", None))
        self.campsattendedqueryComboBox.setItemText(2, _translate("MainWindow", "CATC", None))
        self.vegitarianqueryComboBox.setItemText(0, _translate("MainWindow", "veg", None))
        self.vegitarianqueryComboBox.setItemText(1, _translate("MainWindow", "nonveg", None))
        self.bloodgroupqueryComboBox.setItemText(0, _translate("MainWindow", "O+", None))
        self.bloodgroupqueryComboBox.setItemText(1, _translate("MainWindow", "O-", None))
        self.bloodgroupqueryComboBox.setItemText(2, _translate("MainWindow", "A+", None))
        self.bloodgroupqueryComboBox.setItemText(3, _translate("MainWindow", "A-", None))
        self.bloodgroupqueryComboBox.setItemText(4, _translate("MainWindow", "B+", None))
        self.bloodgroupqueryComboBox.setItemText(5, _translate("MainWindow", "B-", None))
        self.bloodgroupqueryComboBox.setItemText(6, _translate("MainWindow", "AB+", None))
        self.bloodgroupqueryComboBox.setItemText(7, _translate("MainWindow", "AB-", None))
        self.certificatequeryComboBox.setItemText(0, _translate("MainWindow", "A", None))
        self.certificatequeryComboBox.setItemText(1, _translate("MainWindow", "B", None))
        self.certificatequeryComboBox.setItemText(2, _translate("MainWindow", "C", None))
        self.rankqueryComboBox.setItemText(0, _translate("MainWindow", "Cadet (CDT)", None))
        self.rankqueryComboBox.setItemText(1, _translate("MainWindow", "Lance Corporal (LCPL)", None))
        self.rankqueryComboBox.setItemText(2, _translate("MainWindow", "Corporal  (CPL)", None))
        self.rankqueryComboBox.setItemText(3, _translate("MainWindow", "Sergent (SGT)", None))
        self.rankqueryComboBox.setItemText(4, _translate("MainWindow", "Company Sergent Major (CSM)", None))
        self.rankqueryComboBox.setItemText(5, _translate("MainWindow", "Junior Under Officer (JUO)", None))
        self.rankqueryComboBox.setItemText(6, _translate("MainWindow", "Senior Under Officer (SUO)", None))
        self.sexqueryComboBox.setItemText(0, _translate("MainWindow", "Male", None))
        self.sexqueryComboBox.setItemText(1, _translate("MainWindow", "Female", None))
        self.datequeryDateEdit.setDisplayFormat(_translate("MainWindow", "dd/MMM/yyyy", None))
        self.insertcondition.setText(_translate("MainWindow", "Insert", None))
        self.clearcondition.setText(_translate("MainWindow", "Clear", None))
        self.querycondition.setText(_translate("MainWindow", "Query", None))
        self.generateexcelqueryPushButton.setText(_translate("MainWindow", "Generate CSV", None))
        self.mytab.setTabText(self.mytab.indexOf(self.Query), _translate("MainWindow", "Query", None))
        self.mytab.setTabToolTip(self.mytab.indexOf(self.Query), _translate("MainWindow", "Query", None))
        self.saveExelPushButton.setText(_translate("MainWindow", "Generate Form", None))
        self.updateExelPushButton.setText(_translate("MainWindow", "Update Form", None))
        self.label_3.setText(_translate("MainWindow", "Enter Enrollment numbers", None))
        self.formsComboBox.setItemText(0, _translate("MainWindow", "New Item", None))
        self.formsComboBox.setItemText(1, _translate("MainWindow", "New Item", None))
        self.formsComboBox.setItemText(2, _translate("MainWindow", "New Item", None))
        self.formsComboBox.setItemText(3, _translate("MainWindow", "New Item", None))
        self.formsComboBox.setItemText(4, _translate("MainWindow", "New Item", None))
        self.label_12.setText(_translate("MainWindow", "Choose your Form", None))
        self.mytab.setTabText(self.mytab.indexOf(self.Forms), _translate("MainWindow", "Forms", None))
        self.mytab.setTabToolTip(self.mytab.indexOf(self.Forms), _translate("MainWindow", "Forms", None))
        self.institutionuploaddatacomboBox.setItemText(0, _translate("MainWindow", "Select Institution", None))
        self.institutionuploaddatacomboBox.setItemText(1, _translate("MainWindow", "SIT", None))
        self.institutionuploaddatacomboBox.setItemText(2, _translate("MainWindow", "Sarvodaya PU College", None))
        self.typecomboBox.setItemText(0, _translate("MainWindow", "Select Type", None))
        self.typecomboBox.setItemText(1, _translate("MainWindow", "Upload Marks(A)", None))
        self.typecomboBox.setItemText(2, _translate("MainWindow", "Upload Marks(B)", None))
        self.typecomboBox.setItemText(3, _translate("MainWindow", "Upload Marks(C)", None))
        self.typecomboBox.setItemText(4, _translate("MainWindow", "Add Camps", None))
        self.typecomboBox.setItemText(5, _translate("MainWindow", "Add Extra Activities", None))
        self.typecomboBox.setItemText(6, _translate("MainWindow", "Add Remarks", None))
        self.openPushButton.setText(_translate("MainWindow", "Open Entry Table", None))
        self.savedataPushButton.setText(_translate("MainWindow", "Save to database", None))
        self.save_data_excelPushButton.setText(_translate("MainWindow", "Generate Excel", None))
        self.mytab.setTabText(self.mytab.indexOf(self.DataEntry), _translate("MainWindow", "Data Entry", None))
        self.mytab.setTabToolTip(self.mytab.indexOf(self.DataEntry), _translate("MainWindow", "Upload data", None))
        self.settings_institutionlistLabel.setText(_translate("MainWindow", "Institution List", None))
        self.settings_instLineEdit.setPlaceholderText(_translate("MainWindow", "Enter the institution name to add it", None))
        self.settings_addPushButton.setText(_translate("MainWindow", "Add", None))
        self.settings_backinstPushButton.setText(_translate("MainWindow", "Back", None))
        self.settings_addinstitutionPushButton.setText(_translate("MainWindow", "Add Institution", None))
        self.removeinstitutionPushButton.setText(_translate("MainWindow", "Remove", None))
        self.settings_institutionListWidget.setSortingEnabled(False)
        self.settings_fieldsknownRadioButton.setText(_translate("MainWindow", "Add known fields", None))
        self.settings_fieldsunknownRadioButton.setText(_translate("MainWindow", "Add Unknown fields", None))
        self.settings_addfieldPushButton.setText(_translate("MainWindow", "Add Field", None))
        self.settings_removefieldPushButton.setText(_translate("MainWindow", "Remove Field", None))
        self.formsandfieldsLabel.setText(_translate("MainWindow", "Forms and Fields Management", None))
        self.settings_formsLabel.setText(_translate("MainWindow", "Forms", None))
        self.settings_addformLineEdit.setPlaceholderText(_translate("MainWindow", "Enter New Form name", None))
        self.settings_fieldsLabel.setText(_translate("MainWindow", "Fields", None))
        __sortingEnabled = self.settings_fieldsListWidget.isSortingEnabled()
        self.settings_fieldsListWidget.setSortingEnabled(False)
        item = self.settings_fieldsListWidget.item(1)
        item.setText(_translate("MainWindow", "Select a Form from the Forms list to display all the corresponding fields of that form", None))
        item.setToolTip(_translate("MainWindow", "Select a Form", None))
        self.settings_fieldsListWidget.setSortingEnabled(__sortingEnabled)
        self.settings_addfieldLineEdit.setPlaceholderText(_translate("MainWindow", "Enter New Field name", None))
        self.settings_addformPushButton.setText(_translate("MainWindow", "Add Form", None))
        self.settings_removeformPushButton.setText(_translate("MainWindow", "Remove Form", None))
        self.settings_candidopenPushButton.setText(_translate("MainWindow", "Open Candidates Picture folder", None))
        self.mytab.setTabText(self.mytab.indexOf(self.Settings), _translate("MainWindow", "Settings", None))
        self.mytab.setTabToolTip(self.mytab.indexOf(self.Settings), _translate("MainWindow", "Settings", None))

from PyQt4 import QtWebKit
import icon_res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

