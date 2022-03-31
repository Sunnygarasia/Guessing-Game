#welcoming user
print("WELCOME TO THE GUESSING GAME.\n YOU WILL HAVE 10 LIFES. EACH WRONG GUESS WILL TAKE YOUR ONE LIFE. ")
#asking user's name
name = input("What is your name ? ")
#asking user's age
age = input("What is your age ? ")
#printing name and age
print("Your name is",name,"and",age,"years old." )
#asking user if they want to play the game
want_to_play = input("ARE YOU READY TO PLAY THE GAME ? (YES/NO)").lower()
#if answer is yes
if want_to_play == "yes":
  print("LET'S START THE GAME !!")
        #assign health
  live = 10
  print("YOU ARE STARTING GAME WITH", live, "LIVES. ")
  level = 0
  print("LEVEL ",level)
  #guessing no.1
  answer = input("I can be taller than a house. Birds live in me. You can build a house in me. I give you fresh air to breathe. What am I ? ").lower()
  #correct answer
  if answer == "tree":
    print("Congratulations. You are correct.")
    level +=1
  else:
  #lost life
    live -= 1
    print("Wrong answer. You lost one life. Remaining lives are",live)
  #guessing no.2
  answer = input("I come in many colors. I get bigger when I am full. I make a loud sound when I break. I will float away if you let me go. What am I ? ").lower()
  #correct answer
  if answer == "ballon":
    print("Congratulations. You are correct.")
    level += 1
    if level == 2:
      print("YOU REACHED LEVEL 2 ")
  #incorrect answer
  else:
  #lost life
    live -= 1
    print("Wrong answer. You lost one life. Remaining lives are",live)
  #guessing no.3 
  answer = input("I always come in a pair. You buy me in a box. You can trip if you don't tie me up. I can get smelly. What am I ? ").lower()
  #correct answer
  if answer == "shoes":
    print("Congratulations. You are correct.")
    level += 1
    if level == 2:
      print("YOU REACHED LEVEL 2 ")
  #incorrect answer
  else:
  #lost life
    live -= 1
    print("Wrong answer. You lost one life. Remaining lives are",live)
  #guessing no.4
  answer = input("I am made from wood. I have many keys. people like to sing along with me. What am I ? ").lower()
  #correct answer
  if answer == "piano":
    print("Congratulations. You are correct.")
    level += 1
    if level == 4:
      print("YOU REACHED LEVEL 3 ")
    if level == 2:
      print("YOU REACHED LEVEL 2 ")
  #incorrect answer
  else:
  #lost life
    live -= 1
    print("Wrong answer. You lost one life. Remaining lives are",live)
  #guessing no.5
  answer = input("You can never touch me. I have many colors. You will see me after it rains. Find me to get a pot of gold. What am I ? ").lower()
  #correct answer
  if answer == "rainbow":
    print("Congratulations. You are correct.")
    level += 1
    if level == 4:
      print("YOU REACHED LEVEL 3 ")
    if level == 2:
      print("YOU REACHED LEVEL 2 ")
  #incorrect answer
  else:
  #lost life
    live -= 1
    print("Wrong answer. You lost one life. Remaining lives are",live)
  #guessing no.6
  answer = input("I am an animal. I like to eat leaves. I am bigger than a tree. My neck is longer than my body. What am I ? ").lower()
  #correct answer
  if answer == "giraffe":
    print("Congratulations. You are correct.")
    level += 1
    if level == 6:
      print("YOU REACHED LEVEL 4 ")
    if level == 4:
      print("YOU REACHED LEVEL 3 ")
    if level == 2:
      print("YOU REACHED LEVEL 2 ")
  #incorrect answer
  else:
  #lost life
    live -= 1
    print("Wrong answer. You lost one life. Remaining lives are",live)
  #guessing no.7
  answer = input("I am very sharp. You use me to eat. You must clean me everyday. What am I ? ").lower()
  #correct answer
  if answer == "teeth":
    print("Congratulations. You are correct.")
    level += 1
    if level == 6:
      print("YOU REACHED LEVEL 4")
    if level == 4:
      print("YOU REACHED LEVEL 3 ")
    if level == 2:
      print("YOU REACHED LEVEL 2 ")
  #incorrect answer
  else:
  #lost life
    live -= 1
    print("Wrong answer. You lost one life. Remaining lives are",live)
  #guessing no.8
  answer = input("You use me when resting. I can be used for fight. I protect your neck and head. What am I ? ").lower()
  #correct answer
  if answer == "pillow":
    print("Congratulations. You are correct.")
    level += 1
    if level == 8:
      print("YOU REACHED LEVEL 5 ")
    if level == 6:
      print("YOU REACHED LEVEL 4 ")
    if level == 4:
      print("YOU REACHED LEVEL 3 ")
    if level == 2:
      print("YOU REACHED LEVEL 2 ")
  #incorrect answer
  else:
  #lost life
    live -= 1
    print("Wrong answer. You lost one life. Remaining lives are",live)
  #guessing no.9
  answer = input("You always look down on me. I can run but I cannot walk. You follow me where I go. I know when things don't smell right. What am I ? ").lower()
  #correct answer
  if answer == "nose":
    print("Congratulations. You are correct.")
    level += 1
    if level == 8:
      print("YOU REACHED LEVEL 5 ")
    if level == 6:
      print("YOU REACHED LEVEL 4 ")
    if level == 4:
      print("YOU REACHED LEVEL 3 ")
    if level == 2:
      print("YOU REACHED LEVEL 2 ")
  #incorrect answer
  else:
  #lost life
    live -= 1
    print("Wrong answer. You lost one life. Remaining lives are",live)
  #guessing no.10
  answer = input("People use me to wake up. I don't use electricity. I come with a comb. I live on a farm. What am I ? ").lower()
  #correct answer
  if answer == "rooster":
    print("Congratulations. You are correct.")
    level += 1
    if level == 10:
      print("YOU HAVE PASSED THE GAME. HURRAY!!")
    if level == 8:
      print("YOU REACHED LEVEL 5 ")
    if level == 6:
      print("YOU REACHED LEVEL 4 ")
    if level == 4:
      print("YOU REACHED LEVEL 3 ")
    if level == 2:
      print("YOU REACHED LEVEL 2 ")
  #incorrect answer
  else:
  #lost life
    live -= 1
    if live == 0:
      print("YOU HAVE LOST ALL LIVES. YOU HAVE LOST THE GAME.")
    else:
      print("GAME OVER. YOU LOST")
    
    #else:
      #print("GAME OVER. YOU LOST")
#if answer is no
else:
  print("YOU CAN COMEBACK LATER. ")