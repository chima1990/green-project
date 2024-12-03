import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Greenhouse Management System")

# Create a canvas to draw the greenhouse
canvas = tk.Canvas(root, width=800, height=600, bg='lightblue')
canvas.pack()

# Draw greenhouse structure
canvas.create_rectangle(100, 100, 700, 500, outline='black', fill='lightgreen', width=2)  # Greenhouse frame
canvas.create_rectangle(150, 150, 650, 450, outline='black', fill='lightyellow', width=2)  # Greenhouse interior

# Draw plants inside the greenhouse
for x in range(150, 650, 100):
    for y in range(150, 450, 100):
        canvas.create_oval(x, y, x + 50, y + 50, outline='black', fill='green', width=2)

# Draw additional elements: sprinklers, window, and fan
# Sprinklers (represented as blue circles)
canvas.create_oval(550, 400, 600, 450, outline='black', fill='blue', width=2, tags="sprinkler")
canvas.create_oval(200, 400, 250, 450, outline='black', fill='blue', width=2, tags="sprinkler")

# Window (represented as a gray rectangle)
canvas.create_rectangle(300, 50, 500, 100, outline='black', fill='gray', width=2, tags="window")

# Fan (represented as a gray circle with blades)
canvas.create_oval(600, 50, 650, 100, outline='black', fill='gray', width=2, tags="fan")
canvas.create_line(625, 50, 625, 100, fill='black', width=2, tags="fan")  # Vertical blade
canvas.create_line(600, 75, 650, 75, fill='black', width=2, tags="fan")  # Horizontal blade

# Add name tags
canvas.create_text(575, 475, text="Sprinkler 1", font=("Helvetica", 12), fill="black")
canvas.create_text(225, 475, text="Sprinkler 2", font=("Helvetica", 12), fill="black")
canvas.create_text(400, 25, text="Window", font=("Helvetica", 12), fill="black")
canvas.create_text(625, 125, text="Fan", font=("Helvetica", 12), fill="black")

# Create placeholder functions for buttons
def monitor_conditions():
    output_label.config(text="Monitoring conditions...")

def add_light():
    output_label.config(text="Increasing lighting...")

def add_water():
    output_label.config(text="Increasing watering...")

def toggle_sprinklers():
    current_fill = canvas.itemcget("sprinkler", "fill")
    new_fill = 'lightblue' if current_fill == 'blue' else 'blue'
    canvas.itemconfig("sprinkler", fill=new_fill)
    output_label.config(text="Toggled sprinklers.")

def toggle_window():
    current_fill = canvas.itemcget("window", "fill")
    new_fill = 'lightgray' if current_fill == 'gray' else 'gray'
    canvas.itemconfig("window", fill=new_fill)
    output_label.config(text="Toggled window.")

def toggle_fan():
    current_fill = canvas.itemcget("fan", "fill")
    new_fill = 'lightgray' if current_fill == 'gray' else 'gray'
    canvas.itemconfig("fan", fill=new_fill)
    output_label.config(text="Toggled fan.")

# Create buttons
monitor_button = tk.Button(root, text="Monitor Conditions", command=monitor_conditions)
monitor_button.pack(pady=10)

add_light_button = tk.Button(root, text="Increase Lighting", command=add_light)
add_light_button.pack(pady=10)

add_water_button = tk.Button(root, text="Increase Watering", command=add_water)
add_water_button.pack(pady=10)

toggle_sprinklers_button = tk.Button(root, text="Toggle Sprinklers", command=toggle_sprinklers)
toggle_sprinklers_button.pack(pady=10)

toggle_window_button = tk.Button(root, text="Toggle Window", command=toggle_window)
toggle_window_button.pack(pady=10)

toggle_fan_button = tk.Button(root, text="Toggle Fan", command=toggle_fan)
toggle_fan_button.pack(pady=10)

# Output label to display results
output_label = tk.Label(root, text="", bg="white", font=("Helvetica", 12))
output_label.pack(pady=10, fill=tk.X)

# Start the Tkinter event loop
root.mainloop()


