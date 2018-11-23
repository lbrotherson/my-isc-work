import netCDF4
ds = netCDF4.Dataset('ggas2014121200_00-18.nc')
for i in ds.variables:
	print(i)
sst = ds.variables['SSTK']
print(sst)
for j in sst.dimensions:
	print(j,len(ds.variables[j]))
print(sst.size,sst.shape)
for attr in sst.ncattrs():
	print(attr,'=',getattr(sst,attr))
	
