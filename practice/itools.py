import itertools

# Simple counter with a start and step value
counter = itertools.count(1)
data = [100, 200, 300, 400]
mapped = zip(counter, data)
for k, v in mapped:
    print(k, v)

# Cyclic Iterator
cyclic_counter = itertools.cycle((0, 5, 10, 20))
data = [20, 10, 5, 0, 1, 4, 7]
mapped_2 = zip(cyclic_counter, data)
for k, v in mapped_2:
    print(k, v)
# Repeating Iterator
repeater = list(itertools.repeat('x', times=3))
print(repeater)

# Use case for a repater -> Calculate the first 5 cubes
first_5_cubes = list(map(pow, range(5), itertools.repeat(3)))

print(first_5_cubes)

# Combinations (order is not important) (a,b) = (b,a)
letters = ['A', 'B', 'C']
combs = itertools.combinations(letters, 2)
print(list(combs))

# Permutations (order is important) (a,b) != (b,a)
letters_2 = ['A', 'B', 'C']
perms = itertools.permutations(letters_2, 2)
print(list(perms))
