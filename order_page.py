from tkinter import *
import pickle
from tkinter import ttk
import server_payment_gateway
from datetime import datetime
from PIL import ImageTk, Image
from pygame import mixer
import dbm

class page2:                                                    # Class to create the second page
    def __init__(self):                                         # Constructor which creates a new window
        self.booked_lst = []                                    # List to store the items added
        self.root = Tk()                                        # Create a new window
        self.root.title("Categories Available")    
        self.root.state("zoomed")             
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.width = 1200
        self.height = 600
        self.root.geometry("%dx%d+%d+%d"%(self.width, self.height,(self.screen_width-self.width)/2, (self.screen_height-self.height)/2))
        self.root.iconbitmap("images/canteen1.ico")             # Configuring the window with icons and geometry

        mixer.init()
        mixer.music.load("audios/Your-valuable-order-.mp3")
        mixer.music.play()                                      # Playing the music for that window

        self.img = Image.open("images/bg.png")
        self.bg = ImageTk.PhotoImage(self.img)                  
        label = Label(self.root,image = self.bg)
        label.place(x = 0, y = 0)                               # Setting the background image

        self.noodles_fr = Frame(self.root)
        self.fried_rice = Frame(self.root)
        self.drinks_fr = Frame(self.root)
        self.extras_fr = Frame(self.root)
        self.book_fr = Frame(self.root)
        self.payment_fr = Frame(self.root)                      # Predefining all the frames required further
        
        # Creating all the buttons required and for categories creating with images
        photo1 = PhotoImage(file = "images/fried_rice.png")
        Button(self.root, text = "Fried Rice" ,image = photo1 , compound = TOP, height=110, width=110, command=self.friedrices).place(x = 0, y =0)
        photo2 = PhotoImage(file = "images/noodles.png")
        Button(self.root, text = "Noodles" ,image = photo2 , compound = TOP, height=110, width=110, command=self.noodles).place(x = 0, y = 121)
        photo3 = PhotoImage(file = "images/drinks.png")
        Button(self.root, text = "Drinks" ,image = photo3 , compound = TOP, height=110, width=110, command =self.drinks).place(x=121, y=0)
        photo4 = PhotoImage(file = "images/extras.png")
        Button(self.root, text = "Extras" ,image = photo4 , compound = TOP, height=110, width=110, command=self.extras).place(x= 121, y= 121)
        Button(self.root, text = "Click here to place order", command = self.book).place(x = 650, y = 10)
        self.order = Button(self.root, text = "Proceed to payment", command = self.payment).place(x = 670, y = 400)
        
        self.root.mainloop()
    
    # A special function which is used to destroy the frame along with it contents when new category is selected
    def destroy_frame(self):

        # winfo_children() retruns all the labels, buttons in that frame
        if self.fried_rice.winfo_exists():
            for i in self.fried_rice.winfo_children():          
                i.destroy()
            self.fried_rice.destroy()

        if self.noodles_fr.winfo_exists():
            for i in self.noodles_fr.winfo_children():
                i.destroy()
            self.noodles_fr.destroy()

        if self.drinks_fr.winfo_exists():
            for i in self.drinks_fr.winfo_children():
                i.destroy()
            self.drinks_fr.destroy()

        if self.extras_fr.winfo_exists():
            for i in self.extras_fr.winfo_children():
                i.destroy()
            self.extras_fr.destroy()
       
    # A function to create a frame having the data of all fried rices
    def friedrices(self):

        self.destroy_frame()                                            # Calling the destroy function to destroy all the previous frames
        self.fried_rice = Frame(self.root, background="#DAF5FF")        # Creating a new fried_rice frame
        
        # Adding labels to fried_rice frame
        f1 = Label(self.fried_rice, text = "Code", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        f2 = Label(self.fried_rice, text = "Name", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        f3 = Label(self.fried_rice, text = "Cost", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        
        # Organizing the above labels
        f1.grid(row =0, column = 0)
        f2.grid(row =0, column = 1)
        f3.grid(row =0, column = 2)
        
        # Creating a list to get the data of fried rices
        lst = []
        try:
            f = open("files/list.pickle", "rb")
            while True:
                k = pickle.load(f)                                  # Loading data from pickle file
                if k[0] == "Fried Rice":
                    lst = k
                    f.close()
                    break
        except:                                                     # If any exception raises then Data base Error is printed
            print("Data Base Error, Contact the Customer Care")
                                                
        r = 1
        for i in lst[1]:                                            # In each iteration an item is choosen from list
            # Labels are created to add in the frame
            c = 0
            c_temp = Label(self.fried_rice, text = i["Code"], bg = "#DAF5FF")
            l_temp = Label(self.fried_rice, text = i["Name"], bg = "#DAF5FF")
            p_temp = Label(self.fried_rice, text = i["Cost"], bg = "#DAF5FF")
            c_temp.grid(row = r, column = c)
            l_temp.grid(row = r, column = c+1)
            p_temp.grid(row = r, column = c+2)
            r = r + 1
        
        self.fried_rice.place(x = 50, y = 275)                      # The frame is placed in the main root window

    # A function to create a frame having the data of all noodles
    def noodles(self):

        self.destroy_frame()                                        # Calling the destroy function to destroy all the previous frames              
        self.noodles_fr = Frame(self.root, background="#DAF5FF")    # Creating a new noodles frame
        
        # Adding labels to noodles frame
        f1 = Label(self.noodles_fr, text = "Code", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        f2 = Label(self.noodles_fr, text = "Name", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        f3 = Label(self.noodles_fr, text = "Cost", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        
        # Organizing the above labels
        f1.grid(row =0, column = 0)
        f2.grid(row =0, column = 1)
        f3.grid(row =0, column = 2)
       
        # Creating a list to get the data of noodles
        lst = []
        try:
            f = open("files/list.pickle", "rb")
            while True:
                k = pickle.load(f)                                  # Loading data from pickle file
                if k[0] == "Noodles":
                    lst = k
                    f.close()
                    break   
        except:                                                     # If any exception raises then Data base Error is printed
            print("Data Base Error, Contact the Customer Care")

        r = 1
        for i in lst[1]:                                              # In each iteration an item is choosen from list
            # Labels are created to add in the frame
            c = 0
            c_temp = Label(self.noodles_fr, text = i["Code"], bg = "#DAF5FF")
            l_temp = Label(self.noodles_fr, text = i["Name"], bg = "#DAF5FF")
            p_temp = Label(self.noodles_fr, text = i["Cost"], bg = "#DAF5FF")
            c_temp.grid(row = r, column = c)
            l_temp.grid(row = r, column = c+1)
            p_temp.grid(row = r, column = c+2)
            r = r + 1

        self.noodles_fr.place(x = 50, y = 275)                       # The frame is placed in the main root window

    # A function to create a frame having the data of all drinks
    def drinks(self):

        self.destroy_frame()                                         # Calling the destroy function to destroy all the previous frames
        self.drinks_fr = Frame(self.root, background="#DAF5FF")      # Creating a new drinks frame
        
        # Adding labels to drinks frame
        f1 = Label(self.drinks_fr, text = "Code", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        f2 = Label(self.drinks_fr, text = "Name", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        f3 = Label(self.drinks_fr, text = "Cost", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        
        # Organizing the above labels
        f1.grid(row =0, column = 0)
        f2.grid(row =0, column = 1)
        f3.grid(row =0, column = 2)
        
        # Creating a list to get the data of drinks
        lst = []
        try:
            f = open("files/list.pickle", "rb")
            while True:
                k = pickle.load(f)                                  # Loading data from pickle file
                if k[0] == "Drinks":
                    lst = k
                    f.close()
                    break
        except:                                                     # If any exception raises then Data base Error is printed
            print("Data Base Error, Contact the Customer Care")

        r = 1
        for i in lst[1]:                                            # In each iteration an item is choosen from list
            # Labels are created to add in the frame
            c = 0
            c_temp = Label(self.drinks_fr, text = i["Code"], bg = "#DAF5FF")
            l_temp = Label(self.drinks_fr, text = i["Name"], bg = "#DAF5FF")
            p_temp = Label(self.drinks_fr, text = i["Cost"], bg = "#DAF5FF")
            c_temp.grid(row = r, column = c)
            l_temp.grid(row = r, column = c+1)
            p_temp.grid(row = r, column = c+2)
            r = r + 1

        self.drinks_fr.place(x = 50, y = 275)                       # The frame is placed in the main root window

    # A function to create a frame having the data of all extras
    def extras(self):

        self.destroy_frame()                                        # Calling the destroy function to destroy all the previous frames
        self.extras_fr = Frame(self.root, background="#DAF5FF")     # Creating a new extras frame
        
        # Adding labels to extras frame
        f1 = Label(self.extras_fr, text = "Code", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        f2 = Label(self.extras_fr, text = "Name", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        f3 = Label(self.extras_fr, text = "Cost", font = "TimesNewRoman 12 bold", bg = "#DAF5FF")
        
        # Organizing the above labels
        f1.grid(row =0, column = 0)
        f2.grid(row =0, column = 1)
        f3.grid(row =0, column = 2)
        
        lst = []
        try:
            f = open("files/list.pickle", "rb")
            while True:
                k = pickle.load(f)                                  # Loading data from pickle file
                if k[0] == "Extras":
                    lst = k
                    f.close()
                    break
        except:                                                     # If any exception raises then Data base Error is printed
            print("Data Base Error, Contact the Customer Care")

        r = 1
        for i in lst[1]:                                            # In each iteration an item is choosen from list
            # Labels are created to add in the frame
            c = 0
            c_temp = Label(self.extras_fr, text = i["Code"], bg = "#DAF5FF")
            l_temp = Label(self.extras_fr, text = i["Name"], bg = "#DAF5FF")
            p_temp = Label(self.extras_fr, text = i["Cost"], bg = "#DAF5FF")
            c_temp.grid(row = r, column = c)
            l_temp.grid(row = r, column = c+1)
            p_temp.grid(row = r, column = c+2)
            r = r + 1

        self.extras_fr.place(x = 50, y = 275)                       # The frame is placed in the main root window
    
    # This function is used to create a table which takes the inputs of items required
    def book (self):
        
        self.booked_lst = []                                        # The list is cleared if the button is pressed again
        self.book_fr = Frame(self.root)                             # Creating a frame to display table
        # Create Treeview widget for the table
        table = ttk.Treeview(self.book_fr, columns=("item", "count","price"))

        # Define the columns for the table
        table.heading("#0", text="Code")
        table.heading("#1", text="Item")
        table.heading("#2", text="Count")
        table.heading("#3", text="Price")

        # Packing table into window
        table.pack()

        # Function which adds a new item to the table
        def add_item():
            # Getting the values from the entry fields
            cost = 0
            food = None
            item = item_entry.get()                                 # Entry field 1 - Item
            count = price_entry.get()                               # Entry field 2 - Count
            
            try:
                f = open("files/list.pickle", "rb")                 # Opening the pickle file to check the name and cost of item selected
                while True:
                    k = pickle.load(f)
                    lst = k[1]
                    for i in lst:
                        if i["Code"] == int(item):
                            cost = i["Cost"]
                            food = i["Name"]
                            temp_dic = {}
                            temp_dic["Code"] = item
                            temp_dic["Item"] = food
                            temp_dic["Count"] = count
                            temp_dic["Price"] = cost*int(count)
                            self.booked_lst.append(temp_dic)        # Appending the data to the list
                            break
            except:
                f.close()

            # Add the new item to the table
            table.insert("", "end", text=item, values=(food,count,cost*int(count)))

            # Clear the entry fields
            item_entry.delete(0, END)
            price_entry.delete(0, END)

        # Add an entry field for the code
        item_label = Label(self.book_fr, text="Code:")
        item_label.pack()
        item_entry = Entry(self.book_fr)
        item_entry.pack()

        # Add an entry field for the count
        price_label = Label(self.book_fr, text="Count:")
        price_label.pack()
        price_entry = Entry(self.book_fr)
        price_entry.pack()

        # A button to add a new item to the table
        add_button = Button(self.book_fr, text="Add Item", command=add_item)
        add_button.pack()

        self.book_fr.place(x = 325, y = 50)                         # The frame is placed in the main root window
    
    # Function which displays the amount to be paid after calculating the tax
    def payment(self):

        self.payment_fr = Frame(self.root)                          # Creating a new frame to show the bill amount
        
        # Calculating the respective Bill amount to be paid
        bill = 0
        for i in self.booked_lst:
            bill = i["Price"] + bill
        
        # GST calculation based on constraints
        if bill < 500:
            bill = bill + bill*0.005
        elif 500 <= bill < 1000:
            bill = bill + bill*0.1
        elif bill >= 1000:
            bill = bill + bill*0.2

        # Label to show th amount to be paid
        bill_label = Label(self.payment_fr, text = f"Total amount to be paid (Inc. GST) is {bill}")
        bill_label.pack()

        # Button to redirect to payment page
        redirect = Button(self.payment_fr, text = "Click here to redirect page for payment", command = self.payment_page)
        redirect.pack() 

        self.payment_fr.place(x =625, y = 500)                       # The frame is placed in the main root window

    # Function which redirects and displays the payment page
    def payment_page(self):

        self.root.destroy()                                         # Destroys the previous window
        win = Tk()                                                  # Creates new window
        win.title("Payment Page")                                   # Setting title to the window
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        width = 400
        height = 200
        win.configure(bg = "#C7E9B0")
        win.geometry("%dx%d+%d+%d"%(width, height,(screen_width-width)/2, (screen_height-height)/2))
        win.resizable(width = False, height = False)                # Configuring the window
        win.iconbitmap("images/rupee.ico")
        mixer.init()
        mixer.music.load("audios/Please-open-your-UPI_1.mp3")
        mixer.music.play()                                          # Playing the corresponding music

        l1 = Label(win, text = "Open your payment app and pay the Amount.", bg = "#C7E9B0", fg = "black", font = "CourierNew 10 bold")
        
        # Calculating the respective Bill amount to be paid
        bill = 0
        for i in self.booked_lst:
            bill = i["Price"] + bill

        # GST calculation based on constraints
        if bill < 500:
            bill = bill + bill*0.005
        elif 500 <= bill < 1000:
            bill = bill + bill*0.1
        elif bill >= 1000:
            bill = bill + bill*0.2
        
        l2 = Label(win, text = f"Amount to be paid is Rs.{bill}", bg = "#C7E9B0", fg = "black", font = "CourierNew 10 bold")
        l1.place(x = 55, y = 50)
        l2.place(x = 100, y = 100)
        win.mainloop()

        # Calling server program to start and it waits for the payment
        p = server_payment_gateway.server(bill)

        if p == "Success":                                              # If the payment is success then the order is added to pickle files
            fin = open("files/order.pickle", "ab")                      # Appending the order to order.pickle - Current Order
            fin2 = open("files/Totalorders.pickle", "ab")               # Appending the order to Totalorders.pickle - Database
            fin3 = dbm.open("files/item_order", "c")                    # Incrementing count in dbm file
            k = datetime.now()                                          # Getting date and time of order
            s1 = k.strftime("%d-%m-%y")                                 # Formatting the date and time
            s2 = k.strftime("%H:%M:%S")
            lst = []
            lst.append(s1)
            lst.append(s2)
            lst.append(self.booked_lst)
            lst.append(bill)
            pickle.dump(lst, fin)                                       # Dumping the order
            pickle.dump(lst,fin2)

            for i in self.booked_lst:                                   # Incrementing the count of each item in the list.0
                m = fin3[i["Item"]]
                fin3[i["Item"]] = str(int(m.decode()) + int(i["Count"]))
            fin.close()
            fin2.close()
            fin3.close()                                                # Closing all the files opened