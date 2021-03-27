n,m,k=map(int,input().split()) # m개까지 더해서 하나당 k번 중복가능
numbers=[]
sum=0
numbers=list(map(int,input().split()))
# 주의, list내의 원소는 string 취급임.
# new_list=sorted(numbers) list를 오름차순 또는 알파벳순으로 정렬
# numbers.sort() 기존 list를 오름차순 정렬
numbers.sort()
# 오름차순 정렬 numbers=[1,2,3,6,6]
first = numbers[n-1]
while True:
    for i in range(k):
        if m==0:
            break
        sum=sum+first # 가장 큰 애부터 k번 더하고
        m=m-1 # m는 그만큼 줄고
    numbers.pop()  # 맨 뒤를 뺀다.
    n=n-1
    if m==0:
        break
print(sum)
# for num in numbers:
#     sum = sum + num * k
#     numbers = numbers.pop() # 맨 앞에서부터 제거

