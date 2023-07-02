from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime
###################################################################################
operator = ''
IVA = 0.21
price_food = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
price_drink = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
price_dessert = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]
###################################################################################
def click_button(number):
    global operator
    operator = operator + number
    calculator_viewer.delete(0, END)
    calculator_viewer.insert(END, operator)

def clear():
    global operator
    operator = ''
    calculator_viewer.delete(0, END)

def result():
    global operator
    result = str(eval(operator))
    calculator_viewer.delete(0, END)
    calculator_viewer.insert(END, result)
    operator = ''

def review_check():
    x = 0
    for f in food_boxes:
        if food_variable[x].get() == 1:
            food_boxes[x].config(state=NORMAL)
            if food_boxes[x].get() == '0':
                food_boxes[x].delete(0, END)
            food_boxes[x].focus()
        else:
            food_boxes[x].config(state=DISABLED)
            food_text[x].set('0')
        x+=1
    
    y = 0
    for d in drink_boxes:
        if drink_variable[y].get() == 1:
            drink_boxes[y].config(state=NORMAL)
            if drink_boxes[y].get() == '0':
                drink_boxes[y].delete(0, END)
            drink_boxes[y].focus()
        else:
            drink_boxes[y].config(state=DISABLED)
            drink_text[y].set('0')
        y+=1
    
    z = 0
    for c in dessert_boxes:
        if dessert_variable[z].get() == 1:
            dessert_boxes[z].config(state=NORMAL)
            if dessert_boxes[z].get() == '0':
                dessert_boxes[z].delete(0, END)
            dessert_boxes[z].focus()
        else:
            dessert_boxes[z].config(state=DISABLED)
            dessert_text[z].set('0')
        z+=1

def total():
    # ----------------------------------------------------------
    # TOTALS
    # ----------------------------------------------------------
    # food sub total 
    sub_total_food = 0
    p = 0
    for cant in food_text:
        sub_total_food += float(cant.get()) * price_food[p]
        p+=1
    # drink sub total
    sub_total_drink = 0
    p = 0
    for cant in drink_text:
        sub_total_drink += float(cant.get()) * price_drink[p]
        p+=1
    # dessert sub total
    sub_total_dessert = 0
    p = 0
    for cant in dessert_text:
        sub_total_dessert += float(cant.get()) * price_dessert[p]
        p+=1
    sub_total = sub_total_food + sub_total_drink + sub_total_dessert
    taxes = sub_total * IVA
    total = sub_total + taxes
    # ----------------------------------------------------------
    # PRINTS
    # ----------------------------------------------------------
    var_food_cost.set(f'${round(sub_total_food, 2)}')
    var_drink_cost.set(f'${round(sub_total_drink, 2)}')
    var_dessert_cost.set(f'${round(sub_total_dessert, 2)}')
    var_subtotal.set(f'${round(sub_total, 2)}')
    var_import_tax.set(f'${round(taxes, 2)}')
    var_total.set(f'${round(total, 2)}')

def invoice():
    invoice_text.delete(1.0, END)
    num_invoice = f'N# - {random.randint(1000, 9999)}'
    thisDate = datetime.datetime.now()
    date_invoice = f'{thisDate.day}/{thisDate.month}/{thisDate.year} - {thisDate.hour}:{thisDate.minute}'
    invoice_text.insert(END, f'Data: \t {num_invoice}\t\t {date_invoice}\n')
    invoice_text.insert(END, f'*'*55+'\n')
    invoice_text.insert(END, 'Items\t\tCant\t\t\tPrice\n')
    invoice_text.insert(END, f'*'*55+'\n')

    x = 0
    for food in food_text:
        if food.get() != '0':
            invoice_text.insert(END, f'{foods_list[x]}\t\t{food.get()}\t\t'
                                f'${int(food.get())*price_food[x]}\n')
        x+=1
    
    y = 0
    for drink in drink_text:
        if drink.get() != '0':
            invoice_text.insert(END, f'{drinks_list[y]}\t\t{drink.get()}\t\t'
                                f'${int(drink.get())*price_drink[y]}\n')
        y+=1
    
    z = 0
    for dessert in dessert_text:
        if dessert.get() != '0':
            invoice_text.insert(END, f'{desserts_list[z]}\t\t{dessert.get()}\t\t'
                                f'${int(dessert.get())*price_dessert[z]}\n')
        z+=1

    invoice_text.insert(END, f'-'*55+'\n')
    invoice_text.insert(END, f'Food costs:\t\t\t${var_food_cost.get()}\n')
    invoice_text.insert(END, f'Drink costs:\t\t\t${var_drink_cost.get()}\n')
    invoice_text.insert(END, f'Dessert costs:\t\t\t${var_dessert_cost.get()}\n')
    invoice_text.insert(END, f'-'*55+'\n')
    invoice_text.insert(END, f'Subtotal:\t\t\t${var_subtotal.get()}\n')
    invoice_text.insert(END, f'Import tax:\t\t\t${var_import_tax.get()}\n')
    invoice_text.insert(END, f'Total:\t\t\t${var_total.get()}\n')
    invoice_text.insert(END, f'-'*55+'\n')
    invoice_text.insert(END, f'Thanks you. Have a nice day!\n')

def save():
    info_invoice = invoice_text.get(1.0, END)
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    
    with open(file, 'w') as f:
        f.write(info_invoice)
    f.close()
    messagebox.showinfo('Saved', 'Invoice saved')

def clear_all():
    invoice_text.delete(0.1, END)

    for food in food_text:
        food.set('0')
    for drink in drink_text:
        drink.set('0')
    for dessert in dessert_text:
        dessert.set('0')
    
    for box in food_boxes:
        box.config(state=DISABLED)
    for box in drink_boxes:
        box.config(state=DISABLED)
    for box in dessert_boxes:
        box.config(state=DISABLED)

    for var in food_variable:
        var.set(0)
    for var in drink_variable:
        var.set(0)
    for var in dessert_variable:
        var.set(0)

    var_dessert_cost.set('')
    var_drink_cost.set('')
    var_food_cost.set('')
    var_subtotal.set('')
    var_import_tax.set('')
    var_total.set('')

###################################################################################

# INIT TKINTER
app = Tk()

# set window properties
w_height = 630
w_width = 1248
x_init_coordinate = 0
y_init_coordinate = 0
app.geometry(f"{w_width}x{w_height}+{x_init_coordinate}+{y_init_coordinate}")

# disable maximize
app.resizable(0,0)


# set window title
app.title("My Restaurant - Invoice system")

#set background color
app.configure(background="burlywood")

#######################################################################
# UPPER PANEL
upper_panel = Frame(app, bd=1, relief=FLAT)
upper_panel.pack(side=TOP, fill=X)

# Label title
label_title = Label(upper_panel, text="Invoice system", fg="azure4", 
                    font=("Dosis", 58), bg="burlywood",width=30)
label_title.grid(row=0, column=0)
#######################################################################
# LEFT PANEL
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Cost panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT,bg='azure4',padx=50)
cost_panel.pack(side=BOTTOM)

# Food panel
food_panel = LabelFrame(left_panel, text="Food", font=("Dosis", 19, "bold"),
                        bd=1, relief=FLAT, fg="azure4")
food_panel.pack(side=LEFT)

# Drink panel
drink_panel = LabelFrame(left_panel, text="Drinks", font=("Dosis", 19, "bold"),
                        bd=1, relief=FLAT, fg="azure4")
drink_panel.pack(side=LEFT)

# Desserts panel
desserts_panel = LabelFrame(left_panel, text="Desserts", font=("Dosis", 19, "bold"),
                        bd=1, relief=FLAT, fg="azure4")
desserts_panel.pack(side=LEFT)

#######################################################################
# RIGHT PANEL
right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# calc panel
calc_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
calc_panel.pack()

# invoice panel
invoice_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
invoice_panel.pack()

# buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
buttons_panel.pack()

#######################################################################
# MENU PANEL CONTENTS
foods_list    = ["Pizza", "Burger", "Pasta", "Salad", "Soup", "Salad", "Soup", "Salad"]
drinks_list   = ['Wine Merlot', 'Beer', 'Water', 'Juice', 'Wine Malbet', 'Coke', 'Coffee', 'Tea']
desserts_list = ['Chocolate Cake', 'Pudding', 'Ice Cream', 'Sandwich', 'Cream Cake', 'Flan', 'Mousse', 'Brownie']

food_variable = []
food_boxes = []
food_text = []
counter = 0
for item in foods_list:
    food_variable.append('')
    food_variable[counter]=IntVar()
    food = Checkbutton(food_panel, text=item.title(), font=("Dosis", 19, "bold"),
                       onvalue=1,offvalue=0, variable=food_variable[counter],
                       command=review_check)
    
    food.grid(row=counter, column=0,sticky=W)
    # create input boxes
    food_boxes.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set(0)
    food_boxes[counter] = Entry(food_panel,font=("Dosis", 19, "bold"), bd=1,width=6,
                                state=DISABLED,textvariable=food_text[counter])
    food_boxes[counter].grid(row=counter, column=1)
    counter += 1

drink_variable = []
drink_boxes = []
drink_text = []
counter = 0
for item in drinks_list:
    drink_variable.append('')
    drink_variable[counter]=IntVar()
    drink = Checkbutton(drink_panel, text=item.title(), font=("Dosis", 19, "bold"),
                       onvalue=1,offvalue=0, variable=drink_variable[counter],
                       command=review_check)
    drink.grid(row=counter, column=0,sticky=W)
    # create input boxes
    drink_boxes.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set(0)
    drink_boxes[counter] = Entry(drink_panel,font=("Dosis", 19, "bold"), bd=1,width=6,
                                state=DISABLED,textvariable=drink_text[counter])
    drink_boxes[counter].grid(row=counter, column=1)
    counter += 1

dessert_variable = []
dessert_boxes = []
dessert_text = []
counter = 0
for item in desserts_list:
    dessert_variable.append('')
    dessert_variable[counter]=IntVar()
    dessert = Checkbutton(desserts_panel, text=item.title(), font=("Dosis", 19, "bold"),
                       onvalue=1,offvalue=0, variable=dessert_variable[counter],
                       command=review_check)
    dessert.grid(row=counter, column=0,sticky=W)

    # create input boxes
    dessert_boxes.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set(0)
    dessert_boxes[counter] = Entry(desserts_panel,font=("Dosis", 19, "bold"), bd=1,width=6,
                                state=DISABLED,textvariable=dessert_text[counter])
    dessert_boxes[counter].grid(row=counter, column=1)
    counter += 1


#######################################################################
# COST PANEL CONTENTS
var_food_cost = StringVar()
var_drink_cost = StringVar()
var_dessert_cost = StringVar()

var_subtotal = StringVar()
var_import_tax = StringVar()
var_total = StringVar()

#--------------------------------------------------------------------------------
Label_food_cost = Label(cost_panel, text="Food Cost", font=("Dosis", 12, "bold"),
                        bg="azure4", fg="white")
Label_food_cost.grid(row=0, column=0)
text_food_cost = Entry(cost_panel,font=("Dosis", 12, "bold"), bd=1,width=10,
                        state='readonly',textvariable=var_food_cost)
text_food_cost.grid(row=0, column=1,padx=41)

#--------------------------------------------------------------------------------
Label_drink_cost = Label(cost_panel, text="Drink Cost", font=("Dosis", 12, "bold"),
                        bg="azure4", fg="white")
Label_drink_cost.grid(row=1, column=0)
text_drink_cost = Entry(cost_panel,font=("Dosis", 12, "bold"), bd=1,width=10,
                        state='readonly',textvariable=var_food_cost)
text_drink_cost.grid(row=1, column=1,padx=41)

#--------------------------------------------------------------------------------
Label_dessert_cost = Label(cost_panel, text="Dessert Cost", font=("Dosis", 12, "bold"),
                        bg="azure4", fg="white")
Label_dessert_cost.grid(row=2, column=0)
text_dessert_cost = Entry(cost_panel,font=("Dosis", 12, "bold"), bd=1,width=10,
                        state='readonly',textvariable=var_food_cost)
text_dessert_cost.grid(row=2, column=1,padx=41)

#--------------------------------------------------------------------------------
Label_subtotal = Label(cost_panel, text="Subtotal", font=("Dosis", 12, "bold"),
                        bg="azure4", fg="white")
Label_subtotal.grid(row=0, column=2)
text_subtotal = Entry(cost_panel,font=("Dosis", 12, "bold"), bd=1,width=10,
                        state='readonly',textvariable=var_subtotal)
text_subtotal.grid(row=0, column=3,padx=41)

#--------------------------------------------------------------------------------
Label_import_tax = Label(cost_panel, text="Import Tax", font=("Dosis", 12, "bold"),
                        bg="azure4", fg="white")
Label_import_tax.grid(row=1, column=2)
text_import_tax = Entry(cost_panel,font=("Dosis", 12, "bold"), bd=1,width=10,
                        state='readonly',textvariable=var_import_tax)
text_import_tax.grid(row=1, column=3,padx=41)

#--------------------------------------------------------------------------------f
Label_total = Label(cost_panel, text="Total", font=("Dosis", 12, "bold"),
                        bg="azure4", fg="white")
Label_total.grid(row=2, column=2)
text_total = Entry(cost_panel,font=("Dosis", 12, "bold"), bd=1,width=10,
                        state='readonly',textvariable=var_total)
text_total.grid(row=2, column=3,padx=41)


#######################################################################
# BUTTONS PANEL CONTENTS
buttons = ['Total','Invoice','Save','Reset']
created_buttons = []

columns = 0
for button in buttons:
    button = Button(buttons_panel, text=button.title(), font=("Dosis", 14, "bold"),
           bg="azure4", fg="white",bd=1, width=9, command=button)
    columns += 1
    button.grid(row=0, column=columns)
    created_buttons.append(button)

created_buttons[0].config(command=total)
created_buttons[1].config(command=invoice)
created_buttons[2].config(command=save)
created_buttons[3].config(command=clear_all)

#######################################################################
# INVOICE PANEL CONTENTS
invoice_text = Text(invoice_panel, font=("Dosis", 12, "bold"), width=50, height=10)
invoice_text.grid(row=0, column=0)

#######################################################################
# CALC PANEL CONTENTS 
calculator_viewer = Entry(calc_panel,font=("Dosis", 16, "bold"), bd=1,width=32)
calculator_viewer.grid(row=0, column=0,columnspan=4)

buttom_calc = ['7','8','9','+','4','5','6','-','1','2','3','x','=','Clear','0','/']

button_saved = []

rows = 1
cols = 0
for button in buttom_calc:
    button = Button(calc_panel, text=button.title(), font=("Dosis", 16, "bold"),
                    bg="azure4", fg="white",bd=1, width=8)
    
    button_saved.append(button)
    button.grid(row=rows, column=cols)

    if cols == 3: rows += 1
    cols += 1
    if cols == 4: cols = 0
#######################################################################

button_saved[0].config(command=lambda : click_button('7'))
button_saved[1].config(command=lambda : click_button('8'))
button_saved[2].config(command=lambda : click_button('9'))
button_saved[3].config(command=lambda : click_button('+'))
button_saved[4].config(command=lambda : click_button('4'))
button_saved[5].config(command=lambda : click_button('5'))
button_saved[6].config(command=lambda : click_button('6'))
button_saved[7].config(command=lambda : click_button('-'))
button_saved[8].config(command=lambda : click_button('1'))
button_saved[9].config(command=lambda : click_button('2'))
button_saved[10].config(command=lambda : click_button('3'))
button_saved[11].config(command=lambda : click_button('*'))
button_saved[14].config(command=lambda : click_button('0'))
button_saved[15].config(command=lambda : click_button('/'))

button_saved[12].config(command=lambda : result())
button_saved[13].config(command=lambda : clear())

#######################################################################
# keep window open
app.mainloop()