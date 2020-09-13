from collections import OrderedDict
sequence = OrderedDict()

for _ in range(int(input())):
    key = input()
    sequence.setdefault(key, 0)
    sequence[key] += 1
   
print(len(sequence))
print(*sequence.values())
