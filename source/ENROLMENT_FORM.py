import sqlite3


class enroll:

    def enrol_student(self,*fields):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        add = "insert into enrolment values("
        for i in range(len(fields)):
            add=add+"'"+str(fields[i])+"'"
            if i!=len(fields)-1:
                add=add+","
        add=add+")"
        self.cur.execute(add)
        self.conn.commit()
        self.conn.close()
    def update_student_details(self ,*fields):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        delete = "delete from enrolment where Enrolment_Number='{}'".format(fields[0])
        self.execute(delete);
        self.enrol_student(fields)
    def dropping_table(self,table_name):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        self.cur.execute("drop table "+table_name)
        self.conn.commit()
        self.conn.close()
    def search_by_field(self,field,id):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        sql="select * from enrolment where "+field+"='"+id+"'"
        self.cur.execute(sql)
        result = self.cur.fetchone()
        self.conn.close()
        return(result)
    def create_table_Enrolment(self):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        details="""create table  if not exists enrolment(
        Enrolment_Number varchar not null,
        Rank varchar not null,
        Aadhaar_Number varchar unique,
        Student_First_name varchar not null,
        Student_Middle_Name varchar default '',
        Student_Last_Name varchar default '',
        Student_Name varchar not null,
        Fathers_First_Name varchar default '',
        Fathers_Middle_Name varchar default '',
        Fathers_Last_Name varchar default '',
        Fathers_Name varchar default '',
        Mothers_First_Name varchar default '',
        Mothers_Middle_Name varchar default '',
        Mothers_Last_Name varchar default '',
        Mothers_Name varchar default '',
        Sex char(6),
        Date_Of_Birth date,
        Address varchar not null,
        Email varchar  default '',
        Mobile_Number varchar ,
        Blood_Group char,
        Nearest_Railway_Station varchar default '',
        Nearest_Police_Station varchar default '',
        Education varchar default '',
        Education_Marks varchar default '',
        Identification_mark varchar default '',
        Criminal_Court varchar default '',
        Name_of_School_College varchar default '',
        Enroll_Permission varchar default '',
        Earlier_candidate varchar default '',
        Earlier_Enrolment_Number default '',
        Dismissed varchar default '',
        Certificate char(4),
        Camps_Attended varchar default '',
        Extra_Curricular_Activities varchar default '',
        Special_Achievements varchar default '',
        Enrol_Date date,Remarks varchar default '',
        Meal_Preference char not null,
        Bank_Name varchar default '',
        Branch varchar default '',
        Account_Name varchar default '',
        Account_Number varchar default '',
        IFSC_Code varchar default '',
        MICR varchar default '',
        Pan_Number varchar default '',
        Institution char not null  default '',
        Unit varchar not null  default '',
        Seniority varchar default '',
        primary key(Enrolment_Number))"""
        self.cur.execute(details)
        self.conn.commit()
        self.conn.close()
    def create_table_camps(self):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        details = """create table if not exists camps_details(Enrolment_Number varchar(13) not null,Camp_Attended varchar,
        Location varchar,Started_Date date,Ended_Date date,Institution varchar)"""
        self.cur.execute(details)
        self.conn.commit()
        self.conn.close()
    def create_table_marks_A_cert(self):
        self.conn=sqlite3.connect("ncc.db")
        self.cur=self.conn.cursor()
        sql="""create table if not exists A_cert_marks(Enrolment_Number varchar(13) not null,Roll_Number varchar,
        Rank varchar,Student_Name varchar,Fathers_Name varchar,Date_Of_Birth date,Enrol_Date date,Camps_Attended varchar,
        Date_Of_Discharge date,Parade_Attendance_Year1 varchar,Parade_Attendance_Year2 varchar,Part1_Drill_Written varchar,
        Part1_Drill_Practical varchar,Part1_Drill_Total varchar,Part2_WT_Written varchar,Part2_WT_Practical varchar,
        Part2_WT_Total varchar,Part3_Misc_Written varchar,Part4_SplSubjects_Written varchar,Part4_SplSubjects_Practical varchar,
        Part4_SplSubjects_Total varchar,GrandTotal varchar,Grading varchar,Institution varchar,primary key(Enrolment_Number))"""
        self.cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    def create_table_marks_B_cert(self):
        self.conn=sqlite3.connect("ncc.db")
        self.cur=self.conn.cursor()
        sql="""create table if not exists B_cert_marks(Enrolment_Number varchar(13) not null,Roll_Number varchar(8),
        Rank varchar,Student_Name varchar,Fathers_Name varchar,Date_Of_Birth date,Enrol_Date date,Camps_Attended varchar,
        Date_Of_Discharge date,Parade_Attendance_Year1 varchar,Parade_Attendance_Year2 varchar,Part1_Drill_Written varchar,
        Part1_Drill_Practical varchar,Part1_Drill_Total varchar,Part2_WT_Written varchar,Part2_WT_Practical varchar,
        Part2_WT_Total varchar,Part3_Misc_Written varchar,Part4_SplSubjects_Written varchar,Part4_SplSubjects_Practical varchar,
        Part4_SplSubjects_Total varchar,Bonus_Marks_Certificate varchar,GrandTotal varchar,Grading varchar,Institution varchar,primary key(Enrolment_Number))"""
        self.cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    def create_table_marks_C_cert(self):
        self.conn=sqlite3.connect("ncc.db")
        self.cur=self.conn.cursor()
        sql="""create table if not exists C_cert_marks(Enrolment_Number varchar(13) not null,Roll_Number varchar(8),
        Rank varchar,Student_Name varchar,Fathers_Name varchar,Date_Of_Birth date,Enrol_Date date,Camps_Attended varchar,
        Date_Of_Discharge date,Parade_Attendance_Year1 varchar,Parade_Attendance_Year2 varchar,Part1_Drill_Written varchar,
        Part1_Drill_Practical varchar,Part1_Drill_Total varchar,Part2_WT_Written varchar,Part2_WT_Practical varchar,
        Part2_WT_Total varchar,Part3_Misc_Written varchar,Part4_SplSubjects_Written varchar,Part4_SplSubjects_Practical varchar,
        Part4_SplSubjects_Total varchar,Bonus_Marks_Certificate intvarchar,GrandTotal varchar,Grading varchar,Institution varchar,primary key(Enrolment_Number))"""
        self.cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    def create_table_Attendance(self):
        self.conn=sqlite3.connect("ncc.db")
        self.cur=self.conn.cursor()
        sql="""create table if not exists Attendance(
        Enrolment_Number varchar,
        certificate varchar,
        institution varchar,
        eligability varchar,
        year varchar,
        A_cert_attendance_1_year integer,
        A_cert_attendance_2_year integer,
        B_cert_attendance_1_year integer,
        B_cert_attendance_2_year integer,
        C_cert_attendance_1_year integer,
        C_cert_attendance_2_year integer,
        A_cert_attendance_1_year_total_days integer,
        A_cert_attendance_2_year_total_days integer,
        B_cert_attendance_1_year_total_days integer,
        B_cert_attendance_2_year_total_days integer,
        C_cert_attendance_1_year_total_days integer,
        C_cert_attendance_2_year_total_days integer,
        A_cert_attendance_1_year_present_days integer,
        A_cert_attendance_2_year_present_days integer,
        B_cert_attendance_1_year_present_days integer,
        B_cert_attendance_2_year_present_days integer,
        C_cert_attendance_1_year_present_days integer,
        C_cert_attendance_2_year_present_days integer)"""
        self.cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    def search_particular_fields(self,con,con1,*fields):
        sql="select "
        for i in range(len(fields)):
            if i != len(fields) and i != 0:
                sql = sql + ","
            sql = sql + fields[i]   
        sql = sql + " from enrolment"
        if (con !=0):
            sql = sql + " where Enrolment_Number='" + con1 + "'"
        self.cur.execute(sql)
        results=self.cur.fetchall()
        return(results)
    def execute(self,sql):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        return(self.cur.fetchall())
    def insertionexecute(self,sql):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    def delete_by_Enrolment(self,table,enrolment_no):
        sql="delete from "+table +" where Enrolment_Number='"+enrolment_no+"'"
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    def delete_by_Enrolment_camps(self, enrolment_no, camp_name):
        sql = "delete from camps_details where Enrolment_Number='" + enrolment_no + "' and Camp_Attended='" + camp_name + "'"
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    def delete_by_Enrolment_cert(self, enrolment_no, cert_name,year):
        sql = "delete from Attendance where Enrolment_Number='" + enrolment_no + "' and certificate='" + cert_name + "' and year='"+year+"'"
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        self.conn.commit()
        self.conn.close()