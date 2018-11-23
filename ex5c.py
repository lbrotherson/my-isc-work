with open('weather.csv','r') as reader:
    data=reader.readline()
    print('first',data)
    rain=[]
    for line in reader.readlines():
        print(line)
        line.strip().
