from re import match
from tkinter import *
from typing import Match
root=Tk()
root.title("OREVA")
e=Entry(root,width=100,borderwidth=20,fg="grey")
e.grid(row=0,column=0,columnspan=20,padx=30,pady=30)

#declaring the functions
def buttonclick(number):
    #e.delete(0,END) #delete the number visible on the screen
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def clear():
    e.delete(0,END)
def buttonadd():
    firstnum=e.get()
    global fnum
    global Math
    math="add"
    fnum=int(firstnum)
    e.delete(0,END)
def equal():
    secondnum=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,fnum+int(secondnum))
    elif math=="sub":
        e.insert(0,fnum-int(secondnum))
    elif math=="mul":
        e.insert(0,fnum*int(secondnum))
    elif math=="div":
        e.insert(0,fnum/int(secondnum))
    elif math=="pow":
        e.insert(0,fnum**int(secondnum))
def sub():
    firstnum=e.get()
    global fnum
    global math
    math="sub"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def mul():
    firstnum=e.get()
    global fnum
    global math
    math="mul"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def div():
    firstnum=e.get()
    global fnum
    global math
    math="div"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def pow():
    firstname.get()
    global fnum
    global math
    math="pow"
    fnum=int(firstnum)
    e.delete(0,END)
    return
#buttons
button1=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button2=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button3=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button4=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button5=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button6=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button7=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button8=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button9=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button0=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button1=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))
button1=Button(root,text="1",padx=40,pady=40,command=lamda:buttonclick(1))

