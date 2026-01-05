# Write code below 💖

dinero=int(input("Indica el dinero del que dispones en euros: "))
altura=int(input("Indica tu altura en cm: "))
if dinero>=10 and altura>=137:
  print("Disfruta del viaje")
elif dinero>=10 and altura<137:
  print("No eres lo suficientemente alto")  
elif dinero<10 and altura>=137:
  print("NO tienes suficiente dinero")
else:
  print("No cumples ninguno de los requisitos")  
