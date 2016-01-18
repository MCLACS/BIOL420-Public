def calculateFry(population, birthRate, survivalRate):
    return round((birthRate * population) * survivalRate, 0)

def calculateDeath(population, deathRate):
    return round(population * deathRate, 0)

def newPopulation(population, harvest, death, birth):
    ret = population - harvest - death + birth
    if (ret < 0):
        ret = 0
    return ret
