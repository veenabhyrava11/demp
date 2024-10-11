print("hello")
print("veena")

def printHello(*args):
    for arg in args:
        print(arg)

printHello(100,"vena",345)