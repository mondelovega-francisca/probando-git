# Write code below 💖
# Solar System 🪐
# Codédex

from math import pi 
from random import choice as ch

planets = [ 'Mercury', 'Venus', 'Earth', 'Mars', 'Saturn']

random_planet = ch(planets)
print(random_planet)
radio = 0

if random_planet == 'Mercury':
  radio = 2440
elif random_planet == 'Venus':
  radio = 6052
elif random_planet == 'Earth':
  radio = 6371
elif random_planet == 'Mars':
  radio = 3390
elif random_planet == 'Saturn':
  radio = 58232
else:
  print('Oops! An error occurred.')
print (radio)
planet_area = 4 * pi * radio * radio
print(planet_area)
valor=round(planet_area,3)
print(f'Area of {random_planet}: {valor} sq mi')