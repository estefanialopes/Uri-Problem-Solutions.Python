while True:
   N = int(input())
   if N == 0:
       break
   H = [int(i) for i in input().split()]
   H.append(H[0])
   H.append(H[1])
   p = 0
   for j in range(1, N+1):
       if H[j] < H[j-1] and H[j] < H[j+1]:
           p += 1
       elif H[j] > H[j-1] and H[j] > H[j+1]:
           p+= 1
   print(p)
 
