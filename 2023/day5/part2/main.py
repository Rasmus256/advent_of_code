seeds = []
seed_to_soil_map={}

def parseMaps(Lines):
    seedList = Lines[0].strip().split(":")[1].strip().split(" ")
    maps = {}
    Lines = Lines[2:]
    for i in range(6):
        Lines = [l.strip() for l in Lines]
        temp_idx = Lines.index('')
        m =Lines[: temp_idx]
        mapid = m[0].split(" ")[0]
        maps[mapid] =  [constructMap(l) for l in m[1:]]
        Lines = Lines[temp_idx + 1: ]
    m = Lines[0].split(":")
    mapid = m[0].split(" ")[0]
    maps[mapid] =  [constructMap(l) for l in Lines[1:]]
    return (seedList, maps)

def constructMap(l):
    return {
            "dst": int(l.strip().split(" ")[0]),
            "src": int(l.strip().split(" ")[1]),
            "cnt": int(l.strip().split(" ")[2]), 
            "dlt": int(l.strip().split(" ")[1]) - int(l.strip().split(" ")[0])
    }

def maintask(filename):
    global seeds
    global seed_to_soil_map
    file1 = open(filename, 'r')
    Lines = file1.readlines() 
    finalSum = 0
    (seeds, seed_to_soil_map) = parseMaps(Lines)
    for i in range(100000000):
        if seed_id_in_input(location_to_seed(i)):
            return i
        if i % 100000 == 0:
            print("Status: looped through " + str(i))

def seed_id_in_input(lookupId):
    global seeds
    n=2
    pairs = [seeds[i * n:(i + 1) * n] for i in range((len(seeds) + n - 1) // n )]
    return any([int(p[0]) <= lookupId and int(p[0]) + int(p[1]) > lookupId for p in pairs ])

def location_to_seed(lookupId):
    return soil_to_seed(fertilizer_to_soil(water_to_fertilizer(light_to_water(temperature_to_light(humidity_to_temperature(location_to_humidity(lookupId)))))))

def soil_to_seed(lookupId):
    return maplookup(lookupId, 'seed-to-soil')
def fertilizer_to_soil(lookupId):
    return maplookup(lookupId, 'soil-to-fertilizer')
def water_to_fertilizer(lookupId):
    return maplookup(lookupId, 'fertilizer-to-water')
def light_to_water(lookupId):
    return maplookup(lookupId, 'water-to-light')
def temperature_to_light(lookupId):
    return maplookup(lookupId, 'light-to-temperature')
def humidity_to_temperature(lookupId):
    return maplookup(lookupId, 'temperature-to-humidity')
def location_to_humidity(lookupId):
    return maplookup(lookupId, 'humidity-to-location')
def maplookup(lookupId, mapname):
    global seed_to_soil_map
    m = seed_to_soil_map[mapname]
    rule = [lookupId+r['dlt'] for r in m if r['dst'] <= lookupId and r['dst']+r['cnt'] > lookupId]
    if len(rule) == 0:
        return lookupId
    elif len(rule) > 1:
        print("WHAT. MULTIPLE RULES MATCHED!")
    return rule[0]

if __name__ == '__main__':
    print(maintask("puzzle_input.csv"))
