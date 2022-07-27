import random
# Start of the Te Reo quiz game
# Ask player if they want to start (typing "no" will end the game or type random and type "yes" starts the game)
#Colours and etc
End = '\033[0m'
Red = '\033[31m'
Green = '\033[32m'
Bold = '\033[1m'
Underscore = '\033[4m'
Magenta = '\033[35m'
Cyan = '\033[36m'
Concealed = '\033[7m'

print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print (Magenta + Concealed + '\033[1m' + "Hello, welcome to Te Reo Quiz game!" + End)
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
score = 0

Question = [
  " Question 1/20: What is >HELLO< in Te Reo?",
  " Question 2/20: What is >WATER< in Te Reo?",
  " Question 3/20: What is >PIG< in Te Reo?",
  " Question 4/20: What is >SKY< in Te Reo?",
  " Question 5/20: What is >TREE< in Te Reo?",
  " Question 6/20: What is >MAN< in Te Reo?",
  " Question 7/20: What is >WOMAN< in Te Reo?",
  " Question 8/20: What is >FOOD< in Te Reo?",
  " Question 9/20: What is >DRINK< in Te Reo?",
  " Question 10/20: What is >ROCK< in Te Reo?",
  " Question 11/20: What is >PLANT< in Te Reo?",
  " Question 12/20: What is >HUMAN< in Te Reo?",
  " Question 13/20: What is >MOUNTAIN< in Te Reo?",
  " Question 14/20: What is >SICK< in Te Reo?",
  " Question 15/20: What is >ADULT< in Te Reo?",
  " Question 16/20: What is >STUDY< in Te Reo?",
  " Question 17/20: What is >RAIN< in Te Reo?",
  " Question 18/20: What is >CUTE< in Te Reo?",
  " Question 19/20: What is >BEE< in Te Reo?",
  " Question 20/20: What is >COLD< in Te Reo?",
]

correct_answer = [
  "kia ora",
  "wai",
  "poaka",
  "rangi",
  "rakau",
  "tangata",
  "wahine",
  "kai",
  "inu",
  "toka",
  "tipu",
  "tangata",
  "maunga",
  "māuiui",
  "pakeke",
  "ako",
  "ua",
  "orotika",
  "pī",
  "makariri",
]

wrong_answer1 = [
  "ciao",
  "privet",
  "salut",
  "acqua",
  "vesi",
  "auga",
  "porco",
  "beraz",
  "cūka",
  "cer",
  "asûman",
  "leholimo",
  "muti",
  "fa",
  "arbo",
  "mesilane",
  "Studený",
  "auksts",
  "koud",
  "peru",
]

wrong_answer2 = [
  "vir",
  "olona",
  "muž",
  "vehivavy",
  "muller",
  "vrouw",
  "cibus",
  "jídlo",
  "drénken",
  "bibere",
  "İçmek",
  "Rokas",
  "stijena",
  "petra",
  "undersøgelse",
  "studija",
  "estudar",
  "déšť",
  "yağmur",
  "pluvo",
]

wrong_answer3 = [
  "augu",
  "bitki",
  "taim",
  "člověk",
  "cilvēks",
  "bniedem",
  "fjall",
  "montagna",
  "beinn",
  "na-arịa ọrịa",
  "kurwara",
  "ziek",
  "olon-dehibe",
  "adulte",
  "nasa hustong gulang",
  "armas",
  "schattig",
  "sevimli",
  "včela",
  "bitė",
]


def generate_questions(Question,correct_answer,wrong_answer1,wrong_answer2,wrong_answer3):
  global score

  print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
  print ( Underscore + Bold + Cyan + "Score {}".format(score) + End)
  print (Question)

  randomize_answer = random.randint(0,3)

  if (randomize_answer == 0):
    print("1", wrong_answer1)
    print("2", wrong_answer2)
    print("3", wrong_answer3)
    print("4", correct_answer)
    answer = input().lower()
    if answer == "4" or answer == correct_answer:
      score += 1
      print(Green + "Correct, on to the next one!" + End)
    else:
      print(Red + "Wrong answer, Correct answer is",correct_answer + End)

  elif (randomize_answer == 1):
    print("1", wrong_answer1)
    print("2", correct_answer)
    print("3", wrong_answer3)
    print("4", wrong_answer2)
    answer = input().lower()
    if answer == "2" or answer == correct_answer:
      score += 1
      print(Green + "Correct, on to the next one!" + End)
    else:
      print(Red + "Wrong answer, Correct answer is",correct_answer + End)

  elif (randomize_answer == 2):
    print("1", wrong_answer1)
    print("2", wrong_answer3)
    print("3", correct_answer)
    print("4", wrong_answer2)
    answer = input().lower()
    if answer == "3" or answer == correct_answer:
      score += 1
      print(Green + "Correct, on to the next one!" + End)
    else:
      print(Red + "Wrong answer, Correct answer is",correct_answer + End)
  
  elif (randomize_answer == 3):
    print("1", correct_answer)
    print("2", wrong_answer1)
    print("3", wrong_answer3)
    print("4", wrong_answer2)
    answer = input().lower()
    if answer == "1" or answer == correct_answer:
      score += 1
      print(Green + "Correct, on to the next one!" + End)
    else:
      print(Red + "Wrong answer, Correct answer is",correct_answer + End)
      
for i in range (0,20):    
        generate_questions(Question[i],correct_answer[i],wrong_answer1[i],wrong_answer2[i],wrong_answer3[i])

print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print (Bold + Magenta + Concealed + "\n You have reached the end of the game, you have {} out of 20".format(score) + End)
print ("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")