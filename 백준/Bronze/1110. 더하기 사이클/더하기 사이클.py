number = int(input())
number_list = [number]
cnt = 0
for number in number_list:
        a = number // 10
        b = number % 10
        new_number = (b * 10) + ((a + b) % 10)
        cnt += 1
        if new_number not in number_list:
            number_list.append(new_number)
        else:
            print(cnt)