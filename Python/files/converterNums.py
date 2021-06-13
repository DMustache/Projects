from PIL import Image, ImageDraw

image1 = Image.open("Python\Демо1.bmp")
image2 = Image.open("Python\Демо2.bmp")
ANS = Image.open("Python\Демо1.bmp")
draw = ImageDraw.Draw(ANS)
pix1 = image1.load()
pix2 = image2.load()
width = min(image1.size[0], image2.size[0])
height = min(image1.size[1], image2.size[1])
eps = 30
for i in range(width):
	for j in range(height):
		dx1 = pix1[i, j][0] - pix2[i, j][0]
		dx2 = pix1[i, j][1] - pix2[i, j][1]
		dx3 = pix1[i, j][2] - pix2[i, j][2]
		draw.point((i, j), (abs(dx1), abs(dx2), abs(dx3))) # Зарисовываем ответ разницей пикселов наших картинок по модулю.
ANS.save("Python\Демо3.bmp", "BMP")
del draw