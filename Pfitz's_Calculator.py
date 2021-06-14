from tkinter import *
from math import sqrt

root = Tk()
root.title("Pfitz's Calculator")

display = Entry(root, width=21, borderwidth=3, bg="medium aquamarine", font=('Calibri', 22), justify="right")
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

m = 0

def button_click(number):
    num = display.get()
    display.delete(0, END)
    if num == "0":
        display.insert(0, str(num))
    else:
        display.insert(0, str(num) + str(number))

def button_mrc():
    display.delete(0, END)
    global m
    display.insert(0, str(m))

def button_m_minus():
    dis = display.get()
    global m
    if "." in dis:
        m -= float(dis)
    else:
        m -= int(dis)
    display.delete(0, END)

def button_m_plus():
    dis = display.get()
    global m
    if "." in dis:
        m += float(dis)
    else:
        m += int(dis)
    display.delete(0, END)

def button_clear():
    display.delete(0, END)
    global m
    m = 0

def button_del_last():
    numm = display.get()
    last_del = numm[0:-1]
    display.delete(0, END)
    display.insert(0, str(last_del))

def button_percentage():
    display_num2 = display.get()
    display.delete(0, END)
    if symbol == 'X':
        if "." in display_num or "." in display_num2:
            display.insert(0, (float(display_num)/100) * float(display_num2))
        else:
            display.insert(0, (int(display_num)/100) * int(display_num2))

def button_sqrt():
    num = display.get()
    if "." in num:
        rad = sqrt(float(num))
    else:
        rad = sqrt(int(num))
    display.delete(0, END)
    display.insert(0, str(rad))

def button_multiply():
    display_number = display.get()
    global symbol
    global display_num
    symbol = 'X'
    display_num = display_number
    display.delete(0, END)

def button_divide():
    display_number = display.get()
    global symbol
    global display_num
    symbol = '/'
    display_num = display_number
    display.delete(0, END)

def button_add():
    display_number = display.get()
    global symbol
    global display_num
    symbol = '+'
    display_num = display_number
    display.delete(0, END)

def button_subtract():
    display_number = display.get()
    global symbol
    global display_num
    symbol = '-'
    display_num = display_number
    display.delete(0, END)

def button_swap():
    num = display.get()
    if '-' in num:
        display.delete(0, END)
        display.insert(0, str(num[1:]))
    else:
        display.delete(0, END)
        display.insert(0, '-' + str(num))

def button_dot():
    num = display.get()
    display.delete(0, END)
    if "." not in num:
        display.insert(0, str(num) + '.')
    else:
        display.insert(0, str(num))

def button_equal():
    display_number_2 = display.get()
    display.delete(0, END)

    if symbol == '+':
        if "." in display_num or "." in display_number_2:
            display.insert(0, float(display_num) + float(display_number_2))
        else:
            display.insert(0, int(display_num) + int(display_number_2))

    elif symbol == '-':
        if "." in display_num or "." in display_number_2:
            display.insert(0, float(display_num) - float(display_number_2))
        else:
            display.insert(0, int(display_num) - int(display_number_2))

    elif symbol == 'X':
        if "." in display_num or "." in display_number_2:
            display.insert(0, float(display_num) * float(display_number_2))
        else:
            display.insert(0, int(display_num) * int(display_number_2))

    elif symbol == '/':
        if "." in display_num or "." in display_number_2:
            display.insert(0, float(display_num) / float(display_number_2))
        else:
            display.insert(0, int(display_num) / int(display_number_2))

    else:
        display.insert(0, display_number_2)


button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_mrc = Button(root, text='MRC', padx=30, pady=20, command=button_mrc)
button_m_minus = Button(root, text='M- ', padx=33, pady=20, command=button_m_minus)
button_m_plus = Button(root, text='M+ ', padx=32, pady=20, command=button_m_plus)
button_clear = Button(root, text='AC', padx=20, pady=20, command=button_clear)
button_del_last = Button(root, text='←', padx=22, pady=20, command=button_del_last)

button_percentage = Button(root, text='%', padx=23, pady=20, command=button_percentage)
button_sqrt = Button(root, text='√', padx=23, pady=20, command=button_sqrt)

button_multiply = Button(root, text='X ', padx=23, pady=19, command=button_multiply)
button_divide = Button(root, text='/ ', padx=23, pady=20, command=button_divide)

button_add = Button(root, text='+', padx=24, pady=52, command=button_add)
button_subtract = Button(root, text='- ', padx=23, pady=20, command=button_subtract)

button_dot = Button(root, text='. ', padx=40, pady=20, command=button_dot)
button_swap = Button(root, text='+/-', padx=34, pady=20, command=button_swap)
button_equal = Button(root, text='=', padx=23, pady=20, command=button_equal)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=1)

button_mrc.grid(row=1, column=0)
button_m_minus.grid(row=1, column=1)
button_m_plus.grid(row=1, column=2)
button_clear.grid(row=1, column=3)
button_del_last.grid(row=1, column=4)

button_percentage.grid(row=2, column=3)
button_sqrt.grid(row=2, column=4)

button_multiply.grid(row=3, column=3)
button_divide.grid(row=3, column=4)

button_add.grid(row=4, column=3, rowspan=2)
button_subtract.grid(row=4, column=4)

button_swap.grid(row=5, column=0)
button_dot.grid(row=5, column=2)
button_equal.grid(row=5, column=4)

root.mainloop()


