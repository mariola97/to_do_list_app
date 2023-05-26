import tkinter as tk
from tkinter import messagebox
from tkinter import font

zadaci = []

def dodaj_zadatak():
    zadatak = unos.get()
    if zadatak:
        zadaci.append(zadatak)
        listbox.insert(tk.END, zadatak)
        unos.delete(0, tk.END)
    else:
        messagebox.showwarning("Upozorenje", "Unesite zadatak.")

def ukloni_zadatak():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        zadaci.pop(index)
    except IndexError:
        pass

def zavrsi_zadatak():
    try:
        index = listbox.curselection()[0]
        zadatak = listbox.get(index)
        listbox.itemconfig(index, fg="gray")
        listbox.itemconfig(index, font=font.Font(listbox, listbox.cget("font"), #ne_radi ))
        zadaci[index] = f"- {zadatak}"
    except IndexError:
        pass

# Stvaranje glavnog prozora
root = tk.Tk()
root.title("To-Do Aplikacija")

# Stvaranje popisa zadataka
frame = tk.Frame(root)
frame.pack(pady=10)

# Stvaranje liste za prikaz zadataka
listbox = tk.Listbox(frame, width=50, height=10, bd=0, font="TkDefaultFont")
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Stvaranje liste i srolla
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Konfig liste i srolla
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Unos i gumb
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

# Novi zadatak
unos = tk.Entry(entry_frame, font="TkDefaultFont")
unos.pack(side=tk.LEFT)

# Gumb "Dodaj zadatak"
dodaj_gumb = tk.Button(entry_frame, text="Dodaj zadatak", command=dodaj_zadatak)
dodaj_gumb.pack(side=tk.LEFT, padx=10)

# Gumb "Ukloni zadatak"
ukloni_gumb = tk.Button(root, text="Ukloni zadatak", command=ukloni_zadatak)
ukloni_gumb.pack(pady=5)

# Gumb "Završi zadatak"
zavrsi_gumb = tk.Button(root, text="Završi zadatak", command=zavrsi_zadatak)
zavrsi_gumb.pack(pady=5)

# Pokretanje petlje glavnog prozora
root.mainloop()
