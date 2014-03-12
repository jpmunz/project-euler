target = 5
n = 1
cubes = {}

while True:
    cube = n**3

    digits = ''.join(sorted(str(cube)))

    matches = cubes.setdefault(digits, [])

    matches.append(cube)

    if len(matches) == target:
        print "Found candidate: %s" % matches
        print "Smallest cube: %s" % min(matches)
        break

    n += 1
