import random

if __name__ == '__main__':
    x = random.randint(0,1000)
    xStr = str(x)
    xStr = xStr[len(xStr)-1:len(xStr)]
    print(x)
    print(xStr)