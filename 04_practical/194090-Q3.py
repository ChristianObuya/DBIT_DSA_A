def head_count(n):
   if n < 0:
     return
   head_count(n -1)
   print(n)
 
head_count(5)