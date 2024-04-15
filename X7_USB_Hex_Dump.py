import os;
import serial;
import time;
import keyboard;

def ExitState():
    print("Closing application...")
    time.sleep(3)
    exit()


# Set our working directory to the same path as this script
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

print("Mega Everdrive X7 USB Port Hex Dumper V1.0")

try:
	ser = serial.Serial('COM3', timeout=0)	# Open the serial port. baud = 9600, data bits = 8, stop bits = 1 all by default. We need to set timeout to 0 or our code gets trapped waiting for data.
except Exception:
    print("Mega Everdrive X7 could not be found, make sure the catridge is plugged in to your PC, and the console is turned on. If it is, check the port with 'python -m serial.tools.list_ports' and modify this script to use the correct port.")
    time.sleep(10)	# Make sure the user has enough time to read this.
    ExitState()

print("Name the file you would like to dump to:")
dumppath = input()
if(os.path.isfile(dumppath)):
	print(dumppath+" already exits, do you wish to append incoming hex data to it? Y/N")
	ovrwrtdecision = input()
	ovrwrtdecision.lower()
	if(ovrwrtdecision == "n"):
		ExitState()	# If the user says no, then exit.

print("This app will now dump hex data to "+dumppath+" when you are done make sure to press X or the data will not save.")
dumpfile = open(dumppath, "wb")
while True:
    if keyboard.is_pressed('x'):
        break
    indata = ser.read()     # Read from the serial port
    dumpfile.write(indata)  # And send it to our destination file


# If X is pressed we run this.
print("Closing port "+ser.name+" and file "+dumppath)
ser.close()
dumpfile.close()
ExitState()