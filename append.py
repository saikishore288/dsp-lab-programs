#program to append one array into an another arrary
import numpy as np
a=input('enter the array 1:')
b=input('enter the array 2:')
for i in range(0,len(b)):
	a.append(b[i])
print a
