import numpy as np
'''
#sual1
arr=np.arange(15,55)
print(arr[1:-1])
#sual2
arr=np.full((3,4),7)
print(arr)
#sual3
arr=np.arange(10,19).reshape(3,3)
print(arr)
#sual4
arr=np.diag([1,2,3,4,5])
print(arr)
#sual5
arr=np.zeros(10)
arr[5]=11
print(arr)
#sual6
#Convert an array to a float type using np.asfarray(). 
arr=[1,2,3,4,5]
new_arr=np.asarray(arr,dtype=float)
print(new_arr)
#sual7
array1=([[ 0, 1, 2, 3], [ 4, 5, 6, 7], 
[ 8, 9, 10,11]])
array2=np.flip(array1,axis=1)
print(array2)
#sual8
arr = np.array(['python', 'NUMPY', 'Data Science'])
print(np.char.lower(arr))
print(np.char.upper(arr))
print(np.char.title(arr))
print(np.char.capitalize(arr))
print(np.char.swapcase(arr))
#sual9
today=np.datetime64('today')
yesterday=today-np.timedelta64(1,'D')
tomorrow=today+np.timedelta64(1,'D')
print(today)
print(yesterday)
print(tomorrow)
'''
#sual10
array1=[10, 20, 30] 
array2=np.append(array1,[40,50,60,70,80,90])
print(array2)
