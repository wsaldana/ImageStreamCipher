from random import *
    #n longitud de cadena de feedback
    #taps lista con posiciones
    #seed x0 de longitud n
    #iteraciones burnin phase
def LFSR(n, taps, iteraciones):
    seed = ""
    bit = ""
    taps = sorted(taps, reverse = True)
    cont = 0
    r = 0
    
    for i in range(n):
        x = randomNumber()

        seed += str(x)
      
    print("Without LFSR: " + seed)
    
    while (cont != iteraciones):
        x = int(seed[0])
        for i in taps[1:]:
            x = x ^ int(seed[i])
            
        seed = str(x) + seed
        cont += 1
    
    print("Whit LFSR: " + seed)
    
def randomNumber():
    num = randint(0, 1)
    return num   

LFSR(8, [3, 1, 5], 3)