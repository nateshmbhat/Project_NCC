import ENROLMENT_FORM
import append_excel
import forms
from PyQt4 import QtCore, QtGui
from userinterface import Ui_MainWindow


class logic():
    def __init__(self):
        ENROLMENT_FORM.enroll().create_table()
        ui.insertcondition.clicked.connect(self.coninsert)
        ui.clearcondition.clicked.connect(self.conclear)
        ui.backcondition.clicked.connect(self.conback)
        ui.andcondition.clicked.connect(self.conand)
        ui.orcondition.clicked.connect(self.conor)
        ui.equalscondition.clicked.connect(self.conequals)
        ui.openbracecondition.clicked.connect(self.conopen)
        ui.closebracecondition.clicked.connect(self.conclose)
        ui.greatercondition.clicked.connect(self.congreater)
        ui.lessercondition.clicked.connect(self.conlesser)
        ui.querycondition.clicked.connect(self.conquery)
        ui.submitPushButton.clicked.connect(self.check_enrol_form_data);
        ui.searchPushButton.clicked.connect(self.display);

        self.sql = '';

        ui.enrolmentCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.enrolmentCheckBox))
        ui.rankCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.rankCheckBox))
        ui.aadhaarCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.aadhaarCheckBox))
        ui.sfnameCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.sfnameCheckBox))
        ui.ffnameCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.ffnameCheckBox))
        ui.mfnameCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.mfnameCheckBox))
        ui.sexCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.sexCheckBox))
        ui.bloodgroupCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.bloodgroupCheckBox))
        ui.emailCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.emailCheckBox))
        ui.mobileCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.mobileCheckBox))
        ui.addressCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.addressCheckBox))
        ui.dateofbirthCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.dateofbirthCheckBox))
        ui.institutionCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.institutionCheckBox))
        ui.unitCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.unitCheckBox))
        ui.banknameCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.banknameCheckBox))
        ui.bankbranchCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.bankbranchCheckBox))
        ui.accountnameCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.accountnameCheckBox))
        ui.accountnumCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.accountnumCheckBox))
        ui.ifsccodeCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.ifsccodeCheckBox))
        ui.selectallCheckBox.stateChanged.connect(self.queryselectall);
        ui.generate_excell_sheetPushButton.clicked.connect(self.fun)
        
        


    def fun(self):
        x = ui.entryBox.toPlainText()
        s = ''
        enrolno = []
        for i in x:
            if i is ' ':
                enrolno.append(s)
                s = ''
            else:
                s = s + i
        enrolno.append(s)
        print(enrolno)
        sql = """"""
        n = int(ui.comboBox.currentIndex())
        print(n)
        if n is 1:
            sql = forms.form1()
        elif n is 2:
            sql = forms.form2()
        elif n is 3:
            sql = forms.form3()
        elif n is 4:
            sql = forms.form4()
        elif n is 5:
            sql = forms.form5()
        elif n is 6:
            sql = forms.form6()
        elif n is 7:
            sql = forms.form7()
        elif n is 8:
            sql = forms.form8()
        for i in range(len(enrolno)):
            sql = sql + " enrolment_no=\"" + enrolno[i] + "\" "
            if i != len(enrolno) - 1:
                sql = sql + "or"
        print(sql)
        obj = ENROLMENT_FORM.enroll()
        tup = obj.execute(sql)
        print(tup)
        obj1 = append_excel.append()
        obj1.insert(tup, n)
        self.table1(tup,sql)




    def check_enrol_form_data(self):

        proceed = True;

        def set_margin_red_style(obj):

            try:
                obj.setStyleSheet('border-color:red;border-width:2px;border-style:groove;')
                obj.setPlaceholderText('Mandatory field')
            except:
                pass;


        for i in [ui.enrolmentnumLineEdit, ui.fullnameLineEdit, ui.fathernameLineEdit, ui.mothernameLineEdit,ui.addressTextEdit, ui.unitLineEdit]:

            if i == ui.addressTextEdit:
                if i.toPlainText() == '':
                    proceed = False;

                    set_margin_red_style(i)


            elif i.displayText() == '':

                proceed = False
                set_margin_red_style(i)



            else:
                i.setStyleSheet('')
                i.setPlaceholderText('')


        if proceed: #This runs only if all the non-null fields are filled.

            ui.addressTextEdit.setStyleSheet('')

            if len(ui.aadhaarLineEdit.displayText().strip())!=12:
                proceed=False;
                QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                          "\nValid Aadhaar Number should be 12 digits long.\n\n Please make sure that it's a valid 12 digit Aadhaar number",
                                          'OK');
                return ;

            if len(ui.mobileLineEdit.displayText().strip())!=10:
                proceed = False;
                QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                          '\n\n\nPlease Enter a Valid 10 digit Mobile number.',
                                          'OK');
                return


            else:
                proceed = True;
                self.get_enroll_form_data()


        else:
            QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                      '\nMandatory fields should not be empty.\n\nMake sure that all the mandatory fields are filled.',
                                      'OK');




    def queryselectall(self):

        if ui.selectallCheckBox.isChecked():

            ui.selectallCheckBox.setStyleSheet("""

            color:chartreuse;

            font-size:16pt;

            font-family:caladea;

            font-weight:bold;

            text-decoration:underline;

            """)

            for i in ui.checkboxFrame.findChildren(QtGui.QCheckBox):
                if i.objectName() != 'selectallCheckBox':
                    i.setChecked(False);
                    i.setDisabled(True);
                    i.setStyleSheet("""
                    color:gray;
                    font-size:10pt;
                    """)


        else:
            for i in ui.checkboxFrame.findChildren(QtGui.QCheckBox):
                i.setDisabled(False);
                i.setStyleSheet("#{}".format(i.objectName()) + """
                {
                color:white;
                font:13pt cambria ;
                font-weight:bold;
                }
                """ + "#{0}:hover".format(i.objectName()) + """
                {
                    text-decoration:underline;
                    font:15pt cambria;
                    color:yellow;
                }
                """);
            ui.selectallCheckBox.setStyleSheet("""
#selectallCheckBox{
font: 75 16pt "Caladea";
color:rgb(255, 170, 0);
font-weight:bold;
}

#selectallCheckBox:hover{
font: 75 12pt "Georgia";
color:rgb(255, 148, 241);
font-weight:bold;
}
        """)
    def querycheckboxes(self, obj):
        if obj.isChecked():
            obj.setStyleSheet("""
            color:chartreuse;font-size:14.5pt;
            font-weight:bold;
            text-decoration:underline;
            font-family:georgia;""")
        else:
            obj.setStyleSheet("#{}".format(obj.objectName()) + """
{
color:white;
font:13pt cambria ;
font-weight:bold;
}
""" + "#{0}:hover".format(obj.objectName()) + """
{
    text-decoration:underline;
    font:15pt cambria;
    color:yellow;
}
""");


    def display(self):

        obj = ENROLMENT_FORM.enroll()


        if ui.aadhaarnumRadioButton.isChecked():
            field = 'aadhar';
        elif ui.enrolmentnumRadioButton.isChecked():
            field = 'enrolment_no'

        tuple = obj.search_by_field(field ,ui.searchbyfieldLineEdit.displayText())
        dateyear = int(tuple[15][6] + tuple[15][7] + tuple[15][8] + tuple[15][9])
        datemonth = int(tuple[15][3] + tuple[15][4])
        dateday = int(tuple[15][0] + tuple[15][1])
        ui.enrolmentnumLineEdit.setText(tuple[0]);
        ui.rankComboBox.setCurrentIndex(ui.rankComboBox.findText(tuple[1]));
        ui.aadhaarLineEdit.setText(str(tuple[2]));
        ui.fullnameLineEdit.setText(tuple[3]);
        ui.fathernameLineEdit.setText(tuple[6]);
        ui.mothernameLineEdit.setText(tuple[9]);
        ui.sexComboBox.setCurrentIndex(ui.sexComboBox.findText(tuple[16]))
        ui.dateofbirthDateEdit.setDate(QtCore.QDate(dateyear, datemonth, dateday))
        ui.addressTextEdit.setText(tuple[18]);
        ui.emailLineEdit.setText(tuple[19]);
        ui.mobileLineEdit.setText(str(tuple[20]));
        ui.bloodgroupComboBox.setCurrentIndex(ui.bloodgroupComboBox.findText(tuple[17]));
        ui.banknameLineEdit.setText(tuple[21]);
        ui.bankbranchLineEdit.setText(tuple[22]);
        ui.accountnameLineEdit.setText(tuple[23]);
        ui.accountnumLineEdit.setText(str(tuple[24]));
        ui.ifsccodeLineEdit.setText(tuple[25]);
        ui.institutionComboBox.setCurrentIndex(ui.institutionComboBox.findText(tuple[26]))
        ui.unitLineEdit.setText(tuple[27]);




    def get_enroll_form_data(self):
        self.enrolmentnum = ui.enrolmentnumLineEdit.displayText();
        self.aadhaarnum = ui.aadhaarLineEdit.displayText()
        self.rank = ui.rankComboBox.currentText()
        self.fullname = ui.fullnameLineEdit.displayText()
        self.fathername = ui.fathernameLineEdit.displayText()
        self.mothername = ui.mothernameLineEdit.displayText()
        self.sex = ui.sexComboBox.currentText();
        self.dateofbirth = ui.dateofbirthDateEdit.text();
        self.address = ui.addressTextEdit.toPlainText()
        self.email = ui.emailLineEdit.displayText()
        self.mobilenum = ui.mobileLineEdit.displayText()
        self.bloodgroup = ui.bloodgroupComboBox.currentText()
        self.bankname = ui.banknameLineEdit.displayText()
        self.bankbranch = ui.bankbranchLineEdit.displayText()
        self.accountname = ui.accountnameLineEdit.displayText()
        self.accountnum = ui.accountnumLineEdit.displayText()
        self.ifsccode = ui.ifsccodeLineEdit.displayText()
        self.institutionname = ui.institutionLineEdit.displayText()
        self.unit = ui.unitLineEdit.displayText()
        obj = ENROLMENT_FORM.enroll()
        obj.create_table()
        obj.enrol_student(self.enrolmentnum, self.rank, self.aadhaarnum, self.fullname, '', '', self.fathername, '', '',
                          self.mothername, '', '', '', '', '',
                          self.dateofbirth, self.sex, self.bloodgroup, self.address
                          , self.email, self.mobilenum, self.bankname, self.bankbranch, self.accountname,
                          self.accountnum, self.ifsccode
                          , self.institutionname
                          , self.unit)



    def table1(self, res, msg):

        html3 = """

        <html>

        <head>

        <style type="text/css">



        table {

        border-collapse: collapse;

        text-align-last: center;

        vertical-align: middle;

        }

        table, td ,th{

            border: 1px solid black;

            text-align-last: center;

            height: 40px;

            text-align:center;



        }

        td{

            margin:3px 6px;

            text-align:center;



        }

        tr{

            background-color: white;

            text-align-last: center;

        }



        th{

            background-color: #7100b2;

            text-align-last: center;

            font-size: 120%;

            color: white;

        }

        """
        html3 = html3 + """</style>\n</head>\n<body>\n<table>\n<thead>\n"""
        msg1 = msg[7: msg.find('from')]
        print("done")
        i = 0
        mmsg = ""
        while (i < len(msg1)):
            if (msg1[i] == ","):
                html3 = html3 + "\n<th>" + mmsg + "</th>\n"
                mmsg = ""
            else:
                mmsg = mmsg + msg1[i]
            i = i + 1;
        html3 = html3 + "\n<th>" + mmsg + "</th>\n"
        html3 = html3 + "\n<thead>\n"
        for i in range(len(res)):
            html3 = html3 + "<tr>\n"
            for j in range(len(res[i])):
                html3 = html3 + "<td>" + str(res[i][j]) + "</td>\n"
            html3 = html3 + "</tr>\n"
        html3 = html3 + "</table>\n</body>\n</html>"
        ui.webView_2.setHtml(html3)



    def table(self, res, msg):

        html3 = """

        <html>

        <head>

        <style type="text/css">



        table {

        border-collapse: collapse;

        text-align-last: center;

        vertical-align: middle;

        }

        table, td ,th{

            border: 1px solid black;

            text-align-last: center;

            height: 40px;

            text-align:center;



        }

        td{
            margin:3px 6px;
            font-weight:bold;
            text-align:center;
            padding-left:2px;
            padding-right:2px;
        }
        

        tr{

            background-color: rgb(213, 213, 213);
           # background-color:transparent;
            text-align-last: center;
            color:black;

        }



        th{

            background-color: #7100b2;

            text-align-last: center;

            font-size: 120%;

            color: white;

        }

        """

        html3 = html3 + """</style>\n</head>\n<body>\n<table>\n<thead>\n"""
        msg1 = msg[7: msg.find('from')]
        print("done")
        i = 0
        mmsg = ""
        while (i < len(msg1)):
            if (msg1[i] == ","):
                html3 = html3 + "\n<th>" + mmsg + "</th>\n"
                mmsg = ""
            else:
                mmsg = mmsg + msg1[i]
            i = i + 1;
        html3 = html3 + "\n<th>" + mmsg + "</th>\n"
        html3 = html3 + "\n<thead>\n"
        for i in range(len(res)):
            html3 = html3 + "<tr>\n"
            for j in range(len(res[i])):
                html3 = html3 + "<td>" + str(res[i][j]) + "</td>\n"
            html3 = html3 + "</tr>\n"

        html3 = html3 + "</table>\n</body>\n</html>"

        ui.webView.setHtml(html3)



    def conquery(self):
        sql = '';
        if ui.selectallCheckBox.isChecked():
            sql = "*";
        else:
            if ui.enrolmentCheckBox.isChecked(): sql += 'Enrolment_no,';
            if ui.rankCheckBox.isChecked(): sql += 'rank,'
            if ui.aadhaarCheckBox.isChecked(): sql += 'aadhar,'
            if ui.sfnameCheckBox.isChecked(): sql += 'student_name,'
            if ui.ffnameCheckBox.isChecked(): sql += 'fathers_name,'
            if ui.mfnameCheckBox.isChecked(): sql += 'mothers_name,'
            if ui.dateofbirthCheckBox.isChecked(): sql += 'date_of_birth,'
            if ui.sexCheckBox.isChecked(): sql += 'sex,'
            if ui.bloodgroupCheckBox.isChecked(): sql += 'blood_group,'
            if ui.addressCheckBox.isChecked(): sql += 'address,'
            if ui.emailCheckBox.isChecked(): sql += 'g_mail,'
            if ui.mobileCheckBox.isChecked(): sql += 'mobile,'
            if ui.banknameCheckBox.isChecked(): sql += 'bank_name,'
            if ui.bankbranchCheckBox.isChecked(): sql += 'branch,'
            if ui.accountnameCheckBox.isChecked(): sql += 'acc_name,'
            if ui.accountnumCheckBox.isChecked(): sql += 'acc_no,'
            if ui.ifsccodeCheckBox.isChecked(): sql += 'ifsc_code,'
            if ui.institutionCheckBox.isChecked(): sql += 'institution,'
            if ui.unitCheckBox.isChecked(): sql += 'units,'
            sql = sql.strip();
            if len(sql) and sql[-1] == ',': sql = sql[0:-1];
            if not sql:
                sql = '*';
                ui.selectallCheckBox.setChecked(True);
        sql1 = str(ui.conditionsentrylabel.text())
        if sql == '*':
            if sql1 != "":
                sql = """select Enrolment_no,rank,aadhar,student_name,fathers_name,
                mothers_name,date_of_birth ,sex,
                blood_group,address,g_mail,mobile,bank_name,branch,
                acc_name,acc_no,ifsc_code,institution,units from enrolment where """ + str(
                    ui.conditionsentrylabel.text())
            else:
                sql = """select Enrolment_no,rank,aadhar,student_name,fathers_name,
                                mothers_name,date_of_birth ,sex,
                                blood_group,address,g_mail,mobile,bank_name,branch,
                                acc_name,acc_no,ifsc_code,institution,units from enrolment"""

        else:
            sql = ("select " + sql + " from enrolment where " + str(
                ui.conditionsentrylabel.text())) if sql1 != "" else "select " + sql + " from enrolment ";
        if sql[7] == "*":
            sql = """select Enrolment_no,rank,aadhar,student_name,fathers_name,
            mothers_name,date_of_birth ,sex,
            blood_group,address,g_mail,mobile,bank_name,branch,
            acc_name,acc_no,ifsc_code,institution,units""" + sql[9:len(sql)]
            print(sql)

        tup = ENROLMENT_FORM.enroll().execute(sql)

        self.table(tup, sql)



    def congreater(self):
        ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + ">")
    def conlesser(self):
        ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + "<")
    def conequals(self):
        ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + "=")
    def conopen(self):
        ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + "(")
    def conclose(self):
        ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + ")")
    def conand(self):
        ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + " and ")
    def conor(self):
        ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + " or ")
    def conback(self):
        sql = ui.conditionsentrylabel.text().strip()
        ch = sql[-1]
        if sql[-2:] == 'or':
            ui.conditionsentrylabel.setText(sql[0:-2].strip())
        elif sql[-3:] == 'and':
            ui.conditionsentrylabel.setText(sql[0:-3].strip())

        elif ch in '(=)><':
            ui.conditionsentrylabel.setText(sql[0:len(sql) - 1])
        elif ch == "\"":
            ui.conditionsentrylabel.setText(sql[0:str(sql[0:-1]).rfind('"') - 1])
            self.conback();
        else:
            sql = sql.strip()
            if sql.rfind(' ') > 0:
                ui.conditionsentrylabel.setText(sql[0:sql.rfind(' ')])
            else:
                ui.conditionsentrylabel.setText('');




    def conclear(self):
        ui.conditionsentrylabel.setText("")

    flag = 0





    def coninsert(self):
        ch = ui.conditionlistcombobox.currentText()
        ch1 = ui.valuelineEdit.text()
        ch2 = ui.conditionsentrylabel.text().strip() + ' '
        if (len(ch2) > 3):
            if (ch2[len(ch2) - 1] == ' ' and (ch2[len(ch2) - 2] == 'd' or ch2[len(ch2) - 2] == 'r')) or (
                    ch2[len(ch2) - 1] == '(' and
                (ch2[len(ch2) - 2] == ' ' or ch2[len(ch2) - 2] == 'r' or ch2[len(ch2) - 2] == '(' or ch2[
                        len(ch2) - 2] == ')' or
                         ch2[len(ch2) - 2] == 'd')):
                print()

            else:
                QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                          '\nPlease use \'AND\' or \'OR\' between two conditions.',
                                          'OK');
                return
        if ch != "Select":
            if (ch1 != ""):
                if ch == "Aadhar" or ch == "Mobile" or ch == "Account_number":
                    if ch1.isdigit():
                        if ch == "Mobile":
                            if len(ch1) == 10:
                                ui.conditionsentrylabel.setText(
                                    ui.conditionsentrylabel.text() + ch + "=\"" + ch1 + "\"")
                            else:
                                QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                                          '\nMobile number should contains 10 numbers.',
                                                          'OK');
                        elif ch == "Aadhar":
                            if len(ch1) == 12:
                                ui.conditionsentrylabel.setText(
                                    ui.conditionsentrylabel.text() + ch + "=\"" + ch1 + "\"")
                            else:
                                QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                                          '\nAadhar number should contains 12 numbers.',
                                                          'OK');

                        else:
                            ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + ch + "=\"" + ch1 + "\"")

                    else:
                        QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                                  ch+' must contains only integral values.',
                                                  'OK');
                else:
                    ui.conditionsentrylabel.setText(
                        ui.conditionsentrylabel.text().strip() + ' ' + ch + "=\"" + ch1 + "\"")
            else:
                QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                          '\nPlease enter the values for the field selected.',
                                          'OK')
        else:
            QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                      '\nPlease select any one of the fields.',
                                      'OK')


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    myobj = logic();
    MainWindow.show()
    sys.exit(app.exec_())