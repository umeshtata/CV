"""
UPI Payment App
"""

import socket
from tkinter import *
from pygame import mixer

class client:
    def __init__(self):
        host = socket.gethostname()                                 # Getting the host name (Here Server)
        port = 5000                                                 # Assigning a port

        self.client_socket = socket.socket()                             # Creating the socket -> end device
        self.client_socket.connect((host,port))                          # Connecting to the server
        self.data = self.client_socket.recv(1024).decode()                    # Receiving the data upto maximum of 1024 bytes
        self.win = Tk()
        self.win.title("UPI APP")
        self.win.iconbitmap("images/rupee.ico")
        self.win.configure(bg = "#C7E9B0")
        self.screen_width = self.win.winfo_screenwidth()
        self.screen_height = self.win.winfo_screenheight()
        self.width = 400
        self.height = 200
        self.win.geometry("%dx%d+%d+%d"%(self.width, self.height,(self.screen_width-self.width)/2, (self.screen_height-self.height)/2))
        self.win.resizable(width = False, height = False)  
        label = Label(self.win, text = f"Amount to be paid is Rs.{self.data}", bg = "#C7E9B0", fg = "black", font = "TimesNewRoman 12 bold") 
        label.pack()
        button1 = Button(self.win, text = "PAY", command = self.success)
        button1.place(x = 275, y = 100)
        button2 = Button(self.win, text = "CANCEL", command = self.failure)
        button2.place(x = 100, y = 100)

        self.win.mainloop()

    def success(self):
        self.win.destroy()
        message = self.data                                        
        self.client_socket.send(message.encode())                    # Send the amount to be paid
        data = self.client_socket.recv(1024).decode()                # If paid exact amount it returns letter "S" else payment declined
        if data == "S":                                         # If payment is success then a new window is created
            root = Tk()
            root.title("Payment Page")
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            width = 400
            height = 200
            root.configure(bg = "#BAD7E9")
            root.geometry("%dx%d+%d+%d"%(width, height,(screen_width-width)/2, (screen_height-height)/2))
            root.resizable(width = False, height = False)       # Setting the geometry to the window
            root.iconbitmap("images/rupee.ico")                 # Setting the icon
            mixer.init()
            mixer.music.load("audios/Your-order-is-placed_1.mp3")
            mixer.music.play()
            # Adding the labels as Payment Success
            l1 = Label(root, text = "Your Order has been placed Successfully.",bg = "#BAD7E9")
            l2 = Label(root, text = "!!!😊Payment Success😊!!!",bg = "#BAD7E9")
            l3 = Label(root, text = "❤️ THANK YOU FOR PLACING YOUR ORDER ❤️",bg = "#BAD7E9")
            l1.pack()
            l2.pack()
            l3.pack()            
            root.mainloop()

            self.client_socket.close()                                       # Closing the end device   

    def failure(self):
        self.win.destroy()
        root = Tk()
        root.title("Payment Page")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        width = 400
        height = 200
        root.configure(bg = "#C7E9B0")
        root.geometry("%dx%d+%d+%d"%(width, height,(screen_width-width)/2, (screen_height-height)/2))
        root.resizable(width = False, height = False)
        mixer.init()
        mixer.music.load("audios/Failure_payment.mp3")
        mixer.music.play()                       # Setting the geometry to the window
        root.iconbitmap("images/rupee.ico")    
        label = Label(root, text = "Payment failed", font = "TimesNewRoman 13 bold", bg = "#C7E9B0")
        label.pack()
        root.mainloop()       

c = client()
