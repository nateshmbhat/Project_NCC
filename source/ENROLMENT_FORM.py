import sqlite3


class enroll:
    conn = sqlite3.connect("ncc.db")
    cur = conn.cursor()
    def enrol_student(self,*fields):
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
    def dropping_table(self,table_name):
        self.cur.execute("drop table %s",(table_name))
        self.conn.commit()
        print(table_name+"sucessfully deleted")
    def search_by_field(self,field,id):
        sql="select * from enrolment where "+field+"='"+id+"'"
        self.cur.execute(sql)
        return(self.cur.fetchone())
    def create_table_Enrolment(self):
        details="""create table  if not exists enrolment(Enrolment_Number varchar(13) not null,Rank varchar(25) not null,Aadhar_Number bigint(12),
        student_Name varchar(30) not null,Fathers_Name varchar(30) not null,Mothers_Name varchar(30) not null,Sex char(6),Date_Of_Birth date,
        Address varchar(200) not null,Email varchar(50)  default '',Mobile_Number bigint(10) ,Blood_Group char(3),Certificate char(4),
        Camps_Attended varchar(4) default '',Extra_Curricular_Activities varchar(50) default '',Special_Achievements varchar(50) default '',
        Enrol_Date date,Remarks varchar(50) default '',Vegitarian char(7) not null,Bank_Name varchar(30) default '',
        Branch varchar(20) default '',Account_Name varchar(50) default '',Account_Number bigint(16),IFSC_Code varchar(11),MICR bigint(9),
        Institution char(20) not null  default '',Unit varchar(10) not null  default '',primary key(Enrolment_Number))"""
        self.cur.execute(details)
        print("table created sucessfully")
        self.conn.commit()

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
        self.cur.execute(sql)
        return(self.cur.fetchall())