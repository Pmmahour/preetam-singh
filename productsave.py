import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
def productsavescreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Products')
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
    
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Products Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)

    a=Label(t,text='Product Id',font=20,fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=Entry(t,width=40)
    aa.place(x=210,y=100)
    b=Label(t,text='Pcat Id',font=20,fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(t,width=40)
    bb.place(x=210,y=150)
    c=Label(t,text='PName',font=20,fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(t,width=40)
    cc.place(x=210,y=200)
    d=Label(t,text='Price per Unit',font=20,fg='black',bg='pink')
    d.place(x=100,y=250)
    dd=Entry(t,width=40)
    dd.place(x=210,y=250)
    e=Label(t,text='Open Qty',font=20,fg='black',bg='pink')
    e.place(x=100,y=300)
    ee=Entry(t,width=40)
    ee.place(x=210,y=300)
    f=Label(t,text='Current Qty',font=20,fg='black',bg='pink')
    f.place(x=100,y=350)
    ff=Entry(t,width=40)
    ff.place(x=210,y=350)
    b1=Button(t,text='Save',command=savedata,width=8,bg='light grey')
    b1.place(x=250,y=400)
    b2=Button(t,text='Close',command=close,width=8,bg='light grey')
    b2.place(x=350,y=400)
    
    b2=Button(t,text='Check',command=checkdata,width=8,bg='light grey')
    b2.place(x=460,y=100)
    t.mainloop()
