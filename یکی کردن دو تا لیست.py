a = dict ({'a':'20' ,' b':'10'})
b = dict ({'c':'45' , 'g':'80'})
c = dict(**a,**b)
print(c)