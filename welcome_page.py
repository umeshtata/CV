"""
CANTEEN BILLING SYSTEM

Welcome Page:
This is the first page which welcomes the customer.
"""

from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
import order_page

def welcome():
    root.destroy()                                  # Destroying the welcome page 
    k = order_page.page2()                          # A new object is created for the class in the module order_page

root = Tk()                                         # Creating a window
root.title("My Canteen")                            # Title to the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 400
height = 200
root.geometry("%dx%d+%d+%d"%(width, height,(screen_width-width)/2, (screen_height-height)/2))
root.resizable(width = False, height = False)       # Geometry for the window and disabling the resizing of window
root.iconbitmap("images/canteen1.ico")              # Fixing an icon to the window
img = Image.open("images/homepage.png")
bg = ImageTk.PhotoImage(img)   
label = Label(root,image = bg)                      # Setting a backgroung image to the window
label.place(x = 0, y = 0)                           
mixer.init()                                        # Initializing the mixer object
mixer.music.load("audios/Welcome-to-My-cantee.mp3") # Loading background music
mixer.music.play()                                  # Playing the background music


label2 = Label(root, text = "Welcome to My Canteen", font = "Algerian 15 bold")
label2.place(x = 75, y = 50)                        # Creating and placing a label for welcoming

welcome_button  = Button(root, text = "Click here to proceed", command = welcome, font = "Calbiri 10 bold")
welcome_button.place(x = 125, y = 100)              # Creating and placing a button for redirecting to the next page

root.mainloop()