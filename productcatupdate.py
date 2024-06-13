import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
def productcatupdatescreen():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('Product category')
    
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
        sql="update productcat set catname='%s',description=%s where pcatid=%d"%(xb,xc,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','updated')
        bb.delete(0,100)
        cc.delete(0,100)


    can1=Canvas(t,height=40,width=580,bg='light blue')
    can1.place(x=10,y=10)
    can2=Canvas(t,height=540,width=580,bg='pink')
    can2.place(x=10,y=50)
    h1=Label(t,text='Product Categories Data',fg='white',font=60,bg='light blue')
    h1.place(x=220,y=20)
     
    a=Label(t,text='Pcat id',font=20,fg='black',bg='pink')
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,width=37)
    aa.place(x=200,y=100)
    filldata()
    aa['values']=xt
    b1=Button(t,text='Find',command=finddata,width=8,bg='light grey')
    b1.place(x=450,y=100)
    b=Label(t,text='Cat-name',font=20,fg='black',bg='pink')
    b.place(x=100,y=150)
    bb=Entry(t,width=40)
    bb.place(x=200,y=150)
    c=Label(t,text='Description',font=20,fg='black',bg='pink')
    c.place(x=100,y=200)
    cc=Entry(t,width=40)
    cc.place(x=200,y=200)
    
    b2=Button(t,text='Update',command=updatedata,width=8,bg='light grey')
    b2.place(x=250,y=250)
    b3=Button(t,text='Close',command=close,width=8,bg='light grey')
    b3.place(x=350,y=250)
    t.mainloop()
