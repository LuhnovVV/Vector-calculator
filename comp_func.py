import numpy as np


lst1 = [2,3,-3] 
a = np.array(lst1)

lst2 = [1,2,-4] 
b = np.array(lst2)


lst3 = ['i', 'j','k']
c = np.array(lst3)



def scal(vector1, vector2):
    scal = vector1.dot(vector2) 
    
    #return print("Скалярное произведение двух векторов a*b =",scal)
    return scal




def cross(vector1, vector2):
    
    vec = np.cross(vector1, vector2)
    #print(vec)
    if len(vector1) == 2:
        return vec
    
    a = [0] * len(vector1)

    for i in range(len(vector1)):
        if vec[i] < 0:
            a[i] = "-" + str(int(abs(vec[i])))+c[i] 
        else:
            a[i] = "+" + str(int(vec[i]))+c[i]

    return a[0], a[1], a[2]



def tensor(vector1, vector2):
    a = [[0] * len(vector1) for i in range(len(vector1))]

    A = np.zeros((len(vector1), len(vector1)))
    for i in range(len(vector1)):
        for j in range(len(vector1)):
            A[i,j]= vector1[i]*vector2[j]
            a[i][j] = str(int(A[i,j]))+c[i]+c[j]
            
    #print("Тензорное произведение двух векторов ab =",)
    #for k in range(0, len(a)):
      #  for n in range(0, len(a[k])):
        #    print(a[k][n], end=' ')
        #print()
    return a


#scal(a,b)
#cross(a,b)
#tensor(a,b)
