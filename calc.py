from tkinter import *

# Window oif the ap
app = Tk()
app.title('Compound interest calculator')
app.geometry('800x500')

# Equation for calculating interest rates
def calc_amount(principal, interest_rate, compounding_frequency, time):
    interest_amount = principal * (1 + (interest_rate / compounding_frequency)) ** (compounding_frequency * time)
    return interest_amount

def clear():
    pass


# UI
# principal
principal_text = StringVar()
principal_label = Label(app, text="Principal Amount", font=('bold', 14), pady=20)
principal_label.grid(row=0, column=0, sticky=W)
principal_entry = Entry(app, textvariable=principal_text)
principal_entry.grid(row=0, column=1)

# Interest rate
interest_text = StringVar()
interest_label = Label(app, text="Interest rate(%)", font=('bold', 14))
interest_label.grid(row=0, column=2, sticky=W)
interest_entry = Entry(app, textvariable=interest_text)
interest_entry.grid(row=0, column=3)

# compounding frequency
compound_text = StringVar()
compound_label = Label(app, text="Compound Frequency", font=('bold', 14))
compound_label.grid(row=1, column=0, sticky=W)
compound_entry = Entry(app, textvariable=compound_text)
compound_entry.grid(row=1, column=1)

# Time
time_text = StringVar()
time_label = Label(app, text="Time for maturity", font=('bold', 14))
time_label.grid(row=1, column=2, sticky=W)
time_entry = Entry(app, textvariable=interest_text)
time_entry.grid(row=1, column=3)


# Buttons
calculate_btn = Button(app, text='Calculate Amount After Maturity', width=24, command=calc_amount)
calculate_btn.grid(row=2, column=1, pady=20)

clear_btn = Button(app, text='Clear Entries', width=24, command=clear)
clear_btn.grid(row=2, column=2)





# Starting the program
app.mainloop()
