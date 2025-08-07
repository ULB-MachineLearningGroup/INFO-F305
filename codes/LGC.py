import numpy as np

class LGC:
    def __init__(self, seed: int = 25):
        self.current = seed
        self.a = 7**5
        self.c = 0
        self.m = 2**31 - 1

    def __call__(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current/self.m

generator = LGC()

for i in range(5):
    print(generator(), end=" ")

# Sortie:
# 0.00019565923148564027 0.2884447035791561 0.8901330548758307 0.46625329808623217 0.31918093530423053 