# Start of the Te Reo quiz game
# Ask player if they want to start (typing "no" will end the game or type random and type "yes" starts the game)
response1 = input("Hello, welcome to Te Reo Quiz game! would you like to start? \n").lower()
score = 0

# Every correct question the player answer gives 1 score
# Question 1-20
if response1 == "yes":
  play1 = input(" \n Question [1-20] \n What is >hello< in Te Reo? \n Option \n 1: [ciao] \n 2: [privet] \n 3: [salut] \n 4: [kia ora] \n").lower()

elif response1 == "no":
  input ("Bye have a great day!")

else:
    other = input("Bye have a great day!")

if play1 == "4" or play1 == "kia ora":
  print ("Correct, on to the next one!")
  score += 1


elif play1 == "1" or play1 == "ciao" or play1 == "2" or play1 == "privet" or play1 == "3" or play1 == "salut":
    print ("Wrong answer nice try")

#Question 2-20
response2 = input ("Ready for the next round? [YES] [NO] \n").lower()


if response2 == "yes":
  play2 = input("\n Question [2-20] \n What is >water< in Te Reo? \n Option \n 1: [acqua] \n 2: [wai] \n 3: [vesi] \n 4: [auga] \n").lower()

elif response2 == "no":
  input ("Bye have a great day!")
  
if play2 == "2" or play2 == "wai":
  print ("Correct, on to the next one!")
  score += 1

elif play2 == "1" or play2 == "acqua" or play2 == "3" or play2 == "vesi" or play2 == "4" or play2 == "auga":
    print ("Wrong answer nice try")

#Question 3-20
response3 = input ("Ready for the next round? [YES] [NO] \n").lower()


if response3 == "yes":
  play3 = input("\n Question [3-20] \n What is >pig< in Te Reo? \n Option \n 1: [porco] \n 2: [beraz] \n 3: [poaka] \n 4: [cūka] \n").lower()

elif response3 == "no":
  input ("Bye have a great day!")

if play3 == "3" or play3 == "poaka":
  print ("Correct, on to the next one!")
  score += 1

elif play3 == "1" or play3 == "porco" or play3 == "2" or play3 == "beraz" or play3 == "4" or play3 == "cūka":
    print ("Wrong answer nice try")

#Question 4-20
response4 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response4 == "yes":
  play4 = input("\n Question [4-20] \n What is >sky< in Te Reo? \n Option \n 1: [cer] \n 2: [rangi] \n 3: [asûman] \n 4: [leholimo] \n").lower()

elif response4 == "no":
  input ("Bye have a great day!")

if play4 == "2" or play4 == "rangi":
  print ("Correct, on to the next one!")
  score += 1

elif play4 == "1" or play4 == "cer" or play4 == "3" or play4 == "asûman" or play4 == "4" or play4 == "leholimo":
    print ("Wrong answer nice try")

#Question 5-20
response5 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response5 == "yes":
  play5 = input("\n Question [5-20] \n What is >tree< in Te Reo? \n Option \n 1: [muti] \n 2: [fa] \n 3: [rakau] \n 4: [arbo] \n").lower()

elif response5 == "no":
  input ("Bye have a great day!")

if play5 == "3" or play5 == "rakau":
  print ("Correct, on to the next one!")
  score += 1
  
elif play5 == "1" or play5 == "muti" or play5 == "2" or play5 == "fa" or play5 == "4" or play5 == "arbo":
    print ("Wrong answer nice try")

#Question 6-20
response6 = input ("Ready for the next round? [YES] [NO] \n").lower()
  
if response6 == "yes":
  play6 = input("\n Question [6-20] \n What is >man< in Te Reo? \n Option \n 1: [vir] \n 2: [olona] \n 3: [muž] \n 4: [tangata] \n").lower()

elif response6 == "no":
  input ("Bye have a great day!")
  
if play6 == "4" or play6 == "tangata":
  print ("Correct, on to the next one!")
  score += 1

elif play6 == "1" or play6 == "vir" or play6 == "2" or play6 == "olona" or play6 == "4" or play6 == "muž":
    print ("Wrong answer nice try")

#Question 7-20
response7 = input ("Ready for the next round? [YES] [NO] \n").lower()
  
if response7 == "yes":
  play7 = input("\n Question [7-20] \n What is >woman< in Te Reo? \n Option \n 1: [vehivavy] \n 2: [wahine] \n 3: [muller] \n 4: [vrouw] \n").lower()

elif response7 == "no":
  input ("Bye have a great day!")
  
if play7 == "2" or play7 == "wahine":
  print ("Correct, on to the next one!")
  score += 1

elif play7 == "1" or play7 == "vehivavy" or play7 == "3" or play7 == "muller" or play7 == "4" or play7 == "vrouw":
    print ("Wrong answer nice try")

#Question 8-20
response8 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response8 == "yes":
  play8 = input("\n Question [8-20] \n What is >food< in Te Reo? \n Option \n 1: [cibus] \n 2: [jídlo] \n 3: [храна] \n 4: [kai] \n").lower()

elif response8 == "no":
  input ("Bye have a great day!")
  
if play8 == "4" or play8 == "kai":
  print ("Correct, on to the next one!")
  score += 1

elif play8 == "1" or play8 == "cibus" or play8 == "2" or play8 == "jídlo" or play8 == "3" or play8 == "храна":
    print ("Wrong answer nice try")

#Question 9-20
response9 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response9 == "yes":
  play9 = input("\n Question [9-20] \n What is [drink] in Te Reo? \n Option \n 1: [inu] \n 2: [drénken] \n 3: [bibere] \n 4: [İçmek] \n").lower()

elif response9 == "no":
  input ("Bye have a great day!")
  
if play9 == "1" or play9 == "inu":
  print ("Correct, on to the next one!")
  score += 1

elif play9 == "2" or play9 == "drénken" or play9 == "3" or play9 == "bibere" or play9 == "4" or play9 == "İçmek":
    print ("Wrong answer nice try")

#Question 10-20
response10 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response10 == "yes":
  play10 = input("\n Question [10-20] \n What is >rock< in Te Reo? \n Option \n 1: [toka] \n 2: [Rokas] \n 3: [stijena] \n 4: >petra< \n").lower()

elif response10 == "no":
  input ("Bye have a great day!")
  
if play10 == "1" or play10 == "toka":
  print ("Correct, on to the next one!")
  score += 1

elif play10 == "2" or play10 == "Rokas" or play10 == "3" or play10 == "stijena" or play10 == "4" or play10 == "petra":
    print ("Wrong answer nice try")

#Question 11-20
response11 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response11 == "yes":
  play11 = input("\n Question [11-20] \n What is >plant< in Te Reo? \n Option \n 1: [augu] \n 2: [bitki] \n 3: [taim] \n 4: [tipu] \n").lower()

elif response11 == "no":
  input ("Bye have a great day!")
  
if play11 == "4" or play11 == "tipu":
  print ("Correct, on to the next one!")
  score += 1

elif play11 == "1" or play11 == "augu" or play11 == "2" or play11 == "bitki" or play11 == "3" or play11 == "taim":
    print ("Wrong answer nice try")

#Question 12-20
response12 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response12 == "yes":
  play12 = input("\n Question [12-20] \n What is >human< in Te Reo? \n Option \n 1: [člověk] \n 2: [cilvēks] \n 3: [tangata] \n 4: [bniedem] \n").lower()

elif response12 == "no":
  input ("Bye have a great day!")

if play12 == "3" or play12 == "tangata":
  print ("Correct, on to the next one!")
  score += 1

elif play12 == "1" or play12 == "člověk" or play12 == "2" or play12 == "cilvēks" or play12 == "4" or play12 == "bniedem":
    print ("Wrong answer nice try")

#Question 13-20
response13 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response13 == "yes":
  play13 = input("\n Question [13-20] \n What is >mountin< in Te Reo? \n Option \n 1: [fjall] \n 2: [maunga] \n 3: [montagna] \n 4: [beinn] \n").lower()

elif response13 == "no":
  input ("Bye have a great day!")

if play13 == "2" or play13 == "maunga":
  print ("Correct, on to the next one!")
  score += 1

elif play13 == "1" or play13 == "fjall" or play13 == "3" or play13 == "montagna" or play13 == "4" or play13 == "beinn":
    print ("Wrong answer nice try")

#Question 14-20
response14 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response14 == "yes":
  play14 = input("\n Question [14-20] \n What is >sick< in Te Reo? \n Option \n 1: [māuiui] \n 2: [na-arịa ọrịa] \n 3: [kurwara] \n 4: [ziek] \n").lower()

elif response14 == "no":
  input ("Bye have a great day!")

if play14 == "1" or play14 == "māuiui":
  print ("Correct, on to the next one!")
  score += 1

elif play14 == "2" or play14 == "na-arịa ọrịa" or play14 == "3" or play14 == "kurwara" or play14 == "4" or play14 == "ziek":
    print ("Wrong answer nice try")

#Question 15-20
response15 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response15 == "yes":
  play15 = input("\n Question [15-20] \n What is >adult< in Te Reo? \n Option \n 1: [olon-dehibe] \n 2: [adulte] \n 3: [pakeke] \n 4: [nasa hustong gulang] \n").lower()

elif response15 == "no":
  input ("Bye have a great day!")

if play15 == "3" or play15 == "pakeke":
  print ("Correct, on to the next one!")
  score += 1

elif play15 == "1" or play15 == "olon-dehibe" or play15 == "2" or play15 == "adulte" or play15 == "4" or play15 == "nasa hustong gulang":
    print ("Wrong answer nice try")

#Question 16-20
response16 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response16 == "yes":
  play16 = input("\n Question [16-20] \n What is >study< in Te Reo? \n Option \n 1: [undersøgelse] \n 2: [ako] \n 3: [studija] \n 4: [estudar] \n").lower()

elif response16 == "no":
  input ("Bye have a great day!")

if play16 == "2" or play16 == "ako":
  print ("Correct, on to the next one!")
  score += 1

elif play16 == "1" or play16 == "undersøgelse" or play16 == "3" or play16 == "studija" or play16 == "4" or play16 == "estudar":
    print ("Wrong answer nice try")

#Question 17-20
response17 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response17 == "yes":
  play17 = input("\n Question [17-20] \n What is >rain< in Te Reo? \n Option \n 1: [ua] \n 2: [déšť] \n 3: [yağmur] \n 4: [pluvo] \n").lower()

elif response17 == "no":
  input ("Bye have a great day!")

if play17 == "1" or play17 == "ua":
  print ("Correct, on to the next one!")
  score += 1

elif play17 == "2" or play17 == "déšť" or play17 == "3" or play17 == "yağmur" or play17 == "4" or play17 == "pluvo":
    print ("Wrong answer nice try")

#Question 18-20
response18 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response18 == "yes":
  play18 = input("\n Question [18-20] \n What is >cute< in Te Reo? \n Option \n 1: [armas] \n 2: [schattig] \n 3: [sevimli] \n 4: [orotika] \n").lower()

elif response18 == "no":
  input ("Bye have a great day!")

if play18 == "4" or play18 == "orotika":
  print ("Correct, on to the next one!")
  score += 1

elif play18 == "1" or play18 == "armas" or play18 == "2" or play18 == "schattig" or play18 == "3" or play18 == "sevimli":
    print ("Wrong answer nice try")

#Question 19-20
response19 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response19 == "yes":
  play19 = input("\n Question [19-20] \n What is >bee< in Te Reo? \n Option \n 1: [včela] \n 2: [pī] \n 3: [bitė] \n 4: [mesilane] \n").lower()

elif response19 == "no":
  input ("Bye have a great day!")

if play19 == "2" or play19 == "pī":
  print ("Correct, on to the next one!")
  score += 1

elif play19 == "1" or play19 == "včela" or play19 == "3" or play19 == "bitė" or play19 == "4" or play19 == "mesilane":
    print ("Wrong answer nice try")

#Question 20-20
response20 = input ("Ready for the next round? [YES] [NO] \n").lower()

if response20 == "yes":
  play20 = input("\n Question [20-20] \n What is >cold< in Te Reo? \n Option \n 1: [Studený] \n 2: [auksts] \n 3: [koud] \n 4: [makariri] \n").lower()

elif response20 == "no":
  input ("Bye have a great day!")

if play20 == "4" or play20 == "makariri":
  print ("Correct!")
  score += 1

elif play20 == "1" or play20 == "Studený" or play20 == "2" or play20 == "auksts" or play20 == "3" or play20 == "koud":
    print ("Wrong answer nice try")
#End of the Te Reo quiz game, showing the player how much score they have
print ("\n You have reach the end of the game, you have {} out of 20".format(score))