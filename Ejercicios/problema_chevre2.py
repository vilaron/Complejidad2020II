a = input()

cnt = []


def d(ar , ini ,fin):
    if ini == fin:
        if(ar[ini] == " " or ar[ini] == "," or ar[ini] == '.'):
            cnt.append(1)
            return True
        else:
            return False
    else:
        pos = (ini + fin)//2 
        d(ar , ini  , pos)
        d(ar , pos + 1 , fin)
        return False 
        

d(a , 0 , len(a)  - 1 )

print(len(cnt) + 1)