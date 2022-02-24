import socket
import datetime as dt
import threading
import Verify as av


# Select an appropriate port number. 
PORT = 7000
# Set The Server's IP Address
SERVER_IP = '127.0.0.1'
# Set up the Server's Address
ADDR = (SERVER_IP, PORT) 
FORMAT = 'utf-8'

# Add code to initialize the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Write Code to bind Address to the server socket.
server.bind((SERVER_IP, PORT))

# This function processes messages that are read through the Socket.
def clientHandler(conn, addr): 
    # Write Code that allows the Server to receive a connection code from an Agent. 
    print("Connected by client.")
    print("Address: ", addr)
    # Write Code that allows the Server to receive a connection code from an Agent.
    """Your Code here"""
    code = conn.recv(1024).decode(FORMAT)
    print("Received connection code from client.")
   
    # Write Code that allows the Server to check if the connection code received is valid.
    """Your Code here"""
    code_valid = av.check_conn_codes(code)
    if code_valid == -1:
        print("Bad connection code supplied.")
        conn.send("BAD".encode(FORMAT))
        conn.close()
        print("Connection closed.")
        exit(1)

 

    # Write Code that allows the Server to retrieve a random secret question.
    print("Retrieving secret question.")
    secret = av.getSecretQuestion()
    print("Generated secret question.")

     # Write Code that allows the Server to send the random secret question to the Client.
    """Your Code here"""
    question = secret[0]
    conn.send(question.encode(FORMAT))
    print("Sent the secret question to client.")

    # Write Code that allows the Server to receive an answer from the Client.
    """Your Code here"""
    client_answer = conn.recv(1024).decode(FORMAT)

    # Write Code that allows the Server to check if the answer received is correct.
    """Your Code here"""
    correct_answer = secret[1]
    if client_answer != correct_answer:
        print("Incorrect answer supplied.")
        conn.send("BAD answer".encode(FORMAT))
        conn.close()
        print("Connection closed.")
        exit()

    # Write Code that allows the Server to Send Welcome message to agent -> "Welcome Agent X"
    """Your Code here"""
    print("Generating welcome message")
    time = dt.datetime.now().isoformat()
    msg = "Welcome Agent " + code_valid + " Time Logged - " + time
    conn.send(msg.encode(FORMAT))
    conn.close()
    print("Sent welcome message.")
    print("Connection closed.")

def runServer():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=clientHandler, args=(conn,addr) )
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}")

print("[STARTING] The Server is Starting...")
runServer()