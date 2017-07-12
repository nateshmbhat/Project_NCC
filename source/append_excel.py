from tempfile import TemporaryFile
from xlwt import Workbook


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
        Cadet_details = ['Aadhar', 'Enrolment_no', 'Student_Name', "Fathers_Name", "Mothers_Name", 'Sex',
                     'Date_of_Birth', 'address', 'G_Mail', 'Mobile', 'Blood_group', 'Institution',
                     'Units']
        len_Cadet_details = len(Cadet_details)
        print(len_Cadet_details)
        sheet = self.book.add_sheet('CADET DETAILS')
        for i in range(len_Cadet_details):
            sheet.write(0, i, Cadet_details[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i+1,j,str(tup[i][j]))
        self.book.save('Forms.xls')
        self.book.save(TemporaryFile())

    def form2(self, tup):
        Yoga_day = ['Rank', 'Student_Name', "Fathers_Name", 'Units', 'Institution', 'Date_of_Birth', 'Rem']
        len_Yoga_day = len(Yoga_day)
        print(len_Yoga_day)
        sheet = self.book.add_sheet('YOGA DAY')
        for i in range(len_Yoga_day):
            sheet.write(0, i, Yoga_day[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i+1,j,str(tup[i][j]))
        self.book.save('Forms.xls')
        self.book.save(TemporaryFile())

    def form3(self,tup):
        Enrolment_Nominal_roll = ['Units', 'Enrolment_No', 'Rank', 'Student_Name', "Fathers_Name",
                                  "Date_of_Birth",
                                  "Institution", 'Class', 'Address', 'Mobile', 'Aadhar',
                                  'Bank_Name', 'Branch', 'IFSC_code','acc_Name', 'acc_no', 'MICR',
                                  'A/B certificate',
                                  'Camps attended', 'Sports/Music extra curricular activities', 'course grading',
                                  'Any special achievement', 'Year', 'Govt/Aided/Self finances', 'G_Mail',
                                  'Blood Group',
                                  'Remarks']
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
        Camp_Nominal_roll = ['Enrolment No', 'Rank', 'Name of ANO & Cadet', "Fathers_Name with address",
                             'Name of institution with location', 'Aadhar No', 'Year of trg', 'Veg/Non-veg',
                             'Whether able to swim',
                             'Bank account details']
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
        Scholarship_NR =[' Enrolment number','rank', 'Name of the Unit/Gp Institution','Bank account No & MICR No','SC',
                          'ST',
                          'OBC', 'Period of Trg', 'Examination on pass Date/Month/Year',
                          'Science,Arts,Commerce in case of stream SD/SW cadets only', 'Maximum marks',
                          'Minimum marks',
                          'Percentage', '10% Bonus marks secured to SC/ST/OBC applicant', '% of marks',
                          'Position obtained']
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
        A_certe_NR_for_high_school_JDJW = ['Enrolment No.',  'Rank', 'Name',
                                           "Father's name", "Date of birth",'Regiment al/CBSE Roll No', 'Date of Enrollment',
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
        len_A_certe_NR_for_high_school_JDJW = len(A_certe_NR_for_high_school_JDJW)
        print(len_A_certe_NR_for_high_school_JDJW)
        sheet = self.book.add_sheet('A certe NR for High school JDJW')
        for i in range(len_A_certe_NR_for_high_school_JDJW):
            sheet.write(0, i, A_certe_NR_for_high_school_JDJW[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i+1,j,str(tup[i][j]))
            self.book.save('Forms.xls')
            self.book.save(TemporaryFile())



    def form7(self,tup):
        B_certe_NR_SDSW = ['Enrolment_No.','Rank', 'Name', "Father's name",
                           "Date of birth", 'Regiment al/CBSE Roll No', 'Date of Enrollment', 'Date of Discharge', 'Details of Camps attended',
                           'Parade Attendance% Year I', 'Parade Attendance% Year II', 'Photo',
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
        C_certe_NR_SDSW = ['Enrolment_No.', 'Rank', 'Name', "Father's name",
                           "Date of birth", 'Regiment al/CBSE Roll No', 'Date of Enrollment', 'Date of Discharge', 'Details of Camps attended',
                           'Parade Attendance% III Year', 'Photo', 'Part-I-Drill written(10)',
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





