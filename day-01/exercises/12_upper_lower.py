# text=input("Enter the text to convet upper: ")
# upper=text.upper()
# lower=text.lower()
# capital=text.capitalize()
# print(f"The upper is :{capital}")

def upperAndLower(text):
  result=""
  for char in text:
    if char.isupper():
      result+=char.lower()
    elif char.islower():
       result+=char.upper()
    else:
       result+=char


  return result

text=input("Enter the text to convet upper: ")

print("the ans is : ",upperAndLower(text))