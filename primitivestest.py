import secrets
import random
from primePy import primes as p

def PRG1(_in):
    #32-bit PRG
    random.seed(_in)
    return len(str(_in))**32-random.randint(0,len(str(_in))**32)

def PRG2(_in):
    #n->2n PRG
    _bin=bin(_in)[2:]
    _blen=len(str(_bin))*2
    b=format(_in, f"{_blen}b")
    random.seed(b)
    return format(random.getrandbits(_blen), f"{_blen}b")

def GetRandPrime():
    pList = p.between(10000,100000)
    return pList[random.randint(0,len(pList))]

def PRF1(k, _in):
    return (k%GetRandPrime())^_in
    

if __name__=="__main__":
    k = random.getrandbits(32)
    print(k)
    print(PRG2(420))
    print(PRF1(k,420))
