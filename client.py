#application simulates client sending 10 packets to the server

import socket
from socket import AF_INET, SOCK_DGRAM
import time

serverName = "127.0.0.1"
clientSocket = socket.socket(AF_INET,SOCK_DGRAM) #creates the socket
clientSocket.settimeout(1) #sets the timeout to 1 second
sequence_number = 1 #keeps track of packets
message = "Ping" #message
print("%s %s" % (message, serverName))

while sequence_number<=10:
	start = time.time() #assigns the current time to a variable
	clientSocket.sendto(message,(serverName, 12000))
	#sends a message to the server on port 12000

	try:
		message, address = clientSocket.recvfrom(1024) 
		#recieves message from server
		elapsed = ((time.time()-start)*1000) 
		# calculates how much time has elapsed since the start time

		print "64 bytes from %s: icmp_seq=%s time=" % (serverName, sequence_number) + str(elapsed) + " ms"

	except socket.timeout: 
	#if the socket takes longer that 1 second, it does the following
		print("Request timed out for icmp_seq %s" % sequence_number)

	sequence_number+=1 
	#sequence number is increased

	if sequence_number > 10: #closes the socket after 10 packets

		clientSocket.close()