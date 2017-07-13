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
        print(add)
        self.cur.execute(add)
        self.conn.commit()
        print("sucessfully inserted")
        self.conn.close()


    def update_student_details(self ,*fields):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        add = "update enrolment set Enrolment_Number='{0}',Rank='{1}',Aadhar_Number='{2}',Student_Name='{3}',Fathers_Name='{4}',Mothers_Name='{5}' ,Sex='{6}',Date_Of_Birth='{7}', Address = '{8}' ,Email='{9}' , Mobile_Number='{10}' , Blood_Group='{11}' ,Certificate='{12}' ,Camps_Attended='{13}' ,Extra_Curricular_Activities='{14}', Special_Achievements='{15}' , Enrol_Date='{16}' ,Remarks='{17}', Vegitarian='{18}' , Bank_Name='{19}', Branch='{20}' ,Account_Name='{21}',  Account_Number='{22}',   IFSC_Code='{23}',  MICR='{24}',  Institution='{25}',  Unit='{26}'  where Enrolment_Number='{0}'".format(fields[0],fields[1],fields[2],fields[3],fields[4],fields[5],fields[6],fields[7],fields[8],fields[9],fields[10],fields[11],fields[12],fields[13],fields[14],fields[15],fields[16],fields[17],fields[18],fields[19],fields[20],fields[21],fields[22],fields[23],fields[24],fields[25],fields[26],fields[0])
        print(add)
        self.cur.execute(add)
        self.conn.commit()
        self.conn.close()

    def dropping_table(self,table_name):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        self.cur.execute("drop table "+table_name)
        self.conn.commit()
        print(table_name+" sucessfully deleted")
        self.conn.close()

    def search_by_field(self,field,id):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        sql="select * from enrolment where "+field+"='"+id+"'"
        self.cur.execute(sql)
        return(self.cur.fetchone())

    def create_table_Enrolment(self):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        details="""create table  if not exists enrolment(Enrolment_Number varchar(13) not null,Rank varchar(25) not null,Aadhaar_Number varchar(14),
        Student_Name varchar(30) not null,Fathers_Name varchar(30) not null,Mothers_Name varchar(30) not null,Sex char(6),Date_Of_Birth date,
        Address varchar(200) not null,Email varchar(50)  default '',Mobile_Number varchar(10) ,Blood_Group char(3),Certificate char(4),
        Camps_Attended varchar(4) default '',Extra_Curricular_Activities varchar(50) default '',Special_Achievements varchar(50) default '',
        Enrol_Date date,Remarks varchar(50) default '',Vegitarian char(7) not null,Bank_Name varchar(30) default '',
        Branch varchar(35) default '',Account_Name varchar(50) default '',Account_Number varchar(16),IFSC_Code varchar(11),MICR varchar(9),
        Institution char(50) not null  default '',Unit varchar(20) not null  default '',primary key(Enrolment_Number))"""
        self.cur.execute(details)
        print("table created sucessfully")
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
        print("table created sucessfully")
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
        print("table created sucessfully")
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
        print("table created sucessfully")
        self.conn.commit()
        self.conn.close()
    def create_table_Attendance(self):
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        sql = """create table if not exist Attendance(Enrolment_Number varchar(13) not null,
        ,primary key(Enrolment_Number))"""
        self.cur.execute(sql)
        print("table created sucessfully")
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
        print("sucessfully inserted")
        self.conn.close()
    def delete_by_Enrolment(self,table,enrolment_no):
        sql="delete from "+table +" where Enrolment_Number='"+enrolment_no+"'"
        self.conn = sqlite3.connect("ncc.db")
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        self.conn.commit()
        print("sucessfully deleted")
        self.conn.close()