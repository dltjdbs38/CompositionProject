
n=int(input()) # 출석 부른 횟수
nums=input().split() # ['1','2','3'] list class이다.
# print(nums)
# print(type(nums))
# for i in range(1,n): # range(1,n)이면 1,2
#     print(i) # range(n) 이면 0,1,2

for i in range(n):
    nums[i]=int(nums[i]) #int 처리

d=[0 for _ in range(24)]
# d=[]
# for i in range(1,24):
#     d.append(0)

# 출석 count
for i in range(n): # 0~23
    d[nums[i]]=d[nums[i]]+1

# print(d)
for i in range(1,24): # 1 2 3...23
    print(d[i], end=' ')
