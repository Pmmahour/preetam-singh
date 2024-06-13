import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def customersavescreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('customers')
    
    
    
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
    
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=500,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Customers Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
    
    a=Label(t,text='Cust id:',font=20,bg='pink')
    a.place(x=90,y=100)
    aa=Entry(t,width=40)
    aa.place(x=170,y=100)
    
    b=Label(t,text='Cname:',font=20,bg='pink')
    b.place(x=90,y=150)
    bb=Entry(t,width=40)
    bb.place(x=170,y=150)
    
    c=Label(t,text='Address:',font=20,bg='pink')
    c.place(x=90,y=200)
    cc=Entry(t,width=40)
    cc.place(x=170,y=200)
    
    d=Label(t,text='Phone:',font=20,bg='pink')
    d.place(x=90,y=250)
    dd=Entry(t,width=40)
    dd.place(x=170,y=250)
    
    e=Label(t,text='Email:',font=20,bg='pink')
    e.place(x=90,y=300)
    ee=Entry(t,width=40)
    ee.place(x=170,y=300)
    
    
    
    bt1=Button(t,text='Check',command=checkdata,width=8,bg='light grey')
    bt1.place(x=430,y=100)
    
    bt2=Button(t,text='Save',command=savedata,width=8,bg='light grey')
    bt2.place(x=170,y=370)
    
    bt3=Button(t,text='Close',command=close,width=8,bg='light grey')
    bt3.place(x=300,y=370)
    
    
    
    
    
    
    t.mainloop()

