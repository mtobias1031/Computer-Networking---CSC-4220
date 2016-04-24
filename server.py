#UDPPingerServer.py
#application acts like a server which simulates randomized lost packets

import random
import socket
from socket import *

#SOCK_DGRAM is used to create UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', 12000)) #IP and port number of socket
while True:

	#Generates random number in the range of 0 to 10
	rand = random.randint(0, 10)
	#Receives the client packet along with the address it is coming from
	message, address = serverSocket.recvfrom(1024)
	#Capitalize the message from the client
	message = message.upper()
	
	#If rand is less is than 4, we consider the packet lost and do not respond
	if rand < 4:
		continue
	#Otherwise, the server responds
	serverSocket.sendto(message, address)