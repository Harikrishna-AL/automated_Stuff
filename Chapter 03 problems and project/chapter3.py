import sys
try:
    x = int(input())

except:
    sys.exit(

    )
def collaz(num):
    while num>1:
        if (num%2 == 0):
            num = num//2
            print(num)
        else:
            num = (num*3) + 1
            print(num)


collaz(x)