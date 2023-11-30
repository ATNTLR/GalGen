import random
import matplotlib.pyplot as plt

stars = [
    'o star', 'b star', 'a star', 'f star', 'g star', 'k star', 'm star'
]
STARTYPE = {
    'o star':0.00003,
    'b star':0.13,
    'a star':0.6,
    'f star':3.0,
    'g star':7.6,
    'k star':12.1,
    'm star':76.45,
}

GASPLANET = {
    'o star':0.5,
    'b star':0.5,
    'a star':40,
    'f star':90,
    'g star':90,
    'k star':90,
    'm star':90,
}

ROCKPLANET = {
    'o star':0.00003,
    'b star':0.00003,
    'a star':0.0005,
    'f star':90,
    'g star':90,
    'k star':90,
    'm star':90,
}

def startype():
    while True:
        proba = random.randint(0, 6)
        x = stars[proba]
        s = STARTYPE[x]
        starproba = random.randint(0, 100)
        if starproba >= 1:
            if s >= starproba:
                return x
        else:
            random_float = random.random()
            starproba = float(format(random_float, '.8f'))
            if s >= starproba:
                return x

def planet(s):
    num = random.randint(0,8)
    n = 0
    rp = 0
    gp = 0
    while n <= num:
        gas_or_rocky = random.randint(0,100)
        if gas_or_rocky >= 50:
            p = ROCKPLANET[s]
            planet_chance = random.randint(0,100)
            if planet_chance >= 1:
                if p >= planet_chance:
                    n += 1
                    rp += 1
                else:
                    n += 1
            else: 
                random_float = random.random()
                low_planet= float(format(random_float, '.8f'))
                if p >= low_planet:
                    n += 1
                    rp += 1
                else:
                    n += 1
        else:
            planet_chance = random.randint(0,100)
            p = GASPLANET[s]
            if planet_chance >= 1:
                if p >= planet_chance:
                    n += 1
                    gp += 1
                else:
                    n += 1
            else:
                random_float = random.random()
                low_planet= float(format(random_float, '.8f'))
                if p >= low_planet:
                    n += 1
                    gp += 1
                else:
                    n += 1
    return gp, rp
    
star = startype()
planets = planet(star)
gas_planets = planets[0]
rocky_planets = planets[1]
print(f'{star} with {gas_planets} gas planets and {rocky_planets} rocky planets')

startype()