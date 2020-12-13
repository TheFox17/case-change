def myfunc1(*args):
    result=''
    for i in range(0,len(args[0])):
        if i%2==0:
            result+=args[0][i].upper()
        else:
            result+=args[0][i].lower()
    print(result)
msg = input("Write whatever you want here: ")
myfunc1(msg)