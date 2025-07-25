

def decorator(function):
    def i ():
        a=function()
        return a*3
    return i
def decorator1(function):
    def i ():
        a=function()
        return a+5
    return i
@decorator
@decorator1
def number():
    return 9
print(number())