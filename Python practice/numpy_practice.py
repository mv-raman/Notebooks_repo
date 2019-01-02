import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a.shape)
print(type(a))
print(a[0], a[1], a[2])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
print(b[0, 0], b[1, 1])
# auto create arrays
a = np.zeros((2, 2))
print(a)
b = np.ones((3, 3))
print(b)
c = np.full((2, 2), 7)
print(c)
d = np.eye(2)
print(d)
e = np.random.random((2, 2))
print(e)
#array indexing
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
b=a[0:2,1:3]
print(b)
b[0,0]=77
print(a)
#using integer indexing and slicing
print("--------")
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
row_r1=a[1,:]
print(row_r1,row_r1.shape)
row_r2=a[1:2,:]
print(row_r2,row_r2.shape)
col_r1=a[:,1]
print(col_r1,col_r1.shape)
col_r2=a[:,1:2]
print(col_r2,col_r2.shape)

#integer array indexing
print("--------------------")
a=np.array([[1,2],[3,4],[5,6]])
print(a.shape)
print(a[[0,1,2],[1,1,0]])
print(np.array([a[0,1],a[1,1],a[2,0]]))
#create array for selection and mutation
print("--------------------")
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
b=np.array([0,2,0,1])
print(a[np.arange(4),b])
a[np.arange(4),b]+=10
print(a)
#boolean array indexing
print("-------------------")
a=np.array([[1,2],[3,4],[5,6]])
print(a)
bool_idx=(a>2)
print(bool_idx)
print(a[bool_idx])
print(a[a>2])
#datatypes
x=np.array([1,2],dtype=np.int64)
print(x.dtype)
x=np.array([1.0,2.0])
print(x.dtype)
#array math
print("------------------------")
x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)
print("%s %s"%(x,y))    #print(x,y)
print(x+y)
print(np.add(x,y))
print(x-y)      # * is element wise multiplication
print(np.subtract(x,y))
print(np.sqrt(x,y))

#matrix multiplication
print("---------")
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
v=np.array([9,10])
w=np.array([11,12])
print(v.dot(w))
print(np.dot(v,w))
print(np.dot(x,v))
print(np.dot(x,y))
#sum of arrays
print(np.sum(x))
print(np.sum(x,axis=0))#coloum wise
print(np.sum(x,axis=1))
print(x.T)
#broadcasting
print("--------")
x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v=np.array([1,0,1])
y=np.empty_like(x)#create empty matrix with same shape as x
for i in range(4):
    y[i,:]=x[i,:]+v
print(y)
#another approach
vv=np.tile(v,(4,1))
print(vv)
y=vv+x
print(y)
#easy method
y=x+v
print(y)

#broad casting 2
print("--------------")
v=np.array([1,2,3])
w=np.array([4,5])
print(np.reshape(v,(3,1))*w)
x=np.array([[1,2,3],[4,5,6]])
print(x+v)
print(x*2)
print(v.shape)
print(x+np.reshape(w,(2,1)))
print((x.T+w).T)




















