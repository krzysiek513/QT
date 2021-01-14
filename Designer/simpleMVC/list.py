from model import *



list = []

list.append(Student('fsd', 'dsfa', 'dsaf'))
print(type(list))
for c in list:
    print(c.getNick())

print(list[0].getName())