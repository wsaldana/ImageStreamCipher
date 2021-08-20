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
    return [int(i) for i in cadena], cadena

def wichmanHill(k ,t):
    s1 = randint(1, 30000)
    s2 = randint(1, 30000)
    s3 = randint(1, 30000)
    cadena = ''
    for i in range(t):
        s1 = (171 * s1) % 30269
        s2 = (172 * s2) % 30307
        s3 = (170 * s3) % 30323
        v = round((s1/30269 + s2/30307 + s3/30323) % 1)
        
        xb = str(bin(v))[2:]
        if len(xb) > k:
            cadena += xb[:k]
        elif len(xb) < k:
            cadena += ('0'*(k-len(xb))) + xb
        else:
            cadena += xb
    return cadena

    #n longitud de cadena de feedback
    #taps lista con posiciones
    #seed x0 de longitud n
    #iteraciones burnin phase
def LFSR(seed, n, taps, iteraciones):
    #seed = ""
    bit = ""
    taps = sorted(taps, reverse = True)
    cont = 0
    r = 0
    
    while (cont != iteraciones):
        x = int(seed[0])
        for i in taps[1:]:
            x = x ^ int(seed[i])
            
        seed = str(x) + seed
        cont += 1
        
    return [int(i) for i in seed], seed

def randomNumber():
    num = randint(0, 1)
    return num