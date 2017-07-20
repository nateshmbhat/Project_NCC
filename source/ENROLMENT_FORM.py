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
        details="""create table  if not exists enrolment(Enrolment_Number varchar(13) not null,Rank varchar(25) not null,Aadhaar_Number varchar(14),
        Student_First_name varchar not null,Student_Middle_Name varchar,Student_Last_Name varchar,Student_Name varchar not null,
        Fathers_First_Name varchar,Fathers_Middle_Name varchar,Fathers_Last_Name varchar,Fathers_Name varchar,Mothers_First_Name varchar,
        Mothers_Middle_Name varchar,Mothers_Last_Name varchar,Mothers_Name varchar ,Sex char(6),Date_Of_Birth date,
        Address varchar(200) not null,Email varchar(50)  default '',Mobile_Number varchar(10) ,Blood_Group char(3),Certificate char(4),
        Camps_Attended varchar(4) default '',Extra_Curricular_Activities varchar(50) default '',Special_Achievements varchar(50) default '',
        Enrol_Date date,Remarks varchar(50) default '',Vegitarian char(7) not null,Bank_Name varchar(30) default '',
        Branch varchar(35) default '',Account_Name varchar(50) default '',Account_Number varchar(16),IFSC_Code varchar(11),MICR varchar(9),
        Institution char(50) not null  default '',Unit varchar(20) not null  default '',primary key(Enrolment_Number))"""
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
    def delete_by_Enrolment_cert(self, enrolment_no, cert_name):
        sql = "delete from Attendance where Enrolment_Number='" + enrolment_no + "' and certificate='" + cert_name + "'"
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        self.conn.commit()
        self.conn.close()