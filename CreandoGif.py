# Create a GIF with Python 🎞️
# Francisca Vega Mondelo

import imageio.v3 as iio

filenames = ['Start.png', 'End.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)