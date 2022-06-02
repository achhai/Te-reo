# Ask player if they wanna start the game
response1 = input("Hello, welcome to Te Reo Quiz game! would you like to start? ")
score = 0

# Every correct question the player answer gives 1 score
# Question 1
if response1 == "yes":
  play1 = input("What is [hello] in Te Reo? Option  1: ciao  2: privet  3: salut  4: kia ora ")

elif response1 == "no":
  input ("Bye")

else:
    other = input("Bye")

if play1 == "4" or play1 == "kia ora":
  print ("Correct")
  score += 1


elif play1 == "1" or play1 == "ciao" or play1 == "2" or play1 == "privet" or play1 == "3" or play1 == "salut":
    print ("Wrong answer")

