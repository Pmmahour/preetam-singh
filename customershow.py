import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def customershowscreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Stockin Register')
    
    
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
        
    
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
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
    
    
    
    bt1=Button(t,text='First',command=firstdata,width=8,bg='light grey')
    bt1.place(x=100,y=370)
    
    bt2=Button(t,text='Next',command=nextdata,width=8,bg='light grey')
    bt2.place(x=200,y=370)
    
    bt3=Button(t,text='Prev',command=prevdata,width=8,bg='light grey')
    bt3.place(x=300,y=370)
    
    bt4=Button(t,text='Last',command=lastdata,width=8,bg='light grey')
    bt4.place(x=400,y=370)
    
    
    
    filldata()
    
    t.mainloop()

