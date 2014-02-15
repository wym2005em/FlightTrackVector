from Tkinter import *
root = Tk()

root.geometry('150x150+0+0')
print root.pack_slaves()

Label(root,text = 'pack1',bg = 'red').pack(fill = 'y',expand=1,side="left",ipadx = 20)
Label(root,text = 'pack2',bg = 'blue').pack(fill = 'both',expand=0,side="right",ipadx = 20)
Label(root,text = 'pack3',bg = 'green').grid(row=6,column=1)
print root.pack_slaves()
root.mainloop()

