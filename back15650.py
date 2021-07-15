N, M = map(int, input().split())
numbers = list(range(1, N+1))
result = []
def com(n, m, l):
    if m == 0:
        print(' '.join(map(str, result)))
        return 
    else :
        for i in l:
            result.append(i)
            l = l[1:]
            com(n, m-1, l)
            result.pop()
            

com(N, M, numbers)
        
    