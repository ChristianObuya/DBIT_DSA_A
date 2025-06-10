def tail_sum(n, acc=0):
   if n == 0:
     return acc
   else:
     return tail_sum(n - 1, acc + n)

print(tail_sum(8))