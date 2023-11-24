import tkinter as tk
from tkinter import N,S,W,E
from RandomPasswordGenerator import *
from PIL import ImageTk,Image
import random


background = 'pink'
fontground = 'black'
font = 'Microsoft JhengHei'


window = tk.Tk()
window.geometry("500x460")
window.title('Random Password Generator')
window.configure(bg=background)
window.resizable(False,False)


lbl_random_password_generator = tk.Label(
    master=window,
    text="RANDOM PASSWORD GENERATOR",
    font=(font,20,'bold'),
    bg=background,
    fg=fontground,
)
lbl_random_password_generator.grid(padx=10,pady=10)


lbl_lenght = tk.Label(
    master=window,
    text='Enter lenght of the Password :',
    font=(font,14,'bold'),
    fg=fontground,
    bg=background,
)
lbl_lenght.grid(padx=10,pady=10,sticky=W)


ent_lenght = tk.Spinbox(
    master=window,
    font=(font,12,'bold'),
    justify='center',
    width=15,
    from_= 4,
    to_= 12,
    border=5,
)
ent_lenght.grid(padx=20,pady=10,row=1,sticky=E)


lbl_frame = tk.LabelFrame(
    master=window,
    text='Settings',
    font=(font,15,'bold'),
    bg=background,
    fg=fontground,
)
lbl_frame.grid(padx=20,pady=10,sticky=W)


lower_check_btn = tk.IntVar()
upper_check_btn = tk.IntVar()
symbol_check_btn = tk.IntVar()
number_check_btn = tk.IntVar()


lower_btn = tk.Checkbutton(
    master=lbl_frame,
    variable = lower_check_btn,
    text='Lowercase(a-z)',
    font=(font,13,'bold'),
    fg=fontground,
    bg=background,
    border=20,
    selectcolor='aquamarine',
    
)
lower_btn.grid(sticky=W,)


upper_btn = tk.Checkbutton(
    master=lbl_frame,
    variable = upper_check_btn,
    text='Uppercase(A-Z)',
    font=(font,13,'bold'),
    fg=fontground,
    bg=background,
    border=20,
    selectcolor='aquamarine',    
)
upper_btn.grid(sticky=W,)


symbol_btn = tk.Checkbutton(
    master=lbl_frame,
    variable = symbol_check_btn,
    text='Symbolcase(!@#$...)',
    font=(font,13,'bold'),
    fg=fontground,
    bg=background,
    border=20,
    selectcolor='aquamarine',    
)
symbol_btn.grid(sticky=W,)


number_btn = tk.Checkbutton(
    master=lbl_frame,
    variable = number_check_btn,
    text='Numbers(0123...)',
    font=(font,13,'bold'),
    fg=fontground,
    bg=background,
    border=20,
    selectcolor='aquamarine',    
)
number_btn.grid(sticky=W,)


def random_password_char():
    chioces = ''
    if lower_check_btn.get():
        chioces += lower_case_chars()
    if upper_check_btn.get():
        chioces += upper_case_chars()
    if symbol_check_btn.get():
        chioces += symbol_case_chars()
    if number_check_btn.get():
        chioces += number_for_password()

    return random.choice(chioces)


def password_generated(*args):
    ent_risult_password.delete(0 , tk.END)
    final_password = ''
    lenght = int(ent_lenght.get())
    for i in range(lenght):
        final_password += random_password_char()
    
    ent_risult_password.insert(0 , final_password)


def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(ent_risult_password.get())


btn_generate_password = tk.Button(
    master=window,
    text='GENERATE',
    width=12,
    bg='aquamarine',
    font=(font,14,'bold'),
    fg=fontground,
    command=password_generated,
)
btn_generate_password.grid(row=2,padx=(265,1),pady=(1,200))


ent_risult_password = tk.Entry(
    master=window,
    width=15,
    justify='center',
    bg=background,
    fg=fontground,
    font=(font,15,'bold'),
    border=1
)
ent_risult_password.grid(row=2,padx=(265,1),pady=5)


btn_copy = tk.Button(
    master=window,
    text='Copy',
    width=12,
    font=(font,14,'bold'),
    bg='limegreen',
    fg=fontground,
    command=copy_to_clipboard,
)
btn_copy.grid(row=2,padx=(265,1),pady=(200,1))


photo = ImageTk.PhotoImage(Image.open(r"C:/Users/STAR/OneDrive/Desktop/Python/Lock.png"))
window.iconphoto(False,photo)
window.bind('<Return>',password_generated)
window.mainloop()