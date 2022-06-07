set_a = {('anne', 'bjarne'), ('bjarne', 'anne'), ('bjarne', 'cecilie'), ('cecilie', 'daniel'), ('daniel', 'cecilie'), ('eva', 'eva')}
# set_b = {(4, 8), (8, 7), (7, 4)}

union = set_a # | set_b
print(union)

def transitiveclosure(d):
    new_set = set(d)
    while True:
        new_path = set()
        for a in new_set:
            for b in new_set:
                direct_path = (a[0], b[1])
                if a[1] == b[0] and not (direct_path in new_set):
                    # print(f'found {a} and {b} adding {direct_path}')
                    new_path.add(direct_path)
        new_set = new_set | new_path
        if len(new_path) == 0:
            return new_set


print(transitiveclosure(union))
