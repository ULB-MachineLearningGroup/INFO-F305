import numpy as np

class VonNeumann:
    def __init__(self, seed: int = 1234, digits: int = 4):
        self.current = seed
        self.digits = digits

    def __call__(self):
        squared = str(self.current ** 2).zfill(2 * self.digits)
        mid_start = (len(squared) - self.digits) // 2
        self.current = int(squared[mid_start:mid_start + self.digits])
        return self.current / (10 ** self.digits)

generator = VonNeumann()

for i in range(5):
    print(generator(), end=" ")

# Sortie:
# 0.5227 0.3215 0.3362 0.303 0.1809 