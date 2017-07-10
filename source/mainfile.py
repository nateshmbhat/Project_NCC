import pandas as pd
import ENROLMENT_FORM
import os
from tempfile import TemporaryFile
import openpyxl
from userinterface import Ui_MainWindow, _fromUtf8
from PyQt4 import QtCore, QtGui, QtWebKit
import sqlite3
import shutil
import forms
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

from tempfile import TemporaryFile
from openpyxl import Workbook

class append:
    CADET_DETAILS = ['Enrolment_Number', 'Aadhar_Number', 'student_Name', "Fathers_Name", "Mothers_Name", 'Sex',
                     'Date_Of_Birth', 'Address', 'Email', 'Mobile_Number', 'Blood_Group', 'Institution',
                     'Unit']
    YOGA_DAY = ['Rank', 'Student_name', "Fathers_Name", 'Unit', 'Institution', 'Date_Of_Birth', 'Remarks']
    Enrolment_Nominal_roll = ['Unit', 'Enrolment_Number', 'Rank', 'Student_name', "Fathers_name",
                              "Date_of_Birth", "Institution", 'Address', 'Mobile', 'Aadhar',
                              'Bank_Name', 'Branch', 'IFSC_code', 'Account_Name', 'Account_Number', 'MICR',
                              'Certificate', 'Camps_Attended', 'Extra_Curricular_Activities',
                              'Special_Achievements', 'Email', 'Blood Blood_Group', 'Remarks', 'course grading']
    Camp_Nominal_roll = ['Enrolment_Number', 'Aadhar_Number', 'Rank', 'student_Name', "Fathers_Name", 'Address',
                         'Institution', 'Vegitarian', 'Bank_Name', 'Branch',
                         'Account_Name', 'Account_Number', 'IFSC_Code',
                         'Year of training', 'Able to swim or not']
    Scholarship_NR = ['Enrolment_Number', 'Rank', 'Unit', 'Institution', 'Bank_Name', 'Branch', 'Account_Name',
                      'Account_Number', 'IFSC_Code', 'MICR'
        , 'SC', 'ST', 'OBC', 'Period of Trg', 'Examination on pass Date/Month/Year',
                      'Science,Arts,Commerce in case of stream SD/SW cadets only', 'Maximum marks', 'Minimum marks',
                      'Percentage', '10% Bonus marks secured to SC/ST/OBC applicant', '% of marks', 'Position obtained']
    A_certe_NR_for_High_school_JDJW = ['Enrolment_Number', 'Rank', 'student_Name',
                                       "Fathers_Name", "Date_Of_Birth", 'Enrol_Date',
                                       'Date of Discharge', 'Details of Camps attended',
                                       'Parade Attendance% Year I', 'Parade Attendance% Year II',
                                       'Part-I-Drill written(30)', 'Part-I-Drill practical(60)',
                                       'Part-I-Drill Total(90)', 'Part-II:WT Written(40)',
                                       'Part-II:WT Practical(20)', 'Part-II:WT Total(60)',
                                       'Part-III:Misc written(200)', 'Part-IV:Spl Subjects written(115)',
                                       'Part-IV:Spl Subjects practical(30)', 'Part-IV:Spl Subjects Total(150)',
                                       'Grand Total(500)', 'Grading',
                                       'Signature of cadet: Written common subject',
                                       'Signature of cadet: Written Spl subject',
                                       'Signature of cadet: Practical']
    B_certe_NR_SDSW = ['Enrolment_Number.', 'Rank', 'student_Name', "Fathers_Name",
                       "Date_Of_Birth", 'Enrol_Date', 'Photo'
        , 'Date of Discharge', 'Details of Camps attended',
                       'Parade Attendance% Year I', 'Parade Attendance% Year II',
                       'Part-I-Drill written(10)', 'Part-I-Drill practical(80)', 'Part-I-Drill Total(90)',
                       'Part-II:WT Written(35)', 'Part-II:WT Practical(25)', 'Part-II:WT Total(60)',
                       'Part-III:Misc written(200)', 'Part-IV:Spl Subjects written(105)',
                       'Part-IV:Spl Subjects practical(45)', 'Part-IV:Spl Subjects Total(150)',
                       'Bonus Marks Certific', 'Grand Total(500)', 'Grading',
                       'Signature of cadet: Written common subject', 'Signature of cadet: Written Spl subject',
                       'Signature of cadet: Practical']
    C_certe_NR_SDSW = ['Enrolment_Number.', 'Rank', 'student_Name', "Fathers_Name",
                       "Date_Of_Birth", 'Enrol_Date', 'Photo',
                       'Date of Discharge', 'Details of Camps attended',
                       'Parade Attendance% III Year', 'Part-I-Drill written(10)',
                       'Part-I-Drill practical(50)', 'Part-I-Drill Total(60)', 'Part-II:WT Written(10)',
                       'Part-II:WT Practical(55)', 'Part-II:WT Total(65)', 'Part-III:Misc written(225)',
                       'Part-IV:Spl Subjects written(105)', 'Part-IV:Spl Subjects practical(45)',
                       'Part-IV:Spl Subjects Total(150)', 'Grand Total(500)', 'Bonus Marks max-Total-50',
                       'Grading', 'Signature of cadet: Written common subject',
                       'Signature of cadet: Written Spl subject', 'Signature of cadet: Practical']

    def insert(self,tup,n,filename):
        book = Workbook()
        sheet = book.active
        if n==1:
            for i in range(len(self.CADET_DETAILS)):
                sheet.cell(row=1, column=i + 1).value = self.CADET_DETAILS[i]
        elif n==2:
            for i in range(len(self.YOGA_DAY)):
                sheet.cell(row=1, column=i + 1).value = self.YOGA_DAY[i]
        elif n==3:
            for i in range(len(self.Enrolment_Nominal_roll)):
                sheet.cell(row=1, column=i + 1).value = self.Enrolment_Nominal_roll[i]
        elif n==4:
            for i in range(len(self.Camp_Nominal_roll)):
                sheet.cell(row=1, column=i + 1).value = self.Camp_Nominal_roll[i]
        elif n==5:
            for i in range(len(self.Scholarship_NR)):
                sheet.cell(row=1, column=i + 1).value = self.Scholarship_NR[i]
        elif n==6:
            for i in range(len(self.A_certe_NR_for_High_school_JDJW)):
                sheet.cell(row=1, column=i + 1).value = self.A_certe_NR_for_High_school_JDJW[i]
        elif n==7:
            for i in range(len(self.B_certe_NR_SDSW)):
                sheet.cell(row=1, column=i + 1).value = self.B_certe_NR_SDSW[i]
        elif n==8:
            for i in range(len(self.C_certe_NR_SDSW)):
                sheet.cell(row=1, column=i + 1).value = self.C_certe_NR_SDSW[i]

        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.cell(row=i + 2, column=j+1).value= str(tup[i][j])
        book.save(filename)
        book.save(TemporaryFile())
    def insertupdate(self,tup,n,filename):
        book=openpyxl.load_workbook(filename)
        sheet = book.active
        for i in tup:
            sheet.append(i)
        book.save(filename)
        book.save(TemporaryFile())

class logic():
    def __init__(self):
        ui.save_data_excelPushButton.hide()
        ENROLMENT_FORM.enroll().create_table_marks_A_cert()

        ENROLMENT_FORM.enroll().create_table_marks_B_cert()

        ENROLMENT_FORM.enroll().create_table_marks_C_cert()
        ENROLMENT_FORM.enroll().create_table_Enrolment()

        ui.NullcertRadioButton.setChecked(True)

        ui.vegRadioButton.setChecked(True)

        ui.AACCheckBox.clicked.connect(self.checklogic)

        ui.NICCheckBox.clicked.connect(self.checklogic)

        ui.CATCCheckBox.clicked.connect(self.checklogic)

        ui.NULLCampsCheckBox.clicked.connect(self.checklogicnull)

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

        ui.submitPushButton.clicked.connect(self.check_enrol_form_data)

        ui.enrolPushButton.pressed.connect(self.enrol_button_pressed)

        ui.aadhaarnumRadioButton.toggled.connect(self.enrol_adhaar_radio_change)

        self.sql = ''

        self.candidphoto=''


        ui.selectpicturePushButton.clicked.connect(self.picselect)

        ui.bloodgroupqueryComboBox.hide()

        ui.institutionqueryComboBox.hide()

        ui.rankqueryComboBox.hide()

        ui.sexqueryComboBox.hide()

        ui.datequeryDateEdit.hide()

        ui.mobileLineEdit.setValidator(QtGui.QDoubleValidator())

        ui.accountnumLineEdit.setValidator(QtGui.QDoubleValidator())

        ui.micrLineEdit.setValidator(QtGui.QDoubleValidator())

        ui.micrLineEdit.setValidator(QtGui.QDoubleValidator())

        ui.aadhaarLineEdit.setValidator(QtGui.QDoubleValidator())

        ui.vegRadioButton.setChecked(True)

        ui.NullcertRadioButton.setChecked(True)

        ui.enrolmentCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.enrolmentCheckBox))

        ui.searchPushButton.clicked.connect(lambda :self.display(ui.searchPushButton))

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

        ui.specialAchievementsCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.specialAchievementsCheckBox))

        ui.extraCurricularActivitiesCheckBox.stateChanged.connect(lambda :self.querycheckboxes(ui.extraCurricularActivitiesCheckBox))

        ui.remarksCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.remarksCheckBox))

        ui.micrCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.micrCheckBox))

        ui.enrollDateCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.enrollDateCheckBox))

        ui.campsAttendedCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.campsAttendedCheckBox))

        ui.vegitarianCheckBox.stateChanged.connect(lambda: self.querycheckboxes(ui.vegitarianCheckBox))

        ui.selectallCheckBox.stateChanged.connect(self.queryselectall)

        ui.conditionlistcombobox.currentIndexChanged.connect(self.conditionscomboboxlogic)

        ui.saveExelPushButton.clicked.connect(self.fun)

        ui.vegRadioButton.setChecked(True)

        ui.NullcertRadioButton.setChecked(True)

        if not os.path.exists(r'candidate photos'):
            os.mkdir(r'candidate photos')
        ui.openPushButton.clicked.connect(self.openuploaddata)

        ui.savedataPushButton.clicked.connect(self.saveuploadeddata)

        ui.save_data_excelPushButton.clicked.connect(self.saveexceluploadeddata)

        ui.typecomboBox.currentIndexChanged.connect(self.typecomboboxlogic)

        ui.appendDataPushButton.clicked.connect(self.appenddata)

        ui.updateExelPushButton.clicked.connect(self.fun1)

    def typecomboboxlogic(self):
        if ui.typecomboBox.currentText()=="Select Type" or ui.typecomboBox.currentText()=="Add Camps" or ui.typecomboBox.currentText()=="Add Remarks" or ui.typecomboBox.currentText()=="Add Extra Activities":
            ui.save_data_excelPushButton.hide()
        else:
            ui.save_data_excelPushButton.show()

    def appenddata(self):
        check=[]
        if ui.typecomboBox.currentText() == "Upload Marks(A)":
            check = "select * from A_cert_marks where institution='"+ui.institutionuploaddatacomboBox.currentText()+"'"
        if ui.typecomboBox.currentText() == "Upload Marks(B)":
            check = "select * from B_cert_marks where institution='" + ui.institutionuploaddatacomboBox.currentText() + "'"
        if ui.typecomboBox.currentText() == "Upload Marks(C)":
            check = "select * from C_cert_marks where institution='" + ui.institutionuploaddatacomboBox.currentText() + "'"
        tup = ENROLMENT_FORM.enroll().execute(check)
        print(tup)

        data = []
        for i in range(len(self.lineEditObjectnames)):
            data.append([])
            for j in range(len(self.lineEditObjectnames[i])):
                txt = self.lineEdit[i][j].text()
                data[i].append(txt)
        for i in range(len(data)):
            flag=0
            sql=""
            for k in range(len(data)):
                if len(data[k]) < 1:
                    continue
                for l in range(len(tup)):
                    if tup[l][0] == data[k][0]:
                        flag=1
            if flag==0:
                if len(data[i]) < 1:
                    continue
                if ui.typecomboBox.currentText() == "Upload Marks(A)":
                    sql = "insert into A_cert_marks values("
                if ui.typecomboBox.currentText() == "Upload Marks(B)":
                    sql = "insert into B_cert_marks values("
                if ui.typecomboBox.currentText() == "Upload Marks(C)":
                    sql = "insert into C_cert_marks values("

                for j in range(len(data[i])):
                    sql = sql + "'" + data[i][j] + "',"
                sql = sql + "'" + ui.institutionuploaddatacomboBox.currentText() + "')"
                ENROLMENT_FORM.enroll().insertionexecute(sql)
                print(sql)
            else:
                if len(data[i]) < 1:
                    continue
                if ui.typecomboBox.currentText() == "Upload Marks(A)":
                    ENROLMENT_FORM.enroll().delete_by_Enrolment("A_cert_marks",data[i][0])
                if ui.typecomboBox.currentText() == "Upload Marks(B)":
                    ENROLMENT_FORM.enroll().delete_by_Enrolment("B_cert_marks", data[i][0])
                if ui.typecomboBox.currentText() == "Upload Marks(C)":
                    ENROLMENT_FORM.enroll().delete_by_Enrolment("C_cert_marks", data[i][0])

                if ui.typecomboBox.currentText() == "Upload Marks(A)":
                    sql = "insert into A_cert_marks values("
                if ui.typecomboBox.currentText() == "Upload Marks(B)":
                    sql = "insert into B_cert_marks values("
                if ui.typecomboBox.currentText() == "Upload Marks(C)":
                    sql = "insert into C_cert_marks values("

                for j in range(len(data[i])):
                    sql = sql + "'" + data[i][j] + "',"
                sql = sql + "'" + ui.institutionuploaddatacomboBox.currentText() + "')"
                ENROLMENT_FORM.enroll().insertionexecute(sql)
                print(sql)

    def saveuploadeddata(self):
        check = []
        if ui.typecomboBox.currentText() == "Upload Marks(A)":
            check = "select * from A_cert_marks where institution='" + ui.institutionuploaddatacomboBox.currentText() + "'"
        if ui.typecomboBox.currentText() == "Upload Marks(B)":
            check = "select * from B_cert_marks where institution='" + ui.institutionuploaddatacomboBox.currentText() + "'"
        if ui.typecomboBox.currentText() == "Upload Marks(C)":
            check = "select * from C_cert_marks where institution='" + ui.institutionuploaddatacomboBox.currentText() + "'"
        tup = ENROLMENT_FORM.enroll().execute(check)
        print(tup)

        data=[]
        for i in range(len(self.lineEditObjectnames)):
            data.append([])
            for j in range(len(self.lineEditObjectnames[i])):
                txt=self.lineEdit[i][j].text()
                data[i].append(txt)
        for i in range(len(data)):
            if len(data[i])<1:
                continue
            for j in range(len(tup)):
                if tup[j][0]==data[i][0]:
                    QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                              'Marks for some enrolment numbers already exist \nIf you want to add\nplease use append.',
                                              'OK')
                    return
        sql=""
        for i in range(len(data)):
            if ui.typecomboBox.currentText() == "Upload Marks(A)":
                sql = "insert into A_cert_marks values("
            if ui.typecomboBox.currentText() == "Upload Marks(B)":
                sql = "insert into B_cert_marks values("
            if ui.typecomboBox.currentText() == "Upload Marks(C)":
                sql = "insert into C_cert_marks values("
            if len(data[i])<1:
                continue
            for j in range(len(data[i])):
                sql=sql+"'"+data[i][j]+"',"
            sql=sql+"'"+ui.institutionuploaddatacomboBox.currentText()+"')"
            ENROLMENT_FORM.enroll().insertionexecute(sql)
            print(sql)

    def saveexceluploadeddata(self):
        self.name=QtGui.QFileDialog.getSaveFileName(directory="C:\\Users\ADMIN\Documents", caption="Save File", filter=".xlsx")
        data=[]
        if ui.typecomboBox.currentText()=="Upload Marks(A)":
            self.book = openpyxl.load_workbook('A_CERTIFICATES.xlsx')
        elif ui.typecomboBox.currentText()=="Upload Marks(B)":
            self.book = openpyxl.load_workbook('B_CERTIFICATES.xlsx')
        elif ui.typecomboBox.currentText()=="Upload Marks(C)":
            self.book = openpyxl.load_workbook('CC_CERTIFICATES.xlsx')
        if ui.typecomboBox.currentText()=="Upload Marks(A)":
            self.sheet = self.book.get_sheet_by_name('A')
        elif ui.typecomboBox.currentText()=="Upload Marks(B)":
            self.sheet = self.book.get_sheet_by_name('B')
        elif ui.typecomboBox.currentText()=="Upload Marks(C)":
            self.sheet = self.book.get_sheet_by_name('C')
        for i in range(len(self.lineEditObjectnames)):
            data.append([])
            for j in range(len(self.lineEditObjectnames[i])):
                txt=self.lineEdit[i][j].text()
                data[i].append(txt)


        for row in data:
            self.sheet.append(row)
        self.book.save(self.name)
        self.book.save(TemporaryFile())

    vali=valj=0
    label = []
    lineEdit = []
    lineEditObjectnames = []
    labelObjectnames = []
    def openuploaddata(self):

        for i in range(len(self.label)):
            self.label[i].hide()
        for i in range(len(self.lineEdit)):
            for j in range(len(self.lineEdit[i])):
                self.lineEdit[i][j].hide()
        self.label = []
        self.lineEdit = []
        self.lineEditObjectnames = []
        self.labelObjectnames = []
        if ui.institutionuploaddatacomboBox.currentText() == "Select Institution":
            QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                      'Select any one Instituon from combo box.',
                                      'OK')
        elif ui.typecomboBox.currentText() == "Select Type":
            QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                      'Select the Type of Data you want to upload.',
                                      'OK')
        else:
            sql="""select Enrolment_Number from enrolment where Institution='"""+ui.institutionuploaddatacomboBox.currentText()+"'"
            sql1 = """select Enrolment_Number,Rank,Student_Name,Fathers_name,Date_Of_Birth,Enrol_Date,Camps_Attended from enrolment where Institution='""" + ui.institutionuploaddatacomboBox.currentText() + "'"
            tup=ENROLMENT_FORM.enroll().execute(sql)
            tup1=ENROLMENT_FORM.enroll().execute(sql1)
            sql2=""

            if ui.typecomboBox.currentText() == "Upload Marks(A)":
                sql2 = """select Enrolment_Number from A_cert_marks where institution='""" + ui.institutionuploaddatacomboBox.currentText() + "'"
            elif ui.typecomboBox.currentText() == "Upload Marks(B)":
                sql2 = """select Enrolment_Number from B_cert_marks where institution='""" + ui.institutionuploaddatacomboBox.currentText() + "'"
            elif ui.typecomboBox.currentText() == "Upload Marks(C)":
                sql2 = """select Enrolment_Number from C_cert_marks where institution='""" + ui.institutionuploaddatacomboBox.currentText() + "'"
            self.tupple=ENROLMENT_FORM.enroll().execute(sql2)
            print(tup)
            print(tup1)
            print(self.tupple)
            self.labelheading3 = [['Enrolment_Number', 'Rool_Number', 'Rank               ', 'Student_Name', 'Fathers_name', 'Date_Of_Birth',
                           'Enrol_Date',  'Camps_Attended','Date_Of_Discharge','1 year','2 year','Written(30)',
                           'Practical(60)','Total(90)','Written(40)','Practical(20)','Total(60)','Written(200)','Written(115)',
                           'Practical(25)',"Total(150)",'Grand Total(500)','Grading'],
                                  ['Enrolment_Number', 'Rool_Number', 'Rank               ', 'Student_Name', 'Fathers_name', 'Date_Of_Birth',
                           'Enrol_Date', 'Camps_Attended', 'Date_Of_Discharge','1 year','2 year','Written(10)',
                           'Practical(80)','Total(90)','Written(35)','Practical(25)','Total(60)','Written(200)','Written(105)',
                           'Practical(45)',"Total(150)",'Total(25)','Grand Total(500)','Grading'],
                                  ['Enrolment_Number', 'Rool_Number', 'Rank               ', 'Student_Name', 'Fathers_name','Date_Of_Birth',
                                   'Enrol_Date', 'Camps_Attended', 'Date_Of_Discharge', '1 year', '2 year','Written(10)',
                                   'Practical(50)', 'Total(60)', 'Written(10)', 'Practical(55)', 'Total(65)',
                                   'Written(225)', 'Written(105)','Practical(45)', "Total(150)",'Total(50)','Grand Total(500)','Grading'],
                                  ["EnrolMent_Number",'Camps_attended'],["Enrolment_Number",'Extra Activities'],["Enrolment_Number",'Remarks']]
            self.labelheading1=[[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','Marks Obtained',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','Marks Obtained',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','Marks Obtained', ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
            self.labelheading2=[[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','Part-1:Drill',' ',' ','Part-2:WT',' ',' ','Part-3:Misc','Part-4:Spl Subjects',' ',' ',' ',' '],
                               [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','Part-1:Drill', ' ', ' ', 'Part-2:WT', ' ', ' ','Part-3:Misc', 'Part-4:Spl Subjects', ' ',' ', 'Bonus Marks(A-cert)', ' ', ' '],
                               [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', 'Part-1:Drill', ' ', ' ', 'Part-2:WT', ' ', ' ','Part-3:Misc', 'Part-4:Spl Subjects', ' ',' ', 'Bonus Marks(A-cert)', ' ', ' ']]

            self.position=ui.typecomboBox.currentIndex()-1

            i=j=0
            if len(tup)<1:
                QtGui.QMessageBox.warning(ui.Enrol, 'Message',
                                          'There is no one student in the institution '+ui.institutionuploaddatacomboBox.currentText()+'.',
                                          'OK')
                return
            else:
                if self.position == 0 or self.position == 1 or self.position == 2:
                    self.flag=0
                    for i in range(len(tup)+2):
                        self.flag=0
                        self.lineEdit.append([])
                        self.lineEditObjectnames.append([])
                        if i == 0:
                            for p in range(len(self.labelheading1[self.position])):
                                self.label.append(QtGui.QLabel(ui.uploaddatamainframe))
                                self.label[len(self.label) - 1].setStyleSheet(_fromUtf8("background-color:darkblue;\n"
                                                                                        "color:white;\n"
                                                                                        "font-size:30px;font-weight:bold;position:fixed;\n"
                                                                                        ""))
                                self.label[len(self.label) - 1].setObjectName(
                                    _fromUtf8("enrolmentuploaddataLabel" + str(i)))
                                self.label[len(self.label) - 1].setAlignment(QtCore.Qt.AlignCenter)
                                ui.gridLayout_12.addWidget(self.label[len(self.label) - 1], i, p, 1, 1)
                                self.label[len(self.label) - 1].setText(
                                    _translate("MainWindow", self.labelheading1[self.position][p], None))
                            continue
                        if i == 1:
                            for p in range(len(self.labelheading2[self.position])):
                                self.label.append(QtGui.QLabel(ui.uploaddatamainframe))
                                self.label[len(self.label) - 1].setStyleSheet(_fromUtf8("background-color:darkblue;\n"
                                                                                        "color:white;\n"
                                                                                        "font-size:25px;font-weight:bold;\n"
                                                                                        ""))
                                self.label[len(self.label) - 1].setObjectName(
                                    _fromUtf8("enrolmentuploaddataLabel" + str(i)))
                                self.label[len(self.label) - 1].setAlignment(QtCore.Qt.AlignCenter)
                                ui.gridLayout_12.addWidget(self.label[len(self.label) - 1], i, p, 1, 1)
                                self.label[len(self.label) - 1].setText(
                                    _translate("MainWindow", self.labelheading2[self.position][p], None))
                            continue
                        k=l=0
                        for k in range(len(tup)):
                            for l in range(len(self.tupple)):
                                if tup[k][0]==self.tupple[l][0]:
                                    self.flag=1
                                    sql3=""
                                    if ui.typecomboBox.currentText() == "Upload Marks(A)":
                                        sql3="select * from A_cert_marks where Enrolment_Number='" + tup[k][0] + "'"
                                    elif ui.typecomboBox.currentText() == "Upload Marks(B)":
                                        sql3 = "select * from B_cert_marks where Enrolment_Number='" + tup[k][0] + "'"
                                    elif ui.typecomboBox.currentText() == "Upload Marks(C)":
                                        sql3 = "select * from C_cert_marks where Enrolment_Number='" + tup[k][0] + "'"
                                    self.find=ENROLMENT_FORM.enroll().execute(sql3)
                                    break

                            if self.flag==1:
                                break
                        for j in range(len(self.labelheading3[self.position])):
                            if i == 2:
                                self.label.append(QtGui.QLabel(ui.scrollAreaWidgetContents_3))
                                self.label[len(self.label) - 1].setStyleSheet(_fromUtf8("background-color:darkblue;\n"
                                                                                        "color:white;\n"
                                                                                        "font-size:20px;font-weight:bold;\n"
                                                                                        ""))
                                self.label[len(self.label) - 1].setObjectName(
                                    _fromUtf8("enrolmentuploaddataLabel" + str(i)))
                                self.label[len(self.label) - 1].setAlignment(QtCore.Qt.AlignCenter)
                                ui.gridLayout_12.addWidget(self.label[len(self.label) - 1], i, j, 1, 1)
                                self.label[len(self.label) - 1].setText(
                                    _translate("MainWindow", self.labelheading3[self.position][j], None))
                            else:
                                self.lineEdit[i].append(QtGui.QLineEdit(ui.scrollAreaWidgetContents_3))
                                if self.labelheading3[self.position][j]=="Enrolment_Number":
                                    self.lineEdit[i][len(self.lineEdit[i]) - 1].setStyleSheet(
                                        _fromUtf8("background-color:darkorange;font-size:20px;font-weight:bold;"
                                                  "height:30px;color:white;"))
                                else:
                                    self.lineEdit[i][len(self.lineEdit[i]) - 1].setStyleSheet(
                                        _fromUtf8("background-color:darkgray;font-size:15px;font-weight:bold;height:30px;color:white;"))
                                self.lineEdit[i][len(self.lineEdit[i]) - 1].setObjectName(
                                    _fromUtf8("uploaddatalineEdit" + str(i)))

                                self.lineEdit[i][len(self.lineEdit[i]) - 1].setAlignment(QtCore.Qt.AlignCenter)

                                self.lineEditObjectnames[i].append("uploaddatalineEdit" + str(i))
                                ui.gridLayout_12.addWidget(self.lineEdit[i][len(self.lineEdit[i]) - 1], i, j, 1, 1)
                                if self.flag==1:
                                    if self.find[0][0]==tup1[i-1][0]:
                                        if self.find[0][j]!="":
                                            self.lineEdit[i][len(self.lineEdit[i]) - 1].setText(
                                                _translate("MainWindow", self.find[0][j], None))
                                        else:
                                            self.lineEdit[i][len(self.lineEdit[i]) - 1].setPlaceholderText(
                                                _translate("MainWindow", self.labelheading3[self.position][j], None))
                                else:
                                    if i < len(tup1) + 2:
                                        if j<len(tup1[i-2])+1:
                                            if self.labelheading3[self.position][j] == "Enrolment_Number":
                                                self.lineEdit[i][len(self.lineEdit[i]) - 1].setText(
                                                    _translate("MainWindow", tup1[i - 2][0], None))
                                                self.lineEdit[i][len(self.lineEdit[i]) - 1].setEnabled(False)
                                            elif self.labelheading3[self.position][j]!="Rool_Number":
                                                self.lineEdit[i][len(self.lineEdit[i]) - 1].setText(
                                                    _translate("MainWindow", tup1[i-2][j-1], None))
                                                self.lineEdit[i][len(self.lineEdit[i]) - 1].setEnabled(False)
                                        else:
                                            self.lineEdit[i][len(self.lineEdit[i]) - 1].setPlaceholderText(
                                                _translate("MainWindow",self.labelheading3[self.position][j], None))
                        if self.flag==1:
                            tup.pop(k)




                else:
                    for i in range(0,len(tup)):
                        self.lineEdit.append([])
                        self.lineEditObjectnames.append([])
                        for j in range(len(self.labelheading3[self.position])):
                            if i==0:
                                self.label.append(QtGui.QLabel(ui.scrollAreaWidgetContents_3))
                                self.label[len(self.label)-1].setStyleSheet(_fromUtf8("background-color:darkblue;\n"
                                                                      "color:white;\n"
                                                                      "font-size:25px;font-weight:bold;\n"
                                                                      ""))
                                self.label[len(self.label)-1].setObjectName(_fromUtf8("enrolmentuploaddataLabel" + str(i)))
                                self.label[len(self.label)-1].setAlignment(QtCore.Qt.AlignCenter)
                                ui.gridLayout_12.addWidget(self.label[len(self.label)-1], i, j, 1, 1)
                                self.label[len(self.label)-1].setText(_translate("MainWindow",self.labelheading3[self.position][j], None))
                            else:
                                if j==0:
                                    self.label.append(QtGui.QLabel(ui.scrollAreaWidgetContents_3))
                                    self.label[len(self.label)-1].setStyleSheet(_fromUtf8("background-color:darkorange;font-size:15px;font-weight:bold;"
                                                                          "height:30px;color:white;"))
                                    self.label[len(self.label)-1].setObjectName(_fromUtf8("enrolmentuploaddataLabel"+str(i)))
                                    self.labelObjectnames.append("enrolmentuploaddataLabel"+str(i))
                                    self.label[len(self.label) - 1].setAlignment(QtCore.Qt.AlignCenter)
                                    ui.gridLayout_12.addWidget(self.label[len(self.label)-1], i, j, 1, 1)
                                    self.label[len(self.label)-1].setText(_translate("MainWindow", tup[i][0], None))
                                else:
                                    self.lineEdit[i].append(QtGui.QLineEdit(ui.scrollAreaWidgetContents_3))
                                    self.lineEdit[i][len(self.lineEdit[i])-1].setStyleSheet(_fromUtf8("background-color:darkgray;font-size:15px;font-weight:bold;"
                                                                          "height:30px;color:white;"))
                                    self.lineEdit[i][len(self.lineEdit[i])-1].setObjectName(_fromUtf8("uploaddatalineEdit" + str(i)))
                                    self.lineEdit[i][len(self.lineEdit[i]) - 1].setAlignment(QtCore.Qt.AlignCenter)
                                    self.lineEditObjectnames[i].append("uploaddatalineEdit" + str(i))
                                    ui.gridLayout_12.addWidget(self.lineEdit[i][len(self.lineEdit[i])-1], i, j, 1, 1)
                                    self.lineEdit[i][len(self.lineEdit[i]) - 1].setPlaceholderText(
                                        _translate("MainWindow", self.labelheading3[self.position][j], None))

                spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
                ui.gridLayout_12.addItem(spacerItem16, i+1,j+1, 1, 1)
                spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                ui.gridLayout_12.addItem(spacerItem15, i+1, j+1, 1, 1)
                self.vali=i
                self.valj=j

    def conditionscomboboxlogic(self):
        text=ui.conditionlistcombobox.currentText()
        """if text=="Rank" or text=="Institution" or text=="Blood_Group" or text=="Sex" or text=="Enrol_Date" or text=="Date_Of_Birth":"""
        ui.rankqueryComboBox.hide()
        ui.institutionqueryComboBox.hide()
        ui.bloodgroupqueryComboBox.hide()
        ui.sexqueryComboBox.hide()
        ui.datequeryDateEdit.hide()
        ui.valuelineEdit.hide()
        if text=="Rank":
            ui.rankqueryComboBox.show()
        elif text=="Institution":
            ui.institutionqueryComboBox.show()
        elif text=="Blood_Group":
            ui.bloodgroupqueryComboBox.show()
        elif text=="Sex":
            ui.sexqueryComboBox.show()
        elif text=="Enrol_Date" or text=="Date_Of_Birth":
            ui.datequeryDateEdit.show()
        else:
            ui.valuelineEdit.show()

    def checklogicnull(self):
        ui.NICCheckBox.setChecked(False)
        ui.AACCheckBox.setChecked(False)
        ui.CATCCheckBox.setChecked(False)

    def checklogic(self):
        ui.NULLCampsCheckBox.setChecked(False)

    def enrol_button_pressed(self):
        ui.searchbyfieldLineEdit.clear()
        self.enable_form_elements();
        ui.submitPushButton.show()
    def fun1(self):
        if ui.comboBox.currentText()=="-Select":
            QtGui.QMessageBox.warning(ui.Enrol, 'Message',
                                      'Please select a form.',
                                      'OK')
            return
        if ui.entryBox.toPlainText()=="":
            QtGui.QMessageBox.warning(ui.Enrol, 'Message',
                                      'Please enter the enrolment numbers.',
                                      'OK')
            return
        self.formname=""
        self.formname = QtGui.QFileDialog.getOpenFileName(directory="C:\\Users\ADMIN\Documents", caption="Save File")
        if self.formname=="":
            return
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
        sql = """"""
        n = int(ui.comboBox.currentIndex())
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
            sql = sql + " Enrolment_Number=\"" + enrolno[i] + "\" "
            if i != len(enrolno) - 1:
                sql = sql + "or"
        print(sql)
        obj = ENROLMENT_FORM.enroll()
        tup = obj.execute(sql)
        print(tup)
        obj1 = append()
        obj1.insertupdate(tup, n, self.formname)
        self.table1(tup, sql)
    def fun(self):
        if ui.comboBox.currentText()=="-Select":
            QtGui.QMessageBox.warning(ui.Enrol, 'Message',
                                      'Please select a form.',
                                      'OK')
            return
        if ui.entryBox.toPlainText()=="":
            QtGui.QMessageBox.warning(ui.Enrol, 'Message',
                                      'Please enter the enrolment numbers.',
                                      'OK')
            return
        self.formname=""
        self.formname = QtGui.QFileDialog.getSaveFileName(directory="C:\\Users\ADMIN\Documents", caption="Save File" ,filter=".xlsx")
        if self.formname=="":
            return
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
            sql = sql + " Enrolment_Number=\"" + enrolno[i] + "\" "
            if i != len(enrolno) - 1:
                sql = sql + "or"
        print(sql)
        obj = ENROLMENT_FORM.enroll()
        tup = obj.execute(sql)
        print(tup)
        obj1 = append()
        obj1.insert(tup, n,self.formname)
        self.table1(tup,sql)



    def picselect(self):
        self.candidphoto = QtGui.QFileDialog.getOpenFileName(ui.Enrol, 'Select the candidate picture', '.')
        ui.selectpictureLabel.setPixmap(QtGui.QPixmap(self.candidphoto))


    def check_enrol_form_data(self):

        proceed = True;
        sql="select Student_name from enrolment where Enrolment_Number='"+ui.enrolmentnumLineEdit.displayText()+"'"
        tup=ENROLMENT_FORM.enroll().execute(sql)
        if len(tup)!=0 and not ui.updateentryCheckBox.isChecked():
            QtGui.QMessageBox.warning(ui.Enrol, 'Please use another enrolment number',
                                      '\nEnrolment number must be unique.\n someone already has the same enrolment number. If you want to update the present entry , then check the Update Entry check box.',
                                      'OK');
            return


        def set_margin_red_style(obj):

            try:
                obj.setStyleSheet('border-color:red;border-width:2px;border-style:groove;')
                obj.setPlaceholderText('Mandatory field')
            except:
                pass;


        mailid = ui.emailLineEdit.displayText()

        if len(mailid) and  ('@' not in mailid or (mailid.rfind('.') -  mailid.rfind('@'))<2):
            QtGui.QMessageBox.warning(ui.Enrol , "Warning" , "\n\nPlease make sure that the entered Email address is a valid one." ,'OK')

            return



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
            print(len(ui.aadhaarLineEdit.displayText()))
            if len(ui.aadhaarLineEdit.displayText().strip())!=12:
                proceed=False;
                QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                          "\nValid Aadhaar Number should be 12 digits long.\n\n Please make sure that it's a valid 12 digit Aadhaar number",
                                          'OK')
                return ;

            if  len(ui.mobileLineEdit.displayText()) and  len(ui.mobileLineEdit.displayText().strip())!=10:
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
                    
                    font-weight:bold;

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

}""")


    def disable_form_elements(self):

        for i in ui.enrolformFrame.findChildren((QtGui.QLineEdit , QtGui.QComboBox , QtGui.QCheckBox , QtGui.QRadioButton,QtGui.QTextEdit)):
            i.setDisabled(True);

        for i in ui.bankformFrame.findChildren(QtGui.QLineEdit):
            i.setDisabled(True);

        for i in ui.instFrame.findChildren((QtGui.QLineEdit , QtGui.QComboBox)):
            i.setDisabled(True);
        ui.submitPushButton.hide()
        ui.updateentryCheckBox.hide()

    def enable_form_elements(self):

        for i in ui.enrolformFrame.findChildren(
                (QtGui.QLineEdit, QtGui.QComboBox, QtGui.QCheckBox, QtGui.QRadioButton, QtGui.QTextEdit)):
            i.setDisabled(False);

        for i in ui.bankformFrame.findChildren(QtGui.QLineEdit):
            i.setDisabled(False);

        for i in ui.instFrame.findChildren((QtGui.QLineEdit, QtGui.QComboBox)):
            i.setDisabled(False);

        ui.submitPushButton.show()
        ui.updateentryCheckBox.show()


    def display(self , obj): # this executes when the Search button is pressed

        if obj.objectName()=='searchPushButton':
            if ui.searchbyfieldLineEdit.displayText()=='':
                QtGui.QMessageBox.warning(ui.enrolformFrame ,"Warning" , "\n\nSearch field should not be empty while searching",'OK')
                return ;

            self.disable_form_elements() ;



        obj = ENROLMENT_FORM.enroll()

        search_field_text = ui.searchbyfieldLineEdit.displayText()

        if ui.aadhaarnumRadioButton.isChecked():
            self.field = 'Aadhar_Number'
            # if len(search_field_text)==12:
            #     search_field_text = search_field_text[:4]+' '+search_field_text[4:8]+' '+search_field_text[8:]


        elif ui.enrolmentnumRadioButton.isChecked():
            self.field = 'Enrolment_Number'


        ui.enrolPushButton.setChecked(False)

        tuple = obj.search_by_field(self.field, search_field_text);

        # if tuple==None:
        #     QtGui.QMessageBox.warning(ui.enrolformFrame, "Not found",
        #                               "\n\nSpecified Enrolment number was not found", 'OK')
        #     return ;


        print(tuple)
        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        dateyear = int(tuple[7][7] + tuple[7][8] + tuple[7][9] + tuple[7][10])
        datemonth = tuple[7][3] + tuple[7][4]+tuple[7][5]
        datemonth1=0
        for i in range(len(months)):
            if datemonth==months[i]:
                datemonth1=i+1
                break
        dateday = int(tuple[7][0] + tuple[7][1])
        enrolldateyear = int(tuple[16][7] + tuple[16][8] + tuple[16][9] + tuple[16][10])
        enrolldatemonth = tuple[16][3] + tuple[16][4]+tuple[16][5]
        enrolldateday = int(tuple[16][0] + tuple[16][1])
        enrolldatemonth1 = 0
        for i in range(len(months)):
            if enrolldatemonth == months[i]:
                enrolldatemonth1 = i + 1
                break
        ui.enrolmentnumLineEdit.setText(tuple[0])
        ui.rankComboBox.setCurrentIndex(ui.rankComboBox.findText(tuple[1]))
        ui.aadhaarLineEdit.setText(str(tuple[2]))
        ui.fullnameLineEdit.setText(tuple[3])
        ui.fathernameLineEdit.setText(tuple[4])
        ui.mothernameLineEdit.setText(tuple[5])
        ui.sexComboBox.setCurrentIndex(ui.sexComboBox.findText(tuple[6]))
        ui.dateofbirthDateEdit.setDate(QtCore.QDate(dateyear,datemonth1,dateday))
        ui.addressTextEdit.setText(tuple[8])
        ui.emailLineEdit.setText(tuple[9])
        ui.mobileLineEdit.setText(str(tuple[10]))
        ui.bloodgroupComboBox.setCurrentIndex(ui.bloodgroupComboBox.findText(tuple[11]))
        if tuple[12]=="A":
            ui.AcertRadioButton.setChecked(True)
        if tuple[12]=="NULL":
            ui.NullcertRadioButton.setChecked(True)
        if tuple[12]=="B":
            ui.BcertRadioButton.setChecked(True)
        if tuple[12]=="C":
            ui.CcertRadioButton.setChecked(True)
        for i in range(len(tuple[13])):
            if i<len(tuple[13])-2:
                if tuple[13][i]=='N' and tuple[13][i+1]=='I' and tuple[13][i+2]=='C' :
                    ui.NICCheckBox.setChecked(True)
            if i < len(tuple[13]) - 2:
                if tuple[13][i]=='A' and tuple[13][i+1]=='A' and tuple[13][i+2]=='C':
                    ui.AACCheckBox.setChecked(True)
            if i < len(tuple[13]) - 2:
                if tuple[13][i]=='C' and tuple[13][i+1]=='A' and tuple[13][i+2]=='T' and tuple[13][i+3]=='C':
                    ui.CATCCheckBox.setChecked(True)

        ui.extraactivitiesTextEdit.setText(tuple[14])
        ui.specialachievementsTextEdit.setText(tuple[15])
        ui.enroldateDateEdit.setDate(QtCore.QDate(enrolldateyear,enrolldatemonth1,enrolldateday))
        ui.remarksTextEdit.setText(tuple[17])
        if tuple[18]=="veg":
            ui.vegRadioButton.setChecked(1)
        else:
            ui.nonvegRadioButton.setChecked(1)
        ui.banknameLineEdit.setText(tuple[19])
        ui.bankbranchLineEdit.setText(tuple[20])
        ui.accountnumLineEdit.setText(str(tuple[21]))
        ui.accountnameLineEdit.setText(tuple[22])
        ui.ifsccodeLineEdit.setText(tuple[23])
        ui.micrLineEdit.setText(str(tuple[24]))
        ui.institutionenrollComboBox.setCurrentIndex(ui.institutionenrollComboBox.findText(tuple[25]))
        ui.unitLineEdit.setText(tuple[26])





    def enrol_adhaar_radio_change(self):
        if ui.aadhaarnumRadioButton.isChecked():
            ui.searchbyfieldLineEdit.clear();
            ui.searchbyfieldLineEdit.setValidator(QtGui.QDoubleValidator())
            ui.searchbyfieldLineEdit.setMaxLength(12)

        elif ui.enrolmentnumRadioButton.isChecked():
            ui.searchbyfieldLineEdit.clear()
            ui.searchbyfieldLineEdit.setMaxLength(1000)
            ui.searchbyfieldLineEdit.setValidator(None)




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

        self.institutionname = ui.institutionenrollComboBox.currentText()

        self.unit = ui.unitLineEdit.displayText()

        self.enrolldate=ui.enroldateDateEdit.text()

        self.remarks=ui.remarksTextEdit.toPlainText()

        self.specialachievements=ui.specialachievementsTextEdit.toPlainText()

        self.extracurricularactivities=ui.extraactivitiesTextEdit.toPlainText()

        self.micr=ui.micrLineEdit.displayText()
        self.campsattended=""

        if self.candidphoto:
            ext = self.candidphoto[self.candidphoto.rfind('.')+1: ]
            shutil.copy2(self.candidphoto, "candidate photos\{}.{}".format(self.enrolmentnum , ext))


        if ui.NICCheckBox.isChecked():
            self.campsattended = self.campsattended + "NIC,"
        if ui.CATCCheckBox.isChecked():
            self.campsattended = self.campsattended + "CATC,"
        if ui.AACCheckBox.isChecked():
            self.campsattended = self.campsattended + "AAC,"
        if ui.NULLCampsCheckBox.isChecked() and len(self.campsattended)==0:
            self.campsattended=self.campsattended+"NULL,"
        self.campsattended=self.campsattended[0:-1]
        print(self.campsattended)
        self.certificate="NULL"
        if ui.AcertRadioButton.isChecked():
            self.certificate="A"
        if ui.BcertRadioButton.isChecked():
            self.certificate="B"
        if ui.CcertRadioButton.isChecked():
            self.certificate="C"
        self.vegitarian="veg"
        if ui.nonvegRadioButton.isChecked():
            self.vegitarian="nonveg"

        obj=ENROLMENT_FORM.enroll()

        if ui.updateentryCheckBox.isChecked():
            obj.update_student_details(self.enrolmentnum , self.rank, self.aadhaarnum, self.fullname, self.fathername,

                          self.mothername,self.sex,self.dateofbirth,self.address,

                          self.email,self.mobilenum, self.bloodgroup,self.certificate,self.campsattended,self.extracurricularactivities

                          ,self.specialachievements,self.enrolldate,self.remarks,self.vegitarian, self.bankname, self.bankbranch, self.accountname,

                          self.accountnum, self.ifsccode,self.micr, self.institutionname, self.unit);



        else:

            obj.enrol_student(self.enrolmentnum, self.rank, self.aadhaarnum, self.fullname, self.fathername,

                              self.mothername,self.sex,self.dateofbirth,self.address,

                              self.email,self.mobilenum, self.bloodgroup,self.certificate,self.campsattended,self.extracurricularactivities

                              ,self.specialachievements,self.enrolldate,self.remarks,self.vegitarian, self.bankname, self.bankbranch, self.accountname,

                              self.accountnum, self.ifsccode,self.micr, self.institutionname, self.unit)

            QtGui.QToolTip.showText(QtCore.QPoint(100,200) ,"INSERTED SUCCESSFULLY")


        con = sqlite3.connect("ncc.db")
        data = pd.read_sql("select * from enrolment" ,con)
        try:
            data.to_csv(r'All candidate details.csv')
        except(PermissionError):
            print("The csv file is already open. It needs to be closed before updating it.")




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

        sql = """""";

        if ui.selectallCheckBox.isChecked():

            sql = "*";

        else:

            if ui.enrolmentCheckBox.isChecked(): sql += 'Enrolment_Number,';

            if ui.rankCheckBox.isChecked(): sql += 'Rank,'

            if ui.aadhaarCheckBox.isChecked(): sql += 'Adahar_Number,'

            if ui.sfnameCheckBox.isChecked(): sql += 'student_Name,'

            if ui.ffnameCheckBox.isChecked(): sql += 'Fathers_Name,'

            if ui.mfnameCheckBox.isChecked(): sql += 'Mothers_Name,'

            if ui.dateofbirthCheckBox.isChecked(): sql += 'Date_Of_Birth,'

            if ui.sexCheckBox.isChecked(): sql += 'Sex,'

            if ui.bloodgroupCheckBox.isChecked(): sql += 'Blood_Group,'

            if ui.extraCurricularActivitiesCheckBox.isChecked(): sql+= 'Extra_Curricular_Activities,'

            if ui.specialAchievementsCheckBox.isChecked(): sql+='Special_Achievements,'

            if ui.remarksCheckBox.isChecked(): sql+='Remarks,'

            if ui.enrollDateCheckBox.isChecked(): sql+='Enrol_Date,'

            if ui.vegitarianCheckBox.isChecked(): sql+='Vegitarian,'

            if ui.addressCheckBox.isChecked(): sql += 'Address,'

            if ui.emailCheckBox.isChecked(): sql += 'Email,'

            if ui.mobileCheckBox.isChecked(): sql += 'Mobile_Number,'

            if ui.banknameCheckBox.isChecked(): sql += 'Bank_Name,'

            if ui.bankbranchCheckBox.isChecked(): sql += 'Branch,'

            if ui.accountnameCheckBox.isChecked(): sql += 'Account_Name,'

            if ui.accountnumCheckBox.isChecked(): sql += 'Account_Number,'

            if ui.ifsccodeCheckBox.isChecked(): sql += 'IFSC_Code,'

            if ui.institutionCheckBox.isChecked(): sql += 'Institution,'

            if ui.unitCheckBox.isChecked(): sql += 'Unit,'

            if ui.micrCheckBox.isChecked():sql+='MICR,'

            sql = sql.strip();

            if len(sql) and sql[-1] == ',': sql = sql[0:-1];

            if not sql:
                sql = '*';

                ui.selectallCheckBox.setChecked(True);

        sql1 = str(ui.conditionsentrylabel.text())

        if sql == '*':

            if sql1 != "":

                sql = """select Enrolment_Number,Rank,Aadhar_Number,student_Name,Fathers_Name,Mothers_Name,Sex,Date_Of_Birth,
            Address,Email,Mobile_Number,Blood_Group,Certificate,Camps_Attended,Extra_Curricular_Activities,Special_Achievements,
            Enrol_Date,Remarks,Vegitarian,Bank_Name,Branch,Account_Name,Account_Number,IFSC_Code,MICR,Institution,Unit from enrolment where """ + str(
                    ui.conditionsentrylabel.text())

            else:

                sql = """select Enrolment_Number,Rank,Aadhar_Number,student_Name,Fathers_Name,Mothers_Name,Sex,Date_Of_Birth,
            Address,Email,Mobile_Number,Blood_Group,Certificate,Camps_Attended,Extra_Curricular_Activities,Special_Achievements,
            Enrol_Date,Remarks,Vegitarian,Bank_Name,Branch,Account_Name,Account_Number,IFSC_Code,MICR,Institution,Unit from enrolment"""



        else:

            sql = ("select " + sql + " from enrolment where " + str(
                ui.conditionsentrylabel.text())) if sql1 != "" else "select " + sql + " from enrolment ";

        if sql[7] == "*":
            sql = """select Enrolment_Number,Rank,Aadhar_Number,student_Name,Fathers_Name,Mothers_Name,Sex,Date_Of_Birth,
            Address,Email,Mobile_Number,Blood_Group,Certificate,Camps_Attended,Extra_Curricular_Activities,Special_Achievements,
            Enrol_Date,Remarks,Vegitarian,Bank_Name,Branch,Account_Name,Account_Number,IFSC_Code,MICR,Institution,Unit""" + sql[9:len(sql)]

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

        if ch=="Rank":
            ch1 =ui.rankqueryComboBox.currentText()
        elif ch=="Institution":
            ch1 =ui.institutionqueryComboBox.currentText()
        elif ch=="Blood_Group":
            ch1 =ui.bloodgroupqueryComboBox.currentText()
        elif ch=="Sex":
            ch1 =ui.sexqueryComboBox.currentText()
        elif ch=="Enrol_Date" or ch=="Date_Of_Birth":
            ch1 =ui.datequeryDateEdit.currentText()
        else:
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

    @QtCore.pyqtSlot(str)
    def pri(self,msg):
        print(msg)

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    MainWindow = QtGui.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    myobj = logic()

    MainWindow.show()

    sys.exit(app.exec_())