# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:37:09 2023

@author: Enric Garriga
"""

import matplotlib.pyplot as plt
import numpy as np

#Importem aquestes llibreries per poder fer plots en 2d. Yay!!!

d=2
res=1000
y, x = np.meshgrid(np.linspace(-d, d, res), np.linspace(-d, d, res))
#   x i y son dues matrius de mida 100x100. Contenen les coordenades (x i y 
#   respectivament) dels encreuaments de les cel·les del nostre dibuix. Per exemple,
#   si volguessim fer un dibuix quadrat 3x3 (9 cel·les => 4x4=12 encreuaments),
#   aleshores tindriem, per ex:
#   x=[ [0,0,0,0] , [1,1,1,1] , [2,2,2,2] , [3,3,3,3] ]
#   y=[ [0,1,2,3] , [0,1,2,3] , [0,1,2,3] , [0,1,2,3] ]
#   i els encreuaments es trobarien als punts (0,0) , (0,1) , etc.
#   Mentres deixem fixa la x, fem pujar la y i quan acabem incrementem +1 el valor
#   de x i tornem a recorrer tot el rang de y.

#A continuació definim la nostra variable en funció de x i y. En el meu cas 
#vull dibuixar l'atom d'hidrogen per tant la nostra funció és Psi_nlm=R_nl*Y_lm
#per tant anem a calcular Rnl i Ylm per separat
#Per saber les seves expressions... MIRAR TAULES!! (O passar una tarda sencera
#derivant una o dues).

a=5.29*10**(-1) #Bohr Radius

"CAS (n,l,m) = (1,0,0)"
n, l, m = 1, 0, 0

r=np.sqrt(x**2 + y**2) #We will work on the XY plane so z=0

Y00=1/(2*np.sqrt(np.pi))
R10=(2/np.sqrt(a**3))*np.exp(-r/a)

Psi100=R10*Y00

Psi100 = Psi100[:-1, :-1]   #Reduim en 1 la llista de Psi perquè hi ha menys 
                            #caselles que encreuaments.

z=Psi100**2
z_min, z_max = z.min(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, cmap='hot', vmin=z_min, vmax=z_max)
ax.set_title('Hydrogen (1,0,0)')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
plt.gca().set_aspect('equal')
fig.colorbar(c, ax=ax)


total=0
middle = int(res/2)
for i in range(middle,res-1):
        total+=(R10[i,middle]**2)*(x[i,0]**2)

print(total*2*d/res)
