from tkinter import *
import tkinter
cal = tkinter.Tk()


cal.geometry('250x250')
cal.maxsize(width=250,height=180)
cal.minsize(width=250,height=180)
cal.title('Calculator By Pradeep')
cal.configure(bg='black')

l= Label(cal,text='MY CALCULATOR',fg='blue').grid(row=0,column=1,sticky=W)
l1=Label(cal,text='First Number',).grid(row=1,column=0,sticky=W)
l2=Label(cal,text='Second Number',).grid(row=2,column=0,sticky=W)
l3=Label(cal,text='Opeartor',).grid(row=3,column=0,sticky=W)
l4=Label(cal,text='Answer',).grid(row=4,column=0,sticky=W)

E1= Entry(cal,bd=5)
E1.grid(row=1,column=1)
E2= Entry(cal,bd=5)
E2.grid(row=2,column=1)
E3= Entry(cal,bd=5)
E3.grid(row=3,column=1)
E4= Entry(cal,bd=5)
E4.grid(row=4,column=1)



def process():
    number1=Entry.get(E1)
    number2=Entry.get(E2)
    operator=Entry.get(E3)
    number1=int(number1)
    number2=int(number2)
    if operator =="+":
        answer=number1+number2
    if operator =="-":
        answer=number1-number2
    if operator=="*":
        answer=number1*number2
    if operator=="/":
        answer=number1/number2
    Entry.insert(E4,0,answer)
    print(answer)


B=Button(cal, text ="Submit",command = process,bg='yellow').grid(row=5,column=1)


cal.mainloop()