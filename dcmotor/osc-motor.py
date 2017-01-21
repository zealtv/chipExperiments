import CHIP_IO.SOFTPWM as PWM
import CHIP_IO.GPIO as GPIO
import socket, OSC, re, time, threading, math

receive_address = '192.168.1.103', 5051 #CHIP Adress
send_address = '192.168.1.101', 5050 #Remote OSC Adress


#####################
#	MOTOR CONTROL
#####################

pin_pwm = "XIO-P0"
pin_forward = "XIO-P2"
pin_back = "XIO-P4"

def setup():
	#PWM.start(channel, duty, freq=2000, polarity=0)
	#duty values are valid 0 (off) to 100 (on)
	GPIO.setup(pin_forward, GPIO.OUT)
	GPIO.setup(pin_back, GPIO.OUT)
	PWM.start(pin_pwm, 0, 800, 0)
	motorStop()

def motorStop():
	GPIO.output(pin_forward, GPIO.LOW)
	GPIO.output(pin_back, GPIO.LOW)

def motorForward():
	GPIO.output(pin_forward, GPIO.HIGH)
	GPIO.output(pin_back, GPIO.LOW)

def motorBack():
	GPIO.output(pin_forward, GPIO.LOW)
	GPIO.output(pin_back, GPIO.HIGH)

def motorSpeed(p):
	PWM.set_duty_cycle(pin_pwm, p)

def motorDirection(d):
	if(d == 0):
		motorStop()
	elif(d > 0):
		motorForward()
	elif(d < 0):
		motorBack()

def cleanup():
	motorStop()
	PWM.stop(pin_pwm)
	GPIO.cleanup(pin_forward)
	GPIO.cleanup(pin_back)
	PWM.cleanup()



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


def motor_speed_handler(add, tags, stuff, source):
	print("message received:")
	motorSpeed(stuff[0])
	print("Motor Speed %: ") 
	print(stuff[0]) 

def motor_direction_handler(add, tags, stuff, source):
	print("message received:")
	motorDirection(stuff[0])
	print("Motor Direction is: ")
	print(stuff[0])

# adding my functions
s.addMsgHandler("/test", test_handler)
s.addMsgHandler("/motor/speed", motor_speed_handler)
s.addMsgHandler("motor/direction", motor_direction_handler)
# print out OSC handlers
print("Registered Callback-functions are :")
for addr in s.getOSCAddressSpace():
	print(addr)




####################
#	MAIN PROGRAM
####################

#Setup GPIO
setup()
motorForward()

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
	print("cleaning up GPIO")
	cleanup()
	print("Done")


