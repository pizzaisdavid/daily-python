from math import pi as PI

def calculator(filename):
    object_mass, statistics = setup(filename)
    calculate = Calculate(object_mass)
    DECIMAL_PLACE = 3
    for statistic in statistics:
        name, radius, density = statistic
        force = calculate.weight(radius, density)
        print(name, ': ', round(force, DECIMAL_PLACE), sep='')
   
def setup(filename):
    object_mass, count, *planets = open(filename)
    statistics = []
    for planet in planets:
        name, radius, density = planet.split(',')
        statistics.append([name, int(radius), int(density)])
    return int(object_mass), statistics

class Calculate:
    def __init__(self, object_mass):
        self.object_mass = object_mass

    def weight(self, radius, density):
        self.radius = radius
        self.density = density
        Calculate.volume(self)
        Calculate.mass(self)
        return Calculate.force(self)
    
    def volume(self):
        self.volume = 4/3 * PI * self.radius**3

    def mass(self):
        self.mass = self.volume * self.density

    def force(self):
        G = 6.67e-11
        distance = self.radius**2
        return G * self.object_mass * self.mass / distance
         
calculator('planets.txt')
