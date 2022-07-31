'''Peter's Pizza Palace Ordering Application

This program is used to place orders for the fictional pizza restaurant Peter's Pizza Palace. It Includes a home
screen with access to the menu and the ordering page. The ordering page is capable of adding different menu items
to the customer's order and adding the items' cost together to reach a subtotal which is then adjustted for a 7%
sales tax and then displayed to the customer. The customer is also able to see their order as it is being placed
and they can clear the order and start again if they make a mistake.

'''


from tkinter import *


##Global Variables
pizzaTotal = 0 #The price total for the current pizza#
sidesTotal = 0 #The price total for the non pizza items#
addedPizza = "" #The contents of the current pizza#
selectedSize = "" #The selected size of the pizza#

##Button Functions
def orderNow():
    orderWindow = Toplevel(root) #Ordering Window Pop Up
    orderWindow.title("Peter's Pizza Palace Ordering Page")
    orderWindow.geometry("480x975")
    orderWindow.configure(bg="lime")
    orderWindow.iconbitmap("lilpizza.ico")

    banner = PhotoImage(file="banner.gif") #Order Now Banner
    orderBanner = Label(orderWindow, image=banner, bg="lime")
    orderBanner.grid(row=0, column=0, columnspan = 3, sticky=W)
    Label(orderWindow, text="Select Size: (Choose one)", bg = "lime", font=("Bauhaus 93", 16)).grid(row=1, column=1)


    ##Size Radios
    smallvar = StringVar() #Contents of small checkbox
    mediumvar = StringVar() #Contents of medium checkbox
    largevar = StringVar() #Contents of large checkbox

    small = Checkbutton(orderWindow, text="Small $10", bg="lime", anchor=W, variable=smallvar, onvalue="Small", offvalue="")
    small.deselect()
    small.grid(row=2, column=0)

    medium = Checkbutton(orderWindow, text="Medium $15", bg="lime", anchor=W, variable=mediumvar, onvalue="Medium", offvalue="")
    medium.deselect()
    medium.grid(row=2, column=1)

    large = Checkbutton(orderWindow, text="Large $20", bg="lime", anchor=W, variable=largevar, onvalue="Large", offvalue="")
    large.deselect()
    large.grid(row=2, column=2)
    
    ##Ingredient Checkboxes
    Label(orderWindow, text="Select Toppings: ($2 Each)", bg = "lime", font=("Bauhaus 93", 16)).grid(row=4, column=1)
    
    cheesevar = StringVar() #Value of cheese box
    sausagevar = StringVar() #Value of sausage box
    mushroomvar = StringVar() #Value of mushroom box
    greenpepvar = StringVar() ##Value of grn pep box
    hamvar = StringVar() #Value of ham box
    pepperonivar = StringVar() #Value of pepperoni box
    onionvar = StringVar() #Value of onion box
    olivevar = StringVar() #Value of olive box
    anchovyvar = StringVar() #Value of anchovy box

    cheese = Checkbutton(orderWindow, text="Cheese", bg="lime", anchor=W, variable=cheesevar, onvalue="Cheese", offvalue="")
    cheese.deselect()
    cheese.grid(row=5, column=0)
    sausage = Checkbutton(orderWindow, text="Sausage", bg="lime", anchor=W, variable=sausagevar, onvalue="Sausage", offvalue="")
    sausage.deselect()
    sausage.grid(row=5, column=1)
    mushroom = Checkbutton(orderWindow, text="Mushroom", bg="lime", anchor=W, variable=mushroomvar, onvalue="Mushroom", offvalue="")
    mushroom.deselect()
    mushroom.grid(row=5, column=2)

    Label(orderWindow, text="", bg="lime").grid(row=6)

    greenpep = Checkbutton(orderWindow, text="Grn Pepper", bg="lime", anchor=W, variable=greenpepvar, onvalue="Grn Pepper", offvalue="")
    greenpep.deselect()
    greenpep.grid(row=7, column=0)
    ham = Checkbutton(orderWindow, text="Ham", bg="lime", anchor=W, variable=hamvar, onvalue="Ham", offvalue="")
    ham.deselect()
    ham.grid(row=7, column=1)
    pepperoni = Checkbutton(orderWindow, text="Pepperoni", bg="lime", anchor=W, variable=pepperonivar, onvalue="Pepperoni", offvalue="")
    pepperoni.deselect()
    pepperoni.grid(row=7, column=2)

    Label(orderWindow, text="", bg="lime").grid(row=8)

    onion = Checkbutton(orderWindow, text="Onion", bg="lime", anchor=W, variable=onionvar, onvalue="Onion", offvalue="")
    onion.deselect()
    onion.grid(row=9, column=0)
    olive = Checkbutton(orderWindow, text="B. Olive", bg="lime", anchor=W, variable=olivevar, onvalue="Olive", offvalue="")
    olive.deselect()
    olive.grid(row=9, column=1)
    anchovy = Checkbutton(orderWindow, text="Anchovy", bg="lime", anchor=W, variable=anchovyvar, onvalue="Anchovy", offvalue="")
    anchovy.deselect()
    anchovy.grid(row=9, column=2)

    ##Add to Order Button
    def addPizza():
        global sidesTotal
        global pizzaTotal

        #Calculate price
        if smallvar.get() == "Small":
            sidesTotal += 10
            pizzaTotal += 10
        if mediumvar.get() == "Medium":
            sidesTotal += 15
            pizzaTotal += 15
        if largevar.get() == "Large":
            sidesTotal += 20
            pizzaTotal += 20
        if cheesevar.get() == "Cheese":
            sidesTotal += 2
            pizzaTotal += 2
        if sausagevar.get() == "Sausage":
            sidesTotal += 2
            pizzaTotal += 2
        if mushroomvar.get() == "Mushroom":
            sidesTotal += 2
            pizzaTotal += 2
        if greenpepvar.get() == "Grn Pepper":
            sidesTotal += 2
            pizzaTotal += 2
        if hamvar.get() == "Ham":
            sidesTotal += 2
            pizzaTotal += 2
        if pepperonivar.get() == "Pepperoni":
            sidesTotal += 2
            pizzaTotal += 2
        if onionvar.get() == "Onion":
            sidesTotal += 2
            pizzaTotal += 2
        if olivevar.get() == "Olive":
            sidesTotal += 2
            pizzaTotal += 2
        if anchovyvar.get() == "Anchovy":
            sidesTotal += 2        
            pizzaTotal += 2
        bigTotal = (sidesTotal * .07) + sidesTotal
        
        #Display pizza
        addedPizza = smallvar.get() + mediumvar.get() + largevar.get() + "-" + cheesevar.get() + " " + sausagevar.get() + " " + mushroomvar.get() + " " + greenpepvar.get() + " " + hamvar.get() + " " + pepperonivar.get() + " " + onionvar.get() + " " + olivevar.get() + " " + anchovyvar.get() + "-" + "$" + str(pizzaTotal)
            
            
        checkText.configure(state='normal')
        checkText.insert(1.0, addedPizza + '\n' + '\n')
        checkText.configure(state='disabled')

        priceText.configure(state='normal')
        priceText.delete(1.0, "end")
        priceText.insert(1.0, sidesTotal)
        priceText.configure(state='disabled')

        totalText.configure(state='normal')
        totalText.delete(1.0, "end")
        totalText.insert(1.0, bigTotal)
        totalText.configure(state='disabled')

        
        #Deselect boxes
        cheese.deselect()
        sausage.deselect()
        mushroom.deselect()
        greenpep.deselect()
        ham.deselect()
        pepperoni.deselect()
        onion.deselect()
        olive.deselect()
        anchovy.deselect()
        small.deselect()
        medium.deselect()
        large.deselect()

        pizzaTotal = 0
        
    Button(orderWindow, text="Add Pizza to Order!", bg="orange", command=addPizza, font=("Bauhaus 93", 12)).grid(row=10, column=1, padx=50)


    ##Extra Sides Functions

    def addBread():
        global sidesTotal
        sidesTotal += 4
        bigTotal = (sidesTotal * .07) + sidesTotal
        checkText.configure(state='normal')
        checkText.insert(1.0, "Breadsticks - $4" + '\n' + '\n')
        checkText.configure(state='disabled')

        priceText.configure(state='normal')
        priceText.delete(1.0, "end")
        priceText.insert(1.0, sidesTotal)
        priceText.configure(state='disabled')

        totalText.configure(state='normal')
        totalText.delete(1.0, "end")
        totalText.insert(1.0, bigTotal)
        totalText.configure(state='disabled')
        
    def addPop():
        global sidesTotal
        sidesTotal += 3
        bigTotal = (sidesTotal * .07) + sidesTotal
        checkText.configure(state='normal')
        checkText.insert(1.0, "2 Liter of pop - $3" + '\n' + '\n')
        checkText.configure(state='disabled')

        priceText.configure(state='normal')
        priceText.delete(1.0, "end")
        priceText.insert(1.0, sidesTotal)
        priceText.configure(state='disabled')

        totalText.configure(state='normal')
        totalText.delete(1.0, "end")
        totalText.insert(1.0, bigTotal)
        totalText.configure(state='disabled')

    def addSauce():
        global sidesTotal
        sidesTotal += 1
        bigTotal = (sidesTotal * .07) + sidesTotal
        checkText.configure(state='normal')
        checkText.insert(1.0, "Extra side sauce - $1" + '\n' + '\n')
        checkText.configure(state='disabled')

        priceText.configure(state='normal')
        priceText.delete(1.0, "end")
        priceText.insert(1.0, sidesTotal)
        priceText.configure(state='disabled')

        totalText.configure(state='normal')
        totalText.delete(1.0, "end")
        totalText.insert(1.0, bigTotal)
        totalText.configure(state='disabled')

    def clearOrder():
        global sidesTotal
        global totalTotal
        sidesTotal = 0
        priceText.configure(state='normal')
        checkText.configure(state='normal')
        totalText.configure(state='normal')
        priceText.delete(1.0, "end")
        checkText.delete(1.0, "end")
        totalText.delete(1.0, "end")
        priceText.configure(state='disabled')
        checkText.configure(state='disabled')
        totalText.configure(state='disabled')
        

    Label(orderWindow, text="Select Extra Sides:", bg = "lime", font=("Bauhaus 93", 16)).grid(row=11, column=1)
    banner2 = PhotoImage(file="sideitems.gif")
    sidesbanner = Label(orderWindow, image=banner2, bg="lime")
    sidesbanner.grid(row=12, column=0, columnspan=3, sticky=W)

    ##Items
    Label(orderWindow, text="Breadsticks - $4", bg = "lime", font=("Bauhaus 93", 12)).grid(row=13, column=0)
    Label(orderWindow, text="2 Liter of Pop - $3", bg = "lime", font=("Bauhaus 93", 12)).grid(row=13, column=1)
    Label(orderWindow, text="Side Sauce - $1", bg = "lime", font=("Bauhaus 93", 12)).grid(row=13, column=2)

    #Sides Buttons
    Button(orderWindow, text="Add One", bg="orange", font=("Bauhaus 93", 12), command=addBread).grid(row=14, column=0)
    Button(orderWindow, text="Add One", bg="orange", font=("Bauhaus 93", 12), command=addPop).grid(row=14, column=1)
    Button(orderWindow, text="Add One", bg="orange", font=("Bauhaus 93", 12), command=addSauce).grid(row=14, column=2)


    ##Review Order
    Label(orderWindow, text="Review Order: (Scroll Down)", bg = "lime", font=("Bauhaus 93", 14)).grid(row=15, column=0, columnspan = 3)
    checkText = Text(orderWindow, width=50, height=20, bg="orange")
    checkText.grid(row=16, column=0, columnspan=3)
    checkText.configure(state='disabled')

    ##Display Price
    Label(orderWindow, text="Subtotal:", bg = "lime", font=("Bauhaus 93", 14)).grid(row=17, column=0, columnspan = 3)
    priceText = Text(orderWindow, width=25, height=1, bg="orange")
    priceText.grid(row=18, column=1)
    priceText.configure(state='disabled')
    Label(orderWindow, text="Total w/ Tax:", bg = "lime", font=("Bauhaus 93", 14)).grid(row=19, column=0, columnspan = 3)
    totalText = Text(orderWindow, width=25, height=1, bg="orange")
    totalText.grid(row=20, column=1)
    totalText.configure(state='disabled')

    ##Go Back
    orderWindow.grid_rowconfigure(20, weight=1)
    orderWindow.grid_columnconfigure(20, weight=1)
    Button(orderWindow, text="Go Back", width=9, command=orderWindow.destroy) .grid(row=50, column=0, sticky=E)
    

    ##Clear Order
    orderWindow.grid_rowconfigure(20, weight=1)
    orderWindow.grid_columnconfigure(20, weight=1)
    Button(orderWindow, text="Clear Order", width=12, command=clearOrder) .grid(row=50, column=1)

    ##Place Order
    orderWindow.grid_rowconfigure(20, weight=1)
    orderWindow.grid_columnconfigure(20, weight=1)
    Button(orderWindow, text="Place Order!", width=9, command=orderWindow.destroy) .grid(row=50, column=2, sticky=W)


    orderWindow.mainloop()
    
##Exit
def closeWindow():
    root.destroy()
    exit()


##View Menu
def openMenu():
    menuWindow = Toplevel(root)
    menuWindow.title("Peter's Pizza Palace Menu")
    menuWindow.iconbitmap("lilpizza.ico")
    menu = PhotoImage(file="menu.gif")
    menuLabel = Label(menuWindow, image=menu, bg="lime")
    menuLabel.grid(row=0, column=0, sticky=W)
    menuWindow.mainloop()

##Main
root = Tk()
root.title("Peter's Pizza Palace Online App")
root.iconbitmap("lilpizza.ico")
root.configure(background="lime")

menu = PhotoImage(file="menu.gif")
banner = PhotoImage(file="banner.gif")

##Splash Screen Image
splash = PhotoImage(file="splash.gif")
Label(root, image=splash, bg="lime") .grid(row=0, column=0, sticky=W)

##Order Now and Exit
Label(root, text="", bg="lime", fg="lime").grid(row=1, column=0, sticky=W)
Button(root, text="Order Now", width=11, command=orderNow) .grid(row=2, column=0, sticky=W)
menuButton = Button(root, text="View Menu", width=11, command=openMenu) 
menuButton.grid(row=2, column=0, sticky=N)
Button(root, text="Exit", width=11, command=closeWindow) .grid(row=2, column=0, sticky=E)
Label(root, text="", bg="lime", fg="lime").grid(row=3, column=0, sticky=W)


root.mainloop()

