x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
for l in 'Jhon':
   if l == 'o':
      pass
   print(l, end=", ")
   var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)
for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break
str = 'Mysalary 7000';
print(str.isalnum())
str1 = "my isname isisis jameis isis bond";
sub = "is";
print(str1.count(sub, 26))
myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(stringList[1] == myString)
print(stringList[1] is myString)
str1 = "PYnative"
print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
j="welcome to the beautiful world of python"
print(j.title())