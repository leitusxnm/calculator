# Name: Jon Lewyn Tanggaro
# Computer programming

import tkinter as tk

def set_data(data):
    result_entry.insert(tk.END, data)

def get_result():
    expression = result_entry.get()
    try:
        res = eval(expression)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, res)
    except Exception as e:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Error")

main_window = tk.Tk()
main_window.title("Calculator")

result_entry = tk.Entry(main_window)
result_entry.pack()

button_frame = tk.Frame(main_window)

button_1 = tk.Button(master=button_frame, text="1", width=2, command=lambda: set_data("1"))
button_1.grid(row=0, column=0)

button_2 = tk.Button(master=button_frame, text="2", width=2, command=lambda: set_data("2"))
button_2.grid(row=0, column=1)

button_3 = tk.Button(master=button_frame, text="3", width=2, command=lambda: set_data("3"))
button_3.grid(row=0, column=2)

button_4 = tk.Button(master=button_frame, text="4", width=2, command=lambda: set_data("4"))
button_4.grid(row=1, column=0)

button_5 = tk.Button(master=button_frame, text="5", width=2, command=lambda: set_data("5"))
button_5.grid(row=1, column=1)

button_6 = tk.Button(master=button_frame, text="6", width=2, command=lambda: set_data("6"))
button_6.grid(row=1, column=2)

button_7 = tk.Button(master=button_frame, text="7", width=2, command=lambda: set_data("7"))
button_7.grid(row=2, column=0)

button_8 = tk.Button(master=button_frame, text="8", width=2, command=lambda: set_data("8"))
button_8.grid(row=2, column=1)

button_9 = tk.Button(master=button_frame, text="9", width=2, command=lambda: set_data("9"))
button_9.grid(row=2, column=2)

button_dot = tk.Button(master=button_frame, text=".", width=2, command=lambda: set_data("."))
button_dot.grid(row=3, column=0)

button_0 = tk.Button(master=button_frame, text="0", width=6, command=lambda: set_data("0"))
button_0.grid(row=3, column=1, columnspan=2)

button_add = tk.Button(master=button_frame, text="+", width=2, command=lambda: set_data("+"))
button_add.grid(row=0, column=3)

button_subtract = tk.Button(master=button_frame, text="-", width=2, command=lambda: set_data("-"))
button_subtract.grid(row=1, column=3)

button_empty = tk.Button(master=button_frame, text="", width=2, command=lambda: set_data(""))
button_empty.grid(row=2, column=3)

button_divide = tk.Button(master=button_frame, text="/", width=2, command=lambda: set_data("/"))
button_divide.grid(row=3, column=3)

button_equals = tk.Button(master=button_frame, text="=", width=2, command=lambda: get_result())
button_equals.grid(row=4, column=0)

button_frame.pack()

main_window.mainloop()
