from tempfile import TemporaryFile

from xlwt import Workbook


class append:
    book = Workbook()
    def insert(self,tuple,n):
        if n is 1:
            self.form1(tuple)
        elif n is 2:
            self.form2()
        elif n is 3:
            self.form3()
        elif n is 4:
            self.form4()
        elif n is 5:
            self.form5()
        elif n is 6:
            self.form6()
        elif n is 7:
            self.form7()
        elif n is 8:
            self.form8()



    def form1(self,tup):
        CADET_DETAILS = ['Aadhar', 'Enrolment_no', 'student_name', "Fathers_Name", "Mothers_Name", 'Sex',
                     'Date_of_Birth', 'address', 'G_Mail', 'Mobile', 'Blood_group', 'Institution',
                     'Units']
        len_cadet_details = len(CADET_DETAILS)
        print(len_cadet_details)
        sheet = self.book.add_sheet('CADET DETAILS')
        for i in range(len_cadet_details):
            sheet.write(0, i, CADET_DETAILS[i])
        for i in range(len(tup)):
            for j in range(len(tup[i])):
                sheet.write(i+1,j,str(tup[i][j]))
        self.book.save('Forms.xls')
        self.book.save(TemporaryFile())

    def form2(self):
        YOGA_DAY = ['Rank', 'Name', "Father's Name", 'Unit', 'Institution', 'Date of Birth', 'Rem']
        len_YOGA_DAY = len(YOGA_DAY)
        print(len_YOGA_DAY)
        sheet = self.book.add_sheet('YOGA DAY')
        for i in range(len_YOGA_DAY):
            sheet.write(0, i, YOGA_DAY[i])

    def form3(self):
        Enrolment_Nominal_roll = ['Sl No', 'Unit', 'Regimental No', 'Rank', 'Name', "Father's Name",
                                  "Date of Birth",
                                  "Institution", 'Class', 'Residential address', 'Tele/Mobile numbers', 'Aadhar No',
                                  'Bank Name', 'Branch', 'IFSC code', 'Bank account number', 'MICR',
                                  'A/B certificate',
                                  'Camps attended', 'Sports/Music extra curricular activities', 'course grading',
                                  'Any special achievement', 'Year', 'Govt/Aided/Self finances', 'E-Mail',
                                  'Blood Group',
                                  'Remarks']
        len_Enrolment_Nominal_roll = len(Enrolment_Nominal_roll)
        print(len_Enrolment_Nominal_roll)
        sheet = self.book.add_sheet('Enrolment Nominal roll')
        for i in range(len_Enrolment_Nominal_roll):
            sheet.write(0, i, Enrolment_Nominal_roll[i])

    def form4(self):
        Camp_Nominal_roll = ['Sl No', 'Regtl No', 'Rank', 'Name of ANO & Cadet', "Father's Name with address",
                             'Name of institution with location', 'Year of trg', 'Veg/Non-veg',
                             'Whether able to swim',
                             'Aadhar No', 'Bank account details']
        len_Camp_Nominal_roll = len(Camp_Nominal_roll)
        print(len_Camp_Nominal_roll)
        sheet = self.book.add_sheet('Camp Nominal roll')
        for i in range(len_Camp_Nominal_roll):
            sheet.write(0, i, Camp_Nominal_roll[i])

    def form5(self):
        Scholarship_NR = ['Sl No', 'Regtl No. & Rank Name of the cadet', 'Name of the Unit/Gp Institution', 'SC',
                          'ST',
                          'OBC', 'Period of Trg', 'Examination on pass Date/Month/Year',
                          'Science,Arts,Commerce in case of stream SD/SW cadets only', 'Maximum marks',
                          'Minimum marks',
                          'Percentage', '10% Bonus marks secured to SC/ST/OBC applicant', '% of marks',
                          'Position obtained',
                          'Bank account No & MICR No']
        len_Scholarship_NR = len(Scholarship_NR)
        print(len_Scholarship_NR)
        sheet = self.book.add_sheet('Scholarship NR')
        for i in range(len_Scholarship_NR):
            sheet.write(0, i, Scholarship_NR[i])

    def form6(self):
        A_certe_NR_for_High_school_JDJW = ['SrNo', 'Roll No.', 'Regiment al/CBSE Roll No', 'Rank', 'Name',
                                           "Father's name", "Date of birth", 'Date of Enrollment',
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

    def form7(self):
        B_certe_NR_SDSW = ['SrNo', 'Roll No.', 'Regiment al/CBSE Roll No', 'Rank', 'Name', "Father's name",
                           "Date of birth", 'Date of Enrollment', 'Date of Discharge', 'Details of Camps attended',
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

    def form8(self):
        C_certe_NR_SDSW = ['SrNo', 'Roll No.', 'Regiment al/CBSE Roll No', 'Rank', 'Name', "Father's name",
                           "Date of birth", 'Date of Enrollment', 'Date of Discharge', 'Details of Camps attended',
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



