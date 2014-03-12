chain_length = 6

def generate_figurate(p, start, end):
    n = 1

    while True:
        if p == 3:
            num = (n * (n + 1)) / 2
        elif p == 4:
            num = n**2
        elif p == 5:
            num = (n * ((3*n) - 1)) / 2
        elif p == 6:
            num = (n * ((2*n) - 1))
        elif p == 7:
            num = (n * ((5*n) - 3)) / 2
        elif p == 8:
            num = (n * ((3*n) - 2))

        n += 1

        if num < start:
            continue
        elif num > end:
            break
        else:
            yield num


figurate_numbers = []
for p in range(3, 3 + chain_length):
    figurate_numbers.append(list(generate_figurate(p, 1000, 9999)))

begin_sets = []
end_sets = []

for p, numbers in enumerate(figurate_numbers):
    begin_sets.append({})
    end_sets.append({})

    for n in numbers:
        begin = str(n)[:2]
        end = str(n)[2:]

        lst = begin_sets[p].setdefault(begin, [])
        lst.append(n)

        lst = end_sets[p].setdefault(end, [])
        lst.append(n)

def validate_chain(n, current_chain, remaining_sets):
    current_chain.append(n)

    if len(current_chain) > chain_length:
        return False
    elif len(current_chain) == chain_length:
        if str(current_chain[-1])[2:] == str(current_chain[0])[:2]:
            return current_chain
        else:
            return False

    end = str(n)[2:]

    candidate_groups = []
    for i, s in enumerate(remaining_sets):
        found =  s.get(end, [])

        if found:
            candidate_groups.append([i, found])

    if not candidate_groups:
        return False

    for i, candidates in candidate_groups:
        remaining = remaining_sets[0:i] + remaining_sets[i+1:]

        for c in candidates:
            found_chain = validate_chain(c, current_chain[:], remaining)

            if found_chain:
                return found_chain

    return False

for n in figurate_numbers[0]:
    chain = validate_chain(n, [], begin_sets[1:])

    if chain:
        break

print "Chain: %s" % chain
print "Sum: %s" % sum(chain)
