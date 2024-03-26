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
    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
        self.pay =pay
        self.email = first+"."+last+"@company.com"
    pass
pass
emp1= employee("sibo","mhlongo",12000)
print(emp1.email)
print("{} {}".format(emp1.first,emp1.last))