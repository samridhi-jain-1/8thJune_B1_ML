from tkinter import *
import tkinter.font as font
win=Tk()
win.geometry("300x350")
win.title('Basic Calculator')
win.configure(bg='lightgrey')
win.resizable(0,0)
expression=''
equation=StringVar(win)
def press(num):
    global expression
    expression = expression + num
    equation.set(expression)
def clear():
    global equation
    global expression
    expression=''
    equation.set('')
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""
myFont = font.Font(family='Helvetica',size=16,weight='bold')
Font = font.Font(family='Helvetica',size=12)
clr=Button(win,text='clr',command=clear,font=Font,relief=GROOVE)
clr.place(x=25,y=10,height=20,width=50)
e=Entry(win,textvariable=equation,font=('Helvetica',16),bd=2,justify=RIGHT)
e.place(x=25,y=40,height=40,width=250)
seven=Button(win,text='7',command=lambda :press('7'),width=3,height=1,font=myFont,relief=GROOVE)
seven.place(x=37,y=90)
eight=Button(win,text='8',command=lambda :press('8'),width=3,height=1,font=myFont,relief=GROOVE)
eight.place(x=97,y=90)
nine=Button(win,text='9',command=lambda :press('9'),width=3,height=1,font=myFont,relief=GROOVE)
nine.place(x=157,y=90)
add=Button(win,text='+',command=lambda :press('+'),width=3,height=1,font=myFont,relief=GROOVE)
add.place(x=217,y=90)
one=Button(win,text='1',command=lambda :press('1'),width=3,height=1,font=myFont,relief=GROOVE)
one.place(x=37,y=210)
two=Button(win,text='2',command=lambda :press('2'),width=3,height=1,font=myFont,relief=GROOVE)
two.place(x=97,y=210)
three=Button(win,text='3',command=lambda :press('3'),width=3,height=1,font=myFont,relief=GROOVE)
three.place(x=157,y=210)
mul=Button(win,text='*',command=lambda :press('*'),width=3,height=1,font=myFont,relief=GROOVE)
mul.place(x=217,y=210)
four=Button(win,text='4',command=lambda :press('4'),width=3,height=1,font=myFont,relief=GROOVE)
four.place(x=37,y=150)
five=Button(win,text='5',command=lambda :press('5'),width=3,height=1,font=myFont,relief=GROOVE)
five.place(x=97,y=150)
six=Button(win,text='6',command=lambda :press('6'),width=3,height=1,font=myFont,relief=GROOVE)
six.place(x=157,y=150)
sub=Button(win,text='-',command=lambda :press('-'),width=3,height=1,font=myFont,relief=GROOVE)
sub.place(x=217,y=150)
point=Button(win,text='.',command=lambda :press('.'),width=3,height=1,font=myFont,relief=GROOVE)
point.place(x=37,y=270)
zero=Button(win,text='0',command=lambda :press('0'),width=3,height=1,font=myFont,relief=GROOVE)
zero.place(x=97,y=270)
equal=Button(win,text='=',command=lambda :equalpress(),width=3,height=1,font=myFont,relief=GROOVE)
equal.place(x=157,y=270)
divide=Button(win,text='/',command=lambda :press('/'),width=3,height=1,font=myFont,relief=GROOVE)
divide.place(x=217,y=270)
win.mainloop()
