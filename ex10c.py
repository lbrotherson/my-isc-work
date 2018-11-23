if{}:print('hi')
d = {'maggie':'uk','ronnie':'usa'}
counts = {}
print(dir(d))
print(d.items())
print(d.keys())
print(d.values())
print(d.get('maggie','nowhere'))
print(d.get('ronnie','nowhere'))
d.setdefault('fabian','spain')
print(d)

