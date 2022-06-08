import sys,math

if len(sys.argv) > 1:
    r = int(sys.argv[1])

print(f'{math.pi*r*r:.10f}')