import sys

dict = {}

for _ in range(int(sys.stdin.readline())):
    file_name, extension = (sys.stdin.readline().rstrip()).split('.')
    
    if extension not in dict:
        dict[extension] = 1
    else:
        dict[extension] += 1

for key in sorted(dict.keys()):
    print(key, dict[key])