r,g,b=map(int,input().split())
# r, g, b에 각각 가능한 색깔 입력받음
for i in range(r): # 오름차순이니까 가장 마지막 자리수부터 증가
    for j in range(g):
        for k in range(b):
            print(i,j,k)
print(r*g*b)
# r1=r # 2 바뀌지 않는 것
# g1=g # 3
# b1=b # 2
# while True: # 0 0 0 / 0 0 1 / 0 0 2
#     r=r-r1 # 0
#     g=g-g1 # 0
#     for b in range(0,b1): # 오름차순이니까 가장 마지막 자리수부터 증가
#         print('%d %d %d' %(r,g,b))
#         # b=b+1
#     g=g+1 #1
#     if g==g1:
#         r=r+1 #1
#     elif g==g1 and r==r1:
#         break
# print(r1*g1*b1)