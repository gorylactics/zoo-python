import random
def nivelSalud():
    numMin = 0 
    numMax = 100
    nivelS = random.random() *  (numMax - numMin) +  numMin
    return nivelS

def nivelFelicidad():
    numMin = 0 
    numMax = 100
    nivelF = random.random() *  (numMax - numMin) +  numMin
    return nivelF
