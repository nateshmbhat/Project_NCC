import msvcrt
import pandas as pd
from PyQt4.QtGui import QPushButton, QComboBox

import ENROLMENT_FORM
import os
import openpyxl
from userinterface import Ui_MainWindow, _fromUtf8
from PyQt4 import QtCore, QtGui, QtWebKit
import sqlite3
import shutil
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
class logic():
    flag = 0
    def __init__(self):
        ui.save_data_excelPushButton.hide()
        ENROLMENT_FORM.enroll().create_table_marks_A_cert()

        ENROLMENT_FORM.enroll().create_table_marks_B_cert()

        ENROLMENT_FORM.enroll().create_table_marks_C_cert()
        ENROLMENT_FORM.enroll().create_table_Enrolment()

        ui.NullcertRadioButton.setChecked(True)

        ui.vegRadioButton.setChecked(True)

        ui.AACCheckBox.clicked.connect(lambda :ui.NULLCampsCheckBox.setChecked(False))

        ui.NICCheckBox.clicked.connect(lambda :ui.NULLCampsCheckBox.setChecked(False))

        ui.CATCCheckBox.clicked.connect(lambda :ui.NULLCampsCheckBox.setChecked(False))

        ui.NULLCampsCheckBox.clicked.connect(self.checklogicnull)

        ui.insertcondition.clicked.connect(self.coninsert)

        ui.clearcondition.clicked.connect(lambda:ui.conditionsentrylabel.setText(""))

        ui.backcondition.clicked.connect(self.conback)

        ui.andcondition.clicked.connect(lambda :ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text().strip() + " and "))

        ui.orcondition.clicked.connect(lambda :ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text().strip() + " or "))

        ui.equalscondition.clicked.connect(lambda :ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text().strip() + "="))

        ui.openbracecondition.clicked.connect(lambda :ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text().strip() + "("))

        ui.closebracecondition.clicked.connect(lambda :ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text().strip() + ")"))

        ui.greatercondition.clicked.connect(lambda :ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text().strip() + ">"))

        ui.lessercondition.clicked.connect(lambda :ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text().strip() + "<"))

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

        ui.certificatequeryComboBox.hide()

        ui.vegitarianqueryComboBox.hide()

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

        ui.saveExelPushButton.clicked.connect(self.saveExcelfuntion)

        ui.vegRadioButton.setChecked(True)

        ui.NullcertRadioButton.setChecked(True)

        if not os.path.exists(r'candidate photos'):
            os.mkdir(r'candidate photos')
        ui.openPushButton.clicked.connect(self.openuploaddata)

        ui.savedataPushButton.clicked.connect(self.saveuploadeddata)

        ui.save_data_excelPushButton.clicked.connect(self.saveexceluploadeddata)

        ui.typecomboBox.currentIndexChanged.connect(self.typecomboboxlogic)

        ui.updateExelPushButton.clicked.connect(self.update_excel_function)

        ui.settings_addinstitutionPushButton.clicked.connect(lambda: (
            ui.settings_addinstitutionPushButton.hide(), ui.removeinstitutionPushButton.hide(),
            ui.settings_instLineEdit.show(), ui.settings_addPushButton.show(), ui.settings_backinstPushButton.show()))


        ui.settings_addPushButton.clicked.connect(lambda: self.institution_add_or_remove(ui.settings_addPushButton))

        ui.removeinstitutionPushButton.clicked.connect(lambda: self.institution_add_or_remove(ui.removeinstitutionPushButton))

        ui.settings_backinstPushButton.clicked.connect(lambda: self.set_institutions_list())
        self.init_settings()
    def init_settings(self):

        """Sets all the parameters from the settings file"""

        self.settings = QtCore.QSettings('settings.ini', QtCore.QSettings.IniFormat)
        self.institutionlist = self.settings.value('institutionlist').split(',,,')
        self.set_institutions_list()

        '''ALL STANDARD FIELDS LIST (Fields that are in the master enrolment form )'''

        self.all_enrolment_form_fieldslist = self.settings.value('all_enrolment_form_fieldslist').split(',,,')
        ui.mytab.setCurrentIndex(int(self.settings.value('current_tab')))
        geo = [int(i) for i in self.settings.value('window_geometry').split(',,,')]
        MainWindow.setGeometry(geo[0], geo[1], geo[2], geo[3])
        app.aboutToQuit.connect(self.handler)


        """List of all forms in the forms tab"""
        self.formslist = self.settings.value('formslist').strip().split(',,,');
        ui.formsComboBox.clear()
        ui.formsComboBox.addItems(self.formslist)


        '''This is the list of all the types of entry forms in data entry tab'''
        self.dataentrytypes = self.settings.value('dataentrytypes').strip().split(',,,')
        ui.typecomboBox.clear()
        ui.typecomboBox.addItems(self.dataentrytypes)


        '''List of forms and fields in the settings tab'''
        self.formslist = self.settings.value('formslist').strip().split(',,,')
        ui.settings_formsListWidget.clear()

        ui.settings_formsListWidget.setSpacing(1)
        self.set_forms_list()


        '''List of all the fields under Dataentry Types '''

        self.marksA_fieldslist = self.settings.value('marksA_fieldslist').split(',,,')
        self.marksB_fieldslist= self.settings.value('marksB_fieldslist').split(',,,')
        self.marksC_fieldslist = self.settings.value('marksC_fieldslist').split(',,,')
        self.camps_fieldslist = self.settings.value('camps_fieldslist').split(',,,')
        self.extraactivities_fieldslist = self.settings.value('extraactivities_fieldslist').split(',,,')
        self.remarks_fieldslist = self.settings.value('remarks_fieldslist').split(',,,')

        #hiding fields in the settigns_fieldssectoin
        ui.settings_addfieldPushButton.hide()
        ui.settings_addfieldLineEdit.hide()
        ui.settings_fieldsComboBox.hide()
        ui.settings_fieldsknownRadioButton.hide()
        ui.settings_fieldsunknownRadioButton.hide()
        ui.settings_removefieldPushButton.hide()
        ui.settings_removeformPushButton.hide()

        self.nametolistsql ={}
        self.nametolistnotsql = {}

        for form in self.formslist:

            sqlfieldlist = self.settings.value(form.replace(' ','_')+'_sql_fieldslist')
            notsqlfieldlist = self.settings.value(form.replace(' ','_')+'_notsql_fieldslist')

            sqlfieldlist = sqlfieldlist.split(',,,') if sqlfieldlist else []
            notsqlfieldlist = notsqlfieldlist.split(',,,') if notsqlfieldlist else []


            self.nametolistsql.update({form:sqlfieldlist})
            self.nametolistnotsql.update({form:notsqlfieldlist})


        # The below lines are used to connect the widgets to the corresponding functions

        ui.settings_addformPushButton.clicked.connect(
            lambda: self.settings_form_field_add_remove(ui.settings_addformPushButton))
        ui.settings_addfieldPushButton.clicked.connect(
            lambda: self.settings_form_field_add_remove(ui.settings_addfieldPushButton))
        ui.settings_formsListWidget.itemClicked.connect(self.settings_form_item_clicked)

        ui.settings_removefieldPushButton.clicked.connect(
            lambda: self.settings_form_field_add_remove(ui.settings_removefieldPushButton))

        ui.settings_removeformPushButton.clicked.connect(lambda:self.settings_form_field_add_remove(ui.settings_removeformPushButton))

        for i in ui.Enrol.findChildren((QtGui.QLineEdit, QtGui.QComboBox, QtGui.QDateEdit, QtGui.QTextEdit)):
            if i.objectName() == 'searchbyfieldLineEdit':
                continue
            s = '#' + i.objectName() + ''':focus
                    {
                        border:2px groove chartreuse;
                    }'''
            i.setStyleSheet(s)

        ui.settings_candidopenPushButton.clicked.connect(lambda: os.system('start explorer "candidate photos"'))
        ui.enroldateDateEdit.setDate(QtCore.QDate.currentDate())

    def showtooltip(self, text):
        tt = QtGui.QToolTip
        myfont = QtGui.QFont()
        myfont.setFamily("caladea")
        myfont.setBold(True)
        myfont.setPointSize(20)
        tt.setFont(myfont)
        mywin = QtGui.QMainWindow.frameGeometry(MainWindow)
        pos = mywin.center()
        pos.setX(pos.x() - 6.6666667 * len(text));
        pos.setY(mywin.y())
        tt.showText(pos, text, MainWindow,
                    QtGui.QLineEdit.geometry(ui.settings_institutionListWidget))

    def settings_form_item_clicked(self):
        '''THis function is called whenever the user clicks on an item in the forms list of settings tab . It handles the show and hide of various elements and displays the corresponding
        field names in the field tab and also controls the add field combobox
        '''
        ui.settings_addfieldPushButton.show()
        ui.settings_removefieldPushButton.show()

        selected_text= ui.settings_formsListWidget.currentItem().text().strip()

        if selected_text not in ['Cadet details','Yoga day','Enrolment Nominal roll','Camp Nominal roll','Scholarship NR','A certificate','B certificate','C certificate','Speciman signature of cadets','TADA to cadets camps','TADA to cadets for exam']:
            ui.settings_removeformPushButton.show()
        else:ui.settings_removeformPushButton.hide()

        fieldslistsql = self.nametolistsql.get(selected_text)
        fieldslistsql = fieldslistsql if fieldslistsql else []

        fieldslistnotsql = self.nametolistnotsql.get(selected_text)
        fieldslistnotsql = fieldslistnotsql if fieldslistnotsql else []

        self.set_fields_list(fieldslistsql , fieldslistnotsql)

    def handler(self):
        settings = QtCore.QSettings('settings.ini', QtCore.QSettings.IniFormat)
        geo = MainWindow.geometry()
        settings.setValue('window_geometry',
                          ',,,'.join([str(geo.x()), str(geo.y()), str(geo.width()), str(geo.height())]))
        settings.setValue('current_tab', ui.mytab.currentIndex())

    def set_fields_list(self , sqllist , notsqllist):
        """This function is called after a new field is addded to the field list . This function sets the styles for the fields and puts them in the field list of the settings tab"""

        ui.settings_fieldsListWidget.clear()
        ui.settings_addfieldLineEdit.clear()
        ui.settings_fieldsListWidget.setSpacing(1)


        for ele in sqllist:
            item = QtGui.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
            item.setText(ele)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Caladea"))
            font.setPointSize(14)
            font.setBold(False)
            font.setItalic(True)
            font.setWeight(63)
            item.setFont(font)
            item.setToolTip('Standard fields')
            brush = QtGui.QBrush(QtGui.QColor(120, 190, 255, 200))
            brush.setStyle(QtCore.Qt.Dense4Pattern)
            item.setBackground(brush)
            ui.settings_fieldsListWidget.addItem(item)


        for ele in notsqllist:
            if ele in sqllist:
                continue
            item = QtGui.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
            item.setText(ele)
            font = QtGui.QFont()
            item.setToolTip('Non standard fields')
            font.setFamily(_fromUtf8("Caladea"))
            font.setPointSize(14)
            font.setBold(False)
            font.setItalic(True)
            font.setWeight(62)
            item.setFont(font)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255, 200))
            brush.setStyle(QtCore.Qt.Dense4Pattern)
            item.setBackground(brush)
            ui.settings_fieldsListWidget.addItem(item)

        ui.settings_fieldsknownRadioButton.hide()
        ui.settings_fieldsunknownRadioButton.hide()
        ui.settings_removefieldPushButton.show()
        ui.settings_fieldsComboBox.hide()
        ui.settings_addfieldLineEdit.hide()
        #Set the elements that are not already in the corresponding field into the add field combobox

        ui.settings_fieldsComboBox.clear()
        print(sqllist)

        for ele in self.all_enrolment_form_fieldslist:
            if ele not in sqllist:
                ui.settings_fieldsComboBox.addItem(ele)

    def set_forms_list(self):
        """Sets the style and label for the list items in formsListWidget of settings"""
        ui.settings_formsListWidget.clear()
        for inst in self.formslist:
            item = QtGui.QListWidgetItem()
            item.setText(inst)
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Garamond"))
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            brush = QtGui.QBrush(QtGui.QColor(72, 255, 52, 100))
            brush.setStyle(QtCore.Qt.Dense2Pattern)
            item.setBackground(brush)
            ui.settings_formsListWidget.addItem(item)

        ui.settings_removeformPushButton.hide()

    def settings_form_field_add_remove(self,obj):
        '''Called when Add form or Add field buttons of the settings tab are clicked'''

        def removefield_button_states():
            ui.settings_fieldsknownRadioButton.hide()
            ui.settings_fieldsunknownRadioButton.hide()
            ui.settings_removefieldPushButton.show()
            ui.settings_fieldsComboBox.hide()
            ui.settings_addfieldLineEdit.hide()


        selectedform = ui.settings_formsListWidget.currentItem()
        selectedform = '' if not selectedform else selectedform.text().strip()
        selectedfield = ui.settings_fieldsListWidget.currentItem()
        selectedfield = '' if not selectedfield else selectedfield.text().strip()


        '''FORMS'''
        if obj.objectName() == 'settings_addformPushButton' :


            if not ui.settings_addformLineEdit.displayText().strip():
                QtGui.QMessageBox.warning(ui.Settings,'Entry field is blank','\nEnter the name of the new form in the Entrybox that you wish to add and then Click "Add Form"' , 'OK')
                return

            if QtGui.QMessageBox.question(ui.Settings , 'Are you Sure ? ' , 'Are you sure that you wish to add a New Form ? This will add your form through out the software.',"Yes","No")==0:

                formname = ui.settings_addformLineEdit.displayText().strip().strip()


                if formname in self.formslist:
                    QtGui.QMessageBox.warning(ui.Settings,'Form already exists','Make sure that the Entered form name is not already in the forms list and Enter a unique name for your Form and click "Add Form"','OK')
                    return

                self.formslist.append(formname)
                self.settings.setValue('formslist',',,,'.join(self.formslist))
                self.settings.setValue(formname.replace(' ','_')+'_sql_fieldslist' , '')

                ui.settings_addformLineEdit.clear()
                ui.settings_formsListWidget.clear()
                self.set_forms_list()
                return
            else:
                return




        if obj.objectName() == 'settings_removeformPushButton':
            if not selectedform:
                QtGui.QMessageBox.warning(ui.Settings, 'No Form Seleted',
                                          'Please select a form first before removing it.', 'OK')
                return

            if QtGui.QMessageBox.question(ui.Settings , 'Are you sure ?' , 'Are you sure that you want to DELETE the form "{}" from the forms list ? This will remove the form throughout the software'.format(selectedform),'Yes','No' )==0:

                self.formslist.remove(selectedform)
                self.settings.setValue('formslist',',,,'.join(self.formslist))
                self.set_forms_list()



        if obj.objectName() == 'settings_addfieldPushButton':
            ui.settings_removefieldPushButton.hide()

            if ui.settings_fieldsknownRadioButton.isHidden():
                def addfield_lineedit_combobox_decide():
                    if ui.settings_fieldsknownRadioButton.isChecked():
                        ui.settings_fieldsComboBox.show()
                        ui.settings_addfieldLineEdit.hide()
                        ui.settings_removefieldPushButton.hide()

                    else:
                        ui.settings_fieldsComboBox.hide()
                        ui.settings_addfieldLineEdit.show()

                ui.settings_fieldsknownRadioButton.toggled.connect(addfield_lineedit_combobox_decide)
                ui.settings_fieldsComboBox.show()
                ui.settings_fieldsknownRadioButton.show()
                ui.settings_fieldsunknownRadioButton.show()
                ui.settings_fieldsknownRadioButton.setChecked(True)


            else:
                if ui.settings_fieldsknownRadioButton.isChecked():
                    if QtGui.QMessageBox.question(ui.Settings,'Are You Sure ? ' , 'Are you sure that you want to add the field selected in the selection box to the field lists ? This will add the field through out the software.','Yes','No')==0:

                        self.nametolistsql.get(selectedform).append(ui.settings_fieldsComboBox.currentText())
                        self.settings.setValue(selectedform.replace(' ','_')+'_sql_fieldslist',',,,'.join(self.nametolistsql.get(selectedform)))
                        self.set_fields_list(self.nametolistsql.get(selectedform) if self.nametolistsql.get(selectedform) else [] , self.nametolistnotsql.get(selectedform) if self.nametolistnotsql.get(selectedform) else [])
                        removefield_button_states()
                        return
                    else:
                        removefield_button_states()

                else:
                    if not ui.settings_addfieldLineEdit.displayText().strip():
                        QtGui.QMessageBox.warning(ui.Settings , 'Empty Field !','Make sure that the field entry box is not empty before seleting "Add field". Enter a field name in the Editing box provided and click "Add form" to add it to the fields list' , 'OK')
                        removefield_button_states()
                        return


                    if QtGui.QMessageBox.question(ui.Settings, 'Are You Sure ? ' , 'Are you sure that you want to add the entered field to the list of fields of the corresponding form ? This will add the field through out the software.','Yes','No')==0:
                        self.nametolistnotsql.get(selectedform).append(ui.settings_addfieldLineEdit.displayText().strip())
                        self.settings.setValue(selectedform.replace(' ','_')+'_notsql_fieldslist' , ',,,'.join(self.nametolistnotsql.get(selectedform)))
                        self.set_fields_list(self.nametolistsql.get(selectedform) if self.nametolistsql.get(selectedform) else [] , self.nametolistnotsql.get(selectedform) if self.nametolistnotsql.get(selectedform) else [])
                        removefield_button_states()
                        return


        if obj.objectName() =='settings_removefieldPushButton':
            if not selectedfield:
                QtGui.QMessageBox.warning(ui.Settings , 'No field seleted','Please select a field first before removing it.','OK')
                return

            if QtGui.QMessageBox.question(ui.Settings , 'Are you sure ? ' , 'Are you sure that you wish to remove the field "{}" from the selected form ? It will remove the field through out the entire software'.format(selectedfield),'Yes','No')==0:

                sqllist = self.nametolistsql.get(selectedform)
                notsqllist = self.nametolistnotsql.get(selectedform)

                if selectedfield in sqllist:
                    self.nametolistsql.get(selectedform).remove(selectedfield);
                    self.settings.setValue(selectedform.replace(' ','_')+'_sql_fieldslist' , ',,,'.join(self.nametolistsql.get(selectedform)))
                elif selectedfield in notsqllist:
                    self.nametolistnotsql.get(selectedform).remove(selectedfield);
                    self.settings.setValue(selectedform.replace(' ', '_') + '_notsql_fieldslist',',,,'.join(self.nametolistnotsql.get(selectedform)))

                self.set_fields_list(self.nametolistsql.get(selectedform) if self.nametolistsql.get(selectedform) else [],self.nametolistnotsql.get(selectedform) if self.nametolistnotsql.get(selectedform) else [])

    def institution_add_or_remove(self, button):
        """Called whenever user clicks on the add or remove button of the institution list in the settings tab"""

        if button.text().strip() == 'Add':
            if not ui.settings_instLineEdit.displayText().strip():
                QtGui.QMessageBox.warning(ui.Settings, "Empty field",
                                          '\n\nPlease enter an institution name and click "Add" to add it to the present list',
                                          "OK")
                return

            inst_name = ui.settings_instLineEdit.displayText().strip()

            self.institutionlist.append(inst_name)

            self.settings.setValue('institutionlist',",,,".join(self.institutionlist))

            self.set_institutions_list()



        if button.text().strip() == 'Remove':

            selectedItem = ui.settings_institutionListWidget.currentItem()
            if not selectedItem:
                QtGui.QMessageBox.warning(ui.Settings, "Nothing Selected",
                                          '\n\nPlease select an institution first, to remove it.',
                                          "OK")
                return

            if QtGui.QMessageBox.question(ui.Settings, "Are you sure ?",
                                          '\n\nAre you sure you want to remove this Institution from the list of institutions ? \nThe changes are irreversible ! \nClick "Yes" to remove it.',
                                          'Yes', 'No') == 0:


                selected_text = selectedItem.text().strip()

                self.institutionlist.remove(selected_text)

                self.settings.setValue('institutionlist' , ",,,".join(self.institutionlist))

                self.set_institutions_list()

        ui.settings_instLineEdit.clear()

    def set_institutions_list(self):

        """
            Manages the hiding and showing of the buttons in the Institution list in the settings tab and also sets the institutions for all the comboboxes which have institutions
            This function is called whenever an item is added or removed to the institution list
        """
        ui.settings_institutionListWidget.clear()
        ui.settings_addinstitutionPushButton.show()
        ui.removeinstitutionPushButton.show()
        ui.settings_backinstPushButton.show()


        ui.settings_institutionListWidget.setSpacing(1)

        for inst in self.institutionlist:
            item = QtGui.QListWidgetItem()
            item.setText(inst)
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Garamond"))
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            brush = QtGui.QBrush(QtGui.QColor(72, 255, 52, 100))
            brush.setStyle(QtCore.Qt.Dense3Pattern)
            item.setBackground(brush)
            ui.settings_institutionListWidget.addItem(item)



        ui.institutionenrollComboBox.clear()
        ui.institutionenrollComboBox.addItems(self.institutionlist)

        ui.institutionqueryComboBox.clear()
        ui.institutionqueryComboBox.addItems(self.institutionlist)

        ui.institutionuploaddatacomboBox.clear()
        ui.institutionuploaddatacomboBox.addItems(self.institutionlist)


        ui.settings_instLineEdit.hide()
        ui.settings_addPushButton.hide()
        ui.settings_backinstPushButton.hide()

    def typecomboboxlogic(self):
        if ui.typecomboBox.currentText()=="Select Type" or ui.typecomboBox.currentText()=="Camps_Attended" or ui.typecomboBox.currentText()=="Remarks" or ui.typecomboBox.currentText()=="Extra_Curricular_Activities":
            ui.save_data_excelPushButton.hide()
        else:
            ui.save_data_excelPushButton.show()

    def saveuploadeddata(self):
        selectedInstitutionName = ui.institutionuploaddatacomboBox.currentText()
        selectedDataType = ui.typecomboBox.currentText()

        if selectedDataType == "A certificate" or selectedDataType == "B certificate" or selectedDataType == "C certificate":
            fieldsListSql = self.nametolistsql.get(selectedDataType)
            fieldsListNotSql = self.nametolistnotsql.get(selectedDataType)
            if selectedDataType=="A certificate":
                selectedDataType="A_cert_marks"
            if selectedDataType=="B certificate":
                selectedDataType="Bcert_marks"
            if selectedDataType=="C certificate":
                selectedDataType="C_cert_marks"
            sql = """select Enrolment_Number,Rank,Student_Name,Fathers_Name,Date_Of_Birth,Enrol_Date,Camps_Attended from enrolment where institution='""" + selectedInstitutionName + "'"
            sqldata = ENROLMENT_FORM.enroll().execute(sql)
            sqlpresentdata = ENROLMENT_FORM.enroll().execute("select * from " + selectedDataType + " where Institution='" + selectedInstitutionName + "'")

            flag=0
            for i in range(len(sqldata)):
                for k in range(len(sqlpresentdata)):
                    if sqlpresentdata[k][0] == ui.tableWidget.item(i,0).text():
                        print("hello")
                        flag = 1
                        break
                if flag == 1:
                    print("hello")
                    flag=0
                    ENROLMENT_FORM.enroll().delete_by_Enrolment(selectedDataType,sqldata[i][0])
                sql = "insert into " + selectedDataType + " values("
                for j in range(len(fieldsListSql)):
                    if ui.tableWidget.horizontalHeaderItem(j).text()=="Rank":
                        sql=sql+"'"+str(self.rankuploadcombobox[i].currentText())+"'"
                    else:
                        sql=sql+"'"+str(ui.tableWidget.item(i,j).text())+"'"
                    if j!=len(fieldsListSql)-1:
                        sql=sql+","
                sql=sql+")"
                ENROLMENT_FORM.enroll().insertionexecute(sql)
                print("inserted sucessfully")
        else:
            sql = "select Enrolment_Number," + selectedDataType + " from enrolment where institution='" + selectedInstitutionName + "'"
            sqldata = ENROLMENT_FORM.enroll().execute(sql)
            for i in range(len(sqldata)):
                sql1 = "update enrolment set " + selectedDataType + "='"+ui.tableWidget.item(i,1).text()+"' where Enrolment_Number='"+sqldata[i][0]+"'"
                ENROLMENT_FORM.enroll().insertionexecute(sql1)

    def saveexceluploadeddata(self):
        self.name=QtGui.QFileDialog.getSaveFileName(directory="C:\\Users\ADMIN\Documents", caption="Save File", filter=".xlsx")
        data=[]
        if ui.typecomboBox.currentText()=="A certificate":
            self.book = openpyxl.load_workbook('A_CERTIFICATES.xlsx')
            self.sheet = self.book.get_sheet_by_name('A')
        elif ui.typecomboBox.currentText()=="B certificate":
            self.book = openpyxl.load_workbook('B_CERTIFICATES.xlsx')
            self.sheet = self.book.get_sheet_by_name('B')
        elif ui.typecomboBox.currentText()=="C certificate":
            self.book = openpyxl.load_workbook('CC_CERTIFICATES.xlsx')
            self.sheet = self.book.get_sheet_by_name('C')

        for i in range(ui.tableWidget.rowCount()):
            data.append([])
            for j in range(ui.tableWidget.columnCount()):
                if ui.tableWidget.horizontalHeaderItem(j).text()=="Rank":
                    txt=self.rankuploadcombobox[i].currentText()
                elif ui.tableWidget.item(i,j)!=None:
                    txt=ui.tableWidget.item(i,j).text()
                data[i].append(txt)


        for row in data:
            self.sheet.append(row)
        self.book.save(self.name)
        self.book.save(TemporaryFile())

    rankuploadcombobox = []
    campsattendedcombobox=[]
    def openuploaddata(self):
        self.rankuploadcombobox = []
        self.rank=["Cadet (CDT)","Lance Corporal (LCPL)","Corporal (CPL)","Sergent (SGT)","Company Sergent Major (CSM)","Junior Under Officer (JUO)","Senior Under Officer (SUO)"]
        self.camps=["NIC","CATC","AAC"]
        selectedInstitutionName = ui.institutionuploaddatacomboBox.currentText()
        selectedDataType = ui.typecomboBox.currentText()
        sql11="select Enrolment_Number from enrolment where institution='"+selectedInstitutionName+"'"
        verticalheaderdata=ENROLMENT_FORM.enroll().execute(sql11)
        verticalheader=[]
        for i in range(len(verticalheaderdata)):
            verticalheader.append(verticalheaderdata[i][0])

        if selectedDataType=="A certificate" or selectedDataType=="B certificate" or selectedDataType=="C certificate":

            ui.tableWidget.clearContents()
            fieldsListSql=self.nametolistsql.get(selectedDataType)
            fieldsListNotSql=self.nametolistnotsql.get(selectedDataType)
            if selectedDataType=="A certificate":
                selectedDataType="A_cert_marks"
            if selectedDataType=="B certificate":
                selectedDataType="B_cert_marks"
            if selectedDataType=="C certificate":
                selectedDataType="C_cert_marks"
            sql="""select Enrolment_Number,Rank,Student_Name,Fathers_Name,Date_Of_Birth,Enrol_Date,Camps_Attended from enrolment where institution='"""+selectedInstitutionName+"'"
            sqldata=ENROLMENT_FORM.enroll().execute(sql)
            sqlpresentdata=ENROLMENT_FORM.enroll().execute("select * from "+selectedDataType+" where Institution='"+selectedInstitutionName+"'")
            ui.tableWidget.setRowCount(len(sqldata))
            ui.tableWidget.setColumnCount(len(fieldsListSql))
            ui.tableWidget.setHorizontalHeaderLabels(fieldsListSql)
            ui.tableWidget.setVerticalHeaderLabels(verticalheader)
            l=0
            for i in range(len(sqldata)):
                flag = 0
                con = 0

                for l in range(len(sqlpresentdata)):
                    if sqldata[i][0]==sqlpresentdata[l][0]:
                        flag=1
                        break
                if flag==0:
                    for j in range(len(fieldsListSql)):
                        if j<len(sqldata[i]):
                            if fieldsListSql[j] == "Roll_Number":
                                ui.tableWidget.setItem(i, j , QtGui.QTableWidgetItem(""))
                                con = 1
                            if con == 0:
                                if fieldsListSql[j] == "Rank":
                                    self.rankuploadcombobox.append(QComboBox(ui.tableWidget))
                                    ui.tableWidget.setCellWidget(i, j, self.rankuploadcombobox[len(self.rankuploadcombobox) - 1])
                                    for items in range(len(self.rank)):
                                        self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].addItem(_fromUtf8(""))
                                        self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].setItemText(items,_translate("MainWindow",self.rank[items],None))
                                    self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].setStyleSheet("font-weight:bold;")
                                    self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].setCurrentIndex(self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].findText(sqldata[i][j]))
                                else:
                                    ui.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(sqldata[i][j]))
                            if con == 1:
                                if fieldsListSql[j] == "Roll_Number":
                                    self.rankuploadcombobox.append(QComboBox(ui.tableWidget))
                                    ui.tableWidget.setCellWidget(i, j+1, self.rankuploadcombobox[len(self.rankuploadcombobox) - 1])
                                    for items in range(len(self.rank)):
                                        self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].addItem(_fromUtf8(""))
                                        self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].setItemText(items,_translate("MainWindow",self.rank[items],None))
                                    self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].setStyleSheet("font-weight:bold;")
                                    self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].setCurrentIndex(self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].findText(sqldata[i][j]))
                                else:
                                    ui.tableWidget.setItem(i, j + 1, QtGui.QTableWidgetItem(sqldata[i][j]))
                        else:
                            if j!=len(fieldsListSql)-2:
                                ui.tableWidget.setItem(i, j+1, QtGui.QTableWidgetItem(""))
                            if j==len(fieldsListSql)-2:
                                ui.tableWidget.setItem(i, j + 1, QtGui.QTableWidgetItem(selectedInstitutionName))

                if flag==1:
                    for j in range(len(sqlpresentdata[l])):
                        if fieldsListSql[j]=="Rank":
                            self.rankuploadcombobox.append(QComboBox(ui.tableWidget))
                            ui.tableWidget.setCellWidget(i, j, self.rankuploadcombobox[len(self.rankuploadcombobox) - 1])
                            for items in range(len(self.rank)):
                                self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].addItem(_fromUtf8(""))
                                self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].setItemText(items, _translate("MainWindow", self.rank[items], None))
                            self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].setStyleSheet("font-weight:bold;")
                            self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].setCurrentIndex(self.rankuploadcombobox[len(self.rankuploadcombobox) - 1].findText(sqlpresentdata[l][j]))
                        else:
                            ui.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(sqlpresentdata[l][j]))
                if len(sqlpresentdata)>0:
                    sqlpresentdata.pop(l)
        else:
            sql="select Enrolment_Number,"+selectedDataType+" from enrolment where institution='"+selectedInstitutionName+"'"
            sqldata=ENROLMENT_FORM.enroll().execute(sql)
            ui.tableWidget.setColumnCount(2)
            ui.tableWidget.setRowCount(len(sqldata))
            header=["Enrolment Number"]
            header.append(selectedDataType)
            ui.tableWidget.setHorizontalHeaderLabels(header)
            ui.tableWidget.setVerticalHeaderLabels(verticalheader)
            for i in range(len(sqldata)):
                for j in range(len(sqldata[i])):
                    ui.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(sqldata[i][j]))

        myfont = QtGui.QFont()
        myfont.setBold(True)
        myfont.setFamily("georgia")
        for i in range(ui.tableWidget.rowCount()):
            for j in range(ui.tableWidget.columnCount()):
                if ui.tableWidget.item(i, j)!=None:
                    ui.tableWidget.item(i, j).setBackground(QtGui.QColor(170, 170, 170))
                    ui.tableWidget.item(i,j).setFont(myfont)
                    ui.tableWidget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)

        ui.tableWidget.showGrid()
        ui.tableWidget.setStyleSheet(
            "color:black;font-weight:bold;font-size:15px;border:1px solid black;gridline-color:black;")
        ui.tableWidget.horizontalHeader().setStyleSheet(
            "color:darkgreen;font-size:24px;font-weight:bold;font-family:gabriola;border:1px solid black;gridline-color:black;")
        ui.tableWidget.verticalHeader().setStyleSheet(
            "color:darkorange;font-size:20px;font-weight:bold;font-family:caladea;border:1px solid black;gridline-color:black;")
        ui.tableWidget.resizeRowsToContents()
        ui.tableWidget.resizeColumnsToContents()
        ui.tableWidget.hideColumn(0)

    def conditionscomboboxlogic(self):
        text=ui.conditionlistcombobox.currentText()
        """if text=="Rank" or text=="Institution" or text=="Blood_Group" or text=="Sex" or text=="Enrol_Date" or text=="Date_Of_Birth":"""
        ui.rankqueryComboBox.hide()
        ui.institutionqueryComboBox.hide()
        ui.bloodgroupqueryComboBox.hide()
        ui.sexqueryComboBox.hide()
        ui.datequeryDateEdit.hide()
        ui.valuelineEdit.hide()
        ui.certificatequeryComboBox.hide()
        ui.vegitarianqueryComboBox.hide()
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
        elif text=="Vegitarian":
            ui.vegitarianqueryComboBox.show()
        elif text=="Certificate":
            ui.certificatequeryComboBox.show()
        else:
            ui.valuelineEdit.show()

    def checklogicnull(self):
        ui.NICCheckBox.setChecked(False)
        ui.AACCheckBox.setChecked(False)
        ui.CATCCheckBox.setChecked(False)

    def enrol_button_pressed(self):
        ui.searchbyfieldLineEdit.clear()
        self.enable_query_checkbox_elements();
        ui.submitPushButton.show()

    def update_excel_function(self):
        if ui.entryBox.toPlainText()=="":
            QtGui.QMessageBox.warning(ui.Enrol, 'Message',
                                      'Please enter the enrolment numbers.',
                                      'OK')
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
        selectedformname = ui.formsComboBox.currentText()
        self.listdata = self.nametolistsql.get(selectedformname)
        self.listheadingdata = self.nametolistnotsql.get(selectedformname)
        sql = """select """
        if selectedformname!='A certificate' and selectedformname!="B certificate" and selectedformname!="C certificate":
            for i in range(len(self.listdata)):
                sql = sql + self.listdata[i]
                if i != len(self.listdata) - 1:
                    sql = sql + ","
            sql = sql + " from enrolment where "
        else:
            tablename=""
            if selectedformname=="A certificate":
                tablename="A_cert_marks"
            elif selectedformname=="B certificate":
                tablename="B_cert_marks"
            elif selectedformname=="C certificate":
                tablename="C_cert_marks"
            for i in range(len(self.listdata)):
                sql = sql + self.listdata[i]
                if i != len(self.listdata) - 1:
                    sql = sql + ","
            sql = sql + " from "+tablename+" where "

        for i in range(len(enrolno)):
            sql = sql + " Enrolment_Number=\"" + enrolno[i] + "\" "
            if i != len(enrolno) - 1:
                sql = sql + "or"
        print(sql)
        tup = ENROLMENT_FORM.enroll().execute(sql)
        print(tup)
        if len(tup)==0:
            QtGui.QMessageBox.warning(ui.Enrol, 'Message',
                                      'First Enter the feed the data for the respected certificate\nand then generate a form.',
                                      'OK')
            return
        self.formname = ""
        self.formname = QtGui.QFileDialog.getOpenFileName(directory="C:\\Users\ADMIN\Documents", caption="Save File")
        if self.formname == "":
            return
        book = openpyxl.load_workbook(self.formname)
        sheet = book.active
        for i in tup:
            sheet.append(i)
        book.save(self.formname)
        book.save(TemporaryFile())
        self.table1(tup, sql)

    def saveExcelfuntion(self):

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
        selectedformname=ui.formsComboBox.currentText()
        self.listdata=self.nametolistsql.get(selectedformname)
        self.listheadingdata = self.nametolistnotsql.get(selectedformname)
        sql = """select """
        if selectedformname!='A certificate' and selectedformname!="B certificate" and selectedformname!="C certificate":
            for i in range(len(self.listdata)):
                sql = sql + self.listdata[i]
                if i != len(self.listdata) - 1:
                    sql = sql + ","
            sql = sql + " from enrolment where "
        else:
            tablename=""
            if selectedformname=="A certificate":
                tablename="A_cert_marks"
            elif selectedformname=="B certificate":
                tablename="B_cert_marks"
            elif selectedformname=="C certificate":
                tablename="C_cert_marks"
            for i in range(len(self.listdata)):
                sql = sql + self.listdata[i]
                if i != len(self.listdata) - 1:
                    sql = sql + ","
            sql = sql + " from "+tablename+" where "

        for i in range(len(enrolno)):
            sql = sql + " Enrolment_Number=\"" + enrolno[i] + "\" "
            if i != len(enrolno) - 1:
                sql = sql + "or"
        print(sql)
        tup = ENROLMENT_FORM.enroll().execute(sql)
        if len(tup)<1:
            QtGui.QMessageBox.warning(ui.Enrol, 'Message',
                                      'First Enter the feed the data for the respected certificate\nand then generate a form.',
                                      'OK')
            return
        self.formname = ""
        self.formname = QtGui.QFileDialog.getSaveFileName(directory="C:\\Users\ADMIN\Documents", caption="Save File",
                                                          filter=".xlsx")
        if self.formname == "":
            return
        book = Workbook()
        sheet = book.active
        for i in range(len(self.listheadingdata)):
            sheet.cell(row=1, column=i + 1).value = self.listheadingdata[i]
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.cell(row=i + 2, column=j+1).value= str(tup[i][j])
        book.save(self.formname)
        book.save(TemporaryFile())
        self.table1(tup,sql)

    def picselect(self):
        self.candidphoto = QtGui.QFileDialog.getOpenFileName(ui.Enrol, 'Select the candidate picture', '.')
        ui.selectpictureLabel.setPixmap(QtGui.QPixmap(self.candidphoto))

    def check_enrol_form_data(self):

        proceed = True;
        sql="select Student_Name from enrolment where Enrolment_Number='"+ui.enrolmentnumLineEdit.displayText().strip()+"'"
        tup=ENROLMENT_FORM.enroll().execute(sql)
        if len(tup)!=0 and not ui.updateentryCheckBox.isChecked():
            QtGui.QMessageBox.warning(ui.Enrol, 'Please use another enrolment number',
                                      '\nEnrolment number must be unique.\n someone already has the same enrolment number. If you want to update the present entry , then check the Update Entry check box.','OK');
            return


        if len(tup)!=0 and not ui.updateentryCheckBox.isChecked():
            QtGui.QMessageBox.warning(ui.Enrol, 'Aadhaar number already exists',
                                      '\nEnrolment number must be unique.\n someone already has the same enrolment number. If you want to update the present entry , then check the Update Entry check box.','OK');


        def set_margin_red_style(obj):

            try:
                obj.setStyleSheet('border-color:red;border-width:2px;border-style:groove;')
                obj.setPlaceholderText('Mandatory field')
            except:
                pass;


        mailid = ui.emailLineEdit.displayText().strip()

        if len(mailid) and  ('@' not in mailid or (mailid.rfind('.') -  mailid.rfind('@'))<2):
            QtGui.QMessageBox.warning(ui.Enrol , "Warning" , "\n\nPlease make sure that the entered Email address is a valid one." ,'OK')

            return



        for i in [ui.enrolmentnumLineEdit, ui.fullnameLineEdit, ui.fathernameLineEdit, ui.mothernameLineEdit,ui.addressTextEdit, ui.unitLineEdit , ui.aadhaarLineEdit]:

            if i == ui.addressTextEdit:
                if i.toPlainText() == '':
                    proceed = False;

                    set_margin_red_style(i)


            elif i.displayText().strip() == '':

                proceed = False
                set_margin_red_style(i)



            else:
                i.setStyleSheet('')
                i.setPlaceholderText('')


        if proceed: #This runs only if all the non-null fields are filled.

            ui.addressTextEdit.setStyleSheet('')
            print(len(ui.aadhaarLineEdit.displayText().strip()))
            if len(ui.aadhaarLineEdit.displayText().strip().strip())!=12:
                proceed=False;
                QtGui.QMessageBox.warning(ui.Enrol, 'Warning',
                                          "\nValid Aadhaar Number should be 12 digits long.\n\n Please make sure that it's a valid 12 digit Aadhaar number",
                                          'OK')
                return ;

            if  len(ui.mobileLineEdit.displayText().strip()) and  len(ui.mobileLineEdit.displayText().strip().strip())!=10:
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

    def disable_query_checkbox_elements(self):

        for i in ui.enrolformFrame.findChildren((QtGui.QLineEdit , QtGui.QComboBox , QtGui.QCheckBox , QtGui.QRadioButton,QtGui.QTextEdit)):
            i.setDisabled(True);

        for i in ui.bankformFrame.findChildren(QtGui.QLineEdit):
            i.setDisabled(True);

        for i in ui.instFrame.findChildren((QtGui.QLineEdit , QtGui.QComboBox)):
            i.setDisabled(True);
        ui.dateofbirthDateEdit.setDisabled(True)
        ui.enroldateDateEdit.setDisabled(True)
        ui.vegRadioButton.setDisabled(True)
        ui.nonvegRadioButton.setDisabled(True)
        ui.submitPushButton.hide()
        ui.updateentryCheckBox.hide()

    def enable_query_checkbox_elements(self):

        for i in ui.enrolformFrame.findChildren(
                (QtGui.QLineEdit, QtGui.QComboBox, QtGui.QCheckBox, QtGui.QRadioButton, QtGui.QTextEdit)):
            i.setDisabled(False);

        for i in ui.bankformFrame.findChildren(QtGui.QLineEdit):
            i.setDisabled(False);

        for i in ui.instFrame.findChildren((QtGui.QLineEdit, QtGui.QComboBox)):
            i.setDisabled(False);

        ui.dateofbirthDateEdit.setDisabled(False)
        ui.enroldateDateEdit.setDisabled(False)
        ui.vegRadioButton.setDisabled(False)
        ui.nonvegRadioButton.setDisabled(False)
        ui.submitPushButton.show()
        ui.updateentryCheckBox.show()

    def display(self , obj): # this executes when the Search button is pressed


        if obj.objectName()=='searchPushButton':
            if ui.searchbyfieldLineEdit.displayText().strip()=='':
                QtGui.QMessageBox.warning(ui.enrolformFrame ,"Warning" , "\n\nSearch field should not be empty while searching",'OK')
                return ;

            self.disable_query_checkbox_elements() ;



        obj = ENROLMENT_FORM.enroll()

        search_field_text = ui.searchbyfieldLineEdit.displayText().strip()

        if ui.aadhaarnumRadioButton.isChecked():
            self.field = 'Aadhaar_Number'
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
                    ui.NULLCampsCheckBox.setChecked(False)
                    ui.NICCheckBox.setChecked(True)
            if i < len(tuple[13]) - 2:
                if tuple[13][i]=='A' and tuple[13][i+1]=='A' and tuple[13][i+2]=='C':
                    ui.NULLCampsCheckBox.setChecked(False)
                    ui.AACCheckBox.setChecked(True)
            if i < len(tuple[13]) - 2:
                if tuple[13][i]=='C' and tuple[13][i+1]=='A' and tuple[13][i+2]=='T' and tuple[13][i+3]=='C':
                    ui.NULLCampsCheckBox.setChecked(False)
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

        self.enrolmentnum = ui.enrolmentnumLineEdit.displayText().strip();

        self.aadhaarnum = ui.aadhaarLineEdit.displayText().strip()

        self.rank = ui.rankComboBox.currentText()

        self.fullname = ui.fullnameLineEdit.displayText().strip()

        self.fathername = ui.fathernameLineEdit.displayText().strip()

        self.mothername = ui.mothernameLineEdit.displayText().strip()

        self.sex = ui.sexComboBox.currentText();

        self.dateofbirth = ui.dateofbirthDateEdit.text().strip();

        self.address = ui.addressTextEdit.toPlainText()

        self.email = ui.emailLineEdit.displayText().strip()

        self.mobilenum = ui.mobileLineEdit.displayText().strip()

        self.bloodgroup = ui.bloodgroupComboBox.currentText()

        self.bankname = ui.banknameLineEdit.displayText().strip()

        self.bankbranch = ui.bankbranchLineEdit.displayText().strip()

        self.accountname = ui.accountnameLineEdit.displayText().strip()

        self.accountnum = ui.accountnumLineEdit.displayText().strip()

        self.ifsccode = ui.ifsccodeLineEdit.displayText().strip()

        self.institutionname = ui.institutionenrollComboBox.currentText()

        self.unit = ui.unitLineEdit.displayText().strip()

        self.enrolldate=ui.enroldateDateEdit.text().strip()

        self.remarks=ui.remarksTextEdit.toPlainText()

        self.specialachievements=ui.specialachievementsTextEdit.toPlainText()

        self.extracurricularactivities=ui.extraactivitiesTextEdit.toPlainText()

        self.micr=ui.micrLineEdit.displayText().strip()
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
            self.campsattended=self.campsattended+","
        self.campsattended=self.campsattended[0:-1]

        self.certificate=""
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
            self.showtooltip("Updated successfully")



        else:

            obj.enrol_student(self.enrolmentnum, self.rank, self.aadhaarnum, self.fullname, self.fathername,

                              self.mothername,self.sex,self.dateofbirth,self.address,

                              self.email,self.mobilenum, self.bloodgroup,self.certificate,self.campsattended,self.extracurricularactivities

                              ,self.specialachievements,self.enrolldate,self.remarks,self.vegitarian, self.bankname, self.bankbranch, self.accountname,

                              self.accountnum, self.ifsccode,self.micr, self.institutionname, self.unit)

            self.showtooltip("Inserted successfully")


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

            height: 30px;

            text-align:center;

        }

        td{
            margin:3px 6px;
            font-family:cambria;
            background-color:white;
            text-align:center;
            opacity:0.8;
            font-weight:bold;
            
        }

        tr{

            background-color: white;
            text-align-last: center;

        }



        th{

            background-color: rgb(177, 51, 255);
            opacity:0.8;
            font-family:gabriola;
            text-align-last: center;
            font-size: 22px;
            height:20px;
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

                html3 = html3 + "\n<th>" + mmsg.replace('_',' ') + "</th>\n"

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

            if ui.aadhaarCheckBox.isChecked(): sql += 'Aadhaar_Number,'

            if ui.sfnameCheckBox.isChecked(): sql += 'Student_Name,'

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

        sql1 = str(ui.conditionsentrylabel.text().strip())

        if sql == '*':

            if sql1 != "":

                sql = """select Enrolment_Number,Rank,Aadhaar_Number,Student_Name,Fathers_Name,Mothers_Name,Sex,Date_Of_Birth,
            Address,Email,Mobile_Number,Blood_Group,Certificate,Camps_Attended,Extra_Curricular_Activities,Special_Achievements,
            Enrol_Date,Remarks,Vegitarian,Bank_Name,Branch,Account_Name,Account_Number,IFSC_Code,MICR,Institution,Unit from enrolment where """ + str(
                    ui.conditionsentrylabel.text().strip())

            else:

                sql = """select Enrolment_Number,Rank,Aadhaar_Number,Student_Name,Fathers_Name,Mothers_Name,Sex,Date_Of_Birth,
            Address,Email,Mobile_Number,Blood_Group,Certificate,Camps_Attended,Extra_Curricular_Activities,Special_Achievements,
            Enrol_Date,Remarks,Vegitarian,Bank_Name,Branch,Account_Name,Account_Number,IFSC_Code,MICR,Institution,Unit from enrolment"""



        else:

            sql = ("select " + sql + " from enrolment where " + str(
                ui.conditionsentrylabel.text().strip())) if sql1 != "" else "select " + sql + " from enrolment ";

        if sql[7] == "*":
            sql = """select Enrolment_Number,Rank,Aadhaar_Number,Student_Name,Fathers_Name,Mothers_Name,Sex,Date_Of_Birth,
            Address,Email,Mobile_Number,Blood_Group,Certificate,Camps_Attended,Extra_Curricular_Activities,Special_Achievements,
            Enrol_Date,Remarks,Vegitarian,Bank_Name,Branch,Account_Name,Account_Number,IFSC_Code,MICR,Institution,Unit""" + sql[9:len(sql)]

        tup = ENROLMENT_FORM.enroll().execute(sql)
        if len(tup)<1:
            self.showtooltip("No Data Found")
            ui.webView.setHtml("")
            return
        self.table(tup, sql)
        self.showtooltip("Query is Sucessfull")
    def conback(self):

        sql = ui.conditionsentrylabel.text().strip().strip()

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
        elif ch=="Certificate":
            ch1 =ui.certificatequeryComboBox.currentText()
        elif ch=="Vegitarian":
            ch1 =ui.vegitarianqueryComboBox.currentText()
        else:
            ch1 = ui.valuelineEdit.text().strip()

        ch2 = ui.conditionsentrylabel.text().strip().strip() + ' '

        if (len(ch2) > 3):

            if (ch2[len(ch2) - 1] == ' ' and (ch2[len(ch2) - 2] == 'd' or ch2[len(ch2) - 2] == 'r')) or (
                            ch2[len(ch2) - 1] == '(' and

                        (ch2[len(ch2) - 2] == ' ' or ch2[len(ch2) - 2] == 'r' or ch2[len(ch2) - 2] == '(' or ch2[
                                len(ch2) - 2] == ')' or

                                 ch2[len(ch2) - 2] == 'd')):
                print()


            else:
                self.showtooltip("Please use \'AND\' or \'OR\' between two conditions")

                return

        if ch != "Select":

            if (ch1 != ""):

                if ch == "Aadhaar_Number" or ch == "Mobile_Number" or ch == "Account_number":

                    if ch1.isdigit():

                        if ch == "Mobile_Number":

                            if len(ch1) == 10:

                                ui.conditionsentrylabel.setText(
                                    ui.conditionsentrylabel.text().strip() + ch + "=\"" + ch1 + "\"")

                            else:
                                self.showtooltip("Mobile number should contains 10 numbers")

                        elif ch == "Aadhaar_Number":

                            if len(ch1) == 12:

                                ui.conditionsentrylabel.setText(
                                    ui.conditionsentrylabel.text().strip() + ch + "=\"" + ch1 + "\"")

                            else:
                                self.showtooltip("Aadhaar number should contains 12 numbers")


                        elif ch=="Account_Number":
                            if len(ch1) == 16:

                                ui.conditionsentrylabel.setText(
                                    ui.conditionsentrylabel.text().strip() + ch + "=\"" + ch1 + "\"")

                            else:
                                self.showtooltip("Account number should contains 16 numbers")
                        else:

                            ui.conditionsentrylabel.setText(ui.conditionsentrylabel.text().strip() + ch + "=\"" + ch1 + "\"")



                    else:
                        self.showtooltip(ch+' must contains only integral values.')

                else:

                    ui.conditionsentrylabel.setText(
                        ui.conditionsentrylabel.text().strip().strip() + ' ' + ch + "=\"" + ch1 + "\"")

            else:
                self.showtooltip("Please enter the values for the field selected.")

        else:
            self.showtooltip("Please select any one of the fields.")

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    MainWindow = QtGui.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    myobj = logic()

    MainWindow.show()

    sys.exit(app.exec_())