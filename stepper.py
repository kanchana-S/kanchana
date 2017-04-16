#!/usr/bin/python 
##########################################################
# * Python code (Adafruit BBIO Library Version) for 
# * Driving a Stepper Motor Card using BBB
# * Beaglebone Black running Debian 7 Linux distribution
##########################################################
# * Developed by MicroEmbedded Technologies
##########################################################
 
# Import standard python libraries
import sys
import os
import time

# Import GPIO part of Adafruit BBIO Library
import Adafruit_BBIO.GPIO as GPIO

##############################################################
# GPIO Pin definitions for Stepper Motor Interfacing Board 
# Please refer "MicroEmbedded_BBB_Interfacing Details_New.pdf" 
# for all the PIN details
##############################################################

STEPPER_1   =    "P9_11"
STEPPER_2   =    "P8_7"
STEPPER_3   =    "P9_12"
STEPPER_4   =    "P8_8"


##############################################################
# Description 	: This function turns the stepper PIN ON 
# 		  It will setup a PIN as GPIO, sets the 
# 		  direction as OUT and then makes the PIN high  
# Input		: @pin = Pin No associated with LED
# Return	: None	 
# Note		: 
##############################################################

def stepperOn(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
	return 

##############################################################
# Description 	: This function turns the stepper PIN OFF 
# 		  It will setup a PIN as GPIO, sets the 
# 		  direction as OUT and then makes the PIN low  
# Input		: @pin = Pin No associated with LED 
# Return	: None	 
##############################################################
	
def stepperOff(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	return 


##############################################################
# Description 	: This function writes the sequence 5 
# 		  (5 in binary "0101") on stepper motor pins
#		  While writing start from LSB, hence LSB
#		  goes to stepper pin #1 	 
# Input		: None	 
# Return	: None	 
##############################################################

def stepperSeq5():
	stepperOn(STEPPER_1)		# LSB first i.e. write 1 on STEPPER_1 
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOff(STEPPER_2)		# Then next bit i.e. write 0 on STEPPER_2
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOn(STEPPER_3)		# Next bit i.e. write 1 on STEPPER_3
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOff(STEPPER_4)		# Final bit (MSB) i.e. write 0 on STEPPER_4
	time.sleep(0.0001)		# pause for 100 micro seconds
	return 


##############################################################
# Description 	: This function writes the sequence 9 
# 		  (9 in binary "1001") on stepper motor pins
#		  While writing start from LSB, hence LSB
#		  goes to stepper pin #1 	 
# Input		: None	 
# Return	: None	 
##############################################################

def stepperSeq9():
	stepperOn(STEPPER_1)		# LSB first i.e. write 1 on STEPPER_1
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOff(STEPPER_2)		# Then next bit i.e. write 0 on STEPPER_2
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOff(STEPPER_3)		# Next bit i.e. write 0 on STEPPER_3
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOn(STEPPER_4)		# Final bit (MSB) i.e. write 1 on STEPPER_4
	time.sleep(0.0001)		# pause for 100 micro seconds
	return 


##############################################################
# Description 	: This function writes the sequence 10 
# 		  (10 in binary "1010") on stepper motor pins
#		  While writing start from LSB, hence LSB
#		  goes to stepper pin #1 	 
# Input		: None	 
# Return	: None	 
##############################################################

def stepperSeq10():
	stepperOff(STEPPER_1)		# LSB first i.e. write 0 on STEPPER_1
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOn(STEPPER_2)		# Then next bit i.e. write 1 on STEPPER_2
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOff(STEPPER_3)		# Next bit i.e. write 0 on STEPPER_3
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOn(STEPPER_4)		# Final bit (MSB) i.e. write 1 on STEPPER_4
	time.sleep(0.0001)		# pause for 100 micro seconds
	return 


##############################################################
# Description 	: This function writes the sequence 6 
# 		  (6 in binary "0110") on stepper motor pins
#		  While writing start from LSB, hence LSB
#		  goes to stepper pin #1 	 
# Input		: None	 
# Return	: None	 
##############################################################

def stepperSeq6():
	stepperOff(STEPPER_1)		# LSB first i.e. write 0 on STEPPER_1
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOn(STEPPER_2)		# Then next bit i.e. write 1 on STEPPER_2
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOn(STEPPER_3)		# Next bit i.e. write 1 on STEPPER_3
	time.sleep(0.0001)		# pause for 100 micro seconds
	stepperOff(STEPPER_4)		# Final bit (MSB) i.e. write 0 on STEPPER_4
	time.sleep(0.0001)		# pause for 100 micro seconds
	return 


##############################################################
# Description 	: This function rotates the stepper motor one 
# 		  step in left direction (anti-clockwise)
# Input		: None	 
# Return	: None	 
##############################################################
	
def stepperclock():
	stepperSeq5()
	time.sleep(0.01)
	stepperSeq9()
	time.sleep(0.01)
	stepperSeq10()
	time.sleep(0.01)
	stepperSeq6()
	time.sleep(0.01)
	return

##############################################################
# Description 	: This function rotates the stepper motor one 
# 		  step in right direction (clockwise)
# Input		: None	 
# Return	: None	 
##############################################################

def stepperanticlock():
	stepperSeq6()
	time.sleep(0.01)
	stepperSeq10()
	time.sleep(0.01)
	stepperSeq9()
	time.sleep(0.01)
	stepperSeq5()
	time.sleep(0.01)
	return


print "\nStepper Motor Driver using Python\n"
print  "-----------------------------------------------\n" 	
while True:
	for i in range(0, 12):				# Loop for 12 times (to comeplete on revolution)
		stepperclock()			# Rotate stepper left 
	time.sleep(3)					# Sleep for 3 seconds 
	for i in range(0, 12):				# Loop for 12 times (to comeplete on revolution)
		stepperanticlock()			# Rotate stepper right
	time.sleep(3)					# Sleep for 3 seconds
exit()							# Exit from program



