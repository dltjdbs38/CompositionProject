# 2차원 배열 만들고
# list[i][j]
# 바둑돌의 좌표 1 1(1,1) 를 받아서 그 부분만 1로 출력

d=[]
for i in range(20): #19 가로
    d.append([]) # 리스트 안에 다른 리스트
    for j in range(20): # 19 가로
        d[i].append(0) # 리스트 안에 들어있는 리스트 안에 0 추가하기
print(d)
n=int(input())
for i in range(n):
    x,y=input().split()
    d[int(x)][int(y)]=1

for i in range(1,20): #1~19
    for j in range(1,20):
        print(d[i][j],end=' ') # 공백 두고 1 0 0
    print() # 줄바꿈
