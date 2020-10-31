print("Title of program: Encouragement bot")
print()
while True:
  description = input("how are you?")

  list_of_words = description.split()
  

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("its fine, just look at some funny memes")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("nice go study or look at a meme or something you like!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("You are stronger than you think :)")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("YOU NEED TO CHILL AND EAT SOME ICE CREAM")
  if counter == 0:
    
      output = "ur dumb go and repeat again "

  elif counter == 1:
    
      output = "ok you are  " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
