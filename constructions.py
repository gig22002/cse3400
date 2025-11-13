import Crypto
from Crypto.Hash import SHA256

def MerkleDamgard(msgs):
    hashList=[]
    i=0
    prev=0
    for msg in msgs:
        hashList.append(SHA256.new(data=bytes(msg+str(i)+str(prev),'utf-8')).hexdigest())
        prev=hashList[i]
        i+=1
    return hashList

if __name__=="__main__":
    print(MerkleDamgard(["hi","hi2"]))
