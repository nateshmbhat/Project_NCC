from PyQt4.QtGui import QDialog, QPushButton

import ENROLMENT_FORM
import os
from userinterface import Ui_MainWindow, _fromUtf8
import pandas as pd
from PyQt4 import QtCore, QtGui
import sqlite3
import shutil
import forms
import append_excel

from tempfile import TemporaryFile
from xlwt import Workbook

import main
import userinterface


class append:
    book = Workbook()
    def insert(self,tuple,n):
        if n is 1:
            self.form1(tuple)
        elif n is 2:
            self.form2(tuple)
        elif n is 3:
            self.form3(tuple)
        elif n is 4:
            self.form4(tuple)
        elif n is 5:
            self.form5(tuple)
        elif n is 6:
            self.form6(tuple)
        elif n is 7:
            self.form7(tuple)
        elif n is 8:
            self.form8(tuple)



    def form1(self,tup):
        CADET_DETAILS = ['Enrolment_Number','Aadhar_Number', 'student_Name', "Fathers_Name", "Mothers_Name", 'Sex',
                     'Date_Of_Birth', 'Address', 'Email', 'Mobile_Number', 'Blood_Group', 'Institution',
                     'Unit']
        len_cadet_details = len(CADET_DETAILS)
        print(len_cadet_details)
        sheet=""
        if ui.sheetnameComboBox.currentText()=="Select Sheet Name":
            QtGui.QMessageBox.warning(ui.Enrol,"Warning\n",
                                      "Please select sheet name or select new sheet",
                                      'OK')
        elif ui.sheetnameComboBox.currentText()=="New Sheet":
            if ui.sheetnameLineEdit.text()=="":
                QtGui.QMessageBox.warning(ui.Enrol, "warning\n",
                                          "Please enter a sheet name or select any sheet",
                                          'OK')
            else:
                sheet =self.book.add_sheet(ui.sheetnameLineEdit.text())
                ui.sheetnameComboBox.addItem(ui.sheetnameLineEdit.text())
        else:
            sheet =self.book.add_sheet(ui.sheetnameComboBox.currentText())

        for i in range(len_cadet_details):
            sheet.write(0, i, CADET_DETAILS[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i+1,j,str(tup[i][j]))


        if ui.excelfilenameComboBox.currentText()=="Select File Name":
            QtGui.QMessageBox.warning(ui.Enrol,"warning\n",
                                      "Please select file name or select new file",
                                      'OK')
        elif ui.excelfilenameComboBox.currentText()=="New File":
            if ui.excelfilenameLineEdit.text()=="":
                QtGui.QMessageBox.warning(ui.Enrol, "warning\n",
                                          "Please enter a file name or select any file",
                                          'OK')
            else:
                self.book.save(ui.excelfilenameLineEdit.text()+".xls")
                ui.excelfilenameComboBox.addItem(ui.excelfilenameLineEdit.text())
        else:
            self.book.save(ui.sheetnameComboBox.currentText())
        self.book.save(TemporaryFile())

    def form2(self, tup):
        YOGA_DAY = ['Rank', 'Student_name', "Fathers_Name", 'Unit', 'Institution', 'Date_Of_Birth', 'Remarks']
        len_YOGA_DAY = len(YOGA_DAY)
        print(len_YOGA_DAY)
        sheet = self.book.add_sheet('YOGA DAY')
        for i in range(len_YOGA_DAY):
            sheet.write(0, i, YOGA_DAY[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i+1,j,str(tup[i][j]))
        self.book.save('Forms.xls')
        self.book.save(TemporaryFile())

    def form3(self,tup):
        Enrolment_Nominal_roll = ['Unit', 'Enrolment_Number', 'Rank', 'Student_name', "Fathers_name",
                                  "Date_of_Birth","Institution", 'Address', 'Mobile', 'Aadhar',
                                  'Bank_Name', 'Branch', 'IFSC_code','Account_Name', 'Account_Number', 'MICR',
                                  'Certificate','Camps_Attended', 'Extra_Curricular_Activities',
                                  'Special_Achievements','Email','Blood Blood_Group','Remarks', 'course grading']
        len_Enrolment_Nominal_roll = len(Enrolment_Nominal_roll)
        print(len_Enrolment_Nominal_roll)
        sheet = self.book.add_sheet('Enrolment Nominal roll')
        for i in range(len_Enrolment_Nominal_roll):
            sheet.write(0, i, Enrolment_Nominal_roll[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i+1,j,str(tup[i][j]))
        self.book.save('Forms.xls')
        self.book.save(TemporaryFile())

    def form4(self,tup):
        Camp_Nominal_roll = ['Enrolment_Number','Aadhar_Number','Rank', 'student_Name', "Fathers_Name",'Address'
                             'Institution', 'Vegitarian','Bank_Name','Branch',
                             'Account_Name','Account_Number','IFSC_Code',
                             'Year of training','Able to swim or not']
        len_Camp_Nominal_roll = len(Camp_Nominal_roll)
        print(len_Camp_Nominal_roll)
        sheet = self.book.add_sheet('Camp Nominal roll')
        for i in range(len_Camp_Nominal_roll):
            sheet.write(0, i, Camp_Nominal_roll[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i+1,j,str(tup[i][j]))
            self.book.save('Forms.xls')
            self.book.save(TemporaryFile())

    def form5(self,tup):
        Scholarship_NR =['Enrolment_Number','Rank', 'Unit','Institution','Bank_Name','Branch','Account_Name',
                         'Account_Number','IFSC_Code','MICR'
                          ,'SC','ST','OBC', 'Period of Trg', 'Examination on pass Date/Month/Year',
                          'Science,Arts,Commerce in case of stream SD/SW cadets only', 'Maximum marks','Minimum marks',
                          'Percentage', '10% Bonus marks secured to SC/ST/OBC applicant', '% of marks','Position obtained']
        len_Scholarship_NR = len(Scholarship_NR)
        print(len_Scholarship_NR)
        sheet = self.book.add_sheet('Scholarship NR')
        for i in range(len_Scholarship_NR):
            sheet.write(0, i, Scholarship_NR[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i+1,j,str(tup[i][j]))
            self.book.save('Forms.xls')
            self.book.save(TemporaryFile())

    def form6(self,tup):
        A_certe_NR_for_High_school_JDJW = ['Enrolment_Number',  'Rank', 'student_Name',
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
        len_A_certe_NR_for_High_school_JDJW = len(A_certe_NR_for_High_school_JDJW)
        print(len_A_certe_NR_for_High_school_JDJW)
        sheet = self.book.add_sheet('A certe NR for High school JDJW')
        for i in range(len_A_certe_NR_for_High_school_JDJW):
            sheet.write(0, i, A_certe_NR_for_High_school_JDJW[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i+1,j,str(tup[i][j]))
            self.book.save('Forms.xls')
            self.book.save(TemporaryFile())



    def form7(self,tup):
        B_certe_NR_SDSW = ['Enrolment_Number.','Rank', 'student_Name', "Fathers_Name",
                           "Date_Of_Birth", 'Enrol_Date', 'Photo'
                            ,'Date of Discharge', 'Details of Camps attended',
                           'Parade Attendance% Year I', 'Parade Attendance% Year II',
                           'Part-I-Drill written(10)', 'Part-I-Drill practical(80)', 'Part-I-Drill Total(90)',
                           'Part-II:WT Written(35)', 'Part-II:WT Practical(25)', 'Part-II:WT Total(60)',
                           'Part-III:Misc written(200)', 'Part-IV:Spl Subjects written(105)',
                           'Part-IV:Spl Subjects practical(45)', 'Part-IV:Spl Subjects Total(150)',
                           'Bonus Marks Certific', 'Grand Total(500)', 'Grading',
                           'Signature of cadet: Written common subject', 'Signature of cadet: Written Spl subject',
                           'Signature of cadet: Practical']
        len_B_certe_NR_SDSW = len(B_certe_NR_SDSW)
        print(len_B_certe_NR_SDSW)
        sheet = self.book.add_sheet('B_certe_NR_SDSW')
        for i in range(len_B_certe_NR_SDSW):
            sheet.write(0, i, B_certe_NR_SDSW[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i + 1, j, str(tup[i][j]))
            self.book.save('Forms.xls')
            self.book.save(TemporaryFile())

    def form8(self,tup):
        C_certe_NR_SDSW = ['Enrolment_Number.', 'Rank', 'student_Name', "Fathers_Name",
                           "Date_Of_Birth", 'Enrol_Date','Photo',
                           'Date of Discharge', 'Details of Camps attended',
                           'Parade Attendance% III Year',  'Part-I-Drill written(10)',
                           'Part-I-Drill practical(50)', 'Part-I-Drill Total(60)', 'Part-II:WT Written(10)',
                           'Part-II:WT Practical(55)', 'Part-II:WT Total(65)', 'Part-III:Misc written(225)',
                           'Part-IV:Spl Subjects written(105)', 'Part-IV:Spl Subjects practical(45)',
                           'Part-IV:Spl Subjects Total(150)', 'Grand Total(500)', 'Bonus Marks max-Total-50',
                           'Grading', 'Signature of cadet: Written common subject',
                           'Signature of cadet: Written Spl subject', 'Signature of cadet: Practical']
        len_C_certe_NR_SDSW = len(C_certe_NR_SDSW)
        print(len_C_certe_NR_SDSW)
        sheet = self.book.add_sheet('C_certe_NR_SDSW')
        for i in range(len_C_certe_NR_SDSW):
            sheet.write(0, i, C_certe_NR_SDSW[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i + 1, j, str(tup[i][j]))
            self.book.save('Forms.xls')
            self.book.save(TemporaryFile())






class logic():
    def __init__(self):

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

        ui.searchPushButton.clicked.connect(lambda :self.display(ui.searchPushButton))


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

        ui.vegRadioButton.setChecked(True)

        ui.NullcertRadioButton.setChecked(True)

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

        ui.excelfilenameLineEdit.hide()

        ui.sheetnameLineEdit.hide()

        ui.excelfilenameComboBox.currentIndexChanged.connect(self.formscomboboxlogic)

        ui.sheetnameComboBox.currentIndexChanged.connect(self.formscomboboxlogic1)

        ui.vegRadioButton.setChecked(True)

        ui.NullcertRadioButton.setChecked(True)






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




    def formscomboboxlogic(self):
        print("hello")
        if ui.excelfilenameComboBox.currentText()=="New File":
            ui.excelfilenameLineEdit.show()
        else:
            ui.excelfilenameLineEdit.hide()
    def formscomboboxlogic1(self):
        print("hello")
        if ui.sheetnameComboBox.currentText()=="New Sheet":
            ui.sheetnameLineEdit.show()
        else:
            ui.sheetnameLineEdit.hide()
    def checklogicnull(self):
        ui.NICCheckBox.setChecked(False)
        ui.AACCheckBox.setChecked(False)
        ui.CATCCheckBox.setChecked(False)

    def checklogic(self):
        ui.NULLCampsCheckBox.setChecked(False)



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
            sql = sql + " Enrolment_Number=\"" + enrolno[i] + "\" "
            if i != len(enrolno) - 1:
                sql = sql + "or"
        print(sql)
        obj = ENROLMENT_FORM.enroll()
        tup = obj.execute(sql)
        print(tup)
        obj1 = append()
        obj1.insert(tup, n)
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
                                      '\nEnrolment number must be unique.\n someone already has the same enrolment number',
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
            if len(ui.aadhaarLineEdit.displayText().strip())!=14:
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

    def enable_form_elements(self):

        for i in ui.enrolformFrame.findChildren(
                (QtGui.QLineEdit, QtGui.QComboBox, QtGui.QCheckBox, QtGui.QRadioButton, QtGui.QTextEdit)):
            i.setDisabled(False);

        for i in ui.bankformFrame.findChildren(QtGui.QLineEdit):
            i.setDisabled(False);

        for i in ui.instFrame.findChildren((QtGui.QLineEdit, QtGui.QComboBox)):
            i.setDisabled(False);



    def display(self , obj): # this executes when the Search button is pressed
        ui.enrolPushButton.setChecked(False)

        if obj.objectName()=='searchPushButton':
            if ui.searchbyfieldLineEdit.displayText()=='':
                QtGui.QMessageBox.warning(ui.enrolformFrame ,"Warning" , "\n\nSearch field should not be entry while searching",'OK')
                return ;

            self.disable_form_elements() ;
            ui.submitPushButton.hide()


        obj = ENROLMENT_FORM.enroll()

        if ui.aadhaarnumRadioButton.isChecked():
            self.field = 'Aadhar_Number'
        elif ui.enrolmentnumRadioButton.isChecked():
            self.field = 'Enrolment_Number'


        tuple = obj.search_by_field(self.field, ui.searchbyfieldLineEdit.displayText())
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
        ui.institutionComboBox.setCurrentIndex(ui.institutionComboBox.findText(tuple[25]))
        ui.unitLineEdit.setText(tuple[26])



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

        self.institutionname = ui.institutionComboBox.currentText()

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


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    MainWindow = QtGui.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    myobj = logic();

    MainWindow.show()

    sys.exit(app.exec_())