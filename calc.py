from tkinter import *

# Window oif the ap
app = Tk()
app.title('Compound interest calculator')
app.geometry('700x700')

# UI
# principal
principal_text = StringVar()
principal_label = Label(app, text="Principal Amount", font=('bold', 14), pady=20)
principal_label.grid(row=0, column=0, sticky=W)
principal_entry = Entry(app, textvariable=principal_text)
principal_entry.grid(row=0, column=1)

# Interest rate
interest_text = StringVar()
interest_label = Label(app, text="Interest rate", font=('bold', 14), pady=20)
interest_label.grid(row=1, column=0, sticky=W)
interest_entry = Entry(app, textvariable=interest_text)
interest_entry.grid(row=1, column=1)





# Starting the program
app.mainloop()






# Equation for calculating interest rates
principal = 0
interest_rate = 0
compounding_frequency = 0
time = 0

interest_amount = principal * (1 + (interest_rate / compounding_frequency)) ** (compounding_frequency * time)