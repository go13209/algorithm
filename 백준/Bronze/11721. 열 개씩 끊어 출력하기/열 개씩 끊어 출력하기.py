str = input()

while True:
    print(str[:10])
    str = str.replace(str[:10], '')
    if len(str) < 10:
        print(str)
        break