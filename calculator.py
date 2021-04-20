while True:
    a=int(input('enter a number'))
    b=int(input('enter a number'))
    i=(input('enter +\-\*\/\%'))
    if i=='+':
        print(a+b)
    elif i=='-':
        print(a-b)
    elif i=='*':
        print(a*b)
    elif i=='/':
        print(a/b)
    elif i=='%':
        print(a%b)
    n=input("enter y to continue and q to exit ")
    if n=='y':
        continue
    elif n=='q':
        break