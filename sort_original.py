import sys

desc = False
if sys.argv[1] == 'desc':
    args = sys.argv[2:]
    desc = True
else:
    args = sys.argv[1:]
numbers = list(map(int, args))
numbers.sort(reverse = desc)
print(numbers)
