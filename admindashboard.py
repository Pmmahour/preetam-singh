import tkinter
from tkinter import *
from stockinsave import *
from stockindelete import *
from stockinupdate import *
from stockinfind import *
from stockinshow import *
from customersave import *
from customershow import *
from customerupdate import *
from customerfind import *
from customerdelete import *
from dispatchsave import *
from dispatchdelete import *
from dispatchshow import *
from dispatchupdate import *
from dispatchfind import *
from ordersave import *
from orderdelete import *
from orderfind import *
from ordershow import *
from orderupdate import *
from productcatdelete import *
from productcatsave import *
from productcatshow import *
from productcatfind import *
from productcatupdate import *
from storesave import *
from storedelete import *
from storeshow import *
from storeupdate import *
from storefind import *
from productsave import *
from productshow import *
from productdelete import *
from productupdate import *
from productfind import *
from suppliersave import *
from supplierdelete import *
from supplierupdate import *
from supplierfind import *
from suppliershow import *


t=tkinter.Tk()
t.geometry('600x600')
t.title('Stock Management-Dashboard')

def close():
    t.destroy()


can1=Canvas(t,height=450,width=105,bg='grey')
can1.place(x=5,y=5)

can2=Canvas(t,height=30,width=480,bg='grey')
can2.place(x=110,y=5)

can3=Canvas(t,height=415,width=480,bg='beige')
can3.place(x=110,y=40)

can4=Canvas(t,height=540,width=580,bg='grey')
can4.place(x=5,y=450)

btn1=Button(t,text='Back to Login',bg='light green')
btn1.place(x=18,y=12)

btn1=Button(t,text='Close Panel',bg='red',command=close)
btn1.place(x=515,y=10)

h1=Label(t,text='ADMIN PANEL',font=40,bg='grey')
h1.place(x=290,y=10)

a1=Label(t,text='Store:',font=20,bg='grey')
a1.place(x=20,y=50)
b1=Button(t,text='Insert',command=storesavescreen,bg='green',width=8,fg='white')
b1.place(x=120,y=50)
b2=Button(t,text='Delete',command=storedeletescreen,bg='red',width=8,fg='white')
b2.place(x=220,y=50)
b3=Button(t,text='Update',command=storeupdatescreen,bg='blue',width=8,fg='white')
b3.place(x=320,y=50)
b4=Button(t,text='Find',command=storefindscreen,bg='orange',width=8,fg='white')
b4.place(x=420,y=50)
b5=Button(t,text='Show',command=storeshowscreen,bg='purple',width=8,fg='white')
b5.place(x=520,y=50)

a2=Label(t,text='Prod.Catg:',font=20,bg='grey')
a2.place(x=20,y=100)
c1=Button(t,text='Insert',command=productcatsavescreen,bg='green',width=8,fg='white')
c1.place(x=120,y=100)
c2=Button(t,text='Delete',command=productcatdeletescreen,bg='red',width=8,fg='white')
c2.place(x=220,y=100)
c3=Button(t,text='Update',command=productcatupdatescreen,bg='blue',width=8,fg='white')
c3.place(x=320,y=100)
c4=Button(t,text='Find',command=productcatfindscreen,bg='orange',width=8,fg='white')
c4.place(x=420,y=100)
c5=Button(t,text='Show',command=productcatshowscreen,bg='purple',width=8,fg='white')
c5.place(x=520,y=100)

a3=Label(t,text='Products:',font=20,bg='grey')
a3.place(x=20,y=150)
d1=Button(t,text='Insert',command=productsavescreen,bg='green',width=8,fg='white')
d1.place(x=120,y=150)
d2=Button(t,text='Delete',command=productdeletescreen,bg='red',width=8,fg='white')
d2.place(x=220,y=150)
d3=Button(t,text='Update',command=productupdatescreen,bg='blue',width=8,fg='white')
d3.place(x=320,y=150)
d4=Button(t,text='Find',command=productfindscreen,bg='orange',width=8,fg='white',)
d4.place(x=420,y=150)
d5=Button(t,text='Show',command=productshowscreen,bg='purple',width=8,fg='white',)
d5.place(x=520,y=150)

a4=Label(t,text='Supplier:',font=20,bg='grey')
a4.place(x=20,y=200)
e1=Button(t,text='Insert',bg='green',width=8,fg='white',command=suppliersavescreen)
e1.place(x=120,y=200)
e2=Button(t,text='Delete',bg='red',width=8,fg='white',command=supplierdeletescreen)
e2.place(x=220,y=200)
e3=Button(t,text='Update',bg='blue',width=8,fg='white',command=supplierupdatescreen)
e3.place(x=320,y=200)
e4=Button(t,text='Find',bg='orange',width=8,fg='white',command=supplierfindscreen)
e4.place(x=420,y=200)
e5=Button(t,text='Show',bg='purple',width=8,fg='white',command=suppliershowscreen)
e5.place(x=520,y=200)


a5=Label(t,text='Stockinreg:',font=20,bg='grey')
a5.place(x=20,y=250)
f1=Button(t,text='Insert',command=stockinsavescreen,bg='green',width=8,fg='white')
f1.place(x=120,y=250)
f2=Button(t,text='Delete',command=stockindeletescreen,bg='red',width=8,fg='white')
f2.place(x=220,y=250)
f3=Button(t,text='Update',command=stockinupdatescreen,bg='blue',width=8,fg='white')
f3.place(x=320,y=250)
f4=Button(t,text='Find',command=stockinfindscreen,bg='orange',width=8,fg='white')
f4.place(x=420,y=250)
f5=Button(t,text='Show',command=stockinshowscreen,bg='purple',width=8,fg='white')
f5.place(x=520,y=250)

a6=Label(t,text='Customer:',font=20,bg='grey')
a6.place(x=20,y=300)
g1=Button(t,text='Insert',command=customersavescreen,bg='green',width=8,fg='white')
g1.place(x=120,y=300)
g2=Button(t,text='Delete',command=customerdeletescreen,bg='red',width=8,fg='white')
g2.place(x=220,y=300)
g3=Button(t,text='Update',command=customerupdatescreen,bg='blue',width=8,fg='white')
g3.place(x=320,y=300)
g4=Button(t,text='Find',command=customerfindscreen,bg='orange',width=8,fg='white')
g4.place(x=420,y=300)
g5=Button(t,text='Show',command=customershowscreen,bg='purple',width=8,fg='white')
g5.place(x=520,y=300)

a7=Label(t,text='Orders:',font=20,bg='grey')
a7.place(x=20,y=350)
h1=Button(t,text='Insert',command=ordersavescreen,bg='green',width=8,fg='white')
h1.place(x=120,y=350)
h2=Button(t,text='Delete',command=orderdeletescreen,bg='red',width=8,fg='white')
h2.place(x=220,y=350)
h3=Button(t,text='Update',command=orderupdatescreen,bg='blue',width=8,fg='white')
h3.place(x=320,y=350)
h4=Button(t,text='Find',command=orderfindscreen,bg='orange',width=8,fg='white')
h4.place(x=420,y=350)
h5=Button(t,text='Show',command=ordershowscreen,bg='purple',width=8,fg='white')
h5.place(x=520,y=350)

a8=Label(t,text='Disptchbill',font=20,bg='grey')
a8.place(x=20,y=400)
i1=Button(t,text='Insert',command=dispatchsavescreen,bg='green',width=8,fg='white')
i1.place(x=120,y=400)
i2=Button(t,text='Delete',command=dispatchdeletescreen,bg='red',width=8,fg='white')
i2.place(x=220,y=400)
i3=Button(t,text='Update',command=dispatchupdatescreen,bg='blue',width=8,fg='white')
i3.place(x=320,y=400)
i4=Button(t,text='Find',command=dispatchfindscreen,bg='orange',width=8,fg='white')
i4.place(x=420,y=400)
i5=Button(t,text='Show',command=dispatchshowscreen,bg='purple',width=8,fg='white')
i5.place(x=520,y=400)

t.mainloop()






