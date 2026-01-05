# Write code below 💖
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]
longitud=len(stock_prices)
print(longitud) #longitud de la lista
#definimos la función price_at(x) que nos de el precio del día x
def price_at(x):
  preciodeldia=stock_prices[x]
  return preciodeldia
print(price_at(2))
def max_price(a,b):
  aa=a-1
  maximo=max(stock_prices[aa:b])
  return maximo
print(max_price(1,7))   #43.41 output
def min_price(a,b):
  aa=a-1
  minimo=min(stock_prices[aa:b])
  return minimo
print(min_price(1,7))  #output 33.97


