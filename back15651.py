N, M = map(int, input().split())
numbers = list(range(1, N+1))
result = []
def com(m, l):
    if m == 0:
        print(' '.join(map(str, result)))
        
        return 
    else :
        for i in l:
            result.append(i)
            com( m-1, l)
            result.pop()
            
            

com(M, numbers)
        
    