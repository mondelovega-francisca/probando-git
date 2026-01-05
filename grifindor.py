# Write code below 💖

scoreGryf=0
scoreRaven=0
scoreHuff=0
scoreSly=0
print("Que te gusta más Dawn or Dusk?")
print("1)Dawn")
print("2)Dusk")
entrada1=int(input("Qué te gusta más Dawn o Dusk?"))
if entrada1==1:
  scoreGryf=scoreGryf+1
  scoreRaven=scoreRaven+1
elif entrada1==2:
  scoreHuff=scoreHuff+1
  scoreSly=scoreSly+1
else:
  print("Wrong imput")    
print("When I´m dead, i want people to remember me as: ")
print("1)The Good")
print("2)The Great")
print("3) The Wise")
print("4)The Bold")
entrada2=int(input("choose: "))
if entrada2==1:
  scoreHuff=scoreHuff+2
elif entrada2==2:
  scoreSly=scoreSly+2
elif entrada2==3:
  scoreRaven=scoreRaven+2
elif entrada2==4:
  scoreGryf=scoreGryf+2
else: 
  print("Wrong input")    
print("Which kind of instrument most pleasesw your ear? ")  
print("1)the violin")
print("2)the trumpet")
print("3)the piano")
print("4)the drum")
entrada3=int(input("Elige: "))
if entrada3==1:
  scoreSly=scoreSly+4
elif entrada3==2:
  scoreHuff=scoreHuff+4
elif entrada3==3:
  scoreRaven=scoreRaven+4
elif entrada3==4:
  scoreGryf=scoreGryf+4
else:    
  print("Wrong imput")

print (scoreRaven)  
print(scoreGryf)
print(scoreHuff)
print(scoreSly)