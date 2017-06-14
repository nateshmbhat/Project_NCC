
import icon_res_rc
import sqlite3
from PyQt4 import QtCore, QtGui
import ENROLMENT_FORM

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
        MainWindow.resize(1154, 999)
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
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/ncc1.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.Enroll = QtGui.QWidget()
        self.Enroll.setStyleSheet(_fromUtf8("#Enroll{\n"
"background-image:url(:/icons/image-blur.png)\n"
"}"))
        self.Enroll.setObjectName(_fromUtf8("Enroll"))
        self.gridLayout = QtGui.QGridLayout(self.Enroll)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.enrolltitleLabel = QtGui.QLabel(self.Enroll)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.enrolltitleLabel.setFont(font)
        self.enrolltitleLabel.setMouseTracking(True)
        self.enrolltitleLabel.setStyleSheet(_fromUtf8("background-image:url(:/icons/graywood.png) ;\n"
"background-position:center;\n"
"font-size:30px;\n"
"color:white;\n"
"border-radius:5px;\n"
"border-width:3px;\n"
"border-color:black;\n"
"border-style:dotted;\n"
"text-decoration:underlined;\n"
"text-shadow:0 1px 0 rgb(204,204,204) , 0 2px 0 rgb(201,201,201) , 0 3px 0 rgb(187,187,187) , 0 4px 0 rgb(185,185,185) , 0 5px 0 rgb(170,170,170) , 0 6px 1px rgba(0,0,0,0.0980392) , 0 0 5px rgba(0,0,0,0.0980392) , 0 1px 3px rgba(0,0,0,0.298039) , 0 3px 5px rgba(0,0,0,0.2) , 0 5px 10px rgba(0,0,0,0.247059) , 0 10px 10px rgba(0,0,0,0.2) , 0 20px 20px rgba(0,0,0,0.14902) ;"))
        self.enrolltitleLabel.setObjectName(_fromUtf8("enrolltitleLabel"))
        self.gridLayout.addWidget(self.enrolltitleLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.searchFrame = QtGui.QFrame(self.Enroll)
        self.searchFrame.setMinimumSize(QtCore.QSize(0, 31))
        self.searchFrame.setStyleSheet(_fromUtf8("#searchFrame{\n"
"background-color:transparent;\n"
"}"))
        self.searchFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.searchFrame.setObjectName(_fromUtf8("searchFrame"))
        self.searchbyenLineEdit = QtGui.QLineEdit(self.searchFrame)
        self.searchbyenLineEdit.setGeometry(QtCore.QRect(0, 0, 230, 26))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.searchbyenLineEdit.setFont(font)
        self.searchbyenLineEdit.setStyleSheet(_fromUtf8("border-radius:2px;\n"
"font-size:20px;\n"
"width:230;"))
        self.searchbyenLineEdit.setText(_fromUtf8(""))
        self.searchbyenLineEdit.setObjectName(_fromUtf8("searchbyenLineEdit"))
        self.searchPushButton = QtGui.QPushButton(self.searchFrame)
        self.searchPushButton.setGeometry(QtCore.QRect(230, 0, 91, 27))
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
        self.gridLayout.addWidget(self.searchFrame, 2, 0, 2, 1)
        self.submitPushButton = QtGui.QPushButton(self.Enroll)
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
        self.gridLayout.addWidget(self.submitPushButton, 12, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 13, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.Enroll)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -195, 1095, 1256))
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
        self.enrollformFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.enrollformFrame.setStyleSheet(_fromUtf8("\n"
"#enrollformFrame{\n"
"font-family:georgia;\n"
"font-weight:bold;\n"
"margin:2px;\n"
"background-color:white;\n"
"border-radius:15px;\n"
"}\n"
"\n"
""))
        self.enrollformFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.enrollformFrame.setObjectName(_fromUtf8("enrollformFrame"))
        self.Enroll_form = QtGui.QFormLayout(self.enrollformFrame)
        self.Enroll_form.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.Enroll_form.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.Enroll_form.setRowWrapPolicy(QtGui.QFormLayout.DontWrapRows)
        self.Enroll_form.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Enroll_form.setContentsMargins(10, -1, 10, -1)
        self.Enroll_form.setHorizontalSpacing(9)
        self.Enroll_form.setVerticalSpacing(10)
        self.Enroll_form.setObjectName(_fromUtf8("Enroll_form"))
        self.aadhaarLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.aadhaarLabel.setFont(font)
        self.aadhaarLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.aadhaarLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.aadhaarLabel.setTextFormat(QtCore.Qt.PlainText)
        self.aadhaarLabel.setObjectName(_fromUtf8("aadhaarLabel"))
        self.Enroll_form.setWidget(2, QtGui.QFormLayout.LabelRole, self.aadhaarLabel)
        self.aadhaarLineEdit = QtGui.QLineEdit(self.enrollformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aadhaarLineEdit.setFont(font)
        self.aadhaarLineEdit.setMouseTracking(True)
        self.aadhaarLineEdit.setAcceptDrops(True)
        self.aadhaarLineEdit.setStyleSheet(_fromUtf8(""))
        self.aadhaarLineEdit.setText(_fromUtf8(""))
        self.aadhaarLineEdit.setFrame(True)
        self.aadhaarLineEdit.setPlaceholderText(_fromUtf8(""))
        self.aadhaarLineEdit.setObjectName(_fromUtf8("aadhaarLineEdit"))
        self.Enroll_form.setWidget(2, QtGui.QFormLayout.FieldRole, self.aadhaarLineEdit)
        self.fullnameLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fullnameLabel.setFont(font)
        self.fullnameLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.fullnameLabel.setObjectName(_fromUtf8("fullnameLabel"))
        self.Enroll_form.setWidget(4, QtGui.QFormLayout.LabelRole, self.fullnameLabel)
        self.fullnameLineEdit = QtGui.QLineEdit(self.enrollformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fullnameLineEdit.setFont(font)
        self.fullnameLineEdit.setStyleSheet(_fromUtf8(""))
        self.fullnameLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.fullnameLineEdit.setText(_fromUtf8(""))
        self.fullnameLineEdit.setObjectName(_fromUtf8("fullnameLineEdit"))
        self.Enroll_form.setWidget(4, QtGui.QFormLayout.FieldRole, self.fullnameLineEdit)
        self.fathernameLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fathernameLabel.setFont(font)
        self.fathernameLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.fathernameLabel.setObjectName(_fromUtf8("fathernameLabel"))
        self.Enroll_form.setWidget(5, QtGui.QFormLayout.LabelRole, self.fathernameLabel)
        self.mothernameLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mothernameLabel.setFont(font)
        self.mothernameLabel.setObjectName(_fromUtf8("mothernameLabel"))
        self.Enroll_form.setWidget(6, QtGui.QFormLayout.LabelRole, self.mothernameLabel)
        self.mothernameLineEdit = QtGui.QLineEdit(self.enrollformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mothernameLineEdit.setFont(font)
        self.mothernameLineEdit.setStyleSheet(_fromUtf8(""))
        self.mothernameLineEdit.setObjectName(_fromUtf8("mothernameLineEdit"))
        self.Enroll_form.setWidget(6, QtGui.QFormLayout.FieldRole, self.mothernameLineEdit)
        self.sexLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.sexLabel.setFont(font)
        self.sexLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.sexLabel.setObjectName(_fromUtf8("sexLabel"))
        self.Enroll_form.setWidget(7, QtGui.QFormLayout.LabelRole, self.sexLabel)
        self.sexComboBox = QtGui.QComboBox(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sexComboBox.setFont(font)
        self.sexComboBox.setStyleSheet(_fromUtf8("width:150px;\n"
"text-align:center;\n"
"align-content:center;"))
        self.sexComboBox.setIconSize(QtCore.QSize(16, 16))
        self.sexComboBox.setObjectName(_fromUtf8("sexComboBox"))
        self.sexComboBox.addItem(_fromUtf8(""))
        self.sexComboBox.addItem(_fromUtf8(""))
        self.Enroll_form.setWidget(7, QtGui.QFormLayout.FieldRole, self.sexComboBox)
        self.dateofbirthLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.dateofbirthLabel.setFont(font)
        self.dateofbirthLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.dateofbirthLabel.setObjectName(_fromUtf8("dateofbirthLabel"))
        self.Enroll_form.setWidget(11, QtGui.QFormLayout.LabelRole, self.dateofbirthLabel)
        self.dateofbirthDateEdit = QtGui.QDateEdit(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateofbirthDateEdit.setFont(font)
        self.dateofbirthDateEdit.setFrame(True)
        self.dateofbirthDateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.dateofbirthDateEdit.setCalendarPopup(True)
        self.dateofbirthDateEdit.setObjectName(_fromUtf8("dateofbirthDateEdit"))
        self.Enroll_form.setWidget(11, QtGui.QFormLayout.FieldRole, self.dateofbirthDateEdit)
        self.addressLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.addressLabel.setFont(font)
        self.addressLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.Enroll_form.setWidget(12, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtGui.QTextEdit(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addressLineEdit.setFont(font)
        self.addressLineEdit.setStyleSheet(_fromUtf8(""))
        self.addressLineEdit.setObjectName(_fromUtf8("addressLineEdit"))
        self.Enroll_form.setWidget(12, QtGui.QFormLayout.FieldRole, self.addressLineEdit)
        self.emailLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.emailLabel.setFont(font)
        self.emailLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.Enroll_form.setWidget(13, QtGui.QFormLayout.LabelRole, self.emailLabel)
        self.emailLineEdit = QtGui.QLineEdit(self.enrollformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setStyleSheet(_fromUtf8(""))
        self.emailLineEdit.setText(_fromUtf8(""))
        self.emailLineEdit.setObjectName(_fromUtf8("emailLineEdit"))
        self.Enroll_form.setWidget(13, QtGui.QFormLayout.FieldRole, self.emailLineEdit)
        self.mobileLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mobileLabel.setFont(font)
        self.mobileLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.mobileLabel.setObjectName(_fromUtf8("mobileLabel"))
        self.Enroll_form.setWidget(14, QtGui.QFormLayout.LabelRole, self.mobileLabel)
        self.mobileLineEdit = QtGui.QLineEdit(self.enrollformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mobileLineEdit.setFont(font)
        self.mobileLineEdit.setStyleSheet(_fromUtf8(""))
        self.mobileLineEdit.setObjectName(_fromUtf8("mobileLineEdit"))
        self.Enroll_form.setWidget(14, QtGui.QFormLayout.FieldRole, self.mobileLineEdit)
        self.bloodgroupLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bloodgroupLabel.setFont(font)
        self.bloodgroupLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.bloodgroupLabel.setObjectName(_fromUtf8("bloodgroupLabel"))
        self.Enroll_form.setWidget(15, QtGui.QFormLayout.LabelRole, self.bloodgroupLabel)
        self.bloodgroupLineEdit = QtGui.QLineEdit(self.enrollformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bloodgroupLineEdit.setFont(font)
        self.bloodgroupLineEdit.setStyleSheet(_fromUtf8(""))
        self.bloodgroupLineEdit.setObjectName(_fromUtf8("bloodgroupLineEdit"))
        self.Enroll_form.setWidget(15, QtGui.QFormLayout.FieldRole, self.bloodgroupLineEdit)
        self.fathernameLineEdit = QtGui.QLineEdit(self.enrollformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fathernameLineEdit.setFont(font)
        self.fathernameLineEdit.setStyleSheet(_fromUtf8(""))
        self.fathernameLineEdit.setObjectName(_fromUtf8("fathernameLineEdit"))
        self.Enroll_form.setWidget(5, QtGui.QFormLayout.FieldRole, self.fathernameLineEdit)
        self.enrolmentnumLabel = QtGui.QLabel(self.enrollformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.enrolmentnumLabel.setFont(font)
        self.enrolmentnumLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.enrolmentnumLabel.setObjectName(_fromUtf8("enrolmentnumLabel"))
        self.Enroll_form.setWidget(0, QtGui.QFormLayout.LabelRole, self.enrolmentnumLabel)
        self.enrolmentnumLineEdit = QtGui.QLineEdit(self.enrollformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enrolmentnumLineEdit.setFont(font)
        self.enrolmentnumLineEdit.setStyleSheet(_fromUtf8(""))
        self.enrolmentnumLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.enrolmentnumLineEdit.setText(_fromUtf8(""))
        self.enrolmentnumLineEdit.setObjectName(_fromUtf8("enrolmentnumLineEdit"))
        self.Enroll_form.setWidget(0, QtGui.QFormLayout.FieldRole, self.enrolmentnumLineEdit)
        self.gridLayout_3.addWidget(self.enrollformFrame, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.bankdetailsLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.bankdetailsLabel.setFont(font)
        self.bankdetailsLabel.setAcceptDrops(False)
        self.bankdetailsLabel.setAutoFillBackground(False)
        self.bankdetailsLabel.setStyleSheet(_fromUtf8("\n"
"\n"
"font-size:25px;\n"
"background-color:transparent;\n"
"color:yellow;\n"
"border-width:2px;\n"
"border-color:black;\n"
"border-style:groove;\n"
"margin-bottom:5px;"))
        self.bankdetailsLabel.setObjectName(_fromUtf8("bankdetailsLabel"))
        self.gridLayout_3.addWidget(self.bankdetailsLabel, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
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
        self.ncclogoLabel.setFont(font)
        self.ncclogoLabel.setStyleSheet(_fromUtf8("background-size:10px;\n"
"font-size:50%;"))
        self.ncclogoLabel.setFrameShape(QtGui.QFrame.WinPanel)
        self.ncclogoLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.ncclogoLabel.setText(_fromUtf8(""))
        self.ncclogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ncc1.png")))
        self.ncclogoLabel.setScaledContents(True)
        self.ncclogoLabel.setObjectName(_fromUtf8("ncclogoLabel"))
        self.gridLayout_3.addWidget(self.ncclogoLabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 13, 1, 1, 1)
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
        self.gridLayout_3.addWidget(self.line_2, 12, 1, 1, 1, QtCore.Qt.AlignHCenter)
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
        self.gridLayout_3.addWidget(self.line, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 5, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 11, 1, 1, 1)
        self.bankformFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bankformFrame.setFont(font)
        self.bankformFrame.setStyleSheet(_fromUtf8("\n"
"#bankformFrame\n"
"{font-weight:bold;\n"
"background-color:white;\n"
"border-radius:10px;\n"
"}"))
        self.bankformFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bankformFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.bankformFrame.setObjectName(_fromUtf8("bankformFrame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.bankformFrame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.bankbranchLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bankbranchLineEdit.setFont(font)
        self.bankbranchLineEdit.setObjectName(_fromUtf8("bankbranchLineEdit"))
        self.gridLayout_2.addWidget(self.bankbranchLineEdit, 1, 1, 1, 1)
        self.accountnumLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.accountnumLabel.setFont(font)
        self.accountnumLabel.setObjectName(_fromUtf8("accountnumLabel"))
        self.gridLayout_2.addWidget(self.accountnumLabel, 4, 0, 1, 1)
        self.bankbranchLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bankbranchLabel.setFont(font)
        self.bankbranchLabel.setObjectName(_fromUtf8("bankbranchLabel"))
        self.gridLayout_2.addWidget(self.bankbranchLabel, 1, 0, 1, 1)
        self.accountnumLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.accountnumLineEdit.setFont(font)
        self.accountnumLineEdit.setObjectName(_fromUtf8("accountnumLineEdit"))
        self.gridLayout_2.addWidget(self.accountnumLineEdit, 4, 1, 1, 1)
        self.isfccodeLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.isfccodeLabel.setFont(font)
        self.isfccodeLabel.setObjectName(_fromUtf8("isfccodeLabel"))
        self.gridLayout_2.addWidget(self.isfccodeLabel, 5, 0, 1, 1)
        self.isfccodeLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.isfccodeLineEdit.setFont(font)
        self.isfccodeLineEdit.setObjectName(_fromUtf8("isfccodeLineEdit"))
        self.gridLayout_2.addWidget(self.isfccodeLineEdit, 5, 1, 1, 1)
        self.accountnameLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.accountnameLabel.setFont(font)
        self.accountnameLabel.setObjectName(_fromUtf8("accountnameLabel"))
        self.gridLayout_2.addWidget(self.accountnameLabel, 2, 0, 1, 1)
        self.accountnameLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.accountnameLineEdit.setFont(font)
        self.accountnameLineEdit.setObjectName(_fromUtf8("accountnameLineEdit"))
        self.gridLayout_2.addWidget(self.accountnameLineEdit, 2, 1, 1, 1)
        self.banknameLabel = QtGui.QLabel(self.bankformFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.banknameLabel.setFont(font)
        self.banknameLabel.setObjectName(_fromUtf8("banknameLabel"))
        self.gridLayout_2.addWidget(self.banknameLabel, 0, 0, 1, 1)
        self.banknameLineEdit = QtGui.QLineEdit(self.bankformFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.banknameLineEdit.setFont(font)
        self.banknameLineEdit.setObjectName(_fromUtf8("banknameLineEdit"))
        self.gridLayout_2.addWidget(self.banknameLineEdit, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.bankformFrame, 7, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.instFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.instFrame.setStyleSheet(_fromUtf8("#instFrame\n"
"{\n"
"width:500px;\n"
"border-radius:10px;\n"
"}"))
        self.instFrame.setObjectName(_fromUtf8("instFrame"))
        self.gridLayout_4 = QtGui.QGridLayout(self.instFrame)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.institutionLineEdit = QtGui.QLineEdit(self.instFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.institutionLineEdit.setFont(font)
        self.institutionLineEdit.setObjectName(_fromUtf8("institutionLineEdit"))
        self.gridLayout_4.addWidget(self.institutionLineEdit, 0, 4, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 1, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 1, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 7, 1, 1)
        self.unitLabel = QtGui.QLabel(self.instFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.unitLabel.setFont(font)
        self.unitLabel.setStyleSheet(_fromUtf8("#instFrame{\n"
"border-radius:15px;\n"
"width:500px;\n"
"margin:auto;\n"
"}\n"
""))
        self.unitLabel.setObjectName(_fromUtf8("unitLabel"))
        self.gridLayout_4.addWidget(self.unitLabel, 1, 0, 1, 1)
        self.institutionLabel = QtGui.QLabel(self.instFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.institutionLabel.setFont(font)
        self.institutionLabel.setObjectName(_fromUtf8("institutionLabel"))
        self.gridLayout_4.addWidget(self.institutionLabel, 0, 0, 1, 1)
        self.unitLineEdit = QtGui.QLineEdit(self.instFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.unitLineEdit.setFont(font)
        self.unitLineEdit.setObjectName(_fromUtf8("unitLineEdit"))
        self.gridLayout_4.addWidget(self.unitLineEdit, 1, 4, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 1, 3, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 0, 5, 1, 1)
        self.gridLayout_3.addWidget(self.instFrame, 14, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, 8, 1, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 2, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 7, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/Screenshots/Screenshot (113).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mytab.addTab(self.Enroll, icon1, _fromUtf8(""))
        self.Yoga = QtGui.QWidget()
        self.Yoga.setObjectName(_fromUtf8("Yoga"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/Screenshots/Screenshot (107).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mytab.addTab(self.Yoga, icon2, _fromUtf8(""))
        self.Attendence = QtGui.QWidget()
        self.Attendence.setObjectName(_fromUtf8("Attendence"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/Screenshots/Screenshot (98).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mytab.addTab(self.Attendence, icon3, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.mytab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mytab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.searchPushButton, self.enrolmentnumLineEdit)
        MainWindow.setTabOrder(self.enrolmentnumLineEdit, self.aadhaarLineEdit)
        MainWindow.setTabOrder(self.aadhaarLineEdit, self.fullnameLineEdit)
        MainWindow.setTabOrder(self.fullnameLineEdit, self.fathernameLineEdit)
        MainWindow.setTabOrder(self.fathernameLineEdit, self.mothernameLineEdit)
        MainWindow.setTabOrder(self.mothernameLineEdit, self.sexComboBox)
        MainWindow.setTabOrder(self.sexComboBox, self.dateofbirthDateEdit)
        MainWindow.setTabOrder(self.dateofbirthDateEdit, self.addressLineEdit)
        MainWindow.setTabOrder(self.addressLineEdit, self.emailLineEdit)
        MainWindow.setTabOrder(self.emailLineEdit, self.mobileLineEdit)
        MainWindow.setTabOrder(self.mobileLineEdit, self.bloodgroupLineEdit)
        MainWindow.setTabOrder(self.bloodgroupLineEdit, self.banknameLineEdit)
        MainWindow.setTabOrder(self.banknameLineEdit, self.bankbranchLineEdit)
        MainWindow.setTabOrder(self.bankbranchLineEdit, self.accountnameLineEdit)
        MainWindow.setTabOrder(self.accountnameLineEdit, self.accountnumLineEdit)
        MainWindow.setTabOrder(self.accountnumLineEdit, self.isfccodeLineEdit)
        MainWindow.setTabOrder(self.isfccodeLineEdit, self.institutionLineEdit)
        MainWindow.setTabOrder(self.institutionLineEdit, self.unitLineEdit)
        MainWindow.setTabOrder(self.unitLineEdit, self.submitPushButton)
        MainWindow.setTabOrder(self.submitPushButton, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.mytab)
        MainWindow.setTabOrder(self.mytab, self.searchbyenLineEdit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NCC", None))
        self.enrolltitleLabel.setText(_translate("MainWindow", "Enrolment Form", None))
        self.searchbyenLineEdit.setPlaceholderText(_translate("MainWindow", "Search by Enrolment No.", None))
        self.searchPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to search</p></body></html>", None))
        self.searchPushButton.setText(_translate("MainWindow", "Search", None))
        self.submitPushButton.setText(_translate("MainWindow", "Submit", None))
        self.aadhaarLabel.setText(_translate("MainWindow", "Aadhaar No.", None))
        self.fullnameLabel.setText(_translate("MainWindow", "Full Name", None))
        self.fathernameLabel.setText(_translate("MainWindow", "Father\'s Name", None))
        self.mothernameLabel.setText(_translate("MainWindow", "Mother\'s Name", None))
        self.sexLabel.setText(_translate("MainWindow", "Sex", None))
        self.sexComboBox.setItemText(0, _translate("MainWindow", "Male", None))
        self.sexComboBox.setItemText(1, _translate("MainWindow", "Female", None))
        self.dateofbirthLabel.setText(_translate("MainWindow", "Date of Birth", None))
        self.dateofbirthDateEdit.setDisplayFormat(_translate("MainWindow", "dd/mm/yyyy", None))
        self.addressLabel.setText(_translate("MainWindow", "Residential Address", None))
        self.emailLabel.setText(_translate("MainWindow", "Email", None))
        self.mobileLabel.setText(_translate("MainWindow", "Mobile", None))
        self.bloodgroupLabel.setText(_translate("MainWindow", "Blood Group", None))
        self.enrolmentnumLabel.setText(_translate("MainWindow", "Enrolment No.", None))
        self.bankdetailsLabel.setText(_translate("MainWindow", "Bank Details", None))
        self.accountnumLabel.setText(_translate("MainWindow", "Account No.", None))
        self.bankbranchLabel.setText(_translate("MainWindow", "Branch", None))
        self.isfccodeLabel.setText(_translate("MainWindow", "ISFC code", None))
        self.accountnameLabel.setText(_translate("MainWindow", "Name", None))
        self.banknameLabel.setText(_translate("MainWindow", "Bank Name", None))
        self.unitLabel.setText(_translate("MainWindow", "Unit", None))
        self.institutionLabel.setText(_translate("MainWindow", "Institution", None))
        self.mytab.setTabText(self.mytab.indexOf(self.Enroll), _translate("MainWindow", "Enrolment form", None))
        self.mytab.setTabToolTip(self.mytab.indexOf(self.Enroll), _translate("MainWindow", "Enrolment form for NCC", None))
        self.mytab.setTabText(self.mytab.indexOf(self.Yoga), _translate("MainWindow", "Yoga Form", None))
        self.mytab.setTabToolTip(self.mytab.indexOf(self.Yoga), _translate("MainWindow", "Do YOGA everyday", None))
        self.mytab.setTabText(self.mytab.indexOf(self.Attendence), _translate("MainWindow", "Attendence", None))
        self.mytab.setTabToolTip(self.mytab.indexOf(self.Attendence), _translate("MainWindow", "Not eligible", None))

        self.submitPushButton.clicked.connect(self.get_enroll_form_data)
        self.searchPushButton.clicked.connect(self.display)


        # self.sexComboBox.setEditable(True)
        # self.sexComboBox.lineEdit().setReadOnly(True);
        # self.sexComboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter);

    def display(self):
        obj=ENROLMENT_FORM.enroll()

        tuple=obj.search_by_enrolmentid(self.searchbyenLineEdit.displayText())
        dateyear=int(tuple[14][6]+tuple[14][7]+tuple[14][8]+tuple[14][9])
        datemonth=int(tuple[14][3]+tuple[14][4])
        dateday=int(tuple[14][0]+tuple[14][1])
        self.enrolmentnumLineEdit.setText(tuple[0]);
        self.aadhaarLineEdit.setText(str(tuple[1]));
        self.fullnameLineEdit.setText(tuple[2]);
        self.fathernameLineEdit.setText(tuple[5]);
        self.mothernameLineEdit.setText(tuple[8]);
        self.sexComboBox.setItemText(1,tuple[15])
        self.dateofbirthDateEdit.setDate(QtCore.QDate(dateyear,datemonth,dateday))
        self.addressLineEdit.setText(tuple[17])
        self.emailLineEdit.setText(tuple[18]);
        self.mobileLineEdit.setText(str(tuple[19]));
        self.bloodgroupLineEdit.setText(tuple[16]);
        self.banknameLineEdit.setText(tuple[20]);
        self.bankbranchLineEdit.setText(tuple[21]);
        self.accountnameLineEdit.setText(tuple[22]);
        self.accountnumLineEdit.setText(str(tuple[23]));
        self.isfccodeLineEdit.setText(tuple[24]);
        self.institutionLineEdit.setText(tuple[25]);
        self.unitLineEdit.setText(tuple[26]);


    def get_enroll_form_data(self):
        self.enrolmentnum = self.enrolmentnumLineEdit.displayText();
        self.aadhaarnum = self.aadhaarLineEdit.displayText()
        self.fullname = self.fullnameLineEdit.displayText()
        self.fathername = self.fathernameLineEdit.displayText()
        self.mothername = self.mothernameLineEdit.displayText()
        self.sex = self.sexComboBox.currentText();
        self.dateofbirth = self.dateofbirthDateEdit.text();
        self.address = self.addressLineEdit.toPlainText()
        self.email = self.emailLineEdit.displayText()
        self.mobilenum = self.mobileLineEdit.displayText()
        self.bloodgroup = self.bloodgroupLineEdit.displayText()
        self.bankname = self.banknameLineEdit.displayText()
        self.bankbranch = self.bankbranchLineEdit.displayText()
        self.accountname = self.accountnameLineEdit.displayText()
        self.accountnum = self.accountnumLineEdit.displayText()
        self.isfccode = self.isfccodeLineEdit.displayText()
        self.institutionname = self.institutionLineEdit.displayText()
        self.unit = self.unitLineEdit.displayText()
        obj = ENROLMENT_FORM.enroll()
        obj.enrol_student(self.enrolmentnum, self.aadhaarnum, self.fullname, '', '', self.fathername, '', '',
                          self.mothername, '', '', '', '', '',
                          self.dateofbirth, self.sex, self.bloodgroup, self.address
                          , self.email, self.mobilenum, self.bankname, self.bankbranch, self.accountname,
                          self.accountnum, self.isfccode
                          , self.institutionname
                          , self.unit)




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())