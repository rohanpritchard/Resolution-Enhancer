from math import floor

import PIL.Image as img


def getVal1D(p, x):
	o = [0] * 4
	for i in range(4):
		o[i] = int(p[1][i] + 0.5 * x * (p[2][i] - p[0][i] + x * (
					2.0 * p[0][i] - 5.0 * p[1][i] + 4.0 * p[2][i] - p[3][i] + x * (
						3.0 * (p[1][i] - p[2][i]) + p[3][i] - p[0][i]))))
	return tuple(o)


def getVal2D(p, x, y):
	arr = [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
	arr[0] = getVal1D(p[0], y)
	arr[1] = getVal1D(p[1], y)
	arr[2] = getVal1D(p[2], y)
	arr[3] = getVal1D(p[3], y)
	return getVal1D(arr, x)


def bicubic(image_in):
	image = image_in.convert('RGBA')
	r, g, b, a = image.getpixel((3, 3))
	oldWidth = image.width
	oldHeight = image.height
	width = oldWidth*4
	height = oldHeight*4
	widthR = oldWidth / width
	heightR = oldHeight / height
	print('from width: ', oldWidth, ' height: ', oldHeight)
	print('to   width: ', width, ' height: ', height)
	output = img.new('RGBA', (width, height))

	for i in range(0, width):
		for j in range(0, height):
			x = i * widthR
			y = j * heightR
			rx = x % 1
			ry = y % 1
			p = [[0] * 4 for _ in range(4)]
			for xi in range(0, 4):
				for yj in range(0, 4):
					px = floor(x) - 1 + xi
					py = floor(y) - 1 + yj
					px = max(0, px)
					py = max(0, py)
					px = min(oldWidth - 1, px)
					py = min(oldHeight - 1, py)
					# print((i, j, px, py))
					p[xi][yj] = image.getpixel((px, py))

			o = getVal2D(p, rx, ry)
			# print(o, i, j)
			output.putpixel((int(i), int(j)), o)
	return output
