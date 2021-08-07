'''
UNIVERSIDAD DEL VALLE DE GUATEMALA
Criptografía y Cifrado de la Información
Sección 10

Walter Danilo Saldaña Salguero 19897
Jose Abraham Gutierrez Corado 19111
Javier Alejandro Cotto Argueta 19324

LABORATORIO #3
'''

import random
from random import seed
from random import randint

def LCG(a, b, N, k, t):
    cadena = ''
    x0 = random.randrange(0,N)
    for i in range(t):
        x1 = (x0 * a + b) % N
        xb = str(bin(x1))[2:]
        if len(xb) > k:
            cadena += xb[:k]
        elif len(xb) < k:
            cadena += ('0'*(k-len(xb))) + xb
        else:
            cadena += xb
        x0 = x1
    return cadena

def wichmanHill(k ,t):
    s1 = randint(1, 300000)
    s2 = randint(1, 300000)
    s3 = randint(1, 300000)
    
    for i in range(t):
        s1 = (171 * s1) % 30269
        s2 = (172 * s2) % 30307
        s3 = (170 * s3) % 30323

        v = (s1/30269 + s2/30307 + s3/30323) % 1
    
    

    return 

    #n longitud de cadena de feedback
    #taps lista con posiciones
    #seed x0 de longitud n
    #iteraciones burnin phase
def LFSR(n, taps, iteraciones):
    seed = ""
    bit = ""
    cont = 0
    for i in range(n):
        x = randomNumber():

        seed += str(x)

    while (cont != iteraciones):
        bit = (seed ^ )

    return 

def randomNumber():
    num = randint(0, 1)
    return num

print(LCG(2,3,5,8,10))