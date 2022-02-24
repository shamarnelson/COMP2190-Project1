import socket

# Select an appropriate port number. 
PORT = 7000
# Set The Server's IP Address
SERVER_IP = '127.0.0.1'
# Set up the Server's Address
ADDR = (SERVER_IP, PORT) 
FORMAT = 'utf-8'

# Add code to initialize the Socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Write Code that will allow the Client (Agent) to send messages to the server. The Function accepts the message as a String (msg) and sends that message to the Server through a connection established.
def send(msg):
    print("Sending message to the server.")
    new_msg = msg.encode(FORMAT)
    client.send(new_msg)

# Write code to Prompts the Agent to enter their connection code and returns the code given.
def getConCode():
    print("Enter the connection code:")
    return input()

# Write code to Prompts the Agent to enter an answer and returns the answer given.
def getAnswer(question):
    print("Provide a response to the question below.")
    print(question)
    print("Enter response:")
    return input()


# Get Connection Code.
connCode = getConCode()

# Send Connection Code to Server.
send(connCode)

# Receive question from server.
question = client.recv(1024).decode(FORMAT)
if question == "BAD":
    print("Wrong connection code supplied.")
    exit(1)

# Get Answer from Agent.
answer = getAnswer(question)

# Send Answer to Server.
send(answer)

# Receive and print response from the server.
resp = client.recv(1024).decode(FORMAT)
print(resp)
