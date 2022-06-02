# Start of the Te Reo quiz game
# Ask player if they want to start (typing "no" will end the game or type random and type "yes" starts the game)
response1 = input("Hello, welcome to Te Reo Quiz game! would you like to start? \n")
score = 0

# Every correct question the player answer gives 1 score
# Question 1
if response1 == "yes":
  play1 = input("\n What is [hello] in Te Reo? Option \n 1: >ciao< \n 2: >privet< \n 3: >salut< \n 4: >kia ora< \n")
  
elif response1 == "no":
  input ("Bye have a great day!")

else:
    other = input("Bye have a great day!")

if play1 == "4" or play1 == "kia ora":
  print ("Correct, on to the next one!")
  score += 1


elif play1 == "1" or play1 == "ciao" or play1 == "2" or play1 == "privet" or play1 == "3" or play1 == "salut":
    print ("Wrong answer nice try")

#Question 2
response2 = input ("Next round? >YES< >NO< \n")


if response2 == "yes":
  play2 = input("\n What is [water] in Te Reo? Option \n 1: >acqua< \n 2: >wai< \n 3: >vesi< \n 4: >auga< \n")

elif response2 == "no":
  input ("Bye have a great day!")
  
if play2 == "2" or play2 == "wai":
  print ("Correct, on to the next one!")
  score += 1

elif play2 == "1" or play2 == "acqua" or play2 == "3" or play2 == "vesi" or play2 == "4" or play2 == "auga":
    print ("Wrong answer nice try")

#Question 3
response3 = input ("Next round? >YES< >NO< \n")


if response3 == "yes":
  play3 = input("\n What is [pig] in Te Reo? Option \n 1: >porco< \n 2: >beraz< \n 3: >poaka< \n 4: >cūka< \n")

elif response3 == "no":
  input ("Bye have a great day!")

if play3 == "3" or play3 == "poaka":
  print ("Correct, on to the next one!")
  score += 1

elif play3 == "1" or play3 == "porco" or play3 == "2" or play3 == "beraz" or play3 == "4" or play3 == "cūka":
    print ("Wrong answer nice try")

#Question 4
response4 = input ("Next round? >YES< >NO< \n")

if response4 == "yes":
  play4 = input("\n What is [sky] in Te Reo? Option \n 1: >cer< \n 2: >rangi< \n 3: >asûman< \n 4: >leholimo< \n")

elif response4 == "no":
  input ("Bye have a great day!")

if play4 == "2" or play4 == "rangi":
  print ("Correct, on to the next one!")
  score += 1

elif play4 == "1" or play4 == "cer" or play4 == "3" or play4 == "asûman" or play4 == "4" or play4 == "leholimo":
    print ("Wrong answer nice try")

#Question 5
response5 = input ("Next round? >YES< >NO< \n")

if response5 == "yes":
  play5 = input("\n What is [tree] in Te Reo? Option \n 1: >muti< \n 2: >fa< \n 3: >rakau< \n 4: >arbo< \n")

elif response5 == "no":
  input ("Bye have a great day!")

if play5 == "3" or play5 == "rakau":
  print ("Correct, on to the next one!")
  score += 1
  
elif play5 == "1" or play5 == "muti" or play5 == "2" or play5 == "fa" or play5 == "4" or play5 == "arbo":
    print ("Wrong answer nice try")

#Question 6
response6 = input ("Next round? >YES< >NO< \n")
  
if response6 == "yes":
  play6 = input("\n What is [man] in Te Reo? Option \n 1: >vir< \n 2: >olona< \n 3: >muž< \n 4: >tangata< \n")

elif response6 == "no":
  input ("Bye have a great day!")
  
if play6 == "4" or play6 == "tangata":
  print ("Correct, on to the next one!")
  score += 1

elif play6 == "1" or play6 == "vir" or play6 == "2" or play6 == "olona" or play6 == "4" or play6 == "muž":
    print ("Wrong answer nice try")

#Question 7
response7 = input ("Next round? >YES< >NO< \n")
  
if response7 == "yes":
  play7 = input("\n What is [woman] in Te Reo? Option \n 1: >vehivavy< \n 2: >wahine< \n 3: >muller< \n 4: >vrouw< \n")

elif response7 == "no":
  input ("Bye have a great day!")
  
if play7 == "2" or play7 == "wahine":
  print ("Correct, on to the next one!")
  score += 1

elif play7 == "1" or play7 == "vehivavy" or play7 == "3" or play7 == "muller" or play7 == "4" or play7 == "vrouw":
    print ("Wrong answer nice try")

#Question 8
response8 = input ("Next round? >YES< >NO< \n")

if response8 == "yes":
  play8 = input("\n What is [food] in Te Reo? Option \n 1: >cibus< \n 2: >jídlo< \n 3: >храна< \n 4: >kai< \n")

elif response8 == "no":
  input ("Bye have a great day!")
  
if play8 == "4" or play8 == "kai":
  print ("Correct, on to the next one!")
  score += 1

elif play8 == "1" or play8 == "cibus" or play8 == "2" or play8 == "jídlo" or play8 == "3" or play8 == "храна":
    print ("Wrong answer nice try")

#Question 9
response9 = input ("Next round? >YES< >NO< \n")

if response9 == "yes":
  play9 = input("\n What is [drink] in Te Reo? Option \n 1: >inu< \n 2: >drénken< \n 3: >bibere< \n 4: >İçmek< \n")

elif response9 == "no":
  input ("Bye have a great day!")
  
if play9 == "1" or play9 == "inu":
  print ("Correct, on to the next one!")
  score += 1

elif play9 == "2" or play9 == "drénken" or play9 == "3" or play9 == "bibere" or play9 == "4" or play9 == "İçmek":
    print ("Wrong answer nice try")

#Question 10
response10 = input ("Next round? >YES< >NO< \n")

if response10 == "yes":
  play10 = input("\n What is [rock] in Te Reo? Option \n 1: >toka< \n 2: >Rokas< \n 3: >stijena< \n 4: >petra< \n")

elif response10 == "no":
  input ("Bye have a great day!")
  
if play10 == "1" or play10 == "toka":
  print ("Correct, on to the next one!")
  score += 1

elif play10 == "2" or play10 == "Rokas" or play10 == "3" or play10 == "stijena" or play10 == "4" or play10 == "petra":
    print ("Wrong answer nice try")

#Question 11
response11 = input ("Next round? >YES< >NO< \n")

if response11 == "yes":
  play11 = input("\n What is [plant] in Te Reo? Option \n 1: >augu< \n 2: >bitki< \n 3: >taim< \n 4: >tipu< \n")

elif response11 == "no":
  input ("Bye have a great day!")
  
if play11 == "4" or play11 == "tipu":
  print ("Correct, on to the next one!")
  score += 1

elif play11 == "1" or play11 == "augu" or play11 == "2" or play11 == "bitki" or play11 == "3" or play11 == "taim":
    print ("Wrong answer nice try")

#Question 12
response12 = input ("Next round? >YES< >NO< \n")

if response12 == "yes":
  play12 = input("\n What is [human] in Te Reo? Option \n 1: >člověk< \n 2: >cilvēks< \n 3: >tangata< \n 4: >bniedem< \n")

elif response12 == "no":
  input ("Bye have a great day!")

if play12 == "3" or play12 == "tangata":
  print ("Correct, on to the next one!")
  score += 1

elif play12 == "1" or play12 == "člověk" or play12 == "2" or play12 == "cilvēks" or play12 == "4" or play12 == "bniedem":
    print ("Wrong answer nice try")

#Question 13
response13 = input ("Next round? >YES< >NO< \n")

if response13 == "yes":
  play13 = input("\n What is [mountin] in Te Reo? Option \n 1: >fjall< \n 2: >maunga< \n 3: >montagna< \n 4: >beinn< \n")

elif response13 == "no":
  input ("Bye have a great day!")

if play13 == "2" or play13 == "maunga":
  print ("Correct, on to the next one!")
  score += 1

elif play13 == "1" or play13 == "fjall" or play13 == "3" or play13 == "montagna" or play13 == "4" or play13 == "beinn":
    print ("Wrong answer nice try")

#Question 14
response14 = input ("Next round? >YES< >NO< \n")

if response14 == "yes":
  play14 = input("\n What is [sick] in Te Reo? Option \n 1: >māuiui< \n 2: >na-arịa ọrịa< \n 3: >kurwara< \n 4: >ziek< \n")

elif response14 == "no":
  input ("Bye have a great day!")

if play14 == "1" or play14 == "māuiui":
  print ("Correct, on to the next one!")
  score += 1

elif play14 == "2" or play14 == "na-arịa ọrịa" or play14 == "3" or play14 == "kurwara" or play14 == "4" or play14 == "ziek":
    print ("Wrong answer nice try")

#Question 15
response15 = input ("Next round? >YES< >NO< \n")

if response15 == "yes":
  play15 = input("\n What is [adult] in Te Reo? Option \n 1: >olon-dehibe< \n 2: >adulte< \n 3: >pakeke< \n 4: >nasa hustong gulang< \n")

elif response15 == "no":
  input ("Bye have a great day!")

if play15 == "3" or play15 == "pakeke":
  print ("Correct, on to the next one!")
  score += 1

elif play15 == "1" or play15 == "olon-dehibe" or play15 == "2" or play15 == "adulte" or play15 == "4" or play15 == "nasa hustong gulang":
    print ("Wrong answer nice try")

#Question 16
response16 = input ("Next round? >YES< >NO< \n")

if response16 == "yes":
  play16 = input("\n What is [study] in Te Reo? Option \n 1: >undersøgelse< \n 2: >ako< \n 3: >studija< \n 4: >estudar< \n")

elif response16 == "no":
  input ("Bye have a great day!")

if play16 == "2" or play16 == "ako":
  print ("Correct, on to the next one!")
  score += 1

elif play16 == "1" or play16 == "undersøgelse" or play16 == "3" or play16 == "studija" or play16 == "4" or play16 == "estudar":
    print ("Wrong answer nice try")

