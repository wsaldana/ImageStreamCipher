'''
UNIVERSIDAD DEL VALLE DE GUATEMALA
Criptografía y Cifrado de la Información
Sección 10

Walter Danilo Saldaña Salguero 19897
Jose Abraham Gutierrez Corado 19111
Javier Alejandro Cotto Argueta 19324

LABORATORIO #3
'''

import numpy as np
import matplotlib.pyplot as plt
import re
from skimage import data, io   # estas librerías solo se usan para
from PIL import Image               # llamar al ejemplo de cameraman.png
import streamCipher as sc

def xor(a, b):
    m = len(a)
    n = len(b)
    maxx = max(m,n)
    if (m < n):
        a = a + (n-m)*'0'
    if (n < m):
        b = b + (m-n)*'0'
        
    c = ''
    for i in range(0, maxx):
        c = c + str(int(a[i]) ^ int(b[i]))
    return c

def img2bits(I):
    ''' Convierte una imagen en escala de grises a cadena de bits.
        Input:  I = imagen, como numpy array de shape (m,n).
        Output: s = string de bits, donde se concatenan cada pixel de I.
    '''
    m, n = I.shape
    s = ''
    for i in range(0, m):
        for j in range(0, n):
            s = s + '{0:08b}'.format(I[i,j])
    return s


def bits2img(x, shape):
    ''' Convierte una cadena de bits a una imagen en escala de grises.
        Input:  s = string de bits, donde se concatenan cada pixel de I.
                shape = dimensiones (m,n) de la imagen de salida I.
        Output: I = imagen, como numpy array de shape (m,n).
    '''

    m, n = shape
    I = np.zeros(m*n).astype(np.uint8)
    bts = re.findall('........', x)
    for i in range(0, len(bts)-1):
        I[i] = int(bts[i], 2)
    I = I.reshape(m,n)
    return I



I = io.imread('mono.png', as_gray = True)

J = Image.fromarray(I)
J = J.resize((J.size[0]//2, J.size[1]//2), Image.LANCZOS)
I = np.array(J) * 255
I = I.astype(float).astype(int)

        
plt.figure()
plt.imshow(I, cmap='gray')
plt.show()

s0 = img2bits(I)

#Stream 1
s1 = sc.LCG(3,5,254,8,int(len(s0)/8))
r1 = xor(s0, s1[0])

#Stream 2
s2 = sc.LFSR(r1, len(r1), [1, 2, 3, 4, 5, 6, 9, 11, 14, 15], 10)
r2 = xor(r1, s2[0])

#Stream 3
s3 = sc.wichmanHill(8,int(len(s0)/8))
r3 = xor(r2, s3[0])

rf = xor(s0, r3)

I1 = bits2img(r1, I.shape)
I2 = bits2img(r2, I.shape)
I3 = bits2img(r3, I.shape)
I4 = bits2img(rf, I.shape)

plt.figure(figsize=(15,8))

#Graficar primera transformación (Con algoritmo LCG)
plt.subplot(2,2,1)
plt.imshow(I1, cmap='gray')

#Graficar segunda transformación (Con algoritmo LFSR)
plt.subplot(2,2,2)
plt.imshow(I2, cmap='gray')

#Graficar tercera transformación (Con algoritmo wichmanHill)
plt.subplot(2,2,3)
plt.imshow(I3, cmap='gray')

#Graficar cuarta transformación (xor de la transformación resultante con la imagen original)
plt.subplot(2,2,4)
plt.imshow(I4, cmap='gray')

plt.show()