from tkinter import *

home = Tk()
home.title("BASE CONVERTER")
home['bg'] = "#ff7a7a"
home.maxsize(width=430, height=680)

inputfield = Entry(home, font=('Arial', 40), fg='Gray25', bg='Gray85',
                   relief='sunken', bd=2)
inputfield.pack(fill='x', pady=10)

def key(value):
    inputfield.insert(END, value)

def clear():
    inputfield.delete(0, END)
    display.configure(state='normal')
    display.delete(1.0, END)
    display.configure(state='disabled')

Numeric = LabelFrame(home, text='Number Keys', bg='#ff7a7a')
Numeric.pack(fill='x', pady=10)

buttons = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['A', 'B', 'C'],
    ['D', 'E', 'F']
]

for i in range(5):
    for j in range(3):
        button = Button(Numeric, text=buttons[i][j], font=('Arial', 20), fg='cyan',
                        bg='#545454', width=8, command=lambda val=buttons[i][j]: key(val))
        button.grid(row=i, column=j)

button0 = Button(Numeric, text='0', font=('Arial', 20), fg='cyan',
                 bg='#545454', width=17, command=lambda: key(0))
button0.grid(row=5, column=0, columnspan=2)

buttonclear = Button(Numeric, text='Clear', font=('Arial', 20),
                     fg='cyan', bg='#545454', width=8, command=clear)
buttonclear.grid(row=5, column=2)

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def octal_to_decimal(octal):
    decimal = 0
    power = len(octal) - 1
    for digit in octal:
        decimal += int(digit) * (8 ** power)
        power -= 1
    return decimal

def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def hex_to_decimal(hexadecimal):
    decimal = 0
    power = len(hexadecimal) - 1
    for digit in hexadecimal:
        if digit.isdigit():
            decimal += int(digit) * (16 ** power)
        else:
            decimal += (ord(digit.upper()) - 55) * (16 ** power)
        power -= 1
    return decimal

def decimal_to_hex(decimal):
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder + 55) + hexadecimal
        decimal //= 16
    return hexadecimal

def Binary():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        decimal = binary_to_decimal(inputfield.get())
        display.insert(END, 'Decimal = ' + str(decimal))
        display.insert(END, '\nOctal = ' + decimal_to_octal(decimal))
        display.insert(END, '\nHexadecimal = ' + decimal_to_hex(decimal))
    except ValueError:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')

def Octal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        decimal = octal_to_decimal(inputfield.get())
        display.insert(END, 'Binary = ' + decimal_to_binary(decimal))
        display.insert(END, '\nDecimal = ' + str(decimal))
        display.insert(END, '\nHexadecimal = ' + decimal_to_hex(decimal))
    except ValueError:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')

def Decimal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        decimal = int(inputfield.get())
        display.insert(END, 'Binary = ' + decimal_to_binary(decimal))
        display.insert(END, '\nOctal = ' + decimal_to_octal(decimal))
        display.insert(END, '\nHexadecimal = ' + decimal_to_hex(decimal))
    except ValueError:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')

def Hexadecimal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        decimal = hex_to_decimal(inputfield.get())
        display.insert(END, 'Binary = ' + decimal_to_binary(decimal))
        display.insert(END, '\nOctal = ' + decimal_to_octal(decimal))
        display.insert(END, '\nDecimal = ' + str(decimal))
    except ValueError:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')

button = LabelFrame(home, text="Input Type Data ", bg='#ff7a7a')
button.pack(fill='both', pady=5)

binaryButton = Button(button, text="Binary", font=('Arial', 15), fg='#f7ff5c', bg='#3b3b3b', width=18, command=Binary)
binaryButton.grid(row=0, column=0)

octalButton = Button(button, text="Octal", font=('Arial', 15), fg='#f7ff5c', bg='#3b3b3b', width=18, command=Octal)
octalButton.grid(row=0, column=1)

decimalButton = Button(button, text="Decimal", font=('Arial', 15), fg='#f7ff5c', bg='#3b3b3b', width=18, command=Decimal)
decimalButton.grid(row=1, column=0)

hexaButton = Button(button, text="Hexa Decimal", font=('Arial', 15), fg='#f7ff5c', bg='#3b3b3b', width=18, command=Hexadecimal)
hexaButton.grid(row=1, column=1)

display = Text(home, font=('Arial', 18), fg='Gray25', bg='Gray85', relief='raised', bd=1)
display.pack(fill='x')
display.configure(state='disabled')

home.mainloop()
