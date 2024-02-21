"""
Longest Stable Subsequence
"""
def lssLength(a, i, j):
    aj = a[j] if 0 <= j < len(a) else None 
    # Implement the recurrence below. Use recursive calls back to lssLength
    n = len(a)
    if i == n:
        return 0
    if i == 0:
        return 1 + lssLength(a, i+1, i)
    if i < n and a[j] != None and abs(a[i] - a[j]) > 1:
        return lssLength(a,i+1, j)
    elif i < n and (a[j] == None or abs(a[i] - a[j]) <= 1):
        return max(1 + lssLength(a,i+1, i),lssLength(a,i+1, j))
    
def memoizeLSS(a):
    T = {}  
    n = len(a)
    for j in range(-1, n):
        T[(n, j)] = 0 # i = n and j 

    for i in range(0,n+1):
        for j in range(-1,n+1):
            T[(i,j)] = 0

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            aj = a[j] if 0 <= j < len(a) else None
            if aj != None and abs(a[i] - a[j]) > 1:
                T[(i,j)] = T[(i+1, j)]
            elif aj == None or abs(a[i] - a[j]) <= 1:
                T[(i, j)] = max(1 + T[(i+1, i)],T[(i+1, j)])
                
    for i in range(n-2, -1, -1):
        T[(i, -1)] = max(T[(i+1, -1)], T[(i+1, 0)], T[(i,0)], 0)
        
    return T


def computeLSS(a):
    # your code here
    T = {}
    S = {}
    n = len(a)
    for j in range(-1, n):
        T[(n, j)] = 0 # i = n and j
        S[(n, j)] = 'empty'

    for i in range(0,n+1):
        for j in range(-1,n+1):
            T[(i,j)] = 0
            S[(i,j)] = ''

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            aj = a[j] if 0 <= j < len(a) else None
            if aj != None and abs(a[i] - a[j]) > 1:
                T[(i,j)] = T[(i+1, j)]
                S[(i,j)] = 'right'
            elif aj == None or abs(a[i] - a[j]) <= 1:
                T[(i, j)], S[(i, j)] = max((1 + T[(i+1, i)], 'match'),(T[(i+1, j)], 'right'))
                
    for i in range(n-2, -1, -1):
        T[(i, -1)] = max(T[(i+1, -1)], T[(i+1, 0)], T[(i,0)])
        S[(i, -1)] = 'empty'
    longest_stable = []
    i,j = 0,0
    while (i < n and j < n):
        if S[(i,j)] == 'match':
            longest_stable.append(a[i])
            i, j = i+1, i
        else:
            i, j = i+1, j
    
    return longest_stable

"""
Target sum
"""

def targetSum(S, i,  tgt):
    # your code here
    k = len(S)
    if tgt < 0:
        return float('inf')
    if i >= k and tgt >= 0:
        return tgt
    res = min(targetSum(S, i+1, tgt-S[i]), targetSum(S, i+1, tgt))
    return res

def memoTargetSum(S, tgt):
    k = len(S)
    assert tgt >= 0
    ## Fill in base case for T[(i,j)] where i == k
    T = {} # Memo table initialized as empty dictionary

        
    # your code here
    for i in range(k):
        for j in range(tgt):
            T[(i,j)] = 0

    for j in range(tgt+1):
        T[(k,j)] = j    
        
    def lookupMemoTable(x,y,s):
        if y < s:
            return T[(x,y)]
        else:
            return min(T[(x,y)], T[(x, y-s)])
                
    for i in range(k-1, -1, -1):
        for j in range(1,tgt+1):
            T[(i,j)] = lookupMemoTable(i+1,j,S[i])
    return T

def getBestTargetSum(S, tgt):
    k = len(S)
    assert tgt >= 0
    # your code here
    T = {} # Memo table initialized as empty dictionary
    s = {} # Recovery table

    for i in range(k):
        for j in range(tgt):
            T[(i,j)] = 0

    for j in range(tgt+1):
        T[(k,j)] = j    
        
    def lookupMemoTable(x,y,s):
        if y < s:
            return T[(x,y)],0
        else:
            return min((T[(x,y)],0), (T[(x, y-s)],1))
                
    for i in range(k-1, -1, -1):
        for j in range(1,tgt+1):
            T[(i,j)], s[(i,j)] = lookupMemoTable(i+1,j,S[i])
            
    # recover the solution
    res = []
    targetNumber = tgt
    for j in range(k):
        if targetNumber > 0 and s[(j,targetNumber)] == 1:
            res.append(S[j])
            targetNumber = targetNumber - S[j]
    return res