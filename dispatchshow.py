import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def dispatchshowscreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Dispatchbill')
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    xg=[]
    xh=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select dispatchid,custid,pcatid,productid,pname,dateofbill,qty,bill from dispatchbill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])
            xf.append(res[5])
            xg.append(res[6])
            xh.append(res[7])
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
        gg.delete(0,100)
        hh.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
        gg.insert(0, xg[i])
        hh.insert(0, xh[i])
         
    def nextdata():
        global i
        i=i+1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        hh.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
        gg.insert(0, xg[i])
        hh.insert(0, xh[i])
        
    def prevdata():
        global i
        i=i-1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        hh.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
        gg.insert(0, xg[i])
        hh.insert(0, xh[i])
        
    def lastdata():
        global i
        i=len(xa)-1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        hh.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
        gg.insert(0, xg[i])
        hh.insert(0, xh[i])
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Dispatch Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)

    a=Label(t,text='Dispt.id:',font=20,bg='pink')
    a.place(x=90,y=100)
    aa=Entry(t,width=40)
    aa.place(x=170,y=100)
    b=Label(t,text='Cust id:',font=20,bg='pink')
    b.place(x=90,y=150)
    bb=Entry(t,width=40)
    bb.place(x=170,y=150)
    c=Label(t,text='pcat id:',font=20,bg='pink')
    c.place(x=90,y=200)
    cc=Entry(t,width=40)
    cc.place(x=170,y=200)
    d=Label(t,text='Prod.id:',font=20,bg='pink')
    d.place(x=90,y=250)
    dd=Entry(t,width=40)
    dd.place(x=170,y=250)
    e=Label(t,text='Pname:',font=20,bg='pink')
    e.place(x=90,y=300)
    ee=Entry(t,width=40)
    ee.place(x=170,y=300)
    f=Label(t,text='Date.bill:',font=20,bg='pink')
    f.place(x=90,y=350)
    ff=Entry(t,width=40)
    ff.place(x=170,y=350)
    g=Label(t,text='Qty:',font=20,bg='pink')
    g.place(x=90,y=400)
    gg=Entry(t,width=40)
    gg.place(x=170,y=400)
    h=Label(t,text='Bill:',font=20,bg='pink')
    h.place(x=90,y=450)
    hh=Entry(t,width=40)
    hh.place(x=170,y=450)
    bt1=Button(t,text='First',command=firstdata,width=8,bg='light grey')
    bt1.place(x=100,y=500)
    bt2=Button(t,text='Next',command=nextdata,width=8,bg='light grey')
    bt2.place(x=200,y=500)
    bt3=Button(t,text='Prev',command=prevdata,width=8,bg='light grey')
    bt3.place(x=300,y=500)
    bt4=Button(t,text='Last',command=lastdata,width=8,bg='light grey')
    bt4.place(x=400,y=500)
    filldata()
    t.mainloop()