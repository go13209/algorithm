while True:
    try:
        n = int(input())
    except:
        break

    num = '1'
    while True:
        if int(num) % n == 0:
            print(len(num))
            break
        num += '1'