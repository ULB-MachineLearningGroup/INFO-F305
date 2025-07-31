import simpy
import random

LAMBDA_ARRIVEE_CLIENTS = 0.2
LAMBDA_LOCATION = 0.05
LAMBDA_CHARGE = 1.5
NOMBRE_VEHICULES = 4
SIMULATION_DUREE = 14 * 60
NOMBRE_ITERATIONS = 1000

class ChargeVehicule:
    def __init__(self, env):
        self.env = env
        self.vehicules = simpy.Resource(env, NOMBRE_VEHICULES)
        self.recharges = [0] * NOMBRE_VEHICULES
        self.vehicule_id = 0

    def louer(self, duree_location):
        yield self.env.timeout(duree_location)

    def charger(self, duree_charge):
        yield self.env.timeout(duree_charge)
        # On incremente le compteur de recharges du vehicule loue
        self.recharges[self.vehicule_id] += 1

def processus_client(env, client_id, charge_vehicule, temps_attente):
    temps_entree = env.now
    # Le client essaie de louer un vehicule
    with charge_vehicule.vehicules.request() as request:
        yield request
        temps_attente.append(env.now - temps_entree)
        # Le client utilise le vehicule pour une duree exponentielle
        duree_location = random.expovariate(LAMBDA_LOCATION)
        yield env.process(charge_vehicule.louer(duree_location))

        # Le vehicule est mis en charge apres utilisation
        duree_charge = random.expovariate(LAMBDA_CHARGE)
        yield env.process(charge_vehicule.charger(duree_charge))

        charge_vehicule.vehicule_id = (charge_vehicule.vehicule_id + 1) % NOMBRE_VEHICULES

def parc(env, charge_vehicule, temps_attente):
    client_id = 0
    while True:
        # Un client arrive
        yield env.timeout(random.expovariate(LAMBDA_ARRIVEE_CLIENTS))
        env.process(processus_client(env, client_id, charge_vehicule, temps_attente))
        client_id += 1


nombre_de_recharges = []
temps_attente = []

for _ in range(NOMBRE_ITERATIONS):
    env = simpy.Environment()
    charge_vehicule = ChargeVehicule(env)
    env.process(parc(env, charge_vehicule, temps_attente))
    env.run(until=SIMULATION_DUREE)

    nombre_de_recharges.extend(charge_vehicule.recharges)

temps_attente_moyen = np.mean(temps_attente)
print(f"Moyenne du temps d'attente: {temps_attente_moyen:.2f}")
plt.figure(figsize=(8, 8))
plt.hist(temps_attente, bins=150)
plt.grid()
plt.show()

moyenne_recharges = np.mean(nombre_de_recharges)
print(f"Moyenne des recharges par vehicule : {moyenne_recharges:.2f}")
plt.figure(figsize=(8, 8))
plt.hist(nombre_de_recharges, bins=50)
plt.grid()
plt.show()