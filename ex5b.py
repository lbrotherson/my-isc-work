with open('weather.csv','r') as reader:
    data=reader.readline()	
    while data!="":
        data=reader.readline()
        print(data)
print("It's over")
    
