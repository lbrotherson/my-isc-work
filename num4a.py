import numpy.ma as MA
a = MA.masked_array(data=range(10), fill_value=-999)
a[2] = MA.masked
print(a,a.fill_value,a.mask)
b=[]
b = MA.masked_where(a>7,a)
print(b)
print(b.fill_value)
c=b.filled()
print(c)
