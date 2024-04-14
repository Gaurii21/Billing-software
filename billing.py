from tkinter import*
import random


root = Tk()
root.geometry("890x580+0+0")
root.title("BILLING SYSTEM")

Tops = Frame(root,bg="azure",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)


#heading
lblinfo = Label(Tops, font=( 'Algerian' ,40, 'bold' ),text="VISUAL EYES",fg="darkslategrey",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)



def Ref():
    x=random.randint(1,10000 )
    randomRef = str(x)
    rand.set(randomRef)

    custname = str(name.get())
    NOVC = float(VincentChase.get())
    NOMC = float(MediumChase.get())
    NOH = float(Hustlr.get())
    NOVA = float(VincentAir.get())
    NOC = float(Cizal.get())

    costofVincentChase = NOVC*1330
    costofMediumChase = NOMC*1325
    costofHustlr = NOH*1230
    costofVincentAir =  NOVA*1440
    costofCizal =  NOC*3440


    Totalcost=( costofVincentChase + costofMediumChase + costofHustlr  + costofVincentAir + costofCizal)
    Ser_Charge=(( costofVincentChase + costofMediumChase + costofHustlr + costofVincentAir+ costofCizal)/99)
    Service=str('%.2f'% Ser_Charge)
    OverAllCost=str(   Totalcost + Ser_Charge  )


    Service_Charge.set(Service)
    # Tax.set(PaidTax)
    Total.set(OverAllCost)


def exit():
    root.destroy()

def reset():
    rand.set("")
    name.set("")
    VincentChase.set("")
    MediumChase.set("")
    Hustlr.set("")
    Total.set("")
    Service_Charge.set("")
    Cizal.set("")
    VincentAir.set("")



rand = StringVar()
name = StringVar()
VincentChase = StringVar()
MediumChase = StringVar()
Hustlr = StringVar()

Total = StringVar()
Service_Charge = StringVar()
Cizal = StringVar()
VincentAir = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="black",bd=20,anchor='w')
lblreference.grid(row=0,column=0)
lblreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="white" ,justify='right', state="readonly")
lblreference.grid(row=0,column=1)

lblname = Label(f1, font=( 'aria' ,16, 'bold' ),text="Customer Name",fg="black",bd=10,anchor='w')
lblname.grid(row=1,column=0)
txtname = Entry(f1,font=('ariel' ,16,'bold'), textvariable=name , bd=6,insertwidth=4,bg="white" ,justify='right')
txtname.grid(row=1,column=1)

lblVincentChase = Label(f1, font=( 'aria' ,16, 'bold' ),text="Vincent Chase",fg="black",bd=10,anchor='w')
lblVincentChase.grid(row=3,column=0)
txtVincentChase = Entry(f1,font=('ariel' ,16,'bold'), textvariable=VincentChase , bd=6,insertwidth=4,bg="white" ,justify='right')
txtVincentChase.grid(row=3,column=1)


lblMediumChase = Label(f1, font=( 'aria' ,16, 'bold' ),text="Medium Chase",fg="black",bd=10,anchor='w')
lblMediumChase.grid(row=4,column=0)
txtMediumChase = Entry(f1,font=('ariel' ,16,'bold'), textvariable=MediumChase , bd=6,insertwidth=4,bg="white" ,justify='right')
txtMediumChase.grid(row=4,column=1)

lblHustlr = Label(f1, font=( 'aria' ,16, 'bold' ),text="Hustlr",fg="black",bd=10,anchor='w')
lblHustlr.grid(row=5,column=0)
txtHustlr = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Hustlr , bd=6,insertwidth=4,bg="white" ,justify='right')
txtHustlr.grid(row=5,column=1)

lblVincentAir = Label(f1, font=( 'aria' ,16, 'bold' ),text="Vincent Air",fg="black",bd=10,anchor='w')
lblVincentAir.grid(row=6,column=0)
txtVincentAir = Entry(f1,font=('ariel' ,16,'bold'), textvariable=VincentAir , bd=6,insertwidth=4,bg="white" ,justify='right')
txtVincentAir.grid(row=6,column=1)


lblCizal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cizal",fg="black",bd=10,anchor='w')
lblCizal.grid(row=2,column=0)
txtCizal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cizal , bd=6,insertwidth=4,bg="white" ,justify='right')
txtCizal.grid(row=2,column=1)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10,anchor='w')
lblService_Charge.grid(row=4,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right')
txtService_Charge.grid(row=4,column=3)


lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="blue",bd=10,anchor='w')
lblTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right', state="readonly")
txtTotal.grid(row=6,column=3)

#buttons
lblTotal = Label(f1,text="                   ",fg="white")
lblTotal.grid(row=7,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="blue",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="light blue",command=Ref)
btnTotal.grid(row=8, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="blue",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="light blue",command=reset)
btnreset.grid(row=8, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="blue",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="light blue",command=exit)
btnexit.grid(row=8, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Frame names", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="               ", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Vincent Chase ", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1330", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Medium Chase ", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1325", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Hustlr ", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1230", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="VincentAir", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1440", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cizal", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3440", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="blue",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="light blue",command=price)
btnprice.grid(row=8, column=0)

root.mainloop()
