inputNumber1=int(input("Enter first number : "))
inputNumber2=int(input("Enter second number : "))
inputNumber3=int(input("Enter third number : "))

if inputNumber1>inputNumber2 and inputNumber1>inputNumber3:
  print(f"{inputNumber1} is greater than {inputNumber2} and {inputNumber3}")
elif inputNumber2>inputNumber1 and inputNumber2>inputNumber3:
     print(f"{inputNumber2} is greater than {inputNumber1} and {inputNumber3}")
elif inputNumber3>inputNumber1 and inputNumber3>inputNumber2:
    print(f"{inputNumber3} is greater than {inputNumber1} and {inputNumber2}")