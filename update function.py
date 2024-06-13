import pymysql
import tkinter
import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
t=tkinter.Tk()
t.geometry('1200x900')

t.title('My Tkinter')

xt=[]
def filldata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='mydb')
    cur=db.cursor()
    sql="select empno from empdata"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        xt.append(res[0])
    db.close()
def finddata():
    xa=int(aa.get())
    db=pymysql.connect(host='localhost',user='root',password='root',database='mydb')
    cur=db.cursor()
    sql="select name,city,salary from empdata where empno=%d"%(xa)
    cur.execute(sql)
    data=cur.fetchone()
    cc.delete(0,100)
    dd.delete(0,100)
    ee.delete(0,100)
    cc.insert(0,data[0])
    dd.insert(0,data[1])
    ee.insert(0,data[2])
    db.close()
def updatedata():
    xa=int(aa.get())
    xb=cc.get()
    xc=dd.get()
    xd=int(ee.get())
    db=pymysql.connect(host='localhost',user='root',password='root',database='mydb')
    cur=db.cursor()
    sql="update empdata set name='%s',city='%s',salary=%d where empno=%d"%(xb,xc,xd,xa)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo('hi','updated')
    cc.delete(0,100)
    dd.delete(0,100)
    ee.delete(0,100)
    
a=Label(t,text='Emp No.')
a.place(x=100,y=200)
aa=ttk.Combobox(t)
aa.place(x=200,y=200)
filldata()
aa['values']=xt
b=Button(t,text='Find',command=finddata)
b.place(x=100,y=250)
c=Label(t,text='Name')
c.place(x=100,y=300)
cc=Entry(t,width=30)
cc.place(x=200,y=300)
d=Label(t,text='City')
d.place(x=100,y=350)
dd=Entry(t,width=30)
dd.place(x=200,y=350)
e=Label(t,text='Salary')
e.place(x=100,y=400)
ee=Entry(t,width=30)
ee.place(x=200,y=400)
f=Button(t,text='Update',command=updatedata)
f.place(x=100,y=450)
g=Button(t,text='Close')
g.place(x=200,y=450)

t.mainloop()