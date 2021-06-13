import re


def initialization():
    global data
    f = open('Input/input_day_23.txt', 'r')
    in_data = f.read()
    f.close()
    lines = in_data.splitlines()
    data = [re.findall(r"-?\d+", l) for l in lines]
    return [[(int(d[0]), int(d[1]), int(d[2])), int(d[3])] for d in data]


data = initialization()


def get_distance(p, q):
    xp, yp, zp = p
    xq, yq, zq = q
    return abs(xp - xq) + abs(yp - yq) + abs(zp - zq)


def get_position_distance(p):
    return get_distance((0, 0, 0), p)


def get_number_of_drones():
    global data
    radius = [d[1] for d in data]
    max_radius = max(radius)
    index = radius.index(max_radius)
    distances = [get_distance(data[index][0], d[0]) for d in data]
    return sum(d <= max_radius for d in distances)


def get_radius_hits(vec):
    global data
    return sum([get_distance(vec, d[0]) <= d[1] for d in data])


def get_maximum_radius_hits():
    global x, y, z, coordinate, maximum_hits
    searched_coordinates = []
    max_radius_hits = 0
    scan_distance = 3
    steps = 1000000
    x, y, z = 0, 0, 0
    while True:
        coordinates = []
        rg = range(-steps * scan_distance, steps * scan_distance, steps)
        for coordinate in [(x + dx, y + dy, z + dz) for dx in rg for dy in rg for dz in rg]:
            if coordinate not in searched_coordinates:
                coordinates.append(coordinate)
                searched_coordinates.append(coordinate)
        if not coordinates:
            return x + y + z
        coordinates = [[coord, get_radius_hits(coord), get_position_distance(coord)] for coord in coordinates]
        maximum_hits = max([d[1] for d in coordinates])
        coord_with_max_hits = list(filter(lambda coord: coord[1] == maximum_hits, coordinates))
        max_hits_and_min_distance = min(coord_with_max_hits, key=lambda coord: coord[2])
        coordinate = max_hits_and_min_distance[0]
        if max_hits_and_min_distance[1] < max_radius_hits:
            steps /= 10
            steps = 1 if steps < 1 else int(steps)
        else:
            max_radius_hits = maximum_hits
            x, y, z = coordinate


result_1 = get_number_of_drones()
result_2 = get_maximum_radius_hits()

print("Result part 1: ", result_1)
print("Result part 2: ", result_2)