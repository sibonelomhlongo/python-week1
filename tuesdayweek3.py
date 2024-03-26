#JAVA SCRIPT OBJECT NOTATION (json)
# decorators
def startend_decorator(func):
    def wrapper():
        print("start")
        func() 
        print("end")
    return wrapper
def printname():
    print("alex")
printname = startend_decorator(printname) 
printname()

class employee:
    def __init__(x,first,last,pay) -> None:
        x.first = first
        x.last = last
        x.pay =pay
        x.email = first+"."+last+"@company.com"
     


emp1= employee("sibo","mhlongo",12000)
emp2=employee('tshidi','pholo',100000)
print(emp1.email)
print("{} {}".format(emp2.first,emp2.last))
print("{} {}".format(emp1.first,emp1.last))
#print(emp2)
class worker(employee):
    def __init__(x, first, last, pay) -> None:
        super().__init__(first, last, pay)
emp9= worker("sibo","mhlongo",12000)
print("{} {}".format(emp9.first,emp9.last))