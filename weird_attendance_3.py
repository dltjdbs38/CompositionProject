n=int(input())
nums=input().split() # 0~9

for i in range(n):
    nums[i]=int(nums[i]) # int 처리
# print(nums)

# sol 1
# nums.sort() # 오름차순 [19 21 38 53 62]
# print(nums[0])
# nums.sort(reverse=True) # 내림차순 [62 53 38 21 19]

# sol 2
# print(min(nums))

# sol 3
min=nums[0]
for i in nums:
  if i<min:
      min=i
print(min)
#
