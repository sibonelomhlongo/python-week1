'''x="hello"[0]
print(x)
y = "  hi  "
z=y.upper()
print(z)

s="i am learning python"\
    .capitalize()
print(s)
s1= {1,2,3,4,5,6}
s2 ={6,7,8,9}
print(s1&s2)
print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
def func1():
    x = 50
    return x
func1()
print(type(0xFF))
str1 = ''str''
print(str1)
x = 75
def myfunc():
    global x
    x += 1
    print(x)

myfunc()
print(x)
x = 50
def fun1():
    x = 25
    print(x)
    
fun1()
print(x)
print(type({''}) is set)
print(type([]) is list)
str1 = """Ault'Kelly"""
print(str1)
print(type(range(5)))
a = 4
b = 11
print(a | b)
print(a >> 2)
print(2%6)
x = 7
y = 2
print(x ** y)
print(x // y)
print(-18 // 4)'''
a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)
print(36 / 4)