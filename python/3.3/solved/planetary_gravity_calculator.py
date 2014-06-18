from math import pi as PI

def calculator(filename):
    object_mass, statistics = setup(filename)
    find = Find(object_mass)
    DECIMAL_PLACE = 3
    for statistic in statistics:
        name, _, _ = statistic
        force = find.weight(statistic)
        weight = round(force, DECIMAL_PLACE)
        print(name, ': ', weight, sep='')
   
def setup(filename):
    mass, count, *planets = open(filename)
    statistics = []
    for planet in planets:
        name, radius, density = planet.split(',')
        statistics.append([name, int(radius), int(density)])
    return int(mass), statistics

class Find:
    def __init__(self, object_mass):
        self.object_mass = object_mass

    def weight(self, statistic):
        G = 6.67e-11
        name, radius, density = statistic
        volume = 4/3 * PI * radius**3
        planet_mass = volume * density
        force = G * self.object_mass * planet_mass / radius**2
        return force

calculator('planets.txt')
