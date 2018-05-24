from PIL import Image

img = Image.open("Grayscale.jpg")

copie = img.copy()

for i in range(copie.height):
    for j in range(copie.width):
        pixel = img.getpixel((j,i))
        if(pixel[0] >= 155):
            p = (255,255,255)
            copie.putpixel((j,i),p)
        elif(pixel[0] < 155):
            p = (0,0,0)
            copie.putpixel((j,i),p)
        

copie.show()
copie.save("Binarized.jpg")
img.close()
