# import sys
# sys.stdin = open("input.txt")
T=int(input())
# 오-아래-왼-위 방향 순서로 map의 끝에 다다르거나
# 가려는 방향에 값이 0이 아닐 경우 방향 바꾸도록.
dy=[1,0,-1,0] # 인덱스는 d: 0 오른 2 왼
dx=[0,1,0,-1] # 1 아래 3 위
for i in range(1,T+1):
    N=int(input()) # N=3
    map1=[[0 for i in range(N)] for j in range(N)]
     # [[0,1,2], [0,1,2], [0,1,2]]
    d,x,y=0,0,0 # x=0~2, y=0~2 d는 방향
    #d 0:오, 1:아래, 2:왼, 3:위
    # count = 달팽이에 넣어지는 숫자 1~9
    for count in range(1,N*N+1):
        map1[x][y]=count # [[1,0,0][0,0,0][0,0,0]]
        # x,y = 00 01 02 12 22//방향바꿔 21 20 10 11
        x=x+dx[d] #d=0 x=0
        y=y+dy[d] # y=1
        # 1) x,y가 최소 0 최대 N-1까지 범위를 벗어나거나
        # 2) 이미 count가 0이 아닌 다른 값이 차 있다면
        # => d 방향 바꿈.
        if x>=N or y>=N or x<0 or y<0 or map1[x][y]!=0:
            # 실행취소 ( 방향 바꿈)
            x=x-dx[d]
            y=y-dy[d]
            d=(d+1)%4 #d=0123 (4567) 0123 0123
            # 다시 go
            x=x+dx[d]
            y=y+dy[d]
    print('#%d' %i, end='\n')
    for x in map1: # [[0,1,2], [0,1,2], [0,1,2]]
        # print(x)
        # print 할 때 list 앞에 *를 붙이면 []가 출력되지 않음.
        print(*x)







