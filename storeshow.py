import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def storeshowscreen():
        
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Store')
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    xg=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select storeid,name,address,city,email,phone,regisno from store"
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
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
        gg.insert(0, xg[i])
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
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
        gg.insert(0, xg[i])
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
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
        gg.insert(0, xg[i])
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
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
        ff.insert(0, xf[i])
        gg.insert(0, xg[i])
    
    
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Store Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
    
    a=Label(t,text='Store id',font=20,fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=Entry(t,width=40)
    aa.place(x=200,y=100)
    btf=Button(t,text='First',command=firstdata,width=8,bg='light grey')
    btf.place(x=120,y=450)
    b=Label(t,text='Name',font=20,fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(t,width=40)
    bb.place(x=200,y=150)
    c=Label(t,text='Address',font=20,fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(t,width=40)
    cc.place(x=200,y=200)
    d=Label(t,text='City',font=20,fg='black',bg='pink')
    d.place(x=100,y=250)
    dd=Entry(t,width=40)
    dd.place(x=200,y=250)
    e=Label(t,text='Email',font=20,fg='black',bg='pink')
    e.place(x=100,y=300)
    ee=Entry(t,width=40)
    ee.place(x=200,y=300)
    f=Label(t,text='Phone',font=20,fg='black',bg='pink')
    f.place(x=100,y=350)
    ff=Entry(t,width=40)
    ff.place(x=200,y=350)
    g=Label(t,text='Regist.no',font=20,fg='black',bg='pink')
    g.place(x=100,y=400)
    gg=Entry(t,width=40)
    gg.place(x=200,y=400)
    h=Button(t,text='Next',command=nextdata,width=8,bg='light grey')
    h.place(x=220,y=450)
    j=Button(t,text='Prev',command=prevdata,width=8,bg='light grey')
    j.place(x=320,y=450)
    k=Button(t,text='Prev',command=prevdata,width=8,bg='light grey')
    k.place(x=420,y=450)
    filldata()
    t.mainloop()
