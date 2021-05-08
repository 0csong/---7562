n=int(input())
m=int(input())
maps=[[0]*n for _ in range(n)]
visited=[False]*n

def bfs(x):
    global count
    for i in range(n):
        if maps[x][i]==1 and not visited[i]:
            visited[i]=True
            count+=1
            bfs(i) 
   
for i in range(m):
    a,b=map(int,input().split())
    maps[a-1][b-1]=1
    maps[b-1][a-1]=1
count=0
visited[0]=True
bfs(0)
print(count)


#다음 방법
import sys
r = sys.stdin.readline #노드의 개수




def dfs(v, egs, ans):#함수가 종료되는 순간은 egs[v]를 다 방문햇을때
    #여기서 종료되는 순간은 egs[5]=[1,2,6]인데 egs[6]=5에서 
    #다시 egs[5]로와서 이미 126을 다 방문햇을때
    for i in egs[v]: #i가 2일때 첫실행
        if i not in ans:
 #i는 2,3,5,6으로 출력 
            ans.append(i)
            dfs(i, egs, ans)
    return ans


N = int(r()) #간선의 개수
edges = [[] for _ in range(N+1)] #간선의 리스트를 만듬
for _ in range(1, int(r())+1):
    e1, e2 = map(int, r().split()) #이어진 점 입력받음
    edges[e1].append(e2) # 리스트에 저장에서 두줄리스트로 만듬
    edges[e2].append(e1)

print(len(dfs(1, edges, [1]))-1)#이미 ans에 1넣어줌