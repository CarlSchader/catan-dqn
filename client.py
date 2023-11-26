import socket, os
from dotenv import load_dotenv

from message_types import interpret_server_message, format_client_message

load_dotenv()

SERVER_PORT = int(os.getenv('SERVER_PORT'))
SERVER_HOST = os.getenv('SERVER_HOST')

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect((SERVER_HOST, SERVER_PORT))

while True:
  server_raw_message = s.recv(1024).decode()
  print('Server:', interpret_server_message(server_raw_message))
  client_message = input('Client: ')
  formatted_message = format_client_message(client_message)
  print('Client Formatted:', formatted_message)
  s.send(bytes(formatted_message, 'ascii'))