#program on linear algebraic operations
import numpy as np
a=np.array(input('enter first 2*2 matrix:'))
b=np.array(input('enter second 2*2 matrix:'))
u=np.add(a,b)
print 'addition of two matirces:\n',u
v=np.subtract(a,b)
print 'subtraction of two matrices:\n',v
e=np.multiply(a,b)
print 'element by element multiplication of two matrices:\n',e
f=np.dot(a,b)
print 'multiplication of two matrices:\n',f
k=np.divide(a,b)
print 'element by element division of two matrices:\n',k
y=np.linalg.inv(a)
print 'inverse of\n',a,'\n is:',y
z=np.linalg.eig(a)
print 'eigen vectors of\n',a,'\n is:',z
w=np.linalg.matrix_rank(a)
print 'rank of a matrix of\n',a,'\n is:',w
x=np.linalg.det(a)
print 'determinant of\n',a,'\n is:',x
s=np.linalg.eigvals(a)
print 'eigen values of\n',a,'\n is:',s
t=np.linalg.qr(a)
print 'qr decomposition of\n',a,'\n is:',s
g=np.linalg.matrix_power(a,3)
print 'matrix power of\n',a,'\n is:',g
