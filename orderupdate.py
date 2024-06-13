import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def orderupdatescreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Orders')
    
    
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
    
    
    
    a=Label(t,text='Order id:')
    a.place(x=50,y=50)
    aa=ttk.Combobox(t,width=27)
    aa.place(x=150,y=50)
    filldata()
    aa['values']=xt
    
    b=Label(t,text='Cust id:')
    b.place(x=50,y=90)
    bb=Entry(t,width=30)
    bb.place(x=150,y=90)
    
    c=Label(t,text='pcat id:')
    c.place(x=50,y=130)
    cc=Entry(t,width=30)
    cc.place(x=150,y=130)
    
    d=Label(t,text='Product id:')
    d.place(x=50,y=170)
    dd=Entry(t,width=30)
    dd.place(x=150,y=170)
    
    e=Label(t,text='Date of order:')
    e.place(x=50,y=210)
    ee=Entry(t,width=30)
    ee.place(x=150,y=210)
    
    f=Label(t,text='Qty:')
    f.place(x=50,y=250)
    ff=Entry(t,width=30)
    ff.place(x=150,y=250)
    
    bt1=Button(t,text='Find',command=finddata)
    bt1.place(x=350,y=50)
    
    bt2=Button(t,text='Update',command=update)
    bt2.place(x=120,y=320)
    
    bt3=Button(t,text='Close',command=close)
    bt3.place(x=170,y=320)
    t.config(bg='pink')

    t.mainloop()

