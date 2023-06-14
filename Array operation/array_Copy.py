import numpy as np

a = np.array([[10,20,30],[40,50,60]])
print(a)
b = np.copy(a)
print("The value of a copied in a = ", b)

# we copied the value of a in b , Now if i even change the b that not effect the a
a[0][1] = 100
print("Array of A",a)
print("Array of B",b)
# we cleary see that even if i changed the value of A that not effect B