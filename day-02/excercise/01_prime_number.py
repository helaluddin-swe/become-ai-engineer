def primeNumber(n):
    if n<=1:
        return False
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            return False
    return True


inputX=int (input("Enter a number :"))
result=primeNumber(inputX)
if result==True:
    print("Prime Number ")
else:
    print("Not a Prime Number")
