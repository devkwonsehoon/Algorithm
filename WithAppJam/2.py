from itertools import combinations as comb

lst = [int(input()) for _ in range(9)]
all_lst = list(comb(lst, 7))

for i in all_lst:
  if sum(i) == 100:
    print(*sorted(i), sep="\n")
    break