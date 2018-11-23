band = ['mel','geri','victoria','mel','emma']
counts = {}
for name in band:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
    print(counts)
    
    
