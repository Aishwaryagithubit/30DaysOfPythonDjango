import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("element at index 2:", arr[2])   
print("slice index 1 to 3:", arr[1:3])

# 2D slicing
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("second row:", arr2[1])
print("element at row 2, col 3:", arr2[1,2])
print("all rows, col 2:", arr2[:,1])

#operations
p = np.array([1,8,9])
q = np.array([4,6,3])

print("Addition:", p + q)     
print("Multiplication:", p * q) 
print("Square: ", p**2)       

# Aggregate functions
print("Sum: ", np.sum(p))      
print("Mean:", np.mean(q))    
print("Max:", np.max(q))      









