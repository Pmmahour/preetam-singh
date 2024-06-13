import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql 
import smtplib
import openpyxl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
t=tkinter.Tk()
t.geometry('800x800')
def storesavescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    def checkdata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select count(*) from store where storeid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
            messagebox.showinfo('Hi','OK pls go ahead')
        else:
            messagebox.showerror('Hi','You cannot enter')        
        db.close()
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0 or len(ff.get())==0 or len(gg.get())==0:
            messagebox.showerror('hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=bb.get()
            xc=cc.get()
            xd=dd.get()
            xe=ee.get()
            xf=ff.get()
            xg=gg.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="insert into store values(%d,'%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf,xg) 
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Saved')
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            ff.delete(0,100)
            gg.delete(0,100)
    def close():
        t.destroy()
        
    a=Label(c2,text='STORE ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Entry(c2,width=30,font=('times new roman',12))
    aa.place(x=275,y=100)
    btf=Button(c2,text='CHECK',font=('times new roman bold',11),bg='orange',command=checkdata)
    btf.place(x=540,y=100)
    b=Label(c2,text='NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Entry(c2,width=30,font=('times new roman',12))
    bb.place(x=275,y=150)
    c=Label(c2,text='ADDRESS',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Entry(c2,width=30,font=('times new roman',12))
    cc.place(x=275,y=200)
    d=Label(c2,text='CITY',font=('times new roman bold',13))
    d.place(x=100,y=250)
    dd=Entry(c2,width=30,font=('times new roman',12))
    dd.place(x=275,y=250)
    e=Label(c2,text='EMAIL',font=('times new roman bold',13))
    e.place(x=100,y=300)
    ee=Entry(c2,width=30,font=('times new roman',12))
    ee.place(x=275,y=300)
    f=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
    f.place(x=100,y=350)
    ff=Entry(c2,width=30,font=('times new roman',12))
    ff.place(x=275,y=350)
    g=Label(c2,text='REGISTRATION NO.',font=('times new roman bold',13))
    g.place(x=100,y=400)
    gg=Entry(c2,width=30,font=('times new roman',12))
    gg.place(x=275,y=400)
    
    
    h=Button(c2,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
    h.place(x=305,y=450)
    j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=385,y=450)
def storedeletescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select storeid from store"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
        
    def delete():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="delete from store where storeid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Deleted')    
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
    def close():
        t.destroy()
    
    a=Label(c2,text='STORE ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(c2,font=('times new roman',12))
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
         
    h=Button(c2,text='DELETE',font=('times new roman bold',11),bg='red',command=delete)
    h.place(x=200,y=200)
    j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=315,y=200)
def storeupdatescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    
    def close():
        t.destroy()
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select storeid from store"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select name,address,city,email,phone,regisno from store where storeid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        gg.insert(0,data[5])
        db.close()
    def updatedata():
        xa=int(aa.get())
        xb=bb.get()
        xc=cc.get()
        xd=dd.get()
        xe=ee.get()
        xf=ff.get()
        xg=gg.get()
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update store set name='%s',address='%s',city='%s',email='%s',phone='%s',regisno='%s' where storeid=%d"%(xb,xc,xd,xe,xf,xg,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','updated')
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)

    
    a=Label(c2,text='STORE ID',font=('times new roman bold',12),bg='pink')
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,width=37)
    aa.place(x=350,y=100)
    filldata()
    aa['values']=xt
    b1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),bg='orange')
    b1.place(x=450,y=100)
    b=Label(c2,text='NAME',font=('times new roman bold',13),bg='pink')
    b.place(x=100,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='ADDRESS',font=('times new roman bold',13),bg='pink')
    c.place(x=100,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='CITY',font=('times new roman bold',13),bg='pink')
    d.place(x=100,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='EMAIL',font=('times new roman bold',13),bg='pink')
    e.place(x=100,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='PHONE',font=('times new roman bold',13),bg='pink')
    f.place(x=100,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    g=Label(c2,text='REGIST.No',font=('times new roman bold',13),bg='pink')
    g.place(x=100,y=400)
    gg=Entry(c2,width=40)
    gg.place(x=200,y=400)
    h=Button(c2,text='UPDATE',font=('times new roman bold',11),fg='white',bg='blue',command=updatedata)
    h.place(x=150,y=450)
    j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=250,y=450)

def storefindscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)

    def new():
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
    
    def close():
        t.destroy()
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select storeid from store"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select name,address,city,email,phone,regisno from store where storeid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        gg.insert(0,data[5])
        db.close()

      
    a=Label(c2,text='STORE ID',font=('times new roman bold',12),bg='pink')
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,width=37)
    aa.place(x=350,y=100)
    filldata()
    aa['values']=xt
    b1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',11),bg='orange')
    b1.place(x=450,y=100)
    b=Label(c2,text='NAME',font=('times new roman bold',13),bg='pink')
    b.place(x=100,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='ADDRESS',font=('times new roman bold',13),bg='pink')
    c.place(x=100,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='CITY',font=('times new roman bold',13),bg='pink')
    d.place(x=100,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='EMAIL',font=('times new roman bold',13),bg='pink')
    e.place(x=100,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='PHONE',font=('times new roman bold',13),bg='pink')
    f.place(x=100,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    g=Label(c2,text='REGIST.No',font=('times new roman bold',13),bg='pink')
    g.place(x=100,y=400)
    gg=Entry(c2,width=40)
    gg.place(x=200,y=400)
    h=Button(c2,text='NEW',font=('times new roman bold',11),fg='white',bg='orange',command=new)
    h.place(x=150,y=450)
    j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=250,y=450)    

def storeshowscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
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

   
    a=Label(c2,text='STORE ID',font=('times new roman bold',12),fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=200,y=100)
    btf=Button(c2,text='FIRST',command=firstdata,width=8,font=('times new roman bold',12),fg='white', bg='orange')
    btf.place(x=120,y=450)
    b=Label(c2,text='NAME',font=('times new roman bold',12),fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='ADDRESS',font=('times new roman bold',12),fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='CITY',font=('times new roman bold',12),fg='black',bg='pink')
    d.place(x=100,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='EMAIL',font=('times new roman bold',12),fg='black',bg='pink')
    e.place(x=100,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='PHONE',font=('times new roman bold',12),fg='black',bg='pink')
    f.place(x=100,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    g=Label(c2,text='REGIST.No',font=('times new roman bold',12),fg='black',bg='pink')
    g.place(x=100,y=400)
    gg=Entry(c2,width=40)
    gg.place(x=200,y=400)
    h=Button(c2,text='NEXT',command=nextdata,width=8,font=('times new roman bold',12),fg='white', bg='green')
    h.place(x=220,y=450)
    j=Button(c2,text='PREV',command=prevdata,width=8,font=('times new roman bold',12),fg='white', bg='red')
    j.place(x=320,y=450)
    k=Button(c2,text='LAST',command=lastdata,width=8,font=('times new roman bold',12),fg='white', bg='blue')
    k.place(x=420,y=450)
    filldata()
def productsavescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    def checkdata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select count(*) from products where productid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
            messagebox.showinfo('Hi','OK pls go ahead')
        else:
            messagebox.showerror('Hi','You cannot enter')        
        db.close()
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0 or let(ff.get())==0:
            messagebox.showerror('hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=int(bb.get())
            xc=cc.get()
            xd=int(dd.get())
            xe=int(ee.get())
            xf=int(ff.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="insert into products values(%d,'%d','%s','%d','%d','%d')"%(xa,xb,xc,xd,xe,xf) 
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Saved')
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            ff.delete(0,100)
    def close():
        t.destroy()
    
    
    a=Label(c2,text='PRODUCT ID',font=('times new roman bold',12),fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=210,y=100)
    b=Label(c2,text='PCAT ID',font=('times new roman bold',12),fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=210,y=150)
    c=Label(c2,text='PNAME',font=('times new roman bold',12),fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=210,y=200)
    d=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',10),fg='black',bg='pink')
    d.place(x=100,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=210,y=250)
    e=Label(c2,text='OPEN Qty',font=('times new roman bold',12),fg='black',bg='pink')
    e.place(x=100,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=210,y=300)
    f=Label(c2,text='CURRENT Qty',font=('times new roman bold',12),fg='black',bg='pink')
    f.place(x=100,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=210,y=350)
    b1=Button(c2,text='SAVE',command=savedata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    b1.place(x=250,y=400)
    b2=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    b2.place(x=350,y=400)
    
    b2=Button(c2,text='CHECK',command=checkdata,width=8,font=('times new roman bold',12),bg='orange')
    b2.place(x=460,y=100)

def productdeletescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def deletedata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')#common step
        cur=db.cursor()#common step
        sql="delete from products where productid=%d" %(xa) 
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        aa.delete(0,100)
    def close():
        t.destroy()
    a=Label(c2,text='PRODUCT ID',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(t,width=37)
    aa.place(x=350,y=100)
    filldata()
    aa['values']=xt
    b1=Button(c2,text='DELETE',command=deletedata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    b1.place(x=200,y=150)
    b2=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    b2.place(x=300,y=150)
def productupdatescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select productid from products"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid,pname,priceperunit,openqty,currqty from products where productid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        db.close()
    def updatedata():
        xa=int(aa.get())
        xb=int(bb.get())
        xc=cc.get()
        xd=int(dd.get())
        xe=int(ee.get())
        xf=int(ff.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update products set pcatid='%d',pname='%s',priceperunit='%d',openqty='%d',currqty='%d' where productid=%d"%(xb,xc,xd,xe,xf,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','updated')
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100) 
    
    def close():
        t.destroy()
  
    a=Label(c2,text='PRODUCT ID',font=('times new roman bold',12),bg='pink')
    a.place(x=80,y=100)
    aa=ttk.Combobox(t,width=36)
    aa.place(x=332,y=100)
    filldata()
    aa['values']=xt
    b1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),bg='orange')
    b1.place(x=430,y=100)
    b=Label(c2,text='PCAT ID',font=('times new roman bold',12),bg='pink')
    b.place(x=80,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=180,y=150)
    c=Label(c2,text='PNAME',font=('times new roman bold',12),bg='pink')
    c.place(x=80,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=180,y=200)
    d=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',10),bg='pink')
    d.place(x=80,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=180,y=250)
    e=Label(c2,text='OPEN Qty',font=('times new roman bold',12),bg='pink')
    e.place(x=80,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=180,y=300)
    f=Label(c2,text='CURRENT Qty',font=('times new roman bold',10),bg='pink')
    f.place(x=80,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=180,y=350)
    b2=Button(c2,text='UPDATE',command=updatedata,width=8,font=('times new roman bold',12),fg='white',bg='Blue')
    b2.place(x=200,y=400)
    b3=Button(c2,text='CLOSE',command=close,width=8, font=('times new roman bold',12),fg='white',bg='purple')
    b3.place(x=300,y=400)

def productfindscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select productid from products"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid,pname,priceperunit,openqty,currqty from products where productid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        db.close()
    def new():
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
    
    def close():
        t.destroy()
    
    a=Label(c2,text='PRODUCT ID',font=('times new roman bold',12),bg='pink')
    a.place(x=80,y=100)
    aa=ttk.Combobox(t,width=36)
    aa.place(x=332,y=100)
    filldata()
    aa['values']=xt
    b1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),bg='orange')
    b1.place(x=430,y=100)
    b=Label(c2,text='PCAT ID',font=('times new roman bold',12),bg='pink')
    b.place(x=80,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=180,y=150)
    c=Label(c2,text='PNAME',font=('times new roman bold',12),bg='pink')
    c.place(x=80,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=180,y=200)
    d=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',10),bg='pink')
    d.place(x=80,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=180,y=250)
    e=Label(c2,text='OPEN Qty',font=('times new roman bold',12),bg='pink')
    e.place(x=80,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=180,y=300)
    f=Label(c2,text='CURRENT Qty',font=('times new roman bold',10),bg='pink')
    f.place(x=80,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=180,y=350)
    b2=Button(c2,text='NEW',command=new,width=8,font=('times new roman bold',12),fg='white', bg='orange')
    b2.place(x=200,y=400)
    b3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white', bg='purple')
    b3.place(x=300,y=400)

def productshowscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
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

    a=Label(c2,text='PRODUCT ID',font=('times new roman bold',12),bg='pink')
    a.place(x=80,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=200,y=100)
    
    b=Label(c2,text='PCAT ID',font=('times new roman bold',12),bg='pink')
    b.place(x=80,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PNAME',font=('times new roman bold',12),bg='pink')
    c.place(x=80,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',10),bg='pink')
    d.place(x=80,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='OPEN Qty',font=('times new roman bold',12),bg='pink')
    e.place(x=80,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='CURRENT Qty',font=('times new roman bold',12),bg='pink')
    f.place(x=80,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    
    b2=Button(c2,text='FIRST',command=firstdata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    b2.place(x=100,y=400)
    b3=Button(c2,text='NEXT',command=nextdata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    b3.place(x=200,y=400)
    b4=Button(c2,text='PREV',command=prevdata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    b4.place(x=300,y=400)
    b5=Button(c2,text='LAST',command=lastdata,width=8,font=('times new roman bold',12),fg='white',bg='blue')
    b5.place(x=400,y=400)
    filldata()

def productcatsavescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    def checkdata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select count(*) from productcat where pcatid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
            messagebox.showinfo('Hi','OK pls go ahead')
        else:
            messagebox.showerror('Hi','You cannot enter')        
        db.close()
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0:
            messagebox.showerror('hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=bb.get()
            xc=cc.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="insert into productcat values(%d,'%s','%s')"%(xa,xb,xc) 
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Saved')
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
    def close():
        t.destroy()

    a=Label(c2,text='PCAT ID',font=('times new roman bold',12),fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=200,y=100)
    btf=Button(c2,text='CHECK',command=checkdata,width=8,font=('times new roman bold',12),bg='orange')
    btf.place(x=450,y=100)
    b=Label(c2,text='CAT-NAME',font=('times new roman bold',12),fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='DESCRIPTION',font=('times new roman bold',10),fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    
    h=Button(c2,text='SAVE',command=savedata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    h.place(x=150,y=250)
    j=Button(c2,text='CLOSE',command=close,width=8, font=('times new roman bold',12),fg='white',bg='purple')
    j.place(x=250,y=250)

def productcatdeletescreen():
    
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    
    def deletedata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')#common step
        cur=db.cursor()#common step
        sql="delete from productcat where pcatid=%d" %(xa) 
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        aa.delete(0,100)
   
    a=Label(c2,text='PCAT ID:',font=('times new roman bold',12),fg='black',bg='pink')
    a.place(x=100,y=200)
    aa=ttk.Combobox(t,width=35)
    aa.place(x=350,y=200)
    filldata()
    aa['values']=xt
    h=Button(c2,text='DELETE',command=deletedata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    h.place(x=200,y=250)
    i=Button(c2,text='Close',width=8,font=('times new roman bold',12),fg='white',bg='purple')
    i.place(x=320,y=250)

def productcatupdatescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    def close():
        t.destroy()
    
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid from productcat"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select catname,description from productcat where pcatid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        db.close()
    def updatedata():
        xa=int(aa.get())
        xb=bb.get()
        xc=cc.get()
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update productcat set catname='%s',description='%s' where pcatid=%d"%(xb,xc,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','updated')
        bb.delete(0,100)
        cc.delete(0,100)
   
    a=Label(c2,text='PCAT ID',font=('times new roman bold',12),fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,width=37)
    aa.place(x=350,y=100)
    filldata()
    aa['values']=xt
    b1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),bg='orange')
    b1.place(x=450,y=100)
    b=Label(c2,text='CAT-NAME',font=('times new roman bold',12),fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='DESCRIPTION',font=('times new roman bold',11),fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    b2=Button(c2,text='UPDATE',command=updatedata,width=8,font=('times new roman bold',12),fg='white',bg='blue')
    b2.place(x=250,y=250)
    b3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    b3.place(x=350,y=250) 

def productcatfindscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid from productcat"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select catname,description from productcat where pcatid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        db.close()
    def new():
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
    
    def close():
        t.destroy()    
   
    a=Label(c2,text='PCAT ID',font=('times new roman bold',12),fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    b1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),bg='orange')
    b1.place(x=450,y=100)
    b=Label(c2,text='CAT-NAME',font=('times new roman bold',12),fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='DESCRIPTION',font=('times new roman bold',10),fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    b2=Button(c2,text='NEW',command=new,width=8, font=('times new roman bold',12),fg='white',bg='orange')
    b2.place(x=250,y=250)
    b3=Button(c2,text='CLOSE',command=close,font=('times new roman bold',12),fg='white',bg='purple')
    b3.place(x=350,y=250)

def productcatshowscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
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
    def close():
        t.destroy()
   
    a=Label(c2,text='PCAT ID',font=('times new roman bold',12),fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=200,y=100)
    b=Label(c2,text='CAT-NAME',font=('times new roman bold',12),fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='DESCRIPTION',font=('times new roman bold',10),fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    b1=Button(c2,text='FIRST',command=firstdata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    b1.place(x=100,y=250)
    b2=Button(c2,text='NEXT',command=nextdata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    b2.place(x=200,y=250)
    b3=Button(c2,text='LAST',command=lastdata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    b3.place(x=300,y=250)
    b4=Button(c2,text='PREVIOUS',command=prevdata,width=8,font=('times new roman bold',12),fg='white',bg='blue')
    b4.place(x=400,y=250)
    b5=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    b5.place(x=500,y=250)
    filldata()

def suppliersavescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    def checkdata():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select count(*) from supplier where supplierid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('Hi','OK pls go ahead')
            else:
                messagebox.showerror('Hi','You cannot enter')        
            db.close()

    def close():
        t.destroy()
    
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0 or len(ff.get())==0 or len(gg.get())==0:
                messagebox.showerror('hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=bb.get()
            xc=cc.get()
            xd=dd.get()
            xe=ee.get()

            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="insert into supplier values(%d,'%s','%s','%s','%s')"%(xa,xb,xc,xd,xe)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','saved')
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            db.close()
    a=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',11),bg='pink')
    a.place(x=90,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=170,y=100)
    b=Label(c2,text='SNAME:',font=('times new roman bold',11),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=170,y=150)
    c=Label(c2,text='ADDRESS:',font=('times new roman bold',11),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=170,y=200)
    d=Label(c2,text='PHONE:',font=('times new roman bold',11),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=170,y=250)
    e=Label(c2,text='EMAIL:',font=('times new roman bold',11),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=170,y=300)
    bt1=Button(c2,text='CHECK',command=checkdata,width=8,font=('times new roman bold',11),bg='orange')
    bt1.place(x=420,y=100)
    bt2=Button(c2,text='SAVE',command=savedata,width=8,font=('times new roman bold',11),fg='white',bg='green')
    bt2.place(x=170,y=370)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',11),fg='white',bg='purple')
    bt3.place(x=300,y=370)
    
def supplierdeletescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select supplierid from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()

    def deletedata():
        xa=int(aa.get())

        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="delete from supplier where supplierid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','deleted')
        
    def close():
        t.destroy()

    a=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',10),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=180,y=100)
    filldata()
    aa['values']=xt
    bt2=Button(c2,text='DELETE',command=deletedata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    bt2.place(x=150,y=150)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=250,y=150)
    
def supplierupdatescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select supplierid from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select sname,address,phone,email from supplier where supplierid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        db.close()
    
    def update():
        xa=int(aa.get())
        xb=bb.get()
        xc=cc.get()
        xd=dd.get()
        xe=ee.get()
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update supplier set sname='%s',address='%s',phone='%s',email='%s' where supplierid=%d"%(xb,xc,xd,xe,xa)
        cur.execute(sql)
        data=cur.fetchall()
        db.commit()
        
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        db.close()
        messagebox.showinfo('hi','data updated')
    def close():
        t.destroy()
    

    a=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',10),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=170,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='SNAME:',font=('times new roman bold',11),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=170,y=150)
    c=Label(c2,text='ADDRESS:',font=('times new roman bold',11),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=170,y=200)
    d=Label(c2,text='PHONE:',font=('times new roman bold',11),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=170,y=250)
    e=Label(c2,text='EMAIL:',font=('times new roman bold',11),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=170,y=300)
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',11),bg='orange')
    bt1.place(x=430,y=100)
    bt2=Button(c2,text='UPDATE',command=update,width=8,font=('times new roman bold',11),fg='white',bg='blue')
    bt2.place(x=170,y=370)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',11),fg='white',bg='purple')
    bt3.place(x=300,y=370)

def supplierfindscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    def new():
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
    def close():
        t.destroy()
    
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select supplierid from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select sname,address,phone,email from supplier where supplierid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        db.close()

    a=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',10),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=170,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='SNAME:',font=('times new roman bold',11),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=170,y=150)
    c=Label(c2,text='ADDRESS:',font=('times new roman bold',11),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=170,y=200)
    d=Label(c2,text='PHONE:',font=('times new roman bold',11),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=170,y=250)
    e=Label(c2,text='EMAIL:',font=('times new roman bold',11),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=170,y=300)
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',11),bg='orange')
    bt1.place(x=430,y=100)
    bt2=Button(c2,text='NEW',command=new,width=8,font=('times new roman bold',11),fg='white',bg='orange')
    bt2.place(x=170,y=370)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',11),fg='white',bg='purple')
    bt3.place(x=300,y=370)
    
def suppliershowscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select supplierid,sname,address,phone,email from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])
            
        db.close()
    def firstdata():
        global i
        i=0
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
    def nextdata():
        global i
        i=i+1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
    def prevdata():
        global i
        i=i-1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
    def lastdata():
        global i
        i=len(xa)-1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
    
    a=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',10),bg='pink')
    a.place(x=90,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=170,y=100)
    b=Label(c2,text='SNAME:',font=('times new roman bold',11),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=170,y=150)
    c=Label(c2,text='ADDRESS:',font=('times new roman bold',11),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=170,y=200)
    d=Label(c2,text='PHONE:',font=('times new roman bold',11),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=170,y=250)
    e=Label(c2,text='EMAIL:',font=('times new roman bold',11),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=170,y=300)
    bt1=Button(c2,text='FIRST',command=firstdata,width=8,font=('times new roman bold',11),fg='white',bg='orange')
    bt1.place(x=100,y=370)
    bt2=Button(c2,text='NEXT',command=nextdata,width=8,font=('times new roman bold',11),fg='white',bg='green')
    bt2.place(x=200,y=370)
    bt3=Button(c2,text='PREV',command=prevdata,width=8,font=('times new roman bold',11),fg='white',bg='red')
    bt3.place(x=300,y=370)
    bt4=Button(c2,text='LAST',command=lastdata,width=8,font=('times new roman bold',11),fg='white',bg='blue')
    bt4.place(x=400,y=370)
    filldata()

def stockinshowscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
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
        sql="select stockinid,supplierid,pcatid,productid,datein,qty from stockin"
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
   
    a=Label(c2,text='STOCK ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=200,y=100)
    b=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='DATE IN:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    bt1=Button(c2,text='FIRST',command=firstdata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt1.place(x=100,y=400)
    bt2=Button(c2,text='NEXT',command=nextdata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    bt2.place(x=200,y=400)
    bt3=Button(c2,text='PREV',command=prevdata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    bt3.place(x=300,y=400)
    bt4=Button(c2,text='LAST',command=lastdata,width=8,font=('times new roman bold',12),fg='white',bg='blue')
    bt4.place(x=400,y=400)
    filldata()

def stockinsavescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)

    def checkdata():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select count(*) from stockin where stockinid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('Hi','OK pls go ahead')
            else:
                messagebox.showerror('Hi','You cannot enter')        
            db.close()
    def close():
        t.destroy()
    
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0 or len(ff.get())==0:
                messagebox.showerror('hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=int(bb.get())
            xc=int(cc.get())
            xd=int(dd.get())
            xe=ee.get()
            xf=int(ff.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="insert into stockin values(%d,%d,%d,%d,'%s',%d)"%(xa,xb,xc,xd,xe,xf)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','saved')
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            ff.delete(0,100)
    
    a=Label(c2,text='STOCK ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=200,y=100)
    b=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT ID',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODUCT ID',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='DATE IN:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    bt1=Button(c2,text='CHECK',command=checkdata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt1.place(x=450,y=100)
    bt2=Button(c2,text='SAVE',command=savedata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    bt2.place(x=150,y=400)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=250,y=400)

def stockindeletescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select stockinid from stockin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def deletedata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="delete from stockin where stockinid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','deleted')
        
    def close():
        t.destroy()
    a=Label(c2,text='STOCKIN ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    bt2=Button(c2,text='DELETE',command=deletedata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    bt2.place(x=180,y=150)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=270,y=150)

def stockinupdatescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    def update():
        xa=int(aa.get())
        xb=int(bb.get())
        xc=int(cc.get())
        xd=int(dd.get())
        xe=ee.get()
        xf=int(ff.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update stockin set supplierid=%d,pcatid=%d,productid=%d,datein='%s',qty=%d where stockinid=%d"%(xb,xc,xd,xe,xf,xa)
        cur.execute(sql)
        
        #data=cur.fetchall()
        db.commit()
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        db.close()
        messagebox.showinfo('hi','data updated')
    def close():
        t.destroy()
    
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select stockinid from stockin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select supplierid,pcatid,productid,datein,qty from stockin where stockinid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()

        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        db.close()
    
    a=Label(c2,text='STOCK ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='DATEIN:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),bg='orange')
    bt1.place(x=450,y=100)
    bt2=Button(c2,text='UPDATE',command=update,width=8,font=('times new roman bold',12),fg='white',bg='blue')
    bt2.place(x=200,y=400)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=350,y=400)    

def stockinfindscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    def new():
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)

    def close():
        t.destroy()
    
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select stockinid from stockin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select supplierid,pcatid,productid,datein,qty from stockin where stockinid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        db.close()
    
    a=Label(c2,text='STOCK ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='DATEIN:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt1.place(x=450,y=100)
    bt2=Button(c2,text='NEW',command=new,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt2.place(x=200,y=400)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=350,y=400)    

def customersavescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)

    def checkdata():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select count(*) from customers where custid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('Hi','OK pls go ahead')
            else:
                messagebox.showerror('Hi','You cannot enter')        
            db.close()
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0:
                messagebox.showerror('hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=bb.get()
            xc=cc.get()
            xd=dd.get()
            xe=ee.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="insert into customers values(%d,'%s','%s','%s','%s')"%(xa,xb,xc,xd,xe)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','saved')
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            db.close()
    def close():
        t.destroy()
    
    a=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=170,y=100)
    b=Label(c2,text='CNAME:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=170,y=150)
    c=Label(c2,text='ADDRESS:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=170,y=200)
    d=Label(c2,text='PHONE:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=170,y=250)
    e=Label(c2,text='EMAIL:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=170,y=300)
    bt1=Button(c2,text='CHECK',command=checkdata,width=8,font=('times new roman bold',12),bg='orange')
    bt1.place(x=430,y=100)
    bt2=Button(c2,text='SAVE',command=savedata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    bt2.place(x=170,y=370)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=300,y=370)    

def customerdeletescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def deletedata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="delete from customers where custid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','deleted')
    def close():
        t.destroy()
    a=Label(c2,text='CUST.ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=170,y=100)
    filldata()
    aa['values']=xt
    bt2=Button(c2,text='DELETE',command=deletedata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    bt2.place(x=150,y=150)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=250,y=150)

def customerupdatescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)

    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select cname,address,phone,email from customers where custid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        db.close()
    def update():
        xa=int(aa.get())
        xb=bb.get()
        xc=cc.get()
        xd=dd.get()
        xe=ee.get()
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update customers set cname='%s',address='%s',phone='%s',email='%s' where custid=%d"%(xb,xc,xd,xe,xa)
        cur.execute(sql)
        data=cur.fetchall()
        db.commit()
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        db.close()
        messagebox.showinfo('hi','data updated')
    def close():
        t.destroy()
        
    a=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=170,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='C NAME:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=170,y=150)
    c=Label(c2,text='ADDRESS:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=170,y=200)
    d=Label(c2,text='PHONE:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=170,y=250)
    e=Label(c2,text='EMAIL:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=170,y=300)
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),bg='orange')
    bt1.place(x=430,y=100)
    bt2=Button(c2,text='UPDATE',command=update,width=8,font=('times new roman bold',12),fg='white',bg='blue')
    bt2.place(x=170,y=370)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=300,y=370)

def customerfindscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)

    def new():
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
    def close():
        t.destroy()
    
    xt=[]
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select cname,address,phone,email from customers where custid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        db.close()
    a=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=170,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='CNAME:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=170,y=150)
    c=Label(c2,text='ADDRESS:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=170,y=200)
    d=Label(c2,text='PHONE:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=170,y=250)
    e=Label(c2,text='EMAIL:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=170,y=300)
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt1.place(x=430,y=100)
    bt2=Button(c2,text='NEW',command=new,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt2.place(x=170,y=370)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=300,y=370)

def customershowscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid,cname,address,phone,email from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])
            
        db.close()
    def firstdata():
        global i
        i=0
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
    def nextdata():
        global i
        i=i+1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
    def prevdata():
        global i
        i=i-1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
    def lastdata():
        global i
        i=len(xa)-1
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        aa.insert(0, xa[i])
        bb.insert(0, xb[i])
        cc.insert(0, xc[i])
        dd.insert(0, xd[i])
        ee.insert(0, xe[i])
    
    a=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=170,y=100)
    b=Label(c2,text='CNAME:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=170,y=150)
    c=Label(c2,text='ADDRESS:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=170,y=200)
    d=Label(c2,text='PHONE:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=170,y=250)
    e=Label(c2,text='EMAIL:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=170,y=300)
    bt1=Button(c2,text='FIRST',command=firstdata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt1.place(x=100,y=370)
    bt2=Button(c2,text='NEXT',command=nextdata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    bt2.place(x=200,y=370)
    bt3=Button(c2,text='PREV',command=prevdata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    bt3.place(x=300,y=370)
    bt4=Button(c2,text='LAST',command=lastdata,width=8,font=('times new roman bold',12),fg='white',bg='blue')
    bt4.place(x=400,y=370)
    filldata()
    
def customersendmailscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)

    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select cname,address,phone,email from customers where custid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        db.close()
    def sendmail():
        from_address ="preetamsingh00001@gmail.com"
        to_address = ee.get()

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] ="Customer Bill"
        msg['From'] = from_address
        msg['To'] = to_address
        # Create the message (HTML).
        html =ff.get()

        # Record the MIME type - text/html.
        part1 = MIMEText(html, 'html')

        # Attach parts into message container
        msg.attach(part1)

        # Credentials
        username = 'preetamsingh00001@gmail.com'  
        password = 'rowvnalckrmjktvb'
        # Sending the email
        ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()
        messagebox.showinfo('hi','mail is send')
               
    def close():
        t.destroy()
        
    a=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=170,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='C NAME:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=170,y=150)
    c=Label(c2,text='ADDRESS:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=170,y=200)
    d=Label(c2,text='PHONE:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=170,y=250)
    e=Label(c2,text='EMAIL:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=170,y=300)
    f=Label(c2,text='MESSAGE',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=170,y=350)
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),bg='orange')
    bt1.place(x=430,y=100)
    bt2=Button(c2,text='SEND MAIL',command=sendmail,width=12,font=('times new roman bold',12),fg='white',bg='blue')
    bt2.place(x=170,y=420)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=300,y=420)

def ordersavescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    def checkdata():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select count(*) from orders where orderid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('Hi','OK pls go ahead')
            else:
                messagebox.showerror('Hi','You cannot enter')        
            db.close()
    
    def close():
        t.destroy()
    
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0 or len(ff.get())==0 or len(gg.get())==0:
                messagebox.showerror('hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=int(bb.get())
            xc=int(cc.get())
            xd=int(dd.get())
            xe=ee.get()
            xf=int(ff.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="insert into orders values(%d,%d,%d,%d,'%s',%d)"%(xa,xb,xc,xd,xe,xf)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','saved')
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            ff.delete(0,100)
    
    a=Label(c2,text='ORDER ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=200,y=100)
    b=Label(c2,text='CUST.ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODCUT.ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='DATEofORDER:',font=('times new roman bold',10),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    bt1=Button(c2,text='CHECK',command=checkdata,width=8,font=('times new roman bold',12),bg='orange')
    bt1.place(x=450,y=100)
    bt2=Button(c2,text='SAVE',command=savedata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    bt2.place(x=200,y=420)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=350,y=420)

def orderdeletescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select orderid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def deletedata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="delete from orders where orderid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','deleted')
        
    def close():
        t.destroy()
    a=Label(c2,text='ORDER ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    bt2=Button(c2,text='DELETE',command=deletedata,font=('times new roman bold',12),fg='white',bg='red')
    bt2.place(x=200,y=150)
    bt3=Button(c2,text='Close',command=close,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=330,y=150)

def orderupdatescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)

    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select orderid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid,pcatid,productid,dateoforder,qty from orders where orderid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        db.close()
        
    def update():
        xa=int(aa.get())
        xb=int(bb.get())
        xc=int(cc.get())
        xd=int(dd.get())
        xe=ee.get()
        xf=int(ff.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update orders set custid=%d,pcatid=%d,productid=%d,dateoforder='%s',qty=%d where orderid='%d'"%(xb,xc,xd,xe,xf,xa)
        cur.execute(sql)
        data=cur.fetchall()
        db.commit()
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        db.close()
        messagebox.showinfo('hi','data updated')
    def close():
        t.destroy()    

    a=Label(c2,text='ORDER ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=50,y=50)
    aa=ttk.Combobox(c2,width=27)
    aa.place(x=200,y=50)
    filldata()
    aa['values']=xt
    b=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=50,y=90)
    bb=Entry(c2,width=30)
    bb.place(x=200,y=90)
    c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=50,y=130)
    cc=Entry(c2,width=30)
    cc.place(x=200,y=130)
    d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=50,y=170)
    dd=Entry(c2,width=30)
    dd.place(x=200,y=170)
    e=Label(c2,text='DATE OF ORDER:',font=('times new roman bold',12),bg='pink')
    e.place(x=50,y=210)
    ee=Entry(c2,width=30)
    ee.place(x=200,y=210)
    f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    f.place(x=50,y=250)
    ff=Entry(c2,width=30)
    ff.place(x=200,y=250)
    bt1=Button(c2,text='FIND',command=finddata,font=('times new roman bold',12),bg='orange')
    bt1.place(x=400,y=50)
    bt2=Button(c2,text='UPDATE',command=update,font=('times new roman bold',12),bg='blue')
    bt2.place(x=200,y=320)
    bt3=Button(c2,text='CLOSE',command=close,font=('times new roman bold',12),bg='purple')
    bt3.place(x=330,y=320)

def orderfindscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    def new():
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
    def close():
        t.destroy()
    
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select orderid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid,pcatid,productid,dateoforder,qty from orders where orderid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        db.close()
    
    a=Label(c2,text='ORDER ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='CUST.ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT.ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='DATEOFORDER:',font=('times new roman bold',10),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),bg='orange')
    bt1.place(x=450,y=100)
    bt2=Button(c2,text='NEW',command=new,width=8,font=('times new roman bold',12),bg='orange')
    bt2.place(x=200,y=420)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),bg='purple')
    bt3.place(x=330,y=420)

def ordershowscreen(): 
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
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
        sql="select orderid,custid,pcatid,productid,dateoforder,qty from orders"
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
    a=Label(c2,text='ORDER ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=200,y=100)
    b=Label(c2,text='CUST.ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT.ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='DATEOFORDER:',font=('times new roman bold',10),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    bt1=Button(c2,text='FIRST',command=firstdata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt1.place(x=100,y=420)
    bt2=Button(c2,text='NEXT',command=nextdata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    bt2.place(x=200,y=420)
    bt3=Button(c2,text='PREVIOUS',command=prevdata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    bt3.place(x=300,y=420)
    bt4=Button(c2,text='LAST',command=lastdata,width=8,font=('times new roman bold',12),fg='white',bg='blue')
    bt4.place(x=400,y=420)
    filldata()

def dispatchsavescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)

    def checkdata():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select count(*) from dispatchbill where dispatchid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('Hi','OK pls go ahead')
            else:
                messagebox.showerror('Hi','You cannot enter')        
            db.close()
    def close():
        t.destroy()
    
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0 or len(ff.get())==0 or len(gg.get())==0:
                messagebox.showerror('hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=int(bb.get())
            xc=int(cc.get())
            xd=int(dd.get())
            xe=ee.get()
            xf=ff.get()
            xg=int(gg.get())
            xh=int(hh.get())
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="insert into dispatchbill values(%d,%d,%d,%d,'%s','%s',%d,%d)"%(xa,xb,xc,xd,xe,xf,xg,xh)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','saved')
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            ff.delete(0,100)
            gg.delete(0,100)
            hh.delete(0,100)
    
    a=Label(c2,text='DISPATCH ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=200,y=100)
    b=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PROD.ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='PNAME:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='DATEOFBILL:',font=('times new roman bold',10),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    g=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    g.place(x=90,y=400)
    gg=Entry(c2,width=40)
    gg.place(x=200,y=400)
    h=Label(c2,text='BILL:',font=('times new roman bold',12),bg='pink')
    h.place(x=90,y=450)
    hh=Entry(c2,width=40)
    hh.place(x=200,y=450)
    bt1=Button(c2,text='CHECK',command=checkdata,width=8,font=('times new roman bold',12),bg='orange')
    bt1.place(x=450,y=100)
    bt2=Button(c2,text='SAVE',command=savedata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    bt2.place(x=200,y=500)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=300,y=500)

def dispatchdeletescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)

    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select dispatchid from dispatchbill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def deletedata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="delete from dispatchbill where dispatchid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','deleted')
    def close():
        t.destroy()
    a=Label(c2,text='DISPATCH ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=40)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    bt2=Button(c2,text='DELETE',command=deletedata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    bt2.place(x=200,y=180)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=300,y=180)

def dispatchupdatescreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    def update():
        xa=int(aa.get())
        xb=int(bb.get())
        xc=int(cc.get())
        xd=int(dd.get())
        xe=ee.get()
        xf=ff.get()
        xg=int(gg.get())
        xh=int(hh.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update dispatchbill set custid=%d,pcatid=%d,productid=%d,pname='%s',dateofbill='%s',qty=%d,bill=%d where dispatchid=%d"%(xb,xc,xd,xe,xf,xg,xh,xa)
        cur.execute(sql)
        data=cur.fetchall()
        db.commit()
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        hh.delete(0,100)
        db.close()
        messagebox.showinfo('hi','data updated')
    def close():
        t.destroy()
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select dispatchid from dispatchbill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid,pcatid,productid,pname,dateofbill,qty,bill from dispatchbill where dispatchid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        hh.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        gg.insert(0,data[5])
        hh.insert(0,data[6])
        db.close()
    
    a=Label(c2,text='DISPATCH ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='PNAME:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='DATEOFBILL',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    g=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    g.place(x=90,y=400)
    gg=Entry(c2,width=40)
    gg.place(x=200,y=400)
    h=Label(c2,text='BILL:',font=('times new roman bold',12),bg='pink')
    h.place(x=90,y=450)
    hh=Entry(c2,width=40)
    hh.place(x=200,y=450)
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt1.place(x=450,y=100)
    bt2=Button(c2,text='UPDATE',command=update,width=8,font=('times new roman bold',12),fg='white',bg='blue')
    bt2.place(x=200,y=500)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=320,y=500)

def dispatchfindscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)

    def new():
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        hh.delete(0,100)
    def close():
        t.destroy()
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select dispatchid from dispatchbill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid,pcatid,productid,pname,dateofbill,qty,bill from dispatchbill where dispatchid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        hh.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        gg.insert(0,data[5])
        hh.insert(0,data[6])
        db.close()
    a=Label(c2,text='DISPATCH ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='PNAME:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='DATEOFBILL',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    g=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    g.place(x=90,y=400)
    gg=Entry(c2,width=40)
    gg.place(x=200,y=400)
    h=Label(c2,text='BILL:',font=('times new roman bold',12),bg='pink')
    h.place(x=90,y=450)
    hh=Entry(c2,width=40)
    hh.place(x=200,y=450)
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),bg='orange')
    bt1.place(x=450,y=100)
    bt2=Button(c2,text='NEW',command=new,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt2.place(x=200,y=500)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=300,y=500)

def dispatchshowscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
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
    
    a=Label(c2,text='DISPATCH ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=Entry(c2,width=40)
    aa.place(x=200,y=100)
    b=Label(c2,text='CUST ID',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='PNAME:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='DATEOFBILL:',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    g=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    g.place(x=90,y=400)
    gg=Entry(c2,width=40)
    gg.place(x=200,y=400)
    h=Label(c2,text='BILL:',font=('times new roman bold',12),bg='pink')
    h.place(x=90,y=450)
    hh=Entry(c2,width=40)
    hh.place(x=200,y=450)
    bt1=Button(c2,text='FIRST',command=firstdata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt1.place(x=100,y=500)
    bt2=Button(c2,text='NEXT',command=nextdata,width=8,font=('times new roman bold',12),fg='white',bg='green')
    bt2.place(x=200,y=500)
    bt3=Button(c2,text='PREVIOUS',command=prevdata,width=8,font=('times new roman bold',12),fg='white',bg='red')
    bt3.place(x=300,y=500)
    bt4=Button(c2,text='LAST',command=lastdata,width=8,font=('times new roman bold',12),fg='white',bg='blue')
    bt4.place(x=400,y=500)
    filldata()

def dispatchsendbillscreen():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    
    def sendmail():
        from_address ="preetamsingh00001@gmail.com"
        to_address = ii.get()

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] ="Customer Bill"
        msg['From'] = from_address
        msg['To'] = to_address
        # Create the message (HTML).
        html =hh.get()

        # Record the MIME type - text/html.
        part1 = MIMEText(html, 'html')

        # Attach parts into message container
        msg.attach(part1)

        # Credentials
        username = 'preetamsingh00001@gmail.com'  
        password = 'rowvnalckrmjktvb'
        # Sending the email
        ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()
        messagebox.showinfo('hi','mail is send')
               
    def close():
        t.destroy()
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select dispatchid from dispatchbill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid,pcatid,productid,pname,dateofbill,qty,bill from dispatchbill where dispatchid='%d'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        hh.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        gg.insert(0,data[5])
        hh.insert(0,data[6])
        db.close()
    
    a=Label(c2,text='DISPATCH ID:',font=('times new roman bold',12),bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(c2,width=37)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    b=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
    b.place(x=90,y=150)
    bb=Entry(c2,width=40)
    bb.place(x=200,y=150)
    c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
    c.place(x=90,y=200)
    cc=Entry(c2,width=40)
    cc.place(x=200,y=200)
    d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
    d.place(x=90,y=250)
    dd=Entry(c2,width=40)
    dd.place(x=200,y=250)
    e=Label(c2,text='PNAME:',font=('times new roman bold',12),bg='pink')
    e.place(x=90,y=300)
    ee=Entry(c2,width=40)
    ee.place(x=200,y=300)
    f=Label(c2,text='DATEOFBILL',font=('times new roman bold',12),bg='pink')
    f.place(x=90,y=350)
    ff=Entry(c2,width=40)
    ff.place(x=200,y=350)
    g=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
    g.place(x=90,y=400)
    gg=Entry(c2,width=40)
    gg.place(x=200,y=400)
    h=Label(c2,text='BILL:',font=('times new roman bold',12),bg='pink')
    h.place(x=90,y=450)
    hh=Entry(c2,width=40)
    hh.place(x=200,y=450)
    i=Label(c2,text='EMAIL Add',font=('times new roman bold',12),bg='pink')
    i.place(x=90,y=500)
    ii=Entry(c2,width=40)
    ii.place(x=200,y=500)
    
    bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
    bt1.place(x=450,y=100)
    bt2=Button(c2,text='SEND BILL',command=sendmail,width=10,font=('times new roman bold',12),fg='white',bg='blue')
    bt2.place(x=200,y=550)
    bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
    bt3.place(x=320,y=550)

    
def storebuttons():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    lblstore=Label(c2,text='STORE DATABASE',font=('times new roman bold',20),fg='blue', bg='pink')
    lblstore.place(x=220,y=10)
    b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=storesavescreen)
    b1.place(x=300,y=60)
    b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=storedeletescreen)
    b2.place(x=300,y=120)
    b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=storeupdatescreen)
    b3.place(x=300,y=180)
    b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=storefindscreen)
    b4.place(x=300,y=240)
    b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=storeshowscreen)
    b5.place(x=300,y=300)    

def productbuttons():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    lblproduct=Label(c2,text='PRODUCTS DATABASE',font=('times new roman bold',20),fg='blue', bg='pink')
    lblproduct.place(x=220,y=10)
    b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=productsavescreen)
    b1.place(x=300,y=60)
    b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=productdeletescreen)
    b2.place(x=300,y=120)
    b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=productupdatescreen)
    b3.place(x=300,y=180)
    b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=productfindscreen)
    b4.place(x=300,y=240)
    b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=productshowscreen)
    b5.place(x=300,y=300)

def productcatbuttons():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    lblpcat=Label(c2,text='PRODUCT CATEGORY DATABASE',font=('times new roman bold',20),fg='blue', bg='pink')
    lblpcat.place(x=150,y=10)
    b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=productcatsavescreen)
    b1.place(x=300,y=60)
    b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=productcatdeletescreen)
    b2.place(x=300,y=120)
    b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=productcatupdatescreen)
    b3.place(x=300,y=180)
    b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=productcatfindscreen)
    b4.place(x=300,y=240)
    b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=productcatshowscreen)
    b5.place(x=300,y=300)

def supplierbuttons():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    lblsupp=Label(c2,text='SUPPLIER DATABASE',font=('times new roman bold',20),fg='blue', bg='pink')
    lblsupp.place(x=220,y=10)
    b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=suppliersavescreen)
    b1.place(x=300,y=60)
    b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=supplierdeletescreen)
    b2.place(x=300,y=120)
    b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=supplierupdatescreen)
    b3.place(x=300,y=180)
    b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=supplierfindscreen)
    b4.place(x=300,y=240)
    b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=suppliershowscreen)
    b5.place(x=300,y=300)

def stockinregbuttons():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    lblstockin=Label(c2,text='STOCKIN DATABASE',font=('times new roman bold',20),fg='blue', bg='pink')
    lblstockin.place(x=220,y=10)
    b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=stockinsavescreen)
    b1.place(x=300,y=60)
    b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=stockindeletescreen)
    b2.place(x=300,y=120)
    b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=stockinupdatescreen)
    b3.place(x=300,y=180)
    b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=stockinfindscreen)
    b4.place(x=300,y=240)
    b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=stockinshowscreen)
    b5.place(x=300,y=300)

def customerbuttons():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    lblcust=Label(c2,text='CUSTOMER DATABASE',font=('times new roman bold',20),fg='blue', bg='pink')
    lblcust.place(x=220,y=10)
    b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=customersavescreen)
    b1.place(x=300,y=60)
    b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=customerdeletescreen)
    b2.place(x=300,y=120)
    b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=customerupdatescreen)
    b3.place(x=300,y=180)
    b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=customerfindscreen)
    b4.place(x=300,y=240)
    b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=customershowscreen)
    b5.place(x=300,y=300)
    b6=Button(c2,text='SEND MAIL',font=('times new roman bold',15),fg='white',bg='purple',command=customersendmailscreen)
    b6.place(x=300,y=360)

def ordersbuttons():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    lblorder=Label(c2,text='ORDER DATABASE',font=('times new roman bold',20),fg='blue', bg='pink')
    lblorder.place(x=220,y=10)
    b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=ordersavescreen)
    b1.place(x=300,y=60)
    b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=orderdeletescreen)
    b2.place(x=300,y=120)
    b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=orderupdatescreen)
    b3.place(x=300,y=180)
    b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=orderfindscreen)
    b4.place(x=300,y=240)
    b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=ordershowscreen)
    b5.place(x=300,y=300)

def dispatchbillbuttons():
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
    lbldispatch=Label(c2,text='DISPATCH BILL DATABASE',font=('times new roman bold',20),fg='blue', bg='pink')
    lbldispatch.place(x=200,y=10)
    b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=dispatchsavescreen)
    b1.place(x=300,y=60)
    b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=dispatchdeletescreen)
    b2.place(x=300,y=120)
    b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=dispatchupdatescreen)
    b3.place(x=300,y=180)
    b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=dispatchfindscreen)
    b4.place(x=300,y=240)
    b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=dispatchshowscreen)
    b5.place(x=300,y=300)
    b6=Button(c2,text='SEND BILL',font=('times new roman bold',15),fg='white',bg='purple',command=dispatchsendbillscreen)
    b6.place(x=300,y=360)

    
c1=Canvas(t,height=800,width=150,bg='aquamarine')
c1.place(x=0,y=0)
c2=Canvas(t,height=800,width=650,bg='pink')
c2.place(x=150,y=0)
sms=Label(t,text='Welcome Stock Management System',font=('times new roman bold',22),bg='pink',fg='black')
sms.place(x=220,y=250)

b1=Button(c1,text='Store',fg='White',bg='orange',font=('arial',15),command=storebuttons)
b1.place(x=10,y=10)
b2=Button(c1,text='Products',fg='White',bg='green',font=('arial',15),command=productbuttons)
b2.place(x=10,y=60)
b3=Button(c1,text='Product Cat.',fg='White',bg='red',font=('arial',15),command=productcatbuttons)
b3.place(x=10,y=110)
b4=Button(c1,text='Supplier',fg='White',bg='blue',font=('arial',15),command=supplierbuttons)
b4.place(x=10,y=160)
b5=Button(c1,text='Stock In Reg.',fg='White',bg='gold',font=('arial',15),command=stockinregbuttons)
b5.place(x=10,y=210)
b6=Button(c1,text='Customer',fg='White',bg='sky blue',font=('arial',15),command=customerbuttons)
b6.place(x=10,y=260)
b7=Button(c1,text='Orders',fg='White',bg='sea green',font=('arial',15),command=ordersbuttons)
b7.place(x=10,y=310)
b8=Button(c1,text='Dispacth Bill',fg='White',bg='orange red',font=('arial',15),command=dispatchbillbuttons)
b8.place(x=10,y=360)
t.mainloop()