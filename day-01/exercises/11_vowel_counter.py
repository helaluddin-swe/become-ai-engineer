def vowelCounter(text):
  vowels="aeiouAEIOU"
  count=0
  for char in text:
       if char in vowels:
        count+=1
  return count

inputText=input("Enter the text ")
totalVowel=vowelCounter(inputText)

print("The vowel of text is ",totalVowel)