
# Start of the Te Reo quiz game
# Ask player if they want to start (typing "no" will end the game or type random and type "yes" starts the game)
#Colours and etc
End = '\033[0m'
Red = '\033[31m'
Green = '\033[32m'
Bold = '\033[1m'


print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print('\033[1m' + "Hello, welcome to Te Reo Quiz game!" + End)
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
score = 0

# Every correct question the player answer gives 1 score
# Question 1-20
play1 = print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play1 = input(" \n Question [1-20] \n What is >HELLO< in Te Reo? \n OPTIONS \n 1: [ciao] \n 2: [privet] \n 3: [salut] \n 4: [kia ora] \n").lower()
if play1 == "4" or play1 == "kia ora":
  print('\033[32m' + "Correct, on to the next one!" + End)
  score += 1


elif play1 == "1" or play1 == "ciao" or play1 == "2" or play1 == "privet" or play1 == "3" or play1 == "salut":
    print ('\033[31m' + "Wrong answer, Correct answer is Kia ora" + End)

#Question 2-20
play2 = print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play2 = input("\n Question [2-20] \n What is >WATER< in Te Reo? \n OPTIONS \n 1: [acqua] \n 2: [wai] \n 3: [vesi] \n 4: [auga] \n").lower()
  
if play2 == "2" or play2 == "wai":
  print ('\033[32m' + "Correct, on to the next one!" + End)
  score += 1

elif play2 == "1" or play2 == "acqua" or play2 == "3" or play2 == "vesi" or play2 == "4" or play2 == "auga":
    print (Red + "Wrong answer, Correct answer is wai" + End)

#Question 3-20
play3 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play3 = input("\n Question [3-20] \n What is >PIG< in Te Reo? \n OPTIONS \n 1: [porco] \n 2: [beraz] \n 3: [poaka] \n 4: [cūka] \n").lower()

if play3 == "3" or play3 == "poaka":
  print ('\033[32m' + "Correct, on to the next one!" + End)
  score += 1

elif play3 == "1" or play3 == "porco" or play3 == "2" or play3 == "beraz" or play3 == "4" or play3 == "cūka":
    print (Red + "Wrong answer, Correct answer is poaka" + End)

#Question 4-20
play4 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play4 = input("\n Question [4-20] \n What is >SKY< in Te Reo? \n OPTIONS \n 1: [cer] \n 2: [rangi] \n 3: [asûman] \n 4: [leholimo] \n").lower()

if play4 == "2" or play4 == "rangi":
  print ('\033[32m' + "Correct, on to the next one!" + End)
  score += 1

elif play4 == "1" or play4 == "cer" or play4 == "3" or play4 == "asûman" or play4 == "4" or play4 == "leholimo":
    print (Red + "Wrong answer, Correct answer is rangi" + End)

#Question 5-20
play5 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play5 = input("\n Question [5-20] \n What is >TREE< in Te Reo? \n OPTIONS \n 1: [muti] \n 2: [fa] \n 3: [rakau] \n 4: [arbo] \n").lower()

if play5 == "3" or play5 == "rakau":
  print ('\033[32m' + "Correct, on to the next one!" + End)
  score += 1
  
elif play5 == "1" or play5 == "muti" or play5 == "2" or play5 == "fa" or play5 == "4" or play5 == "arbo":
    print (Red + "Wrong answer, Correct answer is rakau" + End)

#Question 6-20
play6 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play6 = input("\n Question [6-20] \n What is >MAN< in Te Reo? \n OPTIONS \n 1: [vir] \n 2: [olona] \n 3: [muž] \n 4: [tangata] \n").lower()
  
if play6 == "4" or play6 == "tangata":
  print ('\033[32m' + "Correct, on to the next one!" + End)
  score += 1

elif play6 == "1" or play6 == "vir" or play6 == "2" or play6 == "olona" or play6 == "4" or play6 == "muž":
    print (Red + "Wrong answer, Correct answer is tangata" + End)

#Question 7-20
play7 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play7 = input("\n Question [7-20] \n What is >WOMAN< in Te Reo? \n OPTIONS \n 1: [vehivavy] \n 2: [wahine] \n 3: [muller] \n 4: [vrouw] \n").lower()
  
if play7 == "2" or play7 == "wahine":
  print ('\033[32m' + "Correct, on to the next one!" + End)
  score += 1

elif play7 == "1" or play7 == "vehivavy" or play7 == "3" or play7 == "muller" or play7 == "4" or play7 == "vrouw":
    print (Red + "Wrong answer, Correct answer is wahine" + End)

#Question 8-20
play8 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play8 = input("\n Question [8-20] \n What is >FOOD< in Te Reo? \n OPTIONS \n 1: [cibus] \n 2: [jídlo] \n 3: [храна] \n 4: [kai] \n").lower()
  
if play8 == "4" or play8 == "kai":
  print ('\033[32m' + "Correct, on to the next one!" + End)
  score += 1

elif play8 == "1" or play8 == "cibus" or play8 == "2" or play8 == "jídlo" or play8 == "3" or play8 == "храна":
    print (Red + "Wrong answer, Correct answer is kai" + End)

#Question 9-20

play9 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play9 = input("\n Question [9-20] \n What is >DRINK< in Te Reo? \n OPTIONS \n 1: [inu] \n 2: [drénken] \n 3: [bibere] \n 4: [İçmek] \n").lower()
  
if play9 == "1" or play9 == "inu":
  print ('\033[32m' + "Correct, on to the next one!" + End)
  score += 1

elif play9 == "2" or play9 == "drénken" or play9 == "3" or play9 == "bibere" or play9 == "4" or play9 == "İçmek":
    print (Red + "Wrong answer, Correct answer is inu" + End)

#Question 10-20
play10 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play10 = input("\n Question [10-20] \n What is >ROCK< in Te Reo? \n OPTIONS \n 1: [toka] \n 2: [Rokas] \n 3: [stijena] \n 4: [petra] \n").lower()

if play10 == "1" or play10 == "toka":
  print (Green + "Correct, on to the next one!" + End)
  score += 1

elif play10 == "2" or play10 == "Rokas" or play10 == "3" or play10 == "stijena" or play10 == "4" or play10 == "petra":
    print (Red + "Wrong answer, Correct answer is toka" + End)

#Question 11-20
play11 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play11 = input("\n Question [11-20] \n What is >PLANT< in Te Reo? \n OPTIONS \n 1: [augu] \n 2: [bitki] \n 3: [taim] \n 4: [tipu] \n").lower()
  
if play11 == "4" or play11 == "tipu":
  print (Green + "Correct, on to the next one!" + End)
  score += 1

elif play11 == "1" or play11 == "augu" or play11 == "2" or play11 == "bitki" or play11 == "3" or play11 == "taim":
    print (Red + "Wrong answer, Correct answer is tipu" + End)

#Question 12-20
play12 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play12 = input("\n Question [12-20] \n What is >HUMAN< in Te Reo? \n OPTIONS \n 1: [člověk] \n 2: [cilvēks] \n 3: [tangata] \n 4: [bniedem] \n").lower()

if play12 == "3" or play12 == "tangata":
  print (Green + "Correct, on to the next one!" + End)
  score += 1

elif play12 == "1" or play12 == "člověk" or play12 == "2" or play12 == "cilvēks" or play12 == "4" or play12 == "bniedem":
    print (Red + "Wrong answer, Correct answer is tangata" + End)

#Question 13-20
play13 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play13 = input("\n Question [13-20] \n What is >MOUNTAIN< in Te Reo? \n OPTIONS \n 1: [fjall] \n 2: [maunga] \n 3: [montagna] \n 4: [beinn] \n").lower()

if play13 == "2" or play13 == "maunga":
  print (Green + "Correct, on to the next one!" + End)
  score += 1

elif play13 == "1" or play13 == "fjall" or play13 == "3" or play13 == "montagna" or play13 == "4" or play13 == "beinn":
    print (Red + "Wrong answer, Correct answer is maunga" + End)

#Question 14-20
play14 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play14 = input("\n Question [14-20] \n What is >SICK< in Te Reo? \n OPTIONS \n 1: [māuiui] \n 2: [na-arịa ọrịa] \n 3: [kurwara] \n 4: [ziek] \n").lower()

if play14 == "1" or play14 == "māuiui":
  print (Green + "Correct, on to the next one!" + End)
  score += 1

elif play14 == "2" or play14 == "na-arịa ọrịa" or play14 == "3" or play14 == "kurwara" or play14 == "4" or play14 == "ziek":
    print (Red + "Wrong answer, Correct answer is māuiui" + End)

#Question 15-20
play15 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play15 = input("\n Question [15-20] \n What is >ADULT< in Te Reo? \n OPTIONS \n 1: [olon-dehibe] \n 2: [adulte] \n 3: [pakeke] \n 4: [nasa hustong gulang] \n").lower()

if play15 == "3" or play15 == "pakeke":
  print (Green + "Correct, on to the next one!" + End)
  score += 1

elif play15 == "1" or play15 == "olon-dehibe" or play15 == "2" or play15 == "adulte" or play15 == "4" or play15 == "nasa hustong gulang":
    print (Red + "Wrong answer, Correct answer is pakeke" + End)

#Question 16-20
play16 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play16 = input("\n Question [16-20] \n What is >STUDY< in Te Reo? \n OPTIONS \n 1: [undersøgelse] \n 2: [ako] \n 3: [studija] \n 4: [estudar] \n").lower()

if play16 == "2" or play16 == "ako":
  print (Green + "Correct, on to the next one!" + End)
  score += 1

elif play16 == "1" or play16 == "undersøgelse" or play16 == "3" or play16 == "studija" or play16 == "4" or play16 == "estudar":
    print (Red + "Wrong answer, Correct answer is ako" + End)

#Question 17-20
play17 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play17 = input("\n Question [17-20] \n What is >RAIN< in Te Reo? \n OPTIONS \n 1: [ua] \n 2: [déšť] \n 3: [yağmur] \n 4: [pluvo] \n").lower()

if play17 == "1" or play17 == "ua":
  print (Green + "Correct, on to the next one!" + End)
  score += 1

elif play17 == "2" or play17 == "déšť" or play17 == "3" or play17 == "yağmur" or play17 == "4" or play17 == "pluvo":
    print (Red + "Wrong answer, Correct answer is ua" + End)

#Question 18-20
play18 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play18 = input("\n Question [18-20] \n What is >CUTE< in Te Reo? \n OPTIONS \n 1: [armas] \n 2: [schattig] \n 3: [sevimli] \n 4: [orotika] \n").lower()

if play18 == "4" or play18 == "orotika":
  print (Green + "Correct, on to the next one!" + End)
  score += 1

elif play18 == "1" or play18 == "armas" or play18 == "2" or play18 == "schattig" or play18 == "3" or play18 == "sevimli":
    print (Red + "Wrong answer, Correct answer is orotika" + End)

#Question 19-20
play19 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play19 = input("\n Question [19-20] \n What is >BEE< in Te Reo? \n OPTIONS \n 1: [včela] \n 2: [pī] \n 3: [bitė] \n 4: [mesilane] \n").lower()

if play19 == "2" or play19 == "pī":
  print (Green + "Correct, on to the next one!" + End)
  score += 1

elif play19 == "1" or play19 == "včela" or play19 == "3" or play19 == "bitė" or play19 == "4" or play19 == "mesilane":
    print (Red + "Wrong answer, Correct answer is pī" + End)

#Question 20-20
play20 = print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
play20 = input("\n Question [20-20] \n What is >COLD< in Te Reo? \n OPTIONS \n 1: [Studený] \n 2: [auksts] \n 3: [koud] \n 4: [makariri] \n").lower()

if play20 == "4" or play20 == "makariri":
  print (Green + "Correct!" + End)
  score += 1

elif play20 == "1" or play20 == "Studený" or play20 == "2" or play20 == "auksts" or play20 == "3" or play20 == "koud":
    print (Red + "Wrong answer, Correct answer is makariri" + End)
#End of the Te Reo quiz game, showing the player how much score they have
print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print (Bold + "\n You have reach the end of the game, you have {} out of 20".format(score) + End)
print ("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")