"""
Server Program to accept the payment 
"""
import socket

def server (pay):

    print("Waiting for the payment")
    host = socket.gethostname()                         # Getting the host name of server
    port = 5000                                         # Assigning a port

    server_socket = socket.socket()                     # Creating a socket -> End device
    server_socket.bind((host,port))                     # Binding the server with port

    server_socket.listen(5)                             # Server starts listening creating a queue of size 5

    conn, address = server_socket.accept()              # Accepting the connection from client
    suc = "S"
    dec = "Payment Declined"                            
    print("Got Connection from: " + str(address))       # Printing the address of connection
    amt = str(pay)            
    conn.send(amt.encode())                             # Sending the amount to be paid
    try:
        while True:
            data2 = conn.recv(1024).decode()                # Receiving the amount
            if str(pay) == data2:                           # If exact amount is received, send "Payment Success"
                conn.send(suc.encode())
                break
            else:
                conn.send(dec.encode())                     # If not send "Payment Declined"
        print("Payment Received -> Rs.",pay)        
        conn.close()                                        # Close the socket
        return "Success"
    except:
        pass
