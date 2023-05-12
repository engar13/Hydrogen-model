# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:10:34 2023

@author: Enric Garriga
"""

import matplotlib.pyplot as plt
import numpy as np

#Importem aquestes llibreries per poder fer plots en 2d. Yay!!!

d=20
res=2000
z, x = np.meshgrid(np.linspace(-d, d, res), np.linspace(-d, d, res))
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

r=np.sqrt(x**2 + z**2)

Y10=3/(4*np.pi)*(z/r)**2
R41=25/(16**2 * 15)*1/a**3*(r/a)**2*(1-r/(4*a)+r**2/(80*a**2))**2*np.exp(-r/(2.5*a))

Psi410=R41*Y10

Psi_min, Psi_max = Psi410.min(), Psi410.max()

fig, ax=plt.subplots()
plt.pcolormesh(x, z, Psi410, cmap='seismic', vmin=0, vmax=Psi_max)
plt.colorbar()
ax.set_title('Hydrogen (4,1,0)')
plt.axis([x.min(), x.max(), z.min(), z.max()])
plt.gca().set_aspect('equal')
plt.show()

total=0
middle = int(res/2)
for i in range(middle,res-1):
        total+=(R41[i,middle])*(x[i,0]**2)

print(total*2*d/res)