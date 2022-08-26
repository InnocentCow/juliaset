from PIL import Image
import time

start = time.time()

s = 500
max_iter = 50

b = (0, 0, 0)
w = (255, 255, 255)

img = Image.new("RGB", (3*s, 2*s))

def mandel(z, c):
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return w
    return b

def julia(c):
    for y in range(0, 2*s):
        y2 = (y - s)/s
        print(y2)
        for x in range(0, 3*s):
            x2 = (x - 2*s)/s

            print(x, y)
            img.putpixel((x, y), mandel(x2 + y2*1j, c))
    img.save('julia2' + str(c) + '.png')
    img.show()

julia(0 + 0.8j)

print(time.time() - start)
