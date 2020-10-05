from tkinter import *
root = Tk()
root.title("Simple Calculator")

e=Entry(root,width=50,borderwidth=10,bg="#6B6B69",fg="white")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def add_sum():
    value=e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(value)
    e.delete(0,END)


def equal_press():
    second_number = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0,f_num + int(second_number))
    if math == 'subtract':
        e.insert(0,f_num - int(second_number))
    if math == 'division':
        e.insert(0,f_num / int(second_number))
    if math == 'multiplication':
        e.insert(0,f_num * int(second_number))



def button_subtract():
    value=e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(value)
    e.delete(0,END)

def button_multiply():
    value=e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(value)
    e.delete(0,END)

def button_divide():
    value=e.get()
    global f_num
    global math
    math = "division"
    f_num = int(value)
    e.delete(0,END)


def button_clear():
    e.delete(0,END)


button_1 = Button(root,text="1",padx=50,pady=50,command=lambda :button_click(1),font=1000,bg="light blue")
button_2 = Button(root,text="2",padx=50,pady=50,command=lambda:button_click(2),font=1000,bg="light blue")
button_3 = Button(root,text="3",padx=50,pady=50,command=lambda:button_click(3),font=1000,bg="light blue")
button_4 = Button(root,text="4",padx=50,pady=50,command=lambda:button_click(4),font=1000,bg="light blue")
button_5 = Button(root,text="5",padx=50,pady=50,command=lambda:button_click(5),font=1000,bg="light blue")
button_6 = Button(root,text="6",padx=50,pady=50,command=lambda:button_click(6),font=1000,bg="light blue")
button_7 = Button(root,text="7",padx=50,pady=50,command=lambda:button_click(7),font=1000,bg="light blue")
button_8 = Button(root,text="8",padx=50,pady=50,command=lambda:button_click(8),font=1000,bg="light blue")
button_9 = Button(root,text="9",padx=50,pady=50,command=lambda:button_click(9),font=1000,bg="light blue")
button_0 = Button(root,text="0",padx=50,pady=50,command=lambda:button_click(0),font=1000,bg="light blue")

button_add = Button(root,text="+",padx=50,pady=50,command=add_sum,font=1000,bg="#ffa07a")
button_clear = Button(root,text="Clear",padx=50,pady=50,command=button_clear,font=1000,bg="#1ADC8A")
button_equal = Button(root,text="=",padx=50,pady=50,command=equal_press,font=1000,bg="#ffa07a")
button_multiply = Button(root,text="×",padx=50,pady=50,command=button_multiply,font=1000,bg="#ffa07a")
button_subtract = Button(root,text="-",padx=50,pady=50,command=button_subtract,font=1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,bg="#ffa07a")
button_divide = Button(root,text="/",padx=50,pady=50,command=button_divide,font=1000,bg="#ffa07a")


button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=0)

button_add.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=3)
button_multiply.grid(row=1,column=3)
button_subtract.grid(row=2,column=3)
button_divide.grid(row=3,column=3)


root.mainloop()
