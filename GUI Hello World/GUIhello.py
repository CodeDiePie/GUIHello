# import resources
import tkinter as tk


root = tk.Tk()
root.title("GUI Hello World")


def printtxt():
    helloworld.config(text="Hello World!")

def clear():
    helloworld.config(text="Do it Again...")

# GUI formatting

canvas = tk.Canvas(root, height=200, width=500, background="black")
canvas.pack()

frame = tk.Frame(root, bg="dark orange")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

helloworld = tk.Label(frame, text="Click The Button to Run The Code")
helloworld.pack()

bio = tk.Label(root, text="GUIHello by Joshua Bishop, 12.22.2020", bg="black", fg="white")
bio.place(relx=0.3, rely=0.85)

runprog = tk.Button(frame, text="Run Code", padx=10, pady=6, fg="white", bg="black", command=printtxt)
runprog.place(relx=0.425, rely=0.3)

cleartxt = tk.Button(frame, text="Clear", padx=10, pady=6, fg="white", bg="black", command=clear)
cleartxt.place(relx=0.45, rely=0.6)


root.mainloop()
