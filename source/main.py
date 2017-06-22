from PyQt4.QtGui import QDialog, QPushButton
import ENROLMENT_FORM
from userinterface import Ui_MainWindow
from PyQt4 import QtCore, QtGui

class logic():
    def __init__(self):
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
        ui.submitPushButton.clicked.connect(self.get_enroll_form_data);
        ui.searchPushButton.clicked.connect(self.display);


        self.sql='';
        ui.enrolmentCheckBox.stateChanged.connect(lambda:self.querycheckboxes(ui.enrolmentCheckBox))
        ui.rankCheckBox.stateChanged.connect(lambda:self.querycheckboxes(ui.rankCheckBox))
        ui.aadhaarCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.aadhaarCheckBox))
        ui.sfnameCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.sfnameCheckBox))
        ui.ffnameCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.ffnameCheckBox))
        ui.mfnameCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.mfnameCheckBox))
        ui.sexCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.sexCheckBox))
        ui.bloodgroupCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.bloodgroupCheckBox))
        ui.emailCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.emailCheckBox))
        ui.mobileCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.mobileCheckBox))
        ui.addressCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.addressCheckBox))
        ui.dateofbirthCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.dateofbirthCheckBox))
        ui.institutionCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.institutionCheckBox))
        ui.unitCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.unitCheckBox))
        ui.banknameCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.banknameCheckBox))
        ui.bankbranchCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.bankbranchCheckBox))
        ui.accountnameCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.accountnameCheckBox))
        ui.accountnumCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.accountnumCheckBox))
        ui.ifsccodeCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.ifsccodeCheckBox))
        ui.selectallCheckBox.stateChanged.connect(self.queryselectall);


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
                if i.objectName() !='selectallCheckBox':
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




    def querycheckboxes(self ,obj):
        if obj.isChecked():
            obj.setStyleSheet("""
            color:chartreuse;font-size:14.5pt;
            font-weight:bold;
            text-decoration:underline;
            font-family:georgia;""")
        else:
            obj.setStyleSheet("#{}".format(obj.objectName())+"""
{
color:white;
font:13pt cambria ;
font-weight:bold;
}
"""+"#{0}:hover".format(obj.objectName())+"""
{
    text-decoration:underline;
    font:15pt cambria;
    color:yellow;
}
""");


    def display(self):
        obj=ENROLMENT_FORM.enroll()
        tuple=obj.search_by_enrolmentid(ui.searchbyfieldLineEdit.displayText())
        dateyear=int(tuple[15][6]+tuple[15][7]+tuple[15][8]+tuple[15][9])
        datemonth=int(tuple[15][3]+tuple[15][4])
        dateday=int(tuple[15][0]+tuple[15][1])
        ui.enrolmentnumLineEdit.setText(tuple[0]);
        ui.rankComboBox.setItemText(1,tuple[1])
        ui.aadhaarLineEdit.setText(str(tuple[2]));
        ui.fullnameLineEdit.setText(tuple[3]);
        ui.fathernameLineEdit.setText(tuple[6]);
        ui.mothernameLineEdit.setText(tuple[9]);
        ui.sexComboBox.setItemText(1,tuple[16])
        ui.dateofbirthDateEdit.setDate(QtCore.QDate(dateyear,datemonth,dateday))
        ui.addressTextEdit.setText(tuple[18]);
        ui.emailLineEdit.setText(tuple[19]);
        ui.mobileLineEdit.setText(str(tuple[20]));
        ui.bloodgroupComboBox.setCurrentIndex(ui.bloodgroupComboBox.findText(tuple[17]));
        ui.banknameLineEdit.setText(tuple[21]);
        ui.bankbranchLineEdit.setText(tuple[22]);
        ui.accountnameLineEdit.setText(tuple[23]);
        ui.accountnumLineEdit.setText(str(tuple[24]));
        ui.ifsccodeLineEdit.setText(tuple[25]);
        ui.institutionLineEdit.setText(tuple[26]);
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
        self.mobilenum =ui.mobileLineEdit.displayText()
        self.bloodgroup =ui.bloodgroupComboBox.currentText()
        self.bankname = ui.banknameLineEdit.displayText()
        self.bankbranch = ui.bankbranchLineEdit.displayText()
        self.accountname = ui.accountnameLineEdit.displayText()
        self.accountnum = ui.accountnumLineEdit.displayText()
        self.ifsccode = ui.ifsccodeLineEdit.displayText()
        self.institutionname = ui.institutionLineEdit.displayText()
        self.unit = ui.unitLineEdit.displayText()
        obj = ENROLMENT_FORM.enroll()
        obj.create_table()
        obj.enrol_student(self.enrolmentnum,self.rank, self.aadhaarnum, self.fullname, '', '', self.fathername, '', '',
                          self.mothername, '', '', '', '', '',
                          self.dateofbirth, self.sex, self.bloodgroup, self.address
                          , self.email, self.mobilenum, self.bankname, self.bankbranch, self.accountname,
                          self.accountnum, self.ifsccode
                          , self.institutionname
                          , self.unit)


    def table(self,res,msg):

        html3="""
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
            background-color: darkgray;
            text-align-last: center;
        }

        th{
            background-color: #7100b2;
            text-align-last: center;
            font-size: 120%;
            color: white;
        }
        """
        html3 = html3+"""</style>\n</head>\n<body>\n<table>\n<tr>\n"""
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
        html3 = html3 + "\n<tr>\n"
        for i in range(len(res)):
            html3 = html3 + "<tr>\n"
            for j in range(len(res[i])):
                html3 = html3 + "<td>" + str(res[i][j]) + "</td>\n"
            html3 = html3 + "</tr>\n"
        html3 = html3 + "</table>\n</body>\n</html>"
        ui.webView.setHtml(html3)


    def conquery(self):
        sql='';
        if ui.selectallCheckBox.isChecked():
            sql="*";
        else:
            if ui.enrolmentCheckBox.isChecked():sql+='Enrolment_no,';
            if ui.rankCheckBox.isChecked():sql+='rank,'
            if ui.aadhaarCheckBox.isChecked():sql+='aadhar,'
            if ui.sfnameCheckBox.isChecked():sql+='student_name,'
            if ui.ffnameCheckBox.isChecked():sql+='fathers_name,'
            if ui.mfnameCheckBox.isChecked():sql+='mothers_name,'
            if ui.dateofbirthCheckBox.isChecked():sql+='date_of_birth,'
            if ui.sexCheckBox.isChecked():sql+='sex,'
            if ui.bloodgroupCheckBox.isChecked():sql+='blood_group,'
            if ui.addressCheckBox.isChecked():sql+='address,'
            if ui.emailCheckBox.isChecked():sql+='g_mail,'
            if ui.mobileCheckBox.isChecked():sql+='mobile,'
            if ui.banknameCheckBox.isChecked():sql+='bank_name,'
            if ui.bankbranchCheckBox.isChecked():sql+='branch,'
            if ui.accountnameCheckBox.isChecked():sql+='acc_name,'
            if ui.accountnumCheckBox.isChecked():sql+='acc_no,'
            if ui.ifsccodeCheckBox.isChecked():sql+='ifsc_code,'
            if ui.institutionCheckBox.isChecked():sql+='institution,'
            if ui.unitCheckBox.isChecked():sql+='units,'


            sql = sql.strip();
            if len(sql) and sql[-1]==',': sql = sql[0:-1] ;


        sql1= str(ui.conditionsentrylabel.text())
        if sql=='*':
            if sql1!="":
                sql = """select Enrolment_no,rank,aadhar,student_name,fathers_name,
                mothers_name,date_of_birth ,sex,
                blood_group,address,g_mail,mobile,bank_name,branch,
                acc_name,acc_no,ifsc_code,institution,units from enrolment where """+ str(ui.conditionsentrylabel.text())
            else:
                sql = """select Enrolment_no,rank,aadhar,student_name,fathers_name,
                                mothers_name,date_of_birth ,sex,
                                blood_group,address,g_mail,mobile,bank_name,branch,
                                acc_name,acc_no,ifsc_code,institution,units from enrolment"""

        else:
            sql= ("select "+sql+" from enrolment where "+str(ui.conditionsentrylabel.text())) if sql1!="" else "select " + sql + " from enrolment " ;

        if sql[7]=="*":
            sql="""select Enrolment_no,rank,aadhar,student_name,fathers_name,
            mothers_name,date_of_birth ,sex,
            blood_group,address,g_mail,mobile,bank_name,branch,
            acc_name,acc_no,ifsc_code,institution,units"""+sql[9:len(sql)]
            print(sql)
        tup=ENROLMENT_FORM.enroll().execute(sql)
        self.table(tup,sql)
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
        sql=ui.conditionsentrylabel.text().strip()
        ch = sql[-1]
        if sql[-2:]=='or':ui.conditionsentrylabel.setText(sql[0:-2].strip())
        elif sql[-3:] =='and' :ui.conditionsentrylabel.setText(sql[0:-3].strip())

        elif ch in '(=)><':
            ui.conditionsentrylabel.setText(sql[0:len(sql)-1])
        elif ch=="\"":
            ui.conditionsentrylabel.setText(sql[0:str(sql[0:-1]).rfind('"')-1])
            self.conback();
        else:
            sql= sql.strip()
            if sql.rfind(' ')>0:ui.conditionsentrylabel.setText(sql[0:sql.rfind(' ')])
            else : ui.conditionsentrylabel.setText('');
            # for i in range(len(sql)-1,3,-1):
                # if (sql[i]=='r' and sql[i-1]=='o') or (sql[i]=='d' and sql[i-1]=='n' and sql[i-2]=='a') or sql[i]=='(' or sql[i]==')' or sql[i]=='=' or sql[i]=='>' or sql[i]=='<'or sql[i]==' ':
                #     ui.conditionsentrylabel.setText(sql[0:i])
                #     break;
                # elif i>5:
                #     ui.conditionsentrylabel.setText("")


    def conclear(self):
        ui.conditionsentrylabel.setText("")
    flag=0


    def coninsert(self):
        ch=ui.conditionlistcombobox.currentText()
        ch1=ui.valuelineEdit.text()
        ch2=ui.conditionsentrylabel.text().strip()+' '
        if(len(ch2)>3):
            if (ch2[len(ch2) - 1] == ' ' and (ch2[len(ch2) - 2] == 'd' or ch2[len(ch2) - 2] == 'r')) or (ch2[len(ch2) - 1] == '(' and
                    (ch2[len(ch2) - 2] == ' ' or ch2[len(ch2) - 2] == 'r' or ch2[len(ch2) - 2] == '(' or ch2[len(ch2) - 2] == ')' or
                             ch2[len(ch2) - 2] == 'd')):
                print()
            else:
                return
        if ch!="Select" :
            if(ch1 != ""):
                if ch=="Aadhar" or ch=="Mobile" or ch=="Account_number":
                    if ch1.isdigit():
                        if ch=="Mobile":
                            if len(ch1)==10:
                                ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + ch + "=\"" + ch1 + "\"")
                            else:
                                print("Mobile number should contains 10 numbers")
                        elif ch=="Aadhar":
                            if len(ch1)==12:
                                ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + ch + "=\"" + ch1 + "\"")
                            else:
                                print("Aadhar number should contains 10 numbers")

                        else:
                            ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + ch + "=\"" + ch1 + "\"")

                    else:
                        ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text() + ch + "=\"" + ch1 + "\"")
                else:
                    ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text().strip()+' '+ ch + "=\"" + ch1 + "\"")
            else:
                print("Please enter the values for the field selected")
        else:
            print("Please select any one of the fields")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    myobj = logic();
    MainWindow.show()

    sys.exit(app.exec_())