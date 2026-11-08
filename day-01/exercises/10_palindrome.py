
def isPalindrome(n):
  left=0
  right=len(n)-1
  while left<right:
    if n[left]!=n[right]:
      return False
    left+=1
    right-=1
  return True
inputText=str(input("Enter a string to check palidrome: "))
if(isPalindrome(inputText)==True):
   print("True")
elif isPalindrome(inputText)==False:
    print("False")
  
