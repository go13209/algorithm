T =  int(input())
answers = []
for t in range(T):
    answer = int(input())
    answers.append(answer)
if answers.count(1) > answers.count(0):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')