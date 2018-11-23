from datetime import datetime
import serial
import io

ser=serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE
)

sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser,1),encoding='ascii',newline='\r')
sio._CHUNK_SIZE=1

while  ser.isOpen():
	datastring = sio.readline()
	print(datetime.utcnow().isoformat(), datastring)
ser.close()

