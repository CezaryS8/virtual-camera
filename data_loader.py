from point import Point

def load_data_from_file(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                data = line.split(',')
                x1, y1, z1, x2, y2, z2 = map(int, data)
                lines.append((Point(x1, y1, z1), Point(x2, y2, z2)))
    return lines
