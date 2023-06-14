import numpy as np 

a = np.array([[10,20,30],[40,50,60]])
print(a)
print("Row 0th = ",a[0])
print("Row 1th = " ,a[0][1])
print("index 1 row 1 column = ",a[0][0])

#(10,100,10) = start from 10 to 100 with gap of 10
a = np.arange (10,100,10)
print(a)

#(2:5) print value from index 2 to 5
print(a[2:5])