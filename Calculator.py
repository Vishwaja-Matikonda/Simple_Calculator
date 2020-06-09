#Calculator using Tkinter
from tkinter import *
from math import *

root=Tk()

e=Entry(root,width=50,borderwidth=10)
root.title("Simple Calculator")
e.grid(row=0,column=0,columnspan=4,ipadx=10,ipady=15)

#funtions of the buttons
#button_click
def button_click(number):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,str(cur)+str(number))

#addition
def button_add():
    a=e.get()
    global f
    global ma
    f=int(a)
    ma='addition'
    f=int(a)
    e.delete(0,END)

#subtraction
def button_sub():
    a = e.get()
    global f
    global ma
    f = int(a)
    ma = 'subtraction'
    f = int(a)
    e.delete(0, END)

#multiplication
def button_mul():
    a = e.get()
    global f
    global ma
    f = int(a)
    ma = 'multiplication'
    f = int(a)
    e.delete(0, END)

#division
def button_div():
    a = e.get()
    global f
    global ma
    f = int(a)
    ma = 'division'
    f = int(a)
    e.delete(0, END)

#sine function
def button_sin():
    a = e.get()
    global f
    global ma
    ma = 'sin'
    f=float(a)
    e.delete(0, END)

#cosine function
def button_cos():
    a = e.get()
    global f
    global ma
    f = int(a)
    ma = 'cos'
    f = int(a)
    e.delete(0, END)

#tan function
def button_tan():
    a = e.get()
    global f
    global ma
    f = int(a)
    ma = 'tan'
    f = int(a)
    e.delete(0, END)

#power function
def button_sqrt():
    a = e.get()
    global f
    global ma
    f = int(a)
    ma = 'sqrt'
    b = int(a)
    f=int(a)
    e.delete(0, END)

#log function
def button_log():
    a = e.get()
    global f
    global ma
    f = int(a)
    ma = 'log'
    f = int(a)
    e.delete(0, END)

#absolute function
def button_abs():
    a = e.get()
    global f
    global ma
    f = int(a)
    ma = 'pow'
    f = int(a)
    e.delete(0, END)

#equals to
def button_equal():
    s=e.get()
    if ma=='addition':
        e.delete(0,END)
        e.insert(0, f+int(s))
    if ma=='subtraction':
        e.delete(0,END)
        e.insert(0, f-int(s))
    if ma=='multiplication':
        e.delete(0,END)
        e.insert(0, f*int(s))
    if ma=='division':
        e.delete(0,END)
        e.insert(0, f/int(s))
    if ma=='sin':
        e.delete(0,END)
        e.insert(0, sin(float(f)))
    if ma=='cos':
        e.delete(0,END)
        e.insert(0, cos(float(f)))
    if ma=='tan':
        e.delete(0,END)
        e.insert(0, tan(float(f)))
    if ma=='log':
        e.delete(0,END)
        e.insert(0, log(float(f),10))
    if ma=='pow':
        e.delete(0,END)
        e.insert(0, int(pow(float(f),float(s))))
    if ma=='sqrt':
        e.delete(0,END)
        e.insert(0, sqrt(float(f)))

#clear function
def button_clear():
    e.delete(0, END)


#creating the buttons
button_1=Button(root,text="1",padx=30,pady=10,command=lambda : button_click(1))
button_2=Button(root,text="2",padx=30,pady=10,command=lambda : button_click(2))
button_3=Button(root,text="3",padx=31,pady=10,command=lambda : button_click(3))
button_4=Button(root,text="4",padx=30,pady=10,command=lambda : button_click(4))
button_5=Button(root,text="5",padx=30,pady=10,command=lambda : button_click(5))
button_6=Button(root,text="6",padx=31,pady=10,command=lambda : button_click(6))
button_7=Button(root,text="7",padx=30,pady=10,command=lambda : button_click(7))
button_8=Button(root,text="8",padx=30,pady=10,command=lambda : button_click(8))
button_9=Button(root,text="9",padx=31,pady=10,command=lambda : button_click(9))
button_0=Button(root,text="0",padx=72,pady=10,command=lambda : button_click(0))

button_add=Button(root,text="+",padx=29,pady=10,bg='#b8b894',fg='black',command=button_add)
button_sub=Button(root,text="-",padx=30,pady=10,bg='#b8b894',fg='black',command=button_sub)
button_mul=Button(root,text="*",padx=31,pady=10,bg='#b8b894',fg='black',command=button_mul)
button_div=Button(root,text="/",padx=31,pady=10,bg='#b8b894',fg='black',command=button_div)
button_clear=Button(root,text="AC",padx=25,pady=10,bg='yellow',fg='black',command=button_clear)
button_sin=Button(root,text="sin",padx=25,pady=10,bg='#b8b894',fg='black',command=button_sin)
button_cos=Button(root,text="cos",padx=25,pady=10,bg='#b8b894',fg='black',command=button_cos)
button_tan=Button(root,text="tan",padx=25,pady=10,bg='#b8b894',fg='black',command=button_tan)
button_abs=Button(root,text="pow",padx=22,pady=10,bg='#b8b894',fg='black',command=button_abs)
button_equal=Button(root,text="=",padx=30,pady=29,bg='red',fg='black',command=button_equal)
button_sqrt=Button(root,text="sqrt",padx=24,pady=10,bg='#b8b894',fg='black',command=button_sqrt)
button_log=Button(root,text="log",padx=25,pady=10,bg='#b8b894',fg='black',command=button_log)

#display of the buttons
button_clear.grid(row=1,column=0)
button_sin.grid(row=1,column=1)
button_cos.grid(row=1,column=2)
button_tan.grid(row=1,column=3)

button_add.grid(row=2,column=0)
button_sub.grid(row=2,column=1)
button_mul.grid(row=2,column=2)
button_div.grid(row=2,column=3)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_log.grid(row=3,column=3)

button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)
button_abs.grid(row=4,column=3)

button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)
button_equal.grid(row=5,column=3,rowspan=2)

button_0.grid(row=6,column=0,columnspan=2)
button_sqrt.grid(row=6,column=2)

#looping
root.mainloop()
