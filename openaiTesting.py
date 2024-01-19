import tkinter as tk

def on_button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the center coordinates
center_x = screen_width // 2
center_y = screen_height // 2

# Create a button and place it in the center
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Set the window size and position it in the center
window_width = 300
window_height = 200
x_position = center_x - window_width // 2
y_position = center_y - window_height // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.title("Centered Button")

# Start the Tkinter event loop
root.mainloop()
