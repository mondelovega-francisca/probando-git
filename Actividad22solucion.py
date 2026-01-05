# Write code below 💖
# Write code below 💖

class Restaurant:
  name=''
  category=''
  rating=0.0
  delivery=False

bobs_burgers= Restaurant()
bobs_burgers.name='Bob Burguer'
bobs_burgers.category='American Diner'
bobs_burgers.rating=4.7
bobs_burgers.delivery=False

Vegetal_burguer=Restaurant()
Vegetal_burguer.name='Vegetal Burguer'
Vegetal_burguer.category='Vegan Diner'
Vegetal_burguer.rating=5.7
Vegetal_burguer.delivery=False

Chicken_burguer=Restaurant()
Chicken_burguer.name='Chicken Burguer'
Chicken_burguer.category='American Diner'
Chicken_burguer.rating= 4
Chicken_burguer.delivery=False

print(vars(Chicken_burguer))
print(vars(Vegetal_burguer))
print(vars(bobs_burgers))

