"""
Purpose: This program is created to see the current orders as well as analyze the income 
         gained by the canteen owner so that he can upgrade his business.
"""

import matplotlib.pyplot as plt
import pandas as pd
import pickle
import csv
import dbm
from tkinter import *

class data_management:
    def __init__(self):
        self.root = Tk()                                                     # Creating the user interface from canteen side
        self.root.title("Data Analysis")                                     # Setting the title
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 300
        height = 300
        self.root.geometry("%dx%d+%d+%d"%(width,height,(screen_width - width)/2, (screen_height-height)/2))
        self.root.configure(bg = "#FCEDDA")                                  # Configuring the window as per requirement
        self.root.iconbitmap("images\canteen1.ico")                          # Setting the icon for the window

        # Buttons which are used to redirect for further pages
        b1 = Button(self.root, text = "Visualize the Income", command = self.analyse, bg = "#EE4E34", font = "TimesNewRoman 10 bold")
        b2 = Button(self.root, text = "View the database", command = self.get_total_order, bg = "#EE4E34", font = "TimesNewRoman 10 bold")
        b3 = Button(self.root, text = "Current Orders", command = self.current_order, bg = "#EE4E34", font = "TimesNewRoman 10 bold")
        b4 = Button(self.root, text = "View Each Item Count", command = self.each_item_count, bg = "#EE4E34", font = "TimesNewRoman 10 bold")

        b1.place(x = 75, y = 100)
        b2.place(x = 80, y = 150)
        b3.place(x = 95, y = 50)
        b4.place(x = 75, y = 200)

        self.root.mainloop()

    def get_total_order(self):                                      # Function to view the total orders from the start of establishment of software
        fin = open("files/Totalorders.pickle", "rb")                # Opening the file where the whole database is stored
        root = Tk()                                                 # Creating a new window
        root.iconbitmap("images/canteen1.ico")                      # Fixing an icon to the window        
        root.title("Order List")                                    # Setting title to the window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        width = 600
        height = 400                                                # Setting the geometry to the window
        root.geometry("%dx%d+%d+%d"%(width, height,(screen_width-width)/2,(screen_height-height)/2))
        # We use scroll bar to scroll up and down as well as left and right as database will be more
        s_bar = Scrollbar(root, orient = "vertical")                # Vertical orientation of scroll bar             
        p_bar = Scrollbar(root, orient = "horizontal")              # Horizontal orientation of scroll bar
        s_bar.pack(side = RIGHT, fill  = Y)                         # Sets the scroll-bar of vertical direction at right most
        p_bar.pack(side = BOTTOM, fill = X)                         # Sets the scroll-bar 
        t = Text(root, wrap = NONE, yscrollcommand = s_bar.set)     
        
        try:
            while True:
                k = pickle.load(fin)                                # Loading the data from the pickle file
                l = [k[0], k[1], k[3]]                              # Making the Date, Time and Amount into a single list
                t.insert(END, "\n")                                 
                t.insert(END, l)                                    # Adding the list in the form of text to the window
                for i in k[2]:
                    t.insert(END, i)                                # Adding the items ordered in the the form of text
        # When the whole file is read then exception raises and the file gets closed
        except:
            fin.close()                                             

        t.pack(side = TOP, fill = X)                                # Adding the text to the window
        s_bar.config(command = t.yview)                             # Configuring the Scroll bars
        p_bar.config(command = t.xview)
        root.mainloop()
        
                
    # Function to analyze the income gained date wise. To make it we get the data from .csv file 
    def analyse(self):                                                  
        
        self.root.destroy()                                         # Destroying the root window
        k = pd.read_csv("files/payment.csv")                        # Reading the .csv file
        df = pd.DataFrame(k, columns = ['date', 'amount'])          # Creating a dataframe from the data obtained from csv file
        dic = {}
        data_1 = df["date"]
        data_2 = df["amount"]
        final = len(df)
        for i in range(final):                                      # Looping through the whole data obtained to calculate the income obtained date wise
            if data_1[i] in dic:
                dic[data_1[i]] = dic[data_1[i]] + data_2[i]
            else:
                dic[data_1[i]] = data_2[i]
        print("Sales Date-wise (in Rupees)")
        print(dic)                                                  # Printing the income obtained date wise

        x_axis = []                                                 # Creating a list for plotting the graph for X-axis
        y_axis = []                                                 # Creating a list for plotting the graph for Y-axis
        for i in dic:
            x_axis.append(i)
            y_axis.append(dic[i])

    
        plt.title("Sales Analysis")                                 # Setting the title for the plot
        plt.plot(x_axis, y_axis)                                    # Using line plot
        plt.xlabel("Dates")                                         # Mentioning X - axis
        plt.ylabel("Amount in Rupees")                              # Mentioning Y - axis
        plt.grid()                                                  # Using Grid to visualize perfectly
        plt.xticks(x_axis, rotation= "vertical")                    # As data gets longer we use this to orient in vertical direction
        plt.show()                                                  # Plotting the graph

    # Function that produces the current orders that have to served
    def current_order(self):                                    
        root = Tk()                                                 # Creating a window
        root.title("Order List")                                    # Setting a title 
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        width = 600
        height = 400                                                # Setting the geometry to the window
        root.geometry("%dx%d+%d+%d"%(width, height,(screen_width-width)/2,(screen_height-height)/2)) 
        s_bar = Scrollbar(root, orient = "vertical")                # As data may exceed we use the scroll-bar
        p_bar = Scrollbar(root, orient = "horizontal")
        s_bar.pack(side = RIGHT, fill  = Y)
        p_bar.pack(side = BOTTOM, fill = X)
        t = Text(root, wrap = NONE, yscrollcommand = s_bar.set)
        
        fin = open("files/order.pickle", "rb+")                     # The pickle file is opened to read the data 
        fout = open("files/payment.csv", "a")                       # The csv file is opened to add the contents

        try:
            while True:
                k = pickle.load(fin)                                # Loading the current orders 
                l = [k[0], k[1], k[3]]                              
                t.insert(END, "\n")
                t.insert(END, l)
                for i in k[2]:
                    t.insert(END, "\n")
                    t.insert(END, i["Item"] + " - " + i["Count"])   # Inserting the current orders
                templst = [k[0], k[1], k[3]]
                csv.writer(fout).writerow(templst)                  # Adding data to csv file
            
        # As the whole orders are read then an exception rises then we empty the file as we read the orders and close all the files
        except:
            fin.truncate(0)
            fin.close()
            fout.close()

        t.pack(side = TOP, fill = X)                                # Placing text in the window
        s_bar.config(command = t.yview)
        p_bar.config(command = t.xview)
        root.mainloop()

    def each_item_count(self):                                      # Function which calls the constructor of "each_item" class
        self.root.destroy()                                         # Destroying the root window
        e = each_item()


class each_item:
    def __init__(self):
        # Window creation to analyse each item separately
        self.root = Tk()
        self.root.iconbitmap("images/canteen1.ico")
        self.root.configure(bg = "#FCEDDA")
        self.root.title("Total Order List")
        self.root.resizable(height = False, width=False)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        width = 600
        height = 300                                                # Setting the geometry to the window
        self.root.geometry("%dx%d+%d+%d"%(width, height,(self.screen_width-width)/2,(self.screen_height-height)/2)) 
        self.fin = "files/item_order"
        self.dbo = dbm.open(self.fin, "c")                          # Getting the data from dbm file
        self.item_list = []                                         # Creating the list of items
        self.count_list = []                                        # Creating the count of items

        for i in self.dbo.keys():
            self.item_list.append(i.decode())
            self.count_list.append(int(self.dbo[i].decode()))

        # Buttons to visulose as well as get the data as text
        b1 = Button(self.root, text = "Visualize item count", command= self.visualize_item_count, bg = "#EE4E34", font = "TimesNewRoman 10 bold")
        b1.place(x = 225, y = 50)
        b2 = Button(self.root, text = "Check the total item count", command = self.each_item_count, bg = "#EE4E34", font = "TimesNewRoman 10 bold")
        b2.place(x = 210, y = 100)

        self.dbo.close()                                            # Closing the dbm file 
        self.root.mainloop()

    # Function to see each item count
    def each_item_count(self):
        win = Tk()                                                  # Creating a new window
        win.title("Count List")                                     # Setting the title to the window
        width = 600
        height = 400
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()                    # Setting the geometry for the window
        win.geometry("%dx%d+%d+%d"%(width, height,(screen_width-width)/2,(screen_height-height)/2))
        win.iconbitmap("images/canteen1.ico")                       # Setting the icon for the window                       
        
        s_bar = Scrollbar(win, orient = "vertical")                 # Creating the scroll-bar
        p_bar = Scrollbar(win, orient = "horizontal")
        s_bar.pack(side = RIGHT, fill  = Y)
        p_bar.pack(side = BOTTOM, fill = X)
        t = Text(win, wrap = NONE, yscrollcommand = s_bar.set)

        # Using zip we can iterate across more than lists simultaneously
        for i,j in zip(self.item_list, self.count_list):       
            t.insert(END, f"{i} -> {j}")
            t.insert(END, "\n")
        
        t.pack(side = TOP, fill = X)                                # Packing the text into window
        s_bar.config(command = t.yview)                             # Configuring vertical scroll bar
        p_bar.config(command = t.xview)                             # Configuring horizontal scroll bar
    
    # Function to visulize the whole item data available
    def visualize_item_count(self):

        self.root.destroy()                                         # Destroying the sub window
        plt.bar(self.item_list,self.count_list)                     # Creating a bar plot
        plt.xticks(self.item_list, rotation = "vertical")           # Orienting the x-labels
        plt.ylabel("No. of items ordered till now")                 # Adding the y-label
        plt.xlabel("Items")                                         # Adding the x-label
        plt.grid()                                                  # Grid to analyze perfectly
        plt.show()                                                  # Plotting the graph


d = data_management()