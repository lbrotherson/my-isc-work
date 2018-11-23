def calc_hypo(a,b):
    if type(a) not in (int,float) or type(b) not in (int,float):
        print('Bad argument!')
        return False
    elif a <= 0 or b <= 0:
        print('Invalid!')
        return False 
    else:        
	    hypo = (a**2+b**2)**0.5
	    return hypo

print(calc_hypo(3,0))
