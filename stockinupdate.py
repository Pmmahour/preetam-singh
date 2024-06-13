import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def stockinupdatescreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Stock Management System')
    
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
    
    
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Stockin Register',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
    
    a=Label(t,text='Stock.id:',font=20,bg='pink')
    a.place(x=90,y=100)
    aa=ttk.Combobox(t,width=37)
    aa.place(x=170,y=100)
    filldata()
    aa['values']=xt
    
    b=Label(t,text='Suplr.id:',font=20,bg='pink')
    b.place(x=90,y=150)
    bb=Entry(t,width=40)
    bb.place(x=170,y=150)
    
    c=Label(t,text='pcat.id:',font=20,bg='pink')
    c.place(x=90,y=200)
    cc=Entry(t,width=40)
    cc.place(x=170,y=200)
    
    d=Label(t,text='Prod.id:',font=20,bg='pink')
    d.place(x=90,y=250)
    dd=Entry(t,width=40)
    dd.place(x=170,y=250)
    
    e=Label(t,text='Datein:',font=20,bg='pink')
    e.place(x=90,y=300)
    ee=Entry(t,width=40)
    ee.place(x=170,y=300)
    
    f=Label(t,text='Qty:',font=20,bg='pink')
    f.place(x=90,y=350)
    ff=Entry(t,width=40)
    ff.place(x=170,y=350)
    
    bt1=Button(t,text='Find',command=finddata,width=8,bg='light grey')
    bt1.place(x=420,y=100)
    
    bt2=Button(t,text='Update',command=update,width=8,bg='light grey')
    bt2.place(x=150,y=400)
    
    bt3=Button(t,text='Close',command=close,width=8,bg='light grey')
    bt3.place(x=250,y=400)
    
    
    
    
    
    
    t.mainloop()

