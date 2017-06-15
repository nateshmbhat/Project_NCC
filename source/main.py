
import sqlite3
from PyQt4 import QtCore, QtGui
import ENROLMENT_FORM
from using_the_sqlite3 import Ui_MainWindow


class enrollment(object):

    def __init__(self,ui):
        self.ui = ui ;
        self.ui.submitPushButton.clicked.connect(self.get_enroll_form_data);
        self.ui.searchPushButton.clicked.connect(self.display);


    def display(self):
        obj=ENROLMENT_FORM.enroll()

        tuple=obj.search_by_enrolmentid(self.ui.searchbyenLineEdit.displayText())
        dateyear=int(tuple[15][6]+tuple[15][7]+tuple[15][8]+tuple[15][9])
        datemonth=int(tuple[15][3]+tuple[15][4])
        dateday=int(tuple[15][0]+tuple[15][1])
        self.ui.enrolmentnumLineEdit.setText(tuple[0]);
        self.ui.rankLineEdit.setText(tuple[1])
        self.ui.aadhaarLineEdit.setText(str(tuple[2]));
        self.ui.fullnameLineEdit.setText(tuple[3]);
        self.ui.fathernameLineEdit.setText(tuple[6]);
        self.ui.mothernameLineEdit.setText(tuple[9]);
        self.ui.sexComboBox.setItemText(1,tuple[16])
        self.ui.dateofbirthDateEdit.setDate(QtCore.QDate(dateyear,datemonth,dateday))
        self.ui.addressTextEdit.setText(tuple[18]);
        self.ui.emailLineEdit.setText(tuple[19]);
        self.ui.mobileLineEdit.setText(str(tuple[20]));
        self.ui.bloodgroupLineEdit.setText(tuple[17]);
        self.ui.banknameLineEdit.setText(tuple[21]);
        self.ui.bankbranchLineEdit.setText(tuple[22]);
        self.ui.accountnameLineEdit.setText(tuple[23]);
        self.ui.accountnumLineEdit.setText(str(tuple[24]));
        self.ui.ifsccodeLineEdit.setText(tuple[25]);
        self.ui.institutionLineEdit.setText(tuple[26]);
        self.ui.unitLineEdit.setText(tuple[27]);



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
