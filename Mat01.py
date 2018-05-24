from PIL import Image

img = Image.open("TextBlock.jpg")
a = 0

copie = img.copy()

for i in range (copie.height):
    for j in range (copie.width):
        p = copie.getpixel((j,i))
        a = p[0]
        if (a > 200):
            p = (1,1,1)
            copie.putpixel((j,i),p)
        elif (a <= 200):
            p = (0,0,0)
            copie.putpixel((j,i),p)

img.close()
