from datetime import datetime
import serial

ser=serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE
)

print(datetime.utcnow().isoformat(),ser.read(size=8))
ser.close()

