import socket, OSC, re, time, threading, math

receive_address = '192.168.1.103', 5051 #CHIP Adress, Outgoing Port
send_address = '192.168.1.101', 5050 #Touch OSC Adress, Incoming Port

##########################
#	OSC
##########################

# Initialize the OSC server and the client.
s = OSC.OSCServer(receive_address)
c = OSC.OSCClient()
c.connect(send_address)

s.addDefaultHandlers()

# define a message-handler function for the server to call.
def test_handler(addr, tags, stuff, source):
	print("---")
	print("received new osc msg from %s" % OSC.getUrlStr(source))
	print("with addr : %s" % addr)
	print("typetags %s" % tags)
	print("data %s" % stuff)
	msg = OSC.OSCMessage()
	msg.setAddress(addr)
	msg.append(stuff)
	c.send(msg)
	print("return message %s" % msg)
	print("---")

def moveStop_handler(add, tags, stuff, source):
	addMove(0,0)

def moveJoystick_handler(add, tags, stuff, source):
	print("message received:")
	msg = OSC.OSCMessage()
	msg.setAddress(addr)
	msg.append(stuff)
	c.send(msg)
	print("X Value is: ") 
	print(stuff[0]) 
	print("Y Value is: ")
	print(stuff[1])  #stuff is a 'list' variable

# adding my functions
s.addMsgHandler("/basic/stop", moveStop_handler)
s.addMsgHandler("/basic/joystick", moveJoystick_handler)
# just checking which handlers we have added
print("Registered Callback-functions are :")
for addr in s.getOSCAddressSpace():
	print(addr)

# Start OSCServer
print("\nStarting OSCServer. Use ctrl-C to quit.")
st = threading.Thread( target = s.serve_forever )
st.start()


# Loop while threads are running.
try :
	while 1 :
		time.sleep(10)
 
except KeyboardInterrupt :
	print("\nClosing OSCServer.")
	s.close()
	print("Waiting for Server-thread to finish")
	st.join()
	print("Done")
