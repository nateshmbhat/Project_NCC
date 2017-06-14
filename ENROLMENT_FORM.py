import pymysql
import sqlite3


class enroll:
    conn = sqlite3.connect("ncc.db")
    cur = conn.cursor()
    def enrol_student(self,*fields):
        add = "insert into enrolment values("
        for i in range(len(fields)):
            add=add+"'"+fields[i]+"'"
            if i!=len(fields)-1:
                add=add+","
        add=add+")"
        self.cur.execute(add)
        self.conn.commit()
        print("sucessfully inserted")
    def dropping_table(self,table_name):
        self.cur.execute("drop table %s",(table_name))
        self.conn.commit()
        print(table_name+"sucessfully deleted")
    def search_by_enrolmentid(self,enrol_id):
        sql="select * from enrolment where enrolment_no="+"'"+enrol_id+"'"
        self.cur.execute(sql)
        return(self.cur.fetchone())
    def creat_table(self):
        details="""create table  if not exists enrolment(enrolment_no varchar(13) not null,aadhar bigint(12),sfname varchar(30) not null,
        smname varchar(30) default '',slname varchar(20) default '',ffname varchar(30) not null,fmname varchar(30) default '',
        flname varchar(20) default '',mfname varchar(30) not null,mmname varchar(30) default '',mlname varchar(20) default '',
        s_name varchar(50) default '',f_name varchar(50) default '',m_name varchar(50) default '',date_of_birth date,sex char(6),
        blood_group char(3),address varchar(200) not null,g_mail varchar(50)  default '',mobile bigint(10) ,bank_name varchar(30) default '',
        branch varchar(20) default '',acc_name varchar(50) default '',acc_no bigint(16),ifsc_code varchar(11),
        institution char(20) not null  default '',units varchar(10) not null  default '',primary key(enrolment_no))"""
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
            sql = sql + " where enrolment_no='" + con1 + "'"
        self.cur.execute(sql)
        results=self.cur.fetchall()
        return(results)
