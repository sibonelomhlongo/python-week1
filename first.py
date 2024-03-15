'''mylist=['sibonelo', 'nhlaka','mhlongo', 'ncube']
print(mylist)
mylist.append("orange")
print(mylist)
n= mylist[-1]
print(n)
username = input("Enter username:")
if username in mylist:
    print('True')
else:
    print ('no')
print(len(mylist))'''
def add(*numbers):
    total =0
    for n in numbers:
        total += n
    return total
print(add(3,5,7,7))