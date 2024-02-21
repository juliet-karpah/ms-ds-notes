def lcs(s1, s2):
    m,n = len(s1), len(s2)
    memo_tbl = [[0 for j in range(n+1)] for i in range(m+1)]
    sol_info = [['' for j in range(n+1)] for i in range(m+1)]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s1[i] == s2[j]:
                memo_tbl[i][j] = 1 + memo_tbl[i+1][j+1]
                sol_info[i][j] = 'match'
            else:
                memo_tbl[i][j],sol_info[i][j] = max((memo_tbl[i+1][j],'right'), (memo_tbl[i][j+1],'down'))
    
    lcs_result = ''
    match_ids = []
    i,j = 0,0
    while(i < m and j < n):
        if sol_info[i][j] == 'match':
            lcs_result = lcs_result + s1[i]
            match_ids.append((i,j))
            i,j = i+1, j+1
        elif sol_info[i][j] == "right":
            i, j = i+1, j
        else:
            assert sol_info[i][j] == 'down'
            i, j = i, j + 1
    return lcs_result, match_ids