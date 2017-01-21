import CHIP_IO.SOFTPWM as PWM
import CHIP_IO.GPIO as GPIO
import time

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

def cleanup():
	motorStop()
	PWM.stop(pin_pwm)
	GPIO.cleanup(pin_forward)
	GPIO.cleanup(pin_back)
	PWM.cleanup()

setup()
motorForward()
PWM.set_duty_cycle(pin_pwm, 1)
time.sleep(5)
PWM.set_duty_cycle(pin_pwm, 5)
time.sleep(5)
PWM.set_duty_cycle(pin_pwm, 100)
time.sleep(5)
PWM.set_duty_cycle(pin_pwm, 50)
time.sleep(5)
cleanup()
