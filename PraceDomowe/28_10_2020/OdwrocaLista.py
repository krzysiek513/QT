# odwrócona lista
# http://programista-python.pl/operacje-na-listach-w-pythonie/
from audioop import reverse

Lista = [ "pierwsze", "drugie", "trzecie"]
Lista.append("czwarte")
Lista.append("piąte")
print(Lista)
i = 4
while i >= 0:
    print(Lista[i])
    i = i - 1

print(Lista[::-1])

Lista.reverse()
print(Lista)