# nst = []
# mst = []
# n = int(input())
# nst = list(map(int, input().split()))
# m = int(input())
# mst = list(map(int, input().split()))
#
# for j in mst:
#     l = 0
#     r = len(nst) - 1
#     while (l < r):
#         mid = (l + r) // 2
#         if (nst[mid] >= j):
#             r = mid
#         else:
#             l = mid + 1
#     k = 0
#     if (nst[l] != j):
#         k = 0
#     else:
#         k=k+1
#         for i in range(l, len(nst)-1):
#             if(nst[i+1]!=j):
#                 break
#             else:k=k+1
#         for i in range(l-1, 0, -1):
#             if (nst[i] != j):
#                 break
#             else:
#                 k = k + 1
#     print(k)
#

def counter():
    count=0
    def wrap():
        nonlocal count
        count+=1
        print(count)
    return wrap
c1= counter()
c2=counter()
c1()
c1()
c1()
c1()
c2()
c2()
c1()
