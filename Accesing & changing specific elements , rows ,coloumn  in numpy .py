import numpy as np 
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
# Get a specific element [r,c]
a[1,5]
print(a[1,5])
# Get a specific row :
a[0,:]
print(a[0,:])
a[1,:]
print(a[1,:])
# Get a specific coloumns :
a[:,0]
print(a[:,0])
print(a[:,4])

# Getting a little more fancy [startindex : endindex : stepsize]
print(a[0,2:6:2])
print(a[0,1:-1:2])
# changing the value :-
a[1,5] = 20
print(a)
a[:,2] = 4
print(a)

# 3-D Example :-

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

# Get specific element (work outside in) 
print(b[:,1,:])
# Initializing different types of array :-
# All 0's Matrix
print(np.zeros((5,3,2,2)))
# All 1's matrix :
np.ones((4,2,2),dtype='int32')
print(np.ones((4,2,2),dtype='int32'))
# Any other number :-
np.full((2,2),99)
print(np.full((2,2),99 ,dtype= 'float32'))
# Anyother Number(full_like):
np.full_like(a.shape ,4)
print(np.full_like(a.shape ,4))
print(np.full_like(a,4))
# Random decimal number :-
np.random.rand(4,4)
print(np.random.rand(4,4))
print(np.random.rand(4,3,2))
print(np.random.random_sample(a.shape))
# Random Integer values :-
print(np.random.randint(4,8,size=(3,3)))
# The identity Matrix :-
print(np.identity(3))
# Repeat an array :-
arr = np.array([1,2,3])
r1 = np.repeat(arr,3,axis=0)
print(r1)

output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
print(output)
output[1:4,1:4] = z 
print(output)

# Be careful when copying arrays :
a = np.array([1,2,3])
b = a
print(b)
b[0] = 100
print(b)
b = a.copy()
print(b)

# Mathematics :-
a = np.array([1,2,3,4])
print(a)
a+2
print(a+2)
print(a-2)
print(a*2)
print(a/2)
b = np.array([1,0,1,0])
c = a+b
print(c)
print(a**2)
# Take the sin :-
print(np.sin(a))
print(np.cos(a))

# Linear ALgebra :-
a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)
print(np.matmul(a,b)) # Matrix Multiplication
# Finding Determinant :-
c = np.identity(3)
np.linalg.det(c)
print(np.linalg.det(c)) # Linear Algebra : determinant

# Stastics :-
stats = np.array([[1,2,3],[4,5,6]])
print(stats)
print(np.min(stats))
print(np.min(stats , axis = 0))
print(np.max(stats))

# Re-organizing Arrays :-
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
print(before.shape)
after = before.reshape((4,2))
print(after)

# Vertically stacking vectors :-
v1 = np.array([1,2,3,4,5])
v2 = np.array([6,7,8,9,10])
print(np.vstack([v1,v2,v2,v1]))

# Horizontal stack :-
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(np.hstack((h1,h2)))

# Miscellaneous 
# Load Data from Files
file_Data = np.genfromtxt('Raw Data.txt', delimiter=',')
print(np.genfromtxt('Raw Data.txt' , delimiter = ','))
print(file_Data)
file_Data = file_Data.astype('int32')
# Boolean Masking and advanced indexing:-
file_Data[file_Data > 50]
# You can index with a list in Numpy :
a = np.array([1,2,3,4,5,6,7,8,9])
a[[1,2,8]]
np.any(file_Data > 50 , axis=0)
((file_Data > 50) & (file_Data < 100))