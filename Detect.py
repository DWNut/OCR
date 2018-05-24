from PIL import Image



img = Image.open("Binarized.jpg")

copie = img.copy()
left = 0
right = 0
upper = 0
lower = 0
LL = []
LR = []
LT = []
LB = []


for i in range(copie.height):
    for j in range(copie.width):
        p = copie.getpixel((j,i))
        if(p[0] == 0):
            LL.append(j)
            break

left = min(LL)
    
for i in range(copie.width):
   for j in range(copie.height):
     p = copie.getpixel((i,j))
     if(p[0] == 0):
         LT.append(j)
         break

upper = min(LT)

for i in range(copie.height):
    for j in range(copie.width -1, -1, -1):
        p = copie.getpixel((j,i))
        if(p[0] == 0):
            LR.append(j)
            break

right = max(LR)

for i in range(copie.width):
   for j in range(copie.height -1, -1, -1):
     p = copie.getpixel((i,j))
     if(p[0] == 0):
         LB.append(j)
         break

lower = max(LB)

cropped = copie.crop((left,upper, right,lower))
cropped.show()         
            

cropped.save("TextBlock.jpg")
img.close()
