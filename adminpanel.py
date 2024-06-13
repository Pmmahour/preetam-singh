import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from datetime import datetime
import datetime
import calendar
import smtplib
import openpyxl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
import pymysql 

def adminpanelscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    
    def storesavescreen():
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
        def storesave():
            email=ee.get()
            phone=ff.get()
            if '@' not in email or '.' not in email:
                messagebox.showerror("Error","Please enter a valid email")
                return
            if not phone.isdigit() or len(phone)!=10:
                messagebox.showerror("Error","Please enter a valid Mobile No.")
                return
            
            savedata()
    
        def close():
            t.destroy()
        a1=Label(c2,text='STORE SAVE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=180,y=15)    
        a=Label(c2,text='STORE ID',font=('times new roman bold',13),bg='pink')
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,width=28,font=('times new roman',12))
        aa.place(x=275,y=100)
        filldata()
        aa['values']=xt
        btf=Button(c2,text='CHECK',font=('times new roman bold',11),bg='orange',command=checkdata)
        btf.place(x=540,y=100)
        b=Label(c2,text='NAME',font=('times new roman bold',13),bg='pink')
        b.place(x=100,y=150)
        bb=Entry(c2,width=30,font=('times new roman',12))
        bb.place(x=275,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',13),bg='pink')
        c.place(x=100,y=200)
        cc=Entry(c2,width=30,font=('times new roman',12))
        cc.place(x=275,y=200)
        d=Label(c2,text='CITY',font=('times new roman bold',13),bg='pink')
        d.place(x=100,y=250)
        dd=Entry(c2,width=30,font=('times new roman',12))
        dd.place(x=275,y=250)
        e=Label(c2,text='EMAIL',font=('times new roman bold',13),bg='pink')
        e.place(x=100,y=300)
        ee=Entry(c2,width=30,font=('times new roman',12))
        ee.place(x=275,y=300)
        f=Label(c2,text='PHONE NO.',font=('times new roman bold',13),bg='pink')
        f.place(x=100,y=350)
        ff=Entry(c2,width=30,font=('times new roman',12))
        ff.place(x=275,y=350)
        g=Label(c2,text='REGISTRATION NO.',font=('times new roman bold',13),bg='pink')
        g.place(x=100,y=400)
        gg=Entry(c2,width=30,font=('times new roman',12))
        gg.place(x=275,y=400)
        
        
        h=Button(c2,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=storesave)
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
        a1=Label(c2,text='STORE DELETE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15)     
        a=Label(c2,text='STORE ID',font=('times new roman bold',13),bg='pink')
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
    
        a1=Label(c2,text='STORE UPDATE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15)     
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
        
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
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            bb.config(text=data[0])
            cc.config(text=data[1])
            dd.config(text=data[2])
            ee.config(text=data[3])
            ff.config(text=data[4])
            gg.config(text=data[5])
            db.close()
    
        a1=Label(c2,text='STORE FIND- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=180,y=15)   
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
        bb=Label(c2,width=25,font=('times new roman bold',13),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',13),bg='pink')
        c.place(x=100,y=200)
        cc=Label(c2,width=25,font=('times new roman bold',13),bg='pink')
        cc.place(x=200,y=200)
        d=Label(c2,text='CITY',font=('times new roman bold',13),bg='pink')
        d.place(x=100,y=250)
        dd=Label(c2,width=25,font=('times new roman bold',13),bg='pink')
        dd.place(x=200,y=250)
        e=Label(c2,text='EMAIL',font=('times new roman bold',13),bg='pink')
        e.place(x=100,y=300)
        ee=Label(c2,width=25,font=('times new roman bold',13),bg='pink')
        ee.place(x=200,y=300)
        f=Label(c2,text='PHONE',font=('times new roman bold',13),bg='pink')
        f.place(x=100,y=350)
        ff=Label(c2,width=25,font=('times new roman bold',13),bg='pink')
        ff.place(x=200,y=350)
        g=Label(c2,text='REGIST.No',font=('times new roman bold',13),bg='pink')
        g.place(x=100,y=400)
        gg=Label(c2,width=25,font=('times new roman bold',13),bg='pink')
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
            gg.config(text=xg[i])
        def nextdata():
            global i
            i=i+1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
            gg.config(text=xg[i])
        def prevdata():
            global i
            i=i-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
            gg.config(text=xg[i])
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
            gg.config(text=xg[i])
    
        a1=Label(c2,text='STORE SHOW- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15)   
        a=Label(c2,text='STORE ID',font=('times new roman bold',12),fg='black',bg='pink')
        a.place(x=100,y=100)
        aa=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        aa.place(x=200,y=100)
        btf=Button(c2,text='FIRST',command=firstdata,width=8,font=('times new roman bold',12),fg='white', bg='orange')
        btf.place(x=120,y=450)
        b=Label(c2,text='NAME',font=('times new roman bold',12),fg='black',bg='pink')
        b.place(x=100,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',12),fg='black',bg='pink')
        c.place(x=100,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=200,y=200)
        d=Label(c2,text='CITY',font=('times new roman bold',12),fg='black',bg='pink')
        d.place(x=100,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=200,y=250)
        e=Label(c2,text='EMAIL',font=('times new roman bold',12),fg='black',bg='pink')
        e.place(x=100,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ee.place(x=200,y=300)
        f=Label(c2,text='PHONE',font=('times new roman bold',12),fg='black',bg='pink')
        f.place(x=100,y=350)
        ff=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ff.place(x=200,y=350)
        g=Label(c2,text='REGIST.No',font=('times new roman bold',12),fg='black',bg='pink')
        g.place(x=100,y=400)
        gg=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
        xw=[]
        def filleddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select pcatid from products"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xw.append(res[0])
            db.close()                    
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
            if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0 or len(ff.get())==0:
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
        
        a1=Label(c2,text='PRODUCTS SAVE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15)     
        a=Label(c2,text='PRODUCT ID',font=('times new roman bold',12),fg='black',bg='pink')
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,width=37)
        aa.place(x=210,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='PCAT ID',font=('times new roman bold',12),fg='black',bg='pink')
        b.place(x=100,y=150)
        bb=ttk.Combobox(c2,width=37)
        bb.place(x=210,y=150)
        filleddata()
        bb['values']=xw
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
            
        a1=Label(c2,text='PRODUCTS DELETE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15) 
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
        a1=Label(c2,text='PRODUCTS UPDATE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)   
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
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            bb.config(text=data[0])
            cc.config(text=data[1])
            dd.config(text=data[2])
            ee.config(text=data[3])
            ff.config(text=data[4])
            db.close()
        def new():
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
        
        def close():
            t.destroy()
        a1=Label(c2,text='PRODUCTS FIND- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15)     
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
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=180,y=150)
        c=Label(c2,text='PNAME',font=('times new roman bold',12),bg='pink')
        c.place(x=80,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=180,y=200)
        d=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',10),bg='pink')
        d.place(x=80,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=180,y=250)
        e=Label(c2,text='OPEN Qty',font=('times new roman bold',12),bg='pink')
        e.place(x=80,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ee.place(x=180,y=300)
        f=Label(c2,text='CURRENT Qty',font=('times new roman bold',10),bg='pink')
        f.place(x=80,y=350)
        ff=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
        def nextdata():
            global i
            i=i+1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
        def prevdata():
            global i
            i=i-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
    
        a1=Label(c2,text='PRODUCTS SHOW- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15) 
        a=Label(c2,text='PRODUCT ID',font=('times new roman bold',12),bg='pink')
        a.place(x=80,y=100)
        aa=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        aa.place(x=200,y=100)
        
        b=Label(c2,text='PCAT ID',font=('times new roman bold',12),bg='pink')
        b.place(x=80,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='PNAME',font=('times new roman bold',12),bg='pink')
        c.place(x=80,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=200,y=200)
        d=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',10),bg='pink')
        d.place(x=80,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=200,y=250)
        e=Label(c2,text='OPEN Qty',font=('times new roman bold',12),bg='pink')
        e.place(x=80,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ee.place(x=200,y=300)
        f=Label(c2,text='CURRENT Qty',font=('times new roman bold',12),bg='pink')
        f.place(x=80,y=350)
        ff=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
        a1=Label(c2,text='PRODUCT-CAT SAVE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15) 
        a=Label(c2,text='PCAT ID',font=('times new roman bold',12),fg='black',bg='pink')
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,width=37)
        aa.place(x=200,y=100)
        filldata()
        aa['values']=xt
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
            sql="select pcatid from productcat"
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
    
        a1=Label(c2,text='PRODUCT-CAT DELETE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)    
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
    
        a1=Label(c2,text='PRODUCT-CAT UPDATE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=130,y=15)    
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
            bb.config(text=' ')
            cc.config(text=' ')
            bb.config(text=data[0])
            cc.config(text=data[1])
            db.close()
        def new():
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
        
        def close():
            t.destroy()    
        a1=Label(c2,text='PRODUCT-CAT FIND- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)    
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
        bb=Label(c2,width=20,font=('times new roman bold',12),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='DESCRIPTION',font=('times new roman bold',10),fg='black',bg='pink')
        c.place(x=100,y=200)
        cc=Label(c2,width=20,font=('times new roman bold',12),bg='pink')
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
        def nextdata():
            global i
            i=i+1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
        def prevdata():
            global i
            i=i-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
        def close():
            t.destroy()
        a1=Label(c2,text='PRODUCT-CAT SHOW- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)    
        a=Label(c2,text='PCAT ID',font=('times new roman bold',12),fg='black',bg='pink')
        a.place(x=100,y=100)
        aa=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        aa.place(x=200,y=100)
        b=Label(c2,text='CAT-NAME',font=('times new roman bold',12),fg='black',bg='pink')
        b.place(x=100,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='DESCRIPTION',font=('times new roman bold',10),fg='black',bg='pink')
        c.place(x=100,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
        def suppliersave():
            email=ee.get()
            phone=dd.get()
            if '@' not in email or '.' not in email:
                messagebox.showerror("Error","Please enter a valid email")
                return
            if not phone.isdigit() or len(phone)!=10:
                messagebox.showerror("Error","Please enter a valid Mobile No.")
                return
            savedata()
    
        def close():
            t.destroy()                
        a1=Label(c2,text='SUPPLIER SAVE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15) 
        a=Label(c2,text='SUPLR.ID:',font=('times new roman bold',11),bg='pink')
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
        bt1=Button(c2,text='CHECK',command=checkdata,width=8,font=('times new roman bold',11),bg='orange')
        bt1.place(x=420,y=100)
        bt2=Button(c2,text='SAVE',command=suppliersave,width=8,font=('times new roman bold',11),fg='white',bg='green')
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
        a1=Label(c2,text='SUPPLIER DELETE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15) 
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
        
        a1=Label(c2,text='SUPPLIER UPDATE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15) 
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
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
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            bb.config(text=data[0])
            cc.config(text=data[1])
            dd.config(text=data[2])
            ee.config(text=data[3])
            db.close()
        a1=Label(c2,text='SUPPLIER FIND- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15) 
        a=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',10),bg='pink')
        a.place(x=90,y=100)
        aa=ttk.Combobox(c2,width=37)
        aa.place(x=170,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='SNAME:',font=('times new roman bold',11),bg='pink')
        b.place(x=90,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=170,y=150)
        c=Label(c2,text='ADDRESS:',font=('times new roman bold',11),bg='pink')
        c.place(x=90,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=170,y=200)
        d=Label(c2,text='PHONE:',font=('times new roman bold',11),bg='pink')
        d.place(x=90,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=170,y=250)
        e=Label(c2,text='EMAIL:',font=('times new roman bold',11),bg='pink')
        e.place(x=90,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
        def nextdata():
            global i
            i=i+1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
        def prevdata():
            global i
            i=i-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
        a1=Label(c2,text='SUPPLIER SHOW- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=170,y=15)     
        a=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',10),bg='pink')
        a.place(x=90,y=100)
        aa=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        aa.place(x=170,y=100)
        b=Label(c2,text='SNAME:',font=('times new roman bold',11),bg='pink')
        b.place(x=90,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=170,y=150)
        c=Label(c2,text='ADDRESS:',font=('times new roman bold',11),bg='pink')
        c.place(x=90,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=170,y=200)
        d=Label(c2,text='PHONE:',font=('times new roman bold',11),bg='pink')
        d.place(x=90,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=170,y=250)
        e=Label(c2,text='EMAIL:',font=('times new roman bold',11),bg='pink')
        e.place(x=90,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
        def nextdata():
            global i
            i=i+1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
        def prevdata():
            global i
            i=i-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
        a1=Label(c2,text='STOCK-IN SHOW- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)    
        a=Label(c2,text='STOCK ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        aa.place(x=200,y=100)
        b=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=200,y=200)
        d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=200,y=250)
        e=Label(c2,text='DATE IN:',font=('times new roman bold',12),bg='pink')
        e.place(x=90,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ee.place(x=200,y=300)
        f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
        f.place(x=90,y=350)
        ff=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
        xw=[]
        def filleddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select supplierid from stockin"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xw.append(res[0])
            db.close()                
        xs=[]
        def fildata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select pcatid from stockin"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xs.append(res[0])
            db.close()                
        xz=[]
        def fileddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select productid from stockin"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xz.append(res[0])
            db.close()                
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
                if xf<0:
                    messagebox.showerror('Hi','Wrong Entry')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                    cur=db.cursor()
                    sql="insert into stockin values(%d,%d,%d,%d,'%s',%d)"%(xa,xb,xc,xd,xe,xf)
                    cur.execute(sql)
                    db.commit()
                    db.close()
                    updatestockdata()
                    aa.delete(0,100)
                    bb.delete(0,100)
                    cc.delete(0,100)
                    dd.delete(0,100)
                    ee.delete(0,100)
                    ff.delete(0,100)
                    messagebox.showinfo(' ','Data Added')
        def updatestockdata():
            xd=int(dd.get())
            xf=int(ff.get()) #qty
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="update products set currqty=currqty+%d where productid=%d"%(xf,xd)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi ','Stock updated...')
        
        def date():
            xa=datetime.datetime.now().date()
            ee.insert(0,str(xa))    

        def close():
            t.destroy()
    
        a1=Label(c2,text='STOCK-IN SAVE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)           
        a=Label(c2,text='STOCK ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=ttk.Combobox(c2,width=37)
        aa.place(x=200,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=ttk.Combobox(c2,width=37)
        bb.place(x=200,y=150)
        filleddata()
        bb['values']=xw
        c=Label(c2,text='PCAT ID',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=ttk.Combobox(c2,width=37)
        cc.place(x=200,y=200)
        fildata()
        cc['values']=xs
        d=Label(c2,text='PRODUCT ID',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=ttk.Combobox(c2,width=37)
        dd.place(x=200,y=250)
        fileddata()
        dd['values']=xz
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
        date()
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
        a1=Label(c2,text='STOCK-IN DELETE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)    
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
        a1=Label(c2,text='STOCK-IN UPDATE- DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)        
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
    
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
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            bb.config(text=data[0])
            cc.config(text=data[1])
            dd.config(text=data[2])
            ee.config(text=data[3])
            ff.config(text=data[4])
            db.close()
        
        a=Label(c2,text='STOCK ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=ttk.Combobox(c2,width=37)
        aa.place(x=200,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='SUPPLIER ID:',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=200,y=200)
        d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=200,y=250)
        e=Label(c2,text='DATEIN:',font=('times new roman bold',12),bg='pink')
        e.place(x=90,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ee.place(x=200,y=300)
        f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
        f.place(x=90,y=350)
        ff=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
        def customersave():
            email=ee.get()
            phone=dd.get()
            if '@' not in email or '.' not in email:
                messagebox.showerror("Error","Please enter a valid email")
                return
            if not phone.isdigit() or len(phone)!=10:
                messagebox.showerror("Error","Please enter a valid Mobile No.")
                return
            savedata()
    
        def close():
            t.destroy()                

        a1=Label(c2,text='CUSTOMER-SAVE-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)        
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
        bt1=Button(c2,text='CHECK',command=checkdata,width=8,font=('times new roman bold',12),bg='orange')
        bt1.place(x=430,y=100)
        bt2=Button(c2,text='SAVE',command=customersave,width=8,font=('times new roman bold',12),fg='white',bg='green')
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
        a1=Label(c2,text='CUSTOMER-DELETE-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)        
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
        a1=Label(c2,text='CUSTOMER-UPDATE-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)                
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            bb.config(text=data[0])
            cc.config(text=data[1])
            dd.config(text=data[2])
            ee.config(text=data[3])
            db.close()
        a1=Label(c2,text='CUSTOMER-FIND-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)        
        a=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=ttk.Combobox(c2,width=37)
        aa.place(x=170,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='CNAME:',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=170,y=150)
        c=Label(c2,text='ADDRESS:',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=170,y=200)
        d=Label(c2,text='PHONE:',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=170,y=250)
        e=Label(c2,text='EMAIL:',font=('times new roman bold',12),bg='pink')
        e.place(x=90,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
        def nextdata():
            global i
            i=i+1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
        def prevdata():
            global i
            i=i-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
        a1=Label(c2,text='CUSTOMER-SHOW-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)            
        a=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        aa.place(x=170,y=100)
        b=Label(c2,text='CNAME:',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=170,y=150)
        c=Label(c2,text='ADDRESS:',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=170,y=200)
        d=Label(c2,text='PHONE:',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=170,y=250)
        e=Label(c2,text='EMAIL:',font=('times new roman bold',12),bg='pink')
        e.place(x=90,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
    
    def customerbillscreen():
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
        def send():
           from_address = "preetamsingh00001@gmail.com"
           to_address =ee.get()
    
           # Create message container - the correct MIME type is multipart/alternative.
           msg = MIMEMultipart('alternative')
           msg['Subject'] ="Customer Bill"
           msg['From'] = from_address
           msg['To'] = to_address
           # Create the message (HTML).
           html ="<html><body><h1> Hello Dear "+bb.get()+",<br> Welcome V-Mart Shoping club, Your Total Bill Amount is Rs.</h1></body></html>" + ff.get(1.0,'end-1c')
    
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
        
        h1=Label(c2,text='CUSTOMER BILL',font=('times new roman bold',20),bg='pink',fg='blue')
        h1.place(x=230,y=20)
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
        f=Label(c2,text='GENERATE BILL:',font=('times new roman bold',12),bg='pink')
        f.place(x=60,y=420)
        ff=Text(c2,width=40,height=10)
        ff.place(x=200,y=420)
        
        bt1=Button(c2,text='FIND',command=finddata,width=8,font=('times new roman bold',12),fg='white',bg='orange')
        bt1.place(x=200,y=350)
        bt2=Button(c2,text='NEW',command=new,width=8,font=('times new roman bold',12),fg='white',bg='light blue')
        bt2.place(x=320,y=350)
        
        bt2=Button(c2,text='SEND BILL',command=send,width=9,font=('times new roman bold',12),fg='white',bg='green')
        bt2.place(x=200,y=620)
        bt3=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='purple')
        bt3.place(x=320,y=620)
    
    def ordersavescreen():
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
        xw=[]
        def filleddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select custid from orders"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xw.append(res[0])
            db.close()
        xz=[]
        def fildata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select pcatid from orders"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xz.append(res[0])
            db.close()                      
        xy=[]
        def fileddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select productid from orders"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xy.append(res[0])
            db.close()                                  
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
        def date():
            xa=datetime.datetime.now().date()
            ee.insert(0,str(xa)) 

        def close():
            t.destroy()            

        a1=Label(c2,text='ORDER-SAVE-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=180,y=15)            
        a=Label(c2,text='ORDER ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=ttk.Combobox(c2,width=37)
        aa.place(x=200,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='CUST.ID:',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=ttk.Combobox(c2,width=37)
        bb.place(x=200,y=150)
        filleddata()
        bb['values']=xw
        c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=ttk.Combobox(c2,width=37)
        cc.place(x=200,y=200)
        fildata()
        cc['values']=xz
        d=Label(c2,text='PRODCUT.ID:',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=ttk.Combobox(c2,width=37)
        dd.place(x=200,y=250)
        fileddata()
        dd['values']=xy
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
        date()
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
        a1=Label(c2,text='ORDER-DELETE-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=180,y=15)
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
        a1=Label(c2,text='ORDER-UPDATE-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=180,y=15)
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
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
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            bb.config(text=data[0])
            cc.config(text=data[1])
            dd.config(text=data[2])
            ee.config(text=data[3])
            ff.config(text=data[4])
            db.close()
        a1=Label(c2,text='ORDER-FIND-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=180,y=15)    
        a=Label(c2,text='ORDER ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=ttk.Combobox(c2,width=37)
        aa.place(x=200,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='CUST.ID:',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='PCAT.ID:',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=200,y=200)
        d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=200,y=250)
        e=Label(c2,text='DATEOFORDER:',font=('times new roman bold',10),bg='pink')
        e.place(x=90,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ee.place(x=200,y=300)
        f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
        f.place(x=90,y=350)
        ff=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
        def nextdata():
            global i
            i=i+1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
            
        def prevdata():
            global i
            i=i-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
        a1=Label(c2,text='ORDER-SHOW-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=180,y=15)
        a=Label(c2,text='ORDER ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        aa.place(x=200,y=100)
        b=Label(c2,text='CUST.ID:',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='PCAT.ID:',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=200,y=200)
        d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=200,y=250)
        e=Label(c2,text='DATEOFORDER:',font=('times new roman bold',10),bg='pink')
        e.place(x=90,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ee.place(x=200,y=300)
        f=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
        f.place(x=90,y=350)
        ff=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
        xw=[]
        def filleddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select custid from dispatchbill"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xw.append(res[0])
            db.close()
        xz=[]
        def fildata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select pcatid from dispatchbill"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xz.append(res[0])
            db.close()                      
        xy=[]
        def fileddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select productid from dispatchbill"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xy.append(res[0])
            db.close()                  
    
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
        
        def savedata():
            if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0 or len(ff.get())==0 or len(gg.get())==0 or len(hh.get())==0:
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
                if xg<0:
                    messagebox.showerror('Hi','Wrong Entry')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                    cur=db.cursor()
                    sql="insert into dispatchbill values(%d,%d,%d,%d,'%s','%s',%d,%d)"%(xa,xb,xc,xd,xe,xf,xg,xh)
                    cur.execute(sql)
                    db.commit()
                    db.close()
                    updatedispatchdata()
                    aa.delete(0,100)
                    bb.delete(0,100)
                    cc.delete(0,100)
                    dd.delete(0,100)
                    ee.delete(0,100)
                    ff.delete(0,100)
                    gg.delete(0,100)
                    hh.delete(0,100)
                    messagebox.showinfo(' ','Data Added')
        def updatedispatchdata():
            xd=int(dd.get()) # cust Id 
            xf=int(gg.get()) #qty
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="update products set currqty=(currqty-%d) where productid=%d"%(xf,xd)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi ','Stock updated...')
            
        def close():
            t.destroy()
        def date():
            xa=datetime.datetime.now().date()
            ff.insert(0,str(xa))            
        a1=Label(c2,text='DISPATCH-SAVE-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)    
        a=Label(c2,text='DISPATCH ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=ttk.Combobox(c2,width=37)
        aa.place(x=200,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=ttk.Combobox(c2,width=37)
        bb.place(x=200,y=150)
        filleddata()
        bb['values']=xw
        c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=ttk.Combobox(c2,width=37)
        cc.place(x=200,y=200)
        fildata()
        cc['values']=xz
        d=Label(c2,text='PROD.ID:',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=ttk.Combobox(c2,width=37)
        dd.place(x=200,y=250)
        fileddata()
        dd['values']=xy
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
        date()
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
        a1=Label(c2,text='DISPATCH-DELETE-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)    
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
        a1=Label(c2,text='DISPATCH-UPDATE-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)        
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            hh.config(text=' ')
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
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            hh.config(text=' ')
            bb.config(text=data[0])
            cc.config(text=data[1])
            dd.config(text=data[2])
            ee.config(text=data[3])
            ff.config(text=data[4])
            gg.config(text=data[5])
            hh.config(text=data[6])
            db.close()
        a1=Label(c2,text='DISPATCH-FIND-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)    
        a=Label(c2,text='DISPATCH ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=ttk.Combobox(c2,width=37)
        aa.place(x=200,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='CUST ID:',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=200,y=200)
        d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=200,y=250)
        e=Label(c2,text='PNAME:',font=('times new roman bold',12),bg='pink')
        e.place(x=90,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ee.place(x=200,y=300)
        f=Label(c2,text='DATEOFBILL',font=('times new roman bold',12),bg='pink')
        f.place(x=90,y=350)
        ff=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ff.place(x=200,y=350)
        g=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
        g.place(x=90,y=400)
        gg=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        gg.place(x=200,y=400)
        h=Label(c2,text='BILL:',font=('times new roman bold',12),bg='pink')
        h.place(x=90,y=450)
        hh=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            hh.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
            gg.config(text=xg[i])
            hh.config(text=xh[i])
             
        def nextdata():
            global i
            i=i+1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            hh.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
            gg.config(text=xg[i])
            hh.config(text=xh[i])
            
        def prevdata():
            global i
            i=i-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            hh.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
            gg.config(text=xg[i])
            hh.config(text=xh[i])
            
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text=' ')
            bb.config(text=' ')
            cc.config(text=' ')
            dd.config(text=' ')
            ee.config(text=' ')
            ff.config(text=' ')
            gg.config(text=' ')
            hh.config(text=' ')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
            gg.config(text=xg[i])
            hh.config(text=xh[i])
        a1=Label(c2,text='DISPATCH-SHOW-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=150,y=15)        
        a=Label(c2,text='DISPATCH ID:',font=('times new roman bold',12),bg='pink')
        a.place(x=90,y=100)
        aa=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        aa.place(x=200,y=100)
        b=Label(c2,text='CUST ID',font=('times new roman bold',12),bg='pink')
        b.place(x=90,y=150)
        bb=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        bb.place(x=200,y=150)
        c=Label(c2,text='PCAT ID:',font=('times new roman bold',12),bg='pink')
        c.place(x=90,y=200)
        cc=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        cc.place(x=200,y=200)
        d=Label(c2,text='PRODUCT ID:',font=('times new roman bold',12),bg='pink')
        d.place(x=90,y=250)
        dd=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        dd.place(x=200,y=250)
        e=Label(c2,text='PNAME:',font=('times new roman bold',12),bg='pink')
        e.place(x=90,y=300)
        ee=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ee.place(x=200,y=300)
        f=Label(c2,text='DATEOFBILL:',font=('times new roman bold',12),bg='pink')
        f.place(x=90,y=350)
        ff=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        ff.place(x=200,y=350)
        g=Label(c2,text='QTY:',font=('times new roman bold',12),bg='pink')
        g.place(x=90,y=400)
        gg=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
        gg.place(x=200,y=400)
        h=Label(c2,text='BILL:',font=('times new roman bold',12),bg='pink')
        h.place(x=90,y=450)
        hh=Label(c2,width=40,font=('times new roman bold',12),bg='pink')
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
    
    def sendbillscreen():
        c2=Canvas(t,height=800,width=650,bg='pink')
        c2.place(x=150,y=0)
        def send():
           from_address = "preetamsingh00001@gmail.com"
           to_address =ii.get()
    
           # Create message container - the correct MIME type is multipart/alternative.
           msg = MIMEMultipart('alternative')
           msg['Subject'] ="Total Bill"
           msg['From'] = from_address
           msg['To'] = to_address
           # Create the message (HTML).
           html =aa.get(1.0,'end-1c')
    
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
        a1=Label(c2,text='DISPATCH-SEND BILL-DATA',font=('times new roman bold',20),fg='blue',bg='pink')
        a1.place(x=140,y=15)        
        i=Label(c2,text='CUSTOMER EMAIL:',font=('times new roman bold',12),bg='pink')
        i.place(x=50,y=100)
        ii=Entry(t,width=52)
        ii.place(x=360,y=100)
        a=Label(c2,text='GENERATE BILL:',font=('times new roman bold',12),bg='pink')
        a.place(x=50,y=150)
        aa=Text(c2,width=40,height=8)
        aa.place(x=205,y=150)
        bt1=Button(c2,text='SEND MAIL',command=send,width=9,font=('times new roman bold',12),fg='white',bg='blue4',)
        bt1.place(x=200,y=320)
        bt2=Button(c2,text='CLOSE',command=close,width=8,font=('times new roman bold',12),fg='white',bg='light blue',)
        bt2.place(x=300,y=320)
        
    def storebuttons():
        c2=Canvas(t,height=800,width=650,bg='pink1')
        c2.place(x=150,y=0)
        
        a=Label(c2,text='STORE DATABASE',font=('times new roman bold',20),fg='blue',bg='pink')
        a.place(x=180,y=20)
        b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=storesavescreen,width=8)
        b1.place(x=70,y=150)
        b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=storedeletescreen,width=8)
        b2.place(x=240,y=150)
        b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=storeupdatescreen,width=8)
        b3.place(x=400,y=150)
        b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=storefindscreen,width=8)
        b4.place(x=160,y=240)
        b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=storeshowscreen,width=8)
        b5.place(x=330,y=240)    
    
    def productbuttons():
        c2=Canvas(t,height=800,width=650,bg='pink2')
        c2.place(x=150,y=0)
        
        a=Label(c2,text='PRODUCTS DATABASE',font=('times new roman bold',20),bg='pink',fg='blue')
        a.place(x=180,y=20)
        b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=productsavescreen,width=8)
        b1.place(x=70,y=150)
        b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=productdeletescreen,width=8)
        b2.place(x=240,y=150)
        b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=productupdatescreen,width=8)
        b3.place(x=400,y=150)
        b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=productfindscreen,width=8)
        b4.place(x=160,y=240)
        b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=productshowscreen,width=8)
        b5.place(x=330,y=240)
    
    def productcatbuttons():
        c2=Canvas(t,height=800,width=650,bg='pink3')
        c2.place(x=150,y=0)
        
        a=Label(c2,text='PRODUCTS-CATEGORIES DATABASE',font=('times new roman bold',20),bg='pink',fg='blue')
        a.place(x=100,y=20)
        b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=productcatsavescreen,width=8)
        b1.place(x=70,y=150)
        b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=productcatdeletescreen,width=8)
        b2.place(x=240,y=150)
        b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=productcatupdatescreen,width=8)
        b3.place(x=400,y=150)
        b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=productcatfindscreen,width=8)
        b4.place(x=160,y=240)
        b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=productcatshowscreen,width=8)
        b5.place(x=330,y=240)
    
    def supplierbuttons():
        c2=Canvas(t,height=800,width=650,bg='pink1')
        c2.place(x=150,y=0)
        
        a=Label(c2,text='SUPPLIER DATABASE',font=('times new roman bold',20),bg='pink',fg='blue')
        a.place(x=180,y=20)
        b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=suppliersavescreen,width=8)
        b1.place(x=70,y=150)
        b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=supplierdeletescreen,width=8)
        b2.place(x=240,y=150)
        b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=supplierupdatescreen,width=8)
        b3.place(x=400,y=150)
        b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=supplierfindscreen,width=8)
        b4.place(x=160,y=240)
        b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=suppliershowscreen,width=8)
        b5.place(x=330,y=240)
    
    def stockinregbuttons():
        c2=Canvas(t,height=800,width=650,bg='pink2')
        c2.place(x=150,y=0)
        
        a=Label(c2,text='STOCKIN-REGISTER DATABASE',font=('times new roman bold',20),bg='pink',fg='blue')
        a.place(x=140,y=20)
        b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=stockinsavescreen,width=8)
        b1.place(x=70,y=150)
        b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=stockindeletescreen,width=8)
        b2.place(x=240,y=150)
        b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=stockinupdatescreen,width=8)
        b3.place(x=400,y=150)
        b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=stockinfindscreen,width=8)
        b4.place(x=160,y=240)
        b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=stockinshowscreen,width=8)
        b5.place(x=330,y=240)
    
    def customerbuttons():
        c2=Canvas(t,height=800,width=650,bg='pink3')
        c2.place(x=150,y=0)
        
        a=Label(c2,text='CUSTOMERS DATABASE',font=('times new roman bold',20),bg='pink',fg='blue')
        a.place(x=170,y=20)
        b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=customersavescreen,width=8)
        b1.place(x=70,y=150)
        b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=customerdeletescreen,width=8)
        b2.place(x=240,y=150)
        b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=customerupdatescreen,width=8)
        b3.place(x=400,y=150)
        b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=customerfindscreen,width=8)
        b4.place(x=70,y=240)
        b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=customershowscreen,width=8)
        b5.place(x=240,y=240)
        b6=Button(c2,text='SEND BILL',font=('times new roman bold',15),fg='white',bg='magenta',command=customerbillscreen,width=8)
        b6.place(x=400,y=240)
    
    def ordersbuttons():
        c2=Canvas(t,height=800,width=650,bg='pink1')
        c2.place(x=150,y=0)
        
        a=Label(c2,text='ORDERS DATABASE',font=('times new roman bold',20),bg='pink',fg='blue')
        a.place(x=180,y=20)
        b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=ordersavescreen,width=8)
        b1.place(x=70,y=150)
        b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=orderdeletescreen,width=8)
        b2.place(x=240,y=150)
        b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=orderupdatescreen,width=8)
        b3.place(x=400,y=150)
        b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=orderfindscreen,width=8)
        b4.place(x=160,y=240)
        b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=ordershowscreen,width=8)
        b5.place(x=340,y=240)
    
    def dispatchbillbuttons():
        c2=Canvas(t,height=800,width=650,bg='pink2')
        c2.place(x=150,y=0)
        
        a=Label(c2,text='DISPATCH-BILL DATABASE',font=('times new roman bold',20),bg='pink',fg='blue')
        a.place(x=140,y=20)
        b1=Button(c2,text='INSERT',font=('times new roman bold',15),fg='white', bg='green',command=dispatchsavescreen,width=8)
        b1.place(x=70,y=150)
        b2=Button(c2,text='DELETE',font=('times new roman bold',15),fg='white',bg='red',command=dispatchdeletescreen,width=8)
        b2.place(x=240,y=150)
        b3=Button(c2,text='UPDATE',font=('times new roman bold',15),fg='white',bg='blue',command=dispatchupdatescreen,width=8)
        b3.place(x=400,y=150)
        b4=Button(c2,text='FIND',font=('times new roman bold',15),fg='white',bg='Orange',command=dispatchfindscreen,width=8)
        b4.place(x=70,y=240)
        b5=Button(c2,text='SHOW',font=('times new roman bold',15),fg='white',bg='sky blue',command=dispatchshowscreen,width=8)
        b5.place(x=240,y=240)
        b6=Button(c2,text='SEND BILL',font=('times new roman bold',15),fg='white',bg='magenta',command=sendbillscreen,width=8)
        b6.place(x=400,y=240)
        
    c1=Canvas(t,height=800,width=150,bg='gray25')
    c1.place(x=0,y=0)
    c2=Canvas(t,height=800,width=650,bg='pink')
    c2.place(x=150,y=0)
        
    l1=Label(t,text='Admin Dashboard',width=14,font=('times new roman,bold',11),bg='aquamarine4')
    l1.place(x=12,y=6)
    l2=Label(t,text='Welcome Stock Management System',font=('times new roman bold',28),bg='pink',fg='green')
    l2.place(x=190,y=250)
    
    
    b1=Button(c1,text='Store',fg='White',bg='orange',font=('arial',15),command=storebuttons,width=11)
    b1.place(x=10,y=100)
    b2=Button(c1,text='Product',fg='White',bg='green',font=('arial',15),command=productbuttons,width=11)
    b2.place(x=10,y=160)
    b3=Button(c1,text='Product Cat.',fg='White',bg='red',font=('arial',15),command=productcatbuttons,width=11)
    b3.place(x=10,y=220)
    b4=Button(c1,text='Supplier',fg='White',bg='blue',font=('arial',15),command=supplierbuttons,width=11)
    b4.place(x=10,y=280)
    b5=Button(c1,text='Stock In Reg.',fg='White',bg='goldenrod4',font=('arial',15),command=stockinregbuttons,width=11)
    b5.place(x=10,y=340)
    b6=Button(c1,text='Customer',fg='White',bg='slate blue4',font=('arial',15),command=customerbuttons,width=11)
    b6.place(x=10,y=400)
    b7=Button(c1,text='Orders',fg='White',bg='sea green',font=('arial',15),command=ordersbuttons,width=11)
    b7.place(x=10,y=460)
    b8=Button(c1,text='Dispacth Bill',fg='White',bg='orange red',font=('arial',15),command=dispatchbillbuttons,width=11)
    b8.place(x=10,y=520)
    t.mainloop()
