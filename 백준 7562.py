from collections import deque
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(x,y,z,a,n):
    q=deque()
    q.append([x,y])
    graph[x][y]=1 #시작점을 구분하기위해서 만약 0으로하면 시작점을 다시 들릴수도잇음
    while q:
        x,y=q.popleft()
        if x==z and y==a:
            return graph[x][y]-1 #최종적으로는 이곳에 올테니 그때 값을 하나 빼줌
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                    q.append([nx,ny])
                    graph[nx][ny]=graph[x][y]+1
                    
        
s=int(input())
for i in range(s):
    n=int(input())
    graph=[[0]*n for i in range(n)]
    a,b=map(int,input().split()) #시작 위치 
    c,d=map(int,input().split()) #최종위치
    ans=bfs(a,b,c,d,n)
    print(ans)
    
    
   
   백준 나이트의 이동 
    https://www.acmicpc.net/problem/7562
