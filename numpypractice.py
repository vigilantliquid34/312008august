import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
b = np.arange(5,16)
print(b)
c = np.zeros((3,4))
print(c)
d = np.ones((4,4))
print(d)
e = np.eye(4)
print(e)
arr = np.array([10, 20, 30, 40, 50])
arr_slice = arr[1:4]
print(arr_slice)

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
prod = a*b
print(prod)

x = np.array([5, 10, 15, 20, 25])
mean = np.mean(x)
max = np.max(x)
standard_dev = np.std(x)
print(mean)
print(max)
print(standard_dev)

x = np.array([1, 2, 3, 4, 5, 6])
x = x.reshape(2,3)
print(x)

x = np.arange(1,10)
x = x.reshape(3,3)

a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([1, 0, 1])
print(a+b)

arr = np.array([10, 15, 20, 25, 30])
arr = [arr > 18]