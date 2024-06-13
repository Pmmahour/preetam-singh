import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def orderfindscreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Orders')
    
    
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
    
    
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Orders Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
    
    a=Label(t,text='Order id:',font=20,bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(t,width=37)
    aa.place(x=170,y=100)
    filldata()
    aa['values']=xt
    
    b=Label(t,text='Cust.id:',font=20,bg='pink')
    b.place(x=90,y=150)
    bb=Entry(t,width=40)
    bb.place(x=170,y=150)
    
    c=Label(t,text='Pcat.id:',font=20,bg='pink')
    c.place(x=90,y=200)
    cc=Entry(t,width=40)
    cc.place(x=170,y=200)
    d=Label(t,text='Prodt.id:',font=20,bg='pink')
    d.place(x=90,y=250)
    dd=Entry(t,width=40)
    dd.place(x=170,y=250)
    e=Label(t,text='Date.order:',font=20,bg='pink')
    e.place(x=90,y=300)
    ee=Entry(t,width=40)
    ee.place(x=170,y=300)
    f=Label(t,text='Qty:',font=20,bg='pink')
    f.place(x=90,y=350)
    ff=Entry(t,width=40)
    ff.place(x=170,y=350)
    bt1=Button(t,text='Find',command=finddata,width=8,bg='light grey')
    bt1.place(x=430,y=100)
    bt2=Button(t,text='New',command=new,width=8,bg='light grey')
    bt2.place(x=170,y=420)
    bt3=Button(t,text='Close',command=close,width=8,bg='light grey')
    bt3.place(x=300,y=420)
    t.mainloop()

