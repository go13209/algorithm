import sys
from collections import Counter

lst = []
for _ in range(int(sys.stdin.readline())):
    lst.append(sys.stdin.readline().rstrip())

lst.sort()

book_selling_list = Counter(lst)

print(max(book_selling_list, key=book_selling_list.get))
