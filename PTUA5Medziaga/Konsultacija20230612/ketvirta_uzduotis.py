import tkinter as tk


# Function to convert temperature
def convert_to_f():
    try:
        temperature = float(entry.get())
        result = temperature * 9 / 5 + 32
        result_label.config(text="Result: " + str(result) + "°F")
    except ValueError:
        result_label.config(text="Invalid input")


def convert_to_c():
    try:
        temperature = float(entry.get())
        result = (temperature - 32) * 5 / 9
        result_label.config(text="Result: " + str(result) + "°C")
    except ValueError:
        result_label.config(text="Invalid input")


# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create input field and label
entry = tk.Entry(window)
entry.pack()

# Create the f to c convert button
convert_button = tk.Button(window, text="Fahrenheit to Celsius", command=convert_to_c)
convert_button.pack()

# Create the c to f convert button
convert_button = tk.Button(window, text="Celsius to Fahrenheit", command=convert_to_f)
convert_button.pack()

# Create the result label
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Start the main loop
window.mainloop()
