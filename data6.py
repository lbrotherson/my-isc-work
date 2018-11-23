from datetime import datetime
import serial
import io

outfile='/home/user01/my-isc-work/serial-temperature.tsv'

ser=serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE
)

sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser,1),encoding='ascii',newline='\r')
sio._CHUNK_SIZE=1

with open(outfile,'w') as f: #appends to existing file 
   while ser.isOpen():
      datastring = sio.readline()
      #\t is tab; \n is line separator
      f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
      f.flush() #included to force the system to write to disk
ser.close()

