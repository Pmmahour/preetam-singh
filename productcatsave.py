import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
def productcatsavescreen():
    
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Product Category')
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
    
    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Store Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
    
    a=Label(t,text='Pcat id',font=20,fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=Entry(t,width=40)
    aa.place(x=200,y=100)
    btf=Button(t,text='Check',command=checkdata,width=8,bg='light grey')
    btf.place(x=450,y=100)
    b=Label(t,text='Cat-name',font=20,fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(t,width=40)
    bb.place(x=200,y=150)
    c=Label(t,text='Description',font=20,fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(t,width=40)
    cc.place(x=200,y=200)
    
    h=Button(t,text='Save',command=savedata,width=8,bg='light grey')
    h.place(x=150,y=250)
    j=Button(t,text='Close',command=close,width=8,bg='light grey')
    j.place(x=250,y=250)
    t.mainloop()
