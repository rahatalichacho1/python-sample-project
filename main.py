import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as file:
        content = file.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def save_file(text_edit, window):
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    text_content = text_edit.get(1.0, tk.END)
    with open(filepath, "w") as file:
        file.write(text_content)
    window.title(f"My Text Editor - {filepath}")

def main():
    window = tk.Tk()
    window.title("My Text Editor")
    window.rowconfigure(0, minsize=500)
    window.columnconfigure(0, minsize=200)  # Adjust the column size for the frame
    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=0, sticky="nsew")  # Make the text widget expandable
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(text_edit, window))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")  # Align button to the left
    open_button.grid(row=1, column=0, padx=5, sticky="ew")  # Align button to the left
    frame.grid(row=0, column=1, sticky="ns")  # Place frame on the right side
    window.bind("<Control-s>", lambda x: save_file(text_edit, window))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.mainloop()

main()
