from numpy.distutils.system_info import umfpack_info
import sqlite3
from userinterface import *  ;
from PyQt4 import QtCore, QtGui
import ENROLMENT_FORM

#
# try:
#     _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s
#
# try:
#     _encoding = QtGui.QApplication.UnicodeUTF8
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig)
#


class enrollment(object):

    def __init__(self,ui):
        self.ui = ui ;
        self.ui.submitPushButton.clicked.connect(self.get_enroll_form_data);
        self.ui.searchPushButton.clicked.connect(self.display);


    def display(self):
        obj=ENROLMENT_FORM.enroll()

        tuple=obj.search_by_enrolmentid(self.ui.searchbyenLineEdit.displayText())
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
        self.ifsccodeLineEdit.setText(tuple[24]);
        self.institutionLineEdit.setText(tuple[25]);
        self.unitLineEdit.setText(tuple[26]);



    def get_enroll_form_data(self):
        self.enrolmentnum = self.ui.enrolmentnumLineEdit.displayText();
        self.aadhaarnum = self.ui.aadhaarLineEdit.displayText()
        self.rank = self.ui.rankLineEdit.displayText() ;
        self.fullname = self.ui.fullnameLineEdit.displayText()
        self.fathername = self.ui.fathernameLineEdit.displayText()
        self.mothername = self.ui.mothernameLineEdit.displayText()
        self.sex = self.ui.sexComboBox.currentText();
        self.dateofbirth = self.ui.dateofbirthDateEdit.text();
        self.address = self.ui.addressTextEdit.toPlainText()
        self.email = self.ui.emailLineEdit.displayText()
        self.mobilenum = self.ui.mobileLineEdit.displayText()
        self.bloodgroup = self.ui.bloodgroupLineEdit.displayText()
        self.bankname = self.ui.banknameLineEdit.displayText()
        self.bankbranch = self.ui.bankbranchLineEdit.displayText()
        self.accountname = self.ui.accountnameLineEdit.displayText()
        self.accountnum = self.ui.accountnumLineEdit.displayText()
        self.ifsccode = self.ui.ifsccodeLineEdit.displayText()
        self.institutionname = self.ui.institutionLineEdit.displayText()
        self.unit = self.ui.unitLineEdit.displayText()
        obj = ENROLMENT_FORM.enroll()
        obj.create_table()
        obj.enrol_student(self.enrolmentnum,self.rank, self.aadhaarnum, self.fullname, '', '', self.fathername, '', '',
                          self.mothername, '', '', '', '', '',
                          self.dateofbirth, self.sex, self.bloodgroup, self.address
                          , self.email, self.mobilenum, self.bankname, self.bankbranch, self.accountname,
                          self.accountnum, self.ifsccode
                          , self.institutionname
                          , self.unit)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


    myobj = enrollment(ui);







    MainWindow.show()

    sys.exit(app.exec_())

