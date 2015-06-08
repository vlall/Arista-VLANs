from Tkinter import *
root = Tk()

root.title("VLAN creation GUI")
root.geometry("200x100")

app = Frame(root)
app.grid()

#Variables
status = 0
vlanswitch = vlan()

on = Radiobutton(app, text='On', variable=status, value=1)
on.grid()
off = Radiobutton(app, text='Off', variable=status, value=0)
off.grid()
root.mainloop()
