#To print fibonacci series
def fib(n):
    ser = [0,1]
    for i in range(2,n):
        el = ser[-1] + ser[-2]
        ser.append(el)

    print("the fibonacci sequence is: ", ser)

num = int(input("enter the number of elements: "))
fib(num)