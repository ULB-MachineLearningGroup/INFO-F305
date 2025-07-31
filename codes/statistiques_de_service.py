import simpy
import random

class Client():
    def __init__(self, name: str, environment: simpy.Environment, resource: simpy.Resource, time_before_served: list):
        self.name = name
        self.time_before_served = time_before_served
        self.environment = environment
        self.resource = resource
        self.process = self.environment.process(self.enter())

    def enter(self):
        with self.resource.request() as req:
            yield req
            time_of_service = self.environment.now
            t = random.expovariate(1)
            yield self.environment.timeout(t)
            self.time_before_served.append(self.environment.now - time_of_service)

time_before_served = []
environment = simpy.Environment()
resource = simpy.Resource(environment, capacity=2)
for i in range(5):
    Client(i, environment, resource, time_before_served)
environment.run(until=60)