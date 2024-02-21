"""
## Knapsack Problem (Zero-One Version)

__Inputs:__ Weight limit $W$, list of item weights $[w_1, \ldots, w_k]$, and list of item values $[v_1, \ldots, v_k]$.

__Output:__ For each item, we can choose it in our Knapack $n_i = 1$ or leave it out of our knapsack $n_i = 0$ so that  
   1. Total weight is under the knapsack weight limit: $n_1 w_1 + \cdots + n_k w_k \leq W$. Note here that each $n_i \in \{ 0, 1\} $, depending on whether the item \# i is chosen or not.
   2. The value of stolen goods is maximized: $n_1 v_1 + \ldots + n_k v_k $ is max.
"""

def max_knapsack(W, j, weights, values):
    n = len(weights)
    assert n == len(values)
    assert W >= 0
    if W == 0:
        return 0, []
    T = [ [0 for j in range(n)] for w in range(W+1)]
    S = [[0 for j in range(n)] for w in range(W+1)]

    def get_tbl_entry(w, j):
        if w == 0:
            return 0
        if w < 0:
            return -float('inf')
        if j >= n:
            return 0
        return T[w][j]
    
    for w in range(1, W+1):
        for j in range(n-1, -1, -1):
            (T[w][j], S[w][j]) = max((values[j] + get_tbl_entry(w-weights[j], j+1),1), get_tbl_entry(w,j+1),0)
    goods_to_take = []
    capacity = W
    for j in range(n):
        if S[capacity][j] == 1:
            goods_to_take.append(j)
            capacity = capacity - weights[j]
    return (T[w][0], goods_to_take)

            
