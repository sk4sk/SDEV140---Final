from tkinter import *

#Button Functions
def orderNow():
    orderWindow = Toplevel(root)
    orderWindow.title("Peter's Pizza Palace Ordering Page")
    orderWindow.geometry("475x900")
    orderWindow.configure(bg="lime")
    banner = PhotoImage(file="banner.gif")
    orderBanner = Label(orderWindow, image=banner, bg="lime")
    orderBanner.grid(row=0, column=0, sticky=W)
    orderWindow.mainloop()
    
def closeWindow():
    root.destroy()
    exit()
def openMenu():
    menuWindow = Toplevel(root)
    menuWindow.title("Peter's Pizza Palace Menu")
    menu = PhotoImage(file="menu.gif")
    menuLabel = Label(menuWindow, image=menu, bg="lime")
    menuLabel.grid(row=0, column=0, sticky=W)
    menuWindow.mainloop()

#Main
root = Tk()
root.title("Peter's Pizza Palace Online App")
root.configure(background="lime")

menu = PhotoImage(file="menu.gif")
banner = PhotoImage(file="banner.gif")

#Splash Screen Image
splash = PhotoImage(file="splash.gif")
Label(root, image=splash, bg="lime") .grid(row=0, column=0, sticky=W)

#Buttons
Label(root, text="", bg="lime", fg="lime").grid(row=1, column=0, sticky=W)
Button(root, text="Order Now", width=11, command=orderNow) .grid(row=2, column=0, sticky=W)
menuButton = Button(root, text="View Menu", width=11, command=openMenu) 
menuButton.grid(row=2, column=0, sticky=N)
Button(root, text="Exit", width=11, command=closeWindow) .grid(row=2, column=0, sticky=E)
Label(root, text="", bg="lime", fg="lime").grid(row=3, column=0, sticky=W)


