import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def on_calculate_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values for weight and height.")
        return

    if weight <= 0 or height <= 0:
        messagebox.showerror("Error", "Weight and height must be positive values.")
        return

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Enter your weight in kilograms:")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Enter your height in meters:")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=on_calculate_clicked)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
