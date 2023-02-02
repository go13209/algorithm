import sys

daytime, nighttime, height = map(int, sys.stdin.readline().split())

if (height-daytime) % (daytime-nighttime) == 0:
    print((height-daytime) // (daytime-nighttime) + 1)
else:
    print((height-daytime) // (daytime-nighttime) + 2)