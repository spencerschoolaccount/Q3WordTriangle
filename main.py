word = input("What word do you want to use for the word triangle? \n")
print("")
for i in range(1,len(word)+1):
  for o in range(0,i):
    print(str(word[o]), end="")
  print("")