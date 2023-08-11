from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor

d_or_e = "Disable"
msgbx = 1

window = Tk()
window.title("Pick a color")
window.geometry("400x200")
window.configure(bg="#000000")

def dialog():
    rgb, hex = askcolor(title="Pick a color")
    if msgbx == 1:
        if rgb != None and hex != None:
            yn = messagebox.askyesno("Pick a color", f"You requested a color with hex {hex} and rgb {rgb}. Do you want to choose this color?")
            if yn == 1:
                window.configure(bg=hex)
        else:
            messagebox.showinfo("Pick a color", "You chose no color. Your current color hasn't been changed.")
    else:
        window.configure(bg=hex)

def msgbox():
    global d_or_e, msgbx
    if d_or_e == "Disable":
        d_or_e = "Enable"
        msgbx = 0
    else:
        d_or_e = "Disable"
        msgbx = 1
    btn_2_text.set(f"{d_or_e} messageboxes")

btn = Button(window, text="Pick a color", command=dialog)
btn.place(relx=0.5, rely=0.5, anchor="center")

btn_2_text = StringVar()
btn_2_text.set(f"{d_or_e} messageboxes")
btn_2 = Button(window, textvariable=btn_2_text, command=msgbox)
btn_2.pack(side=BOTTOM)

window.mainloop()