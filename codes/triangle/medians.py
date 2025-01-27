#Code by GVV Sharma
#September 7, 2023
#released under GNU GPL
#Drawing the medians of a triangle


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/gadepall/github/geometry/codes/CoordGeo')        #path to my scripts
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts

#if using termux
import subprocess
import shlex
#end if

'''
#Triangle sides
a = 6
b = 5
c = 4


#Triangle coordinates
[A,B,C] = tri_vert(a,b,c)
'''
#Triangle vertices
A = np.array([1,-1]).reshape(-1,1)
B = np.array([-4,6]).reshape(-1,1) 
C = np.array([-3,-5]).reshape(-1,1) 

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)



#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

#Labeling the coordinates
#tri_coords = np.vstack((A,B,C,O,I)).T
#np.block([[A1,A2,B1,B2]])
'''
A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)
O = O.reshape(-1,1)
I = I.reshape(-1,1)
'''
tri_coords = np.block([[A,B,C]])
#tri_coords = np.block([[A,B,C,O,I]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
#vert_labels = ['A','B','C','O','I']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('tri_sss.pdf')
plt.savefig('figs/triangle/vector.pdf')
#subprocess.run(shlex.split("termux-open ./figs/tri_sss.pdf"))
#else
# image = mpimg.imread('tri_sss.png')
# plt.imshow(image)
plt.show()

'''
#Plotting the circumcircle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circumcircle$')

#Plotting the circumcircle
plt.plot(x_icirc[0,:],x_icirc[1,:],label='$incircle$')


#Generating the circumcircle
[O,R] = ccircle(A,B,C)
x_circ= circ_gen(O,R)

#Generating the incircle
[I,r] = icircle(A,B,C)
x_icirc= circ_gen(I,r)
'''




