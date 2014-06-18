from math import pi as PI

def calculator(filename):
    mass, statistics = setup(filename)
    find = Find(mass)
    DECIMAL_PLACE = 3
    for statistic in statistics:
        name, _, _ = statistic
        force = find.weight(statistic)
        force = round(force, DECIMAL_PLACE)
        print(name, ': ', force, sep='')
   
def setup(filename):
    mass, count, *planets = open(filename)
    statistics = []
    for planet in planets:
        name, radius, density = planet.split(',')
        radius = int(radius)
        density = int(density)
        statistics.append([name, radius, density])
    return int(mass), statistics

class Find:
    def __init__(self, mass):
        self.mass = mass

    def weight(self, statistic):
        G = 6.67e-11
        name, radius, density = statistic
        volume = 4/3 * PI * radius**3
        mass = volume * density
        force = G * self.mass * mass / radius**2
        return force

calculator('planets.txt')
