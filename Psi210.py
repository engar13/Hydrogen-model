# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:53:56 2023

@author: Enric Garriga
"""

import matplotlib.pyplot as plt
import numpy as np

#Importem aquestes llibreries per poder fer plots en 2d. Yay!!!

d=4
res=1500
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

"CAS (n,l,m) = (2,1,0)"
n, l, m = 2, 1, 0

r=np.sqrt(x**2 + z**2) #We will work on the XY plane so z=0

#Aquest cop calcularem directament els QUADRATS de Y i R perquè és el que ens
#interessa (Psi^2) i així estalviem càlculs

#A més, com som al pla XZ (y=0) tenim que cos theta esdevé z/r. Per tant no 
#cal calcuñar theta
Y10=3/(4*np.pi)*(z/r)**2
R21=(1/24)*1/a**3*(r/a)**2*np.exp(-r/a)

Psi210=R21*Y10

Psi210 = Psi210[:-1, :-1]   #Reduim en 1 la llista de Psi perquè hi ha menys 
                            #caselles que encreuaments.
                            

Y00=1/(2*np.sqrt(np.pi))
R10=(2/np.sqrt(a**3))*np.exp(-r/a)

Psi100=R10**2*Y00**2

Psi100 = Psi100[:-1, :-1]   #Reduim en 1 la llista de Psi perquè hi ha menys 
                            #caselles que encreuaments.
                            
                            
#Ara ja anem fins i tot a per la Psi420 vinga!!
#Un cop més, la fem directament quadrada

#z_min, z_max = z.min(), np.abs(z).max()

Psi_min, Psi_max = Psi210.min(), Psi210.max()

fig, ax = plt.subplots()


plt.pcolormesh(x, z, Psi100, cmap='Reds', vmin=0)
plt.colorbar()
#plt.pcolormesh(x, z, Psi210, cmap='Blues', vmin=0, vmax=Psi_max,alpha=0.65)

ax.set_title('Hydrogen (2,1,0)')
# set the limits of the plot to the limits of the data
plt.axis([x.min(), x.max(), z.min(), z.max()])
#fig.colorbar(mappable=None, ax=ax)
plt.gca().set_aspect('equal')
plt.show()

total=0
middle = int(res/2)
for i in range(middle,res-1):
        total+=(R21[i,middle])*(x[i,0]**2)

print(total*2*d/res)
