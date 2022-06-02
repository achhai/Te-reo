# Start of the Te Reo quiz game
# Ask player if they want to start (typing "no" will end the game or type random and type "yes" starts the game)
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
  print ("Correct, on to the next one!")
  score += 1


elif play1 == "1" or play1 == "ciao" or play1 == "2" or play1 == "privet" or play1 == "3" or play1 == "salut":
    print ("Wrong answer")

#Question 2
response2 = input ("Next round? >YES< >NO< ")


if response2 == "yes":
  play2 = input("What is [water] in Te Reo? Option  1: acqua  2: wai  3: vesi  4: auga ")

elif response2 == "no":
  input ("Bye")
  
if play2 == "2" or play2 == "wai":
  print ("Correct, on to the next one!")
  score += 1

elif play2 == "1" or play2 == "acqua" or play2 == "3" or play2 == "vesi" or play2 == "4" or play2 == "auga":
    print ("Wrong answer")

#Question 3
response3 = input ("Next round? >YES< >NO< ")  


if response3 == "yes":
  play3 = input("What is [pig] in Te Reo? Option  1: porco 2: beraz  3: poaka  4: cūka ")

elif response3 == "no":
  input ("Bye")

if play3 == "3" or play3 == "poaka":
  print ("Correct, on to the next one!")
  score += 1

elif play3 == "1" or play3 == "porco" or play3 == "2" or play3 == "beraz" or play3 == "4" or play3 == "cūka":
    print ("Wrong answer")

#Question 4
response4 = input ("Next round? >YES< >NO< ")

if response4 == "yes":
  play4 = input("What is [sky] in Te Reo? Option  1: cer  2: rangi  3: asûman  4: leholimo ")

elif response4 == "no":
  input ("Bye")

if play4 == "2" or play4 == "rangi":
  print ("Correct, on to the next one!")
  score += 1

elif play4 == "1" or play4 == "cer" or play4 == "3" or play4 == "asûman" or play4 == "4" or play4 == "leholimo":
    print ("Wrong answer")

#Question 5
response5 = input ("Next round? >YES< >NO< ")

if response5 == "yes":
  play5 = input("What is [tree] in Te Reo? Option  1: muti  2: fa  3: rakau  4: arbo ")

elif response5 == "no":
  input ("Bye")

if play5 == "3" or play5 == "rakau":
  print ("Correct, on to the next one!")
  score += 1
  
elif play5 == "1" or play5 == "muti" or play5 == "2" or play5 == "fa" or play5 == "4" or play5 == "arbo":
    print ("Wrong answer")

#Question 6
response6 = input ("Next round? >YES< >NO< ")
  
if response6 == "yes":
  play6 = input("What is [man] in Te Reo? Option  1: vir  2: olona  3: muž  4: tangata ")

elif response6 == "no":
  input ("Bye")
  
if play6 == "4" or play6 == "tangata":
  print ("Correct, on to the next one!")
  score += 1

elif play6 == "1" or play6 == "vir" or play6 == "2" or play6 == "olona" or play6 == "4" or play6 == "muž":
    print ("Wrong answer")

