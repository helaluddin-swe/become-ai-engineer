def wordCounter(text):
  words=text.split()

  return len(words)

inputT=input("Enter text: ")
print("Total word of sentense:",wordCounter(inputT))