# dictionaries
#method_1
mydict21 = {"name1" : "sibonelo", "age1" : 25, "city1" : "capetown"}
print(mydict21)
#method_2
mydict2 = dict(name="sibonelo", age=27, city="capetown")
print(mydict2)

'''value = mydict21("name")
print(value)'''
#add key with value on dictionary

mydict2["surname"] = "mhlongo"
print(mydict2)

#delete
mydict2.pop("age")
print(mydict2)

#exceptional statement

try:
    print(mydict21["city"])
except:
    print('KeyError')

'''for key, value in mydict21.items:
    print(key, value)'''

#sets
# no duplicates , mutable

myset= {1,2,3,1,3}
print(myset)

 #union and intersections

odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}
u =odds.union(evens)
print(u)

v = odds.intersection(primes) # only returns all numbers but not the ones in both
print(v)

h= evens.symmetric_difference(primes)
print(h)