from tempfile import TemporaryFile
from xlwt import Workbook
book = Workbook()

def form1():
    CADET_DETAILS = ['Enrolment_Number','Aadhar_Number', 'student_Name', "Fathers_Name", "Mothers_Name", 'Sex',
                     'Date_Of_Birth', 'Address', 'Email', 'Mobile_Number', 'Blood_Group', 'Institution',
                     'Unit']
    sql = """select """
    for i in range(len(CADET_DETAILS)):
        sql=sql+CADET_DETAILS[i]
        if i!=len(CADET_DETAILS)-1:
            sql=sql+","
    sql=sql+" from enrolment where "
    return(sql)

def form2():
    YOGA_DAY = ['Rank', 'Student_name', "Fathers_Name", 'Unit', 'Institution', 'Date_Of_Birth', 'Remarks']

    sql = """select """
    for i in range(len(YOGA_DAY)):
        sql=sql+YOGA_DAY[i]
        if i!= len(YOGA_DAY)-1:
            sql = sql + ","
    sql = sql + " from enrolment where "
    return (sql)

def form3():
    Enrolment_Nominal_roll = ['Unit', 'Enrolment_Number', 'Rank', 'Student_name', "Fathers_name",
                                  "Date_of_Birth","Institution", 'Address', 'Mobile_Number', 'Aadhar_Number',
                                  'Bank_Name', 'Branch', 'IFSC_code','Account_Name', 'Account_Number', 'MICR',
                                  'Certificate','Camps_Attended', 'Extra_Curricular_Activities',
                                  'Special_Achievements','Email','Blood_Group','Remarks']
    sql = """select """
    for i in range(len(Enrolment_Nominal_roll)):
        sql = sql + Enrolment_Nominal_roll[i]
        if i!= len(Enrolment_Nominal_roll) - 1:
            sql = sql + ","
    sql = sql + " from enrolment where "
    return (sql)

def form4():
    Camp_Nominal_roll = ['Enrolment_Number','Aadhar_Number','Rank', 'student_Name', "Fathers_Name",'Address',
                             'Institution', 'Vegitarian','Bank_Name','Branch',
                             'Account_Name','Account_Number','IFSC_Code']
    sql = """select """
    for i in range(len(Camp_Nominal_roll)):
        sql = sql + Camp_Nominal_roll[i]
        if i != len(Camp_Nominal_roll) - 1:
            sql = sql + ","
    sql = sql + " from enrolment where "
    return (sql)


def form5():
    Scholarship_NR = ['Enrolment_Number','Rank', 'Unit','Institution','Bank_Name','Branch','Account_Name',
                         'Account_Number','IFSC_Code','MICR']
    sql = """select """
    for i in range(len(Scholarship_NR)):
        sql = sql + Scholarship_NR[i]
        if i != len(Scholarship_NR) - 1:
            sql = sql + ","
    sql = sql + " from enrolment where "
    return (sql)

def form6():
    A_certe_NR_for_High_school_JDJW=['Enrolment_Number','Rank', 'student_Name', "Fathers_Name",
                           "Date_Of_Birth", 'Enrol_Date']
    sql = """select """
    for i in range(len(A_certe_NR_for_High_school_JDJW)):
        sql = sql + A_certe_NR_for_High_school_JDJW[i]
        if i != len(A_certe_NR_for_High_school_JDJW) - 1:
            sql = sql + ","
    sql = sql + " from enrolment where "
    return (sql)


def form7():
    B_certe_NR_SDSW =['Enrolment_Number', 'Rank', 'student_Name', "Fathers_Name",
                           "Date_Of_Birth", 'Enrol_Date']
    sql = """select """
    for i in range(len(B_certe_NR_SDSW)):
        sql = sql + B_certe_NR_SDSW[i]
        if i != len(B_certe_NR_SDSW) - 1:
            sql = sql + ","
    sql = sql + " from enrolment where "
    return (sql)


def form8():
    C_certe_NR_SDSW=['Enrolment_Number', 'Rank', 'student_Name', "Fathers_Name",
                           "Date_Of_Birth", 'Enrol_Date']
    sql = """select """
    for i in range(len(C_certe_NR_SDSW)):
        sql = sql + C_certe_NR_SDSW[i]
        if i != len(C_certe_NR_SDSW) - 1:
            sql = sql + ","
    sql = sql + " from enrolment where "
    return (sql)


