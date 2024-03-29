#collections
from collections import Counter
n = "ddddhjjjjknnnnkk"
my_counter = Counter(n)
print(my_counter.values()) 
print(my_counter.most_common())
print(list(my_counter.elements()))

from collections import namedtuple
point = namedtuple("point","x,y,z")
pt = point(3,6,9)
print(pt)
print(pt.x ,pt.y , pt.z)

from collections import OrderedDict
Ordered_Dict = OrderedDict()
Ordered_Dict["a"]=2
Ordered_Dict["b"]=4
Ordered_Dict["c"]=3
Ordered_Dict["h"]=7
print(Ordered_Dict)

from collections import defaultdict
d = defaultdict(int)  # returns default integer if printed key isnot available
                      # NEVER returns error
d["a"]=2
d["c"]=3
print(d["b"])

from collections import deque
dec = deque()
dec.append(2)
dec.append(5)
dec.append(7)
print(dec)

# itertools
from itertools import product
a = [1,2]
e = [6,2]
prod = product(a,e, repeat=2)
print(list(prod))

from itertools import permutations
p = [1,4,6,8]
perm = permutations(p, 2)
print(list(perm))

from itertools import combinations, combinations_with_replacement
# make all possible combination within specified length 
c = [1,3,5,6,7]
comb = combinations(c,2)
print(list(comb))
comb_wr = combinations_with_replacement(c,2)
print(list(comb_wr))

from itertools import accumulate
import operator
ac = [2,4,6,8,9]
accu2 = accumulate(ac , func=operator.mod)
accu = accumulate(ac)
print(ac)
print(list(accu))
print(list(accu2))

from itertools import groupby
def smaller_than_7(x):
    return x<7
gb = [2,4,6,8,9]
gb_obj = groupby(gb, key=smaller_than_7)
for key, value in gb_obj:
    print(key,list(value))

gb_obj = groupby(gb, key= lambda x: x<7) # lambda as fuction 
for key, value in gb_obj:
    print(key,list(value))

persons = [{"name":"sibo","age":25},{"name":"simo","age":25},
           {"name":"noh","age":30},{"name":"lwazi","age":30}]
per_obj = groupby(persons,key=lambda x:x["age"])
for key, value in per_obj:
    print(key,list(value))

#infinite operators are COUNT,CYCLE AND REPEAT

# LAMBDA FUNCTION  (lambda arguments:expresion)

add10 = lambda x: x+10
print(add10(4))
multi = lambda x,y: x*y
print(multi(3,4))

pionts2d= [(1,2),(4,7),(7,1),(3,5)]
points2d_sorted = sorted(pionts2d, key=lambda x: x[0]+ x[1])
print(points2d_sorted) c

