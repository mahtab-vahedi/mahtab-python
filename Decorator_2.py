# def test():
#     return 5

def dec1(func):
    def inner():
        x=func()
        return x*3
    return inner

def dec2(func):
    def inner():
        x=func()
        return x+10
    return inner
@dec1
@dec2
def test():
    return 5
print(test())