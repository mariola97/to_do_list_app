import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import ttk

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
        zavrseni_zadatak = f"✓ {zadatak}"
        listbox.delete(index)
        listbox.insert(index, zavrseni_zadatak)
        listbox.itemconfig(index, fg="gray")
    except IndexError:
        pass

# Stvaranje glavnog prozora
root = tk.Tk()
root.title("To-Do Aplikacija")

# Primjena ttk teme na prozor
style = ttk.Style()
style.theme_use("clam")

# Stvaranje okvira za popis zadataka
frame = ttk.Frame(root)
frame.pack(pady=10)

# Stvaranje listboxa za prikaz zadataka
listbox = tk.Listbox(frame, width=50, height=10, bd=0, font="TkDefaultFont")
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Stvaranje klizača za listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Konfiguriranje listboxa i klizača
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Stvaranje okvira za unos i gumbe
entry_frame = ttk.Frame(root)
entry_frame.pack(pady=10)

# Stvaranje polja za unos novih zadataka
unos = ttk.Entry(entry_frame, font="TkDefaultFont")
unos.pack(side=tk.LEFT)

# Stvaranje gumba "Dodaj zadatak"
dodaj_gumb = ttk.Button(entry_frame, text="Dodaj zadatak", command=dodaj_zadatak)
dodaj_gumb.pack(side=tk.LEFT, padx=10)

# Stvaranje gumba "Ukloni zadatak"
ukloni_gumb = ttk.Button(root, text="Ukloni zadatak", command=ukloni_zadatak)
ukloni_gumb.pack(pady=5)

# Stvaranje gumba "Završi zadatak"
zavrsi_gumb = ttk.Button(root, text="Završi zadatak", command=zavrsi_zadatak)
zavrsi_gumb.pack(pady=5)

# Pokretanje petlje glavnog prozora
root.mainloop()
