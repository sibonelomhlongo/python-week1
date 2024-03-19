#converting string to list
mystring = "how are you doing today"
mylist = list(mystring) # each letter as item in list including space 
print(mylist)
mylist1 = mystring.split() # each word become item in list
print(mylist1)
mylist2 = ''.join(mylist1) 
print(mylist2)

var = "SIBONELO"
sentence = "how are you doing today %s" % var
print(sentence)
sentence2 = "sibonelo %s" % mystring
print(sentence2)
var2 = 4.9777732
sentence3 = "sibonelo {} {}".format(mystring,var2)
sentence4 = f"sibonelo {mystring} {var2}"
print(sentence4)

# collections

from collections import Counter  # counter

n = "wwwggjkggbjju"
mycounter = Counter(n)
print(mycounter) # return dictionary
print(list(mycounter.elements()))

from collections import namedtuple # namedtuple

point = namedtuple("point", "x,y,z")
pt = point(1,-3,5)
print(pt)
print(pt.x , pt.y , pt.z)

from collections import OrderedDict # ordereddict

