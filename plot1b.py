import matplotlib.pyplot as plt
time = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1,15.5,16.3,18.1,17.3,19.1,20.2]
plt.plot(time,co2,'--b',label='CO2 (ppm)')
plt.plot(time,temp,'--g',label='Temperature (oC)')
plt.title('CO2/Temperature versus time')
#plt.ylabel('CO2 concentration (ppm)')
plt.xlabel('Time (decade)')
plt.legend()
plt.show()
