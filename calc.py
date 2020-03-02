
import tkinter as tk
from functools import partial


def call_result(label_result, n1, n2, n3, n4):
    principal = (n1.get())
    interest_rate = (n2.get())
    compounding_frequency = (n3.get())
    time = (n4.get())
    print(principal, interest_rate, compounding_frequency, time)
    result = int(principal) * (1 + (int(interest_rate) / int(compounding_frequency))) ** (int(compounding_frequency) * int(time))
    label_result.config(text="Result is %d" % result)
    return


root = tk.Tk()
root.geometry('700x500')
root.title('Simple Calculator')
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()
labelTitle = tk.Label(root, text="Simple Calculator").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Principal($)").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Interest rate(%)").grid(row=2, column=0)
labelNum3 = tk.Label(root, text="Compounding Frequency").grid(row=3, column=0)
labelNum4 = tk.Label(root, text="Time To Maturity(Years)").grid(row=4, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)
entryNum4 = tk.Entry(root, textvariable=number4).grid(row=4, column=2)

call_result = partial(call_result, labelResult, number1, number2, number3, number4)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=6, column=0)
root.mainloop()