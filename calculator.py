import tkinter as tk

def calculate():
    first_number = int(first_number_entry.get())
    second_number = int(second_number_entry.get())
    operator = operator_entry.get()

    if operator == "1":
        result = first_number + second_number
        result_label.config(text="Result: " + str(result))
    elif operator == "2":
        result = first_number - second_number
        result_label.config(text="Result: " + str(result))
    elif operator == "3":
        result = first_number * second_number
        result_label.config(text="Result: " + str(result))
    elif operator == "4":
        result = first_number / second_number
        result_label.config(text="Result: " + str(result))
    else:
        result_label.config(text="Invalid operator")

# GUI setup
root = tk.Tk()
root.title("Calculator")

first_number_label = tk.Label(root, text="First number")
first_number_label.pack()
first_number_entry = tk.Entry(root)
first_number_entry.pack()

second_number_label = tk.Label(root, text="Second number")
second_number_label.pack()
second_number_entry = tk.Entry(root)
second_number_entry.pack()

operator_label = tk.Label(root, text="Operator (1-Addition, 2-Subtraction, 3-Multiplication, 4-Division)")
operator_label.pack()
operator_entry = tk.Entry(root)
operator_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Result")
result_label.pack()

root.mainloop()