import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
def productcatshowscreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Product Category')
    xa=[]
    xb=[]
    xc=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid,catname,description from productcat"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
        db.close()
    def firstdata():
        global i
        i=0
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
    def nextdata():
        global i
        i=i+1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
    def prevdata():
        global i
        i=i-1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
    def lastdata():
        global i
        i=len(xa)-1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Store Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
    
    a=Label(t,text='Pcat id',font=20,fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=Entry(t,width=40)
    aa.place(x=200,y=100)
    
    b=Label(t,text='Cat-name',font=20,fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(t,width=40)
    bb.place(x=200,y=150)
    c=Label(t,text='Description',font=20,fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(t,width=40)
    cc.place(x=200,y=200)
    
    b1=Button(t,text='First',command=firstdata,width=8,bg='light grey')
    b1.place(x=100,y=250)
    b2=Button(t,text='Next',command=nextdata,width=8,bg='light grey')
    b2.place(x=200,y=250)
    b3=Button(t,text='Last',command=lastdata,width=8,bg='light grey')
    b3.place(x=300,y=250)
    b4=Button(t,text='Previous',command=prevdata,width=8,bg='light grey')
    b4.place(x=400,y=250)
    b5=Button(t,text='Close',width=8,bg='light grey')
    b5.place(x=500,y=250)
    filldata()
    t.mainloop()
