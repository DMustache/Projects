import random
import math

def noiser01():
    global mapsize

    for i in range(5):
        random.seed(i)
        print(f'{i}|', *[random.randint(1, random.randint(1, 3))
            for i in range(mapsize)])

def noiser02():
    global mapsize
    def adjacent_min(noise):
        output = []
        for i in range(len(noise) - 1):
            output.append(min(noise[i], noise[i + 1]))
        return output
    
    for i in range(10):
        random.seed(i)
        noise = [random.randint(1, 3) for i in range(mapsize)]
        print(f'{i}|', *adjacent_min(noise))

def noiser03():
    global mapsize
    def noise(freq):
        phase = random.uniform(0, 2*math.pi)
        return [math.sin(2*math.pi * freq*x/mapsize + phase)
            for x in range(mapsize)]

    for i in range(3):
        random.seed(i)
        print(i, noise(1))
mapsize = 10
noiser03()