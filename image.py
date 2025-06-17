import math
from PIL import Image

width = 1600
height = 1600

zoom_factor = 10000000000

img = Image.new("RGB", (width, height), (0, 0, 0))

for x in range(width):
	for y in range(height):
		samp = (
			x / width / zoom_factor - 1 / zoom_factor / 2 - 1.6238612001,
			y / height / zoom_factor - 1 / zoom_factor / 2 - 0.001
		)
		
		curr = (0, 0)
		for i in range(1200):
			curr = (
				curr[0]*curr[0] - curr[1]*curr[1] + samp[0],
				2*curr[0]*curr[1] + samp[1]
			)
			if (curr[0]*curr[0] + curr[1]*curr[1] > 4):
				img.putpixel((x, y), (255, 255, 255))
				break

img.save("img.png")