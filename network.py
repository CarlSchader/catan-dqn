import socket, os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv('PORT'))
HOST = os.getenv('HOST')

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect((HOST, PORT))

while 1:
  print('Server Response:', s.recv(1024).decode())
  s.send(bytes(input("NEW MESSAGE: "), 'ascii'))