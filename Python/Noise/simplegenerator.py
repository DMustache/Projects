import random
import math

def noiser01():
    mapsize = 20

    for i in range(5):
        random.seed(i)
        print(f'{i}|', *[random.randint(1, random.randint(1, 3))
            for i in range(mapsize)])

def noiser02():
    mapsize = 20
    def adjacent_min(noise):
        output = []
        for i in range(len(noise) - 1):
            output.append(min(noise[i], noise[i + 1]))
        return output
    
    for i in range(10):
        random.seed(i)
        noise = [random.randint(1, 3) for i in range(mapsize)]
        print(f'{i}|', *adjacent_min(noise))
noiser02()