import sys

if (len(sys.argv) != 2):
    print(f"Usage: {sys.argv[0]} <amount>")
    exit(1)

cont = 0
for i in range(int(sys.argv[1])):
    print('\'{}teste\','.format(i))
    cont += 1
