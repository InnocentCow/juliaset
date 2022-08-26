from cmath import cos, sin, pi
from PIL import Image
import threading

exitFlag = 0

s = 500
max_iter = 50

b = (0, 0, 0)
w = (255, 255, 255)

nums = []
imgdict = {}
unit = (2*pi) / 500

for i in range(500):
    nums.append(cos(unit*i)/2+sin(unit*i)*1j/2)

for item in nums:
    imgdict[str(item)] = Image.new("RGB", (4*s, 3*s))

class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("Starting " + self.name)
        julia(self.threadID, self.name)
        print("Exiting " + self.name)


def mandel(z, c):
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return w
    return b

def julia(id, threadName):
    c = complex(threadName)
    for y in range(0, 3*s):
        y2 = (y - 1.5*s)/s
        for x in range(0, 4*s):
            x2 = (x - 2*s)/s
            imgdict[threadName].putpixel((x, y), mandel(x2 + y2*1j, c))
    imgdict[threadName].save(f'pics3/julia{id}.png')


for z in range(len(nums)):
    myThread(z + 1, nums[z]).start()
