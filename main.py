def primos(n):
    listaPrimos=[]
    for x in range(2,n):
        val=True
        for y in range(2,x):
            if x%y == 0:
                val=False
                break
        if val:
            listaPrimos.append(x)
    return listaPrimos
n=30
print(primos(n))