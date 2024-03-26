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
