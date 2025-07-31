import simpy
import random

class Client():
    def __init__(self, name: str, env: simpy.Environment):
        self.name = name
        self.env = env
        self.process = self.env.process(self.enter())

    def enter(self):
        yield self.env.timeout(random.uniform(0, 10))
        print(f"{self.name} enters at {self.env.now:.3f}")
        yield self.env.timeout(5)
        print(f"{self.name} leaves at {self.env.now:.3f}")

env = simpy.Environment()
Client("1", env)
env.run(until=20)