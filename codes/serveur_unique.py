import simpy
import random

class Client():
    def __init__(self, name: str, env: simpy.Environment, resource: simpy.Resource):
        self.name = name
        self.env = env
        self.resource = resource
        self.process = self.env.process(self.enter())

    def enter(self):
        with self.resource.request() as req:
            yield req
            t = random.uniform(0, 10)
            print(f"{self.name} enters at {self.env.now:.3f}.")
            print(f"He will stay for {t:.3f}.")
            yield self.env.timeout(t)
        print(f"{self.name} leaves at {self.env.now:.3f}.")

env = simpy.Environment()
resource = simpy.Resource(env, capacity=1)
for i in range(5):
    Client(i, env, resource)
env.run(until=30)