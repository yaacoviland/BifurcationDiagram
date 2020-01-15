from PIL import Image, ImageDraw
import time

start_time = time.time()
print("Started at", start_time)

# Image size (pixels)
WIDTH = 100
HEIGHT = 100

# Plot ranges
XMIN = 2
XMAX = 4
YSTART = 0.5
steps = 1000
precision = 5
max_iter = 2000

def get_orbit(r):
  y=YSTART
  orbit = []
  path = [y]
  for i in range(max_iter):
    y = round(r*y*(1-y), precision)
    path.append(y)
  
  for j in range(max_iter):
    if path.count(path[j]) > 1:
      orbit = path[j:path.index(path[j], j+1)]
      break
  if orbit == []:
    orbit = path
  
  return orbit

orbits = []
for i in range(steps):
  orbits.append([i, get_orbit(XMIN + (XMAX - XMIN)*i / steps)])

print(orbits[100])

orbits_time = time.time()
print("Computed orbits at", orbits_time, ". Took", orbits_time - start_time, "seconds.")

im = Image.new('RGB', (steps, steps), (255, 255, 255))
draw = ImageDraw.Draw(im)
for n, orbit in orbits:
  draw.point([(n, value*steps) for value in orbit], fill=(10, 10, 235))

im.save('bifurcation.png', 'PNG')

end_time = time.time()
print("Done at", end_time, ". Took", end_time - start_time, "seconds.")
