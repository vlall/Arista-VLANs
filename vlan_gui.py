#!/usr/bin/python

from Tkinter import *

class AristaTool(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
        self.parent.title("Arista Tool")
        self.pack(fill=BOTH, expand=1)
        self.var = IntVar()
        status = 0

#Show Vlans
#Scroll through Vlans
#Modify Vlans

        labelButton1 = Label(self, text='Current VLANs')
        listBox = Listbox(self)
        vlanList= ['VLAN001', 'VLAN002', 'VLAN003', 'VLAN004']
        for i in range(len(vlanList)):
            listBox.insert(i, vlanList[i])

        listBoxBtn = LabelFrame(self, text="Edit" )
        listBoxBtn.pack(padx=10, pady=10)
        w = Button(listBoxBtn, text='Check Status')
        w.pack()
        add = Button(listBoxBtn, text='Add')
        add.pack()
        remove = Button(listBoxBtn, text='Remove')
        remove.pack()

       # listBoxBtn = Button(self, text='Check Status')
        createButton = Button(self, text="Confirm")

#Create Vlans
        #onButton.place(x=50, y=20)
        #offButton.place(x=50, y=50)

        labelButton1.grid(row=1, column=2)
        listBox.grid(row=2, column=2)
        listBoxBtn.grid(row=2, column=3)

    def onClick(self):
        if self.var.get() == 1:
            self.master.title("VLAN Too ")
        else:
            self.master.title("")

def main():
    root = Tk()
    root.geometry("550x350+300+300")
    app = AristaTool(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  
