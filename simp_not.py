# def simple_notepad():
#     notepad = {}
#     while True:
#         title = input("\nВведіть заголовок: " )
#         text = input("\nВаш текст: ")
#         if title and text:
#             notepad[title] = text
#         for k, v  in notepad.items():
#             print(f"\nЗаголовок: {k}\nНотаток: {v}") 
# if __name__ == "__main__":        
#     simple_notepad()
import tkinter as tk
from tkinter import messagebox



def save_note():
    title = title_entry.get()
    text = text_entry.get("1.0",tk.END)
    
    if title and text.strip():
        notepad[title] = text.strip()
        
        notes_listbox.insert(tk.END, f"{title}: {text[:30]}")
        title_entry.delete(0, tk.END)
        text_entry.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Error, entry title and text")

def view_selected_note():
    try:
        selected_note_index = notes_listbox.curselection()[0]
        selected_title = notes_listbox.get(selected_note_index).split(":")[0]
        select_text = notepad[selected_title]
        messagebox.showinfo(selected_title, select_text)
    except:
         messagebox.showwarning("Error, entry title to watch")
        
        
def delete_note():
    selected_note_index = notes_listbox.curselection()[0]
    selected_title = notes_listbox.get(selected_note_index).split(":")[0]
    notepad.pop(selected_title)
    notes_listbox.delete(0, tk.END)
    
    for title, text in notepad.items():
        notes_listbox.insert(tk.END, f"{title}: {text}")
    
    
    
    
        
# create main window
root = tk.Tk()
root.title("Simple notepad")
# create vidget
title_lable = tk.Label(root, text="Title")
title_lable.pack()  #add title on a window

title_entry = tk.Entry(root, width=50) #create colum for enter text
title_entry.pack()

text_lable = tk.Label(root, text="Text place")
text_lable.pack()

text_entry = tk.Text(root, width = 50 , height = 10)
text_entry.pack()

save_button = tk.Button(root, text="Save Note", command = save_note)
save_button.pack()

notes_listbox = tk.Listbox(root, height=10, width=50)
notes_listbox.pack()

view_button = tk.Button(root, text = "Show Note", command=view_selected_note)
view_button.pack()

delete_button = tk.Button(root, text="Delete note", command=delete_note)
delete_button.pack()
notepad = {}    
root.mainloop()   
save_note()