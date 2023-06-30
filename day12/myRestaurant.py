from tkinter import *

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
                       onvalue=1,offvalue=0, variable=food_variable[counter])
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
                       onvalue=1,offvalue=0, variable=drink_variable[counter])
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
                       onvalue=1,offvalue=0, variable=dessert_variable[counter])
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

#--------------------------------------------------------------------------------
Label_total = Label(cost_panel, text="Total", font=("Dosis", 12, "bold"),
                        bg="azure4", fg="white")
Label_total.grid(row=2, column=2)
text_total = Entry(cost_panel,font=("Dosis", 12, "bold"), bd=1,width=10,
                        state='readonly',textvariable=var_total)
text_total.grid(row=2, column=3,padx=41)


#######################################################################
# BUTTONS PANEL CONTENTS
buttons = ['Total','Invoice','Save','Reset']

columns = 0
for button in buttons:
    button = Button(buttons_panel, text=button.title(), font=("Dosis", 14, "bold"),
           bg="azure4", fg="white",bd=1, width=9, command=button)
    columns += 1
    button.grid(row=0, column=columns)

#######################################################################
# INVOICE PANEL CONTENTS
invoice_text = Text(invoice_panel, font=("Dosis", 12, "bold"), width=50, height=10)
invoice_text.grid(row=0, column=0)

#######################################################################
# CALC PANEL CONTENTS 
calculator_viewer = Entry(calc_panel,font=("Dosis", 16, "bold"), bd=1,width=32)
calculator_viewer.grid(row=0, column=0,columnspan=4)

buttom_calc = ['7','8','9','+','4','5','6','-','1','2','3','x','CE','Clear','0','/']

rows = 0
cols = 0
for button in buttom_calc:
    button = Button(calc_panel, text=button.title(), font=("Dosis", 16, "bold"),
                    bg="azure4", fg="white",bd=1, width=8)
    button.grid(row=rows, column=cols)

    if cols == 3: rows += 1
    cols += 1
    if cols == 4: cols = 0
#######################################################################
# keep window open
app.mainloop()