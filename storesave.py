import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def storesavescreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Store SMS')
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

    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Store Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
    
    a=Label(t,text='Store id',font=20,fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=Entry(t,width=40)
    aa.place(x=200,y=100)
    btf=Button(t,text='Check',command=checkdata,width=8,bg='light grey')
    btf.place(x=450,y=100)
    b=Label(t,text='Name',font=20,fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(t,width=40)
    bb.place(x=200,y=150)
    c=Label(t,text='Address',font=20,fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(t,width=40)
    cc.place(x=200,y=200)
    d=Label(t,text='City',font=20,fg='black',bg='pink')
    d.place(x=100,y=250)
    dd=Entry(t,width=40)
    dd.place(x=200,y=250)
    e=Label(t,text='Email',font=20,fg='black',bg='pink')
    e.place(x=100,y=300)
    ee=Entry(t,width=40)
    ee.place(x=200,y=300)
    f=Label(t,text='Phone',font=20,fg='black',bg='pink')
    f.place(x=100,y=350)
    ff=Entry(t,width=40)
    ff.place(x=200,y=350)
    g=Label(t,text='Regist.no',font=20,fg='black',bg='pink')
    g.place(x=100,y=400)
    gg=Entry(t,width=40)
    gg.place(x=200,y=400)
    h=Button(t,text='Save',command=savedata,width=8,bg='light grey')
    h.place(x=150,y=450)
    j=Button(t,text='Close',command=close,width=8,bg='light grey')
    j.place(x=250,y=450)
    t.mainloop()
