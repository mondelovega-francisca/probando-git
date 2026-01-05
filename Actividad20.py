# Write code below 💖


menu=['1:🍔 Cheeseburger','2:🍟 Fries','3:🥤 Soda','4:🍦 Ice Cream','5:Ensalada Francisca Vega Mondelo']
#Hay 5 opciones de menú.
#welcome funtion
def welcome():
 print("Welcome, nuestro menú es: ", menu) 
# función get item
def get_item(var):
  var1=var-1
  cocinar=menu[var1]
  
  return cocinar


# código principal
welcome() 

opcion_menu=int(input("Escoge el número de menú: "))
print("El menú escogido es",opcion_menu)

print(get_item(opcion_menu))



  