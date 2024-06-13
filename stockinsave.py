import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def stockinsavescreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Stock IN')
    
    
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

    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Stockin Register',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
    
    a=Label(t,text='Stck.id:',font=20,bg='pink')
    a.place(x=90,y=100)
    aa=Entry(t,width=40)
    aa.place(x=170,y=100)
    
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
    
    bt1=Button(t,text='Check',command=checkdata,width=8,bg='light grey')
    bt1.place(x=420,y=100)
    
    bt2=Button(t,text='Save',command=savedata,width=8,bg='light grey')
    bt2.place(x=150,y=400)
    
    bt3=Button(t,text='Close',command=close,width=8,bg='light grey')
    bt3.place(x=250,y=400)
    
    t.mainloop()


