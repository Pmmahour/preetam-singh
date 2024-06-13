import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
def productshowscreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Stock Management System')
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select productid,pcatid,pname,priceperunit,openqty,currqty from products"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])
            xf.append(res[5])
        db.close()
    def firstdata():
        global i
        i=0
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
    def nextdata():
        global i
        i=i+1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
    def prevdata():
        global i
        i=i-1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
    def lastdata():
        global i
        i=len(xa)-1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])

    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Products Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)    
    
    a=Label(t,text='Product Id',font=20,bg='pink')
    a.place(x=80,y=100)
    aa=Entry(t,width=40)
    aa.place(x=180,y=100)
    
    b=Label(t,text='Pcat Id',font=20,bg='pink')
    b.place(x=80,y=150)
    bb=Entry(t,width=40)
    bb.place(x=180,y=150)
    c=Label(t,text='PName',font=20,bg='pink')
    c.place(x=80,y=200)
    cc=Entry(t,width=40)
    cc.place(x=180,y=200)
    d=Label(t,text='Price per Unit',font=20,bg='pink')
    d.place(x=80,y=250)
    dd=Entry(t,width=40)
    dd.place(x=180,y=250)
    e=Label(t,text='Open Qty',font=20,bg='pink')
    e.place(x=80,y=300)
    ee=Entry(t,width=40)
    ee.place(x=180,y=300)
    f=Label(t,text='Current Qty',font=20,bg='pink')
    f.place(x=80,y=350)
    ff=Entry(t,width=40)
    ff.place(x=180,y=350)
    
    b2=Button(t,text='First',command=firstdata,width=8,bg='light grey')
    b2.place(x=100,y=400)
    b3=Button(t,text='Next',command=nextdata,width=8,bg='light grey')
    b3.place(x=200,y=400)
    b4=Button(t,text='Prev',command=prevdata,width=8,bg='light grey')
    b4.place(x=300,y=400)
    b5=Button(t,text='Last',command=lastdata,width=8,bg='light grey')
    b5.place(x=400,y=400)
    
    filldata()
    t.mainloop()
