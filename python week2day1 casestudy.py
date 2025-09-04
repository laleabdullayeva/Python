#sual1
import numpy as np
'''''
arr=np.linspace(0,1,20)
print(arr)
#sual 2
arr=np.arange(1,26).reshape(5,5)
sum=np.sum(arr,axis=0)
print(sum)
#sual 3
arr=np.arange(0.01,1.01,0.01).reshape(10,10)
print(arr)
#sual 4
arr=np.dtype([("name",'S20'),('Surname','S20'),('age','i1'),('marks','f4')])
c=np.array([("Behram",'Abbasov',26,85),('Yusif','Abdullayev',22,92),('Maryam','Macidova',19,88),('Vaqif','Hesenzade',20,79)],dtype=arr)
print(c)
'''
#sual 5
arr=np.zeros((10,10))
arr[0,:]=99
arr[-1,:]=99
arr[:,(0,-1)]=99
arr[1,1]=1
arr[-2,-2]=1
arr[2,2:-2]=1
arr[3,-2]=1
arr[-3,2:-2]=1
arr[-4,2]=1
arr[-4,-2]=1
arr[5,2]=1
arr[5,4:6]=1
arr[5,-3]=1
arr[4,2]=1
arr[4,4:6]=1
arr[4,-3]=1
arr[3,2]=1
arr[3,-2]=1
print(arr)
