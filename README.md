# Mega Everdrive X7 USB Port Hex Dumper

---
A Python tool to dump hex data from a Mega Everdrive X7's USB port into a file.

### Requirements
[PySerial](https://pypi.org/project/pyserial/)
[Python keyboard library](https://pypi.org/project/keyboard/)

### Usage

Before starting the application, make sure your Mega Everdrive is plugged into your PC, and the console is turned on or you'll get this message:

```
Mega Everdrive X7 could not be found, make sure the catridge is plugged in to your PC, and the console is turned on. If it is, check the port with 'python -m serial.tools.list_ports' and modify this script to use the correct port.
```

The program will then ask you to name the file you'd like to dump the data to. If the file already exists, it will ask if you'd like to append the incoming hex data to the file. Answering no will close the program.

From here the program will continue to listen to Everdrive's port for data and dump it to the file. When you're done recording data, **you must press X on your keyboard to safely close out** due to the way Python buffers data before actually writing it to a file, or else none of the data will save.
