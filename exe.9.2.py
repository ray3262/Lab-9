import tkinter as tk

def clear_messages():
    
    text_widget.delete(1.0, tk.END)


root = tk.Tk()
root.title("Chat")


text_widget = tk.Text(root, height=10, width=40)
text_widget.pack()


text_widget.insert(tk.END, "Message 1\n")
text_widget.insert(tk.END, "Message 2\n")
text_widget.insert(tk.END, "Message 3\n")


clear_button = tk.Button(root, text="Clear", command=clear_messages)
clear_button.pack()


root.mainloop()
