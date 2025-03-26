from tkinter import *
from tkinter import messagebox

window= Tk()
window.title("Don't click")
window.geometry('500x500')
window.config(bg='black')

try:
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, "dclick.png")
    if os.path.exists(icon_path):
        window.iconphoto(True, PhotoImage(file=icon_path))
    else:
        print("Icon file not found, using default icon")
except Exception as e:
    print(f"Could not load window icon: {e}")
    
    
def click():
    if messagebox.askyesno(title="DON'T", message='Are You sure??', icon='error'):
        while True:
            messagebox.showwarning(title='sorry', message='i warned you man')
    else:
        messagebox.showinfo(title=':)', message='You chose the write choice congrats')


button = Button(window, command=click, text="don't click me", font=('Arial', 20),bg='red',activebackground='red')
button.place(x = 170,y = 200)

window.mainloop()
