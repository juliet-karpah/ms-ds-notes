"""
# Dynamic Programming: The Rod Cutting Problem

__Input:__ You are given 
  * length of rod `L` a natural number and 
  * List `sizes`  `[l1, l2, .., lk]`  of possible lengths that we can cut the rod and
  * List `prices`  how much money does each length of rod yield `[p1, p2, .., pk]`
  * Note: The `sizes` and `prices` list must have the same length.

__Assumptions:__ $k \geq 1$, `L` is positive whole number, `li` are all positive, whole numbers, and prices `pi` are positive. 

__Question:__ Why are they reasonable assumptions to make? What do we do if these assumptions do not hold? Ask us on the forum.


"""


def max_revenue(L, sizes, prices):
    memo_table = [0] * (L + 1)
    best_options = [-1] * (L + 1)
    assert len(prices) == len(sizes)
    k = len(sizes)
    for l in range(1, L+1):
        memo_table[l] = 0
        values = [(prices[i] + memo_table[l-sizes[i]], i) for i in range(k) if l - sizes[i] >= 0]
        values.append((0, -1))
        (memo_table[l], best_options[l]) = max(values)
    cuts = []
    l = L 
    while l > 0:
        option_i = best_options[l] # which option is best for length l
        if option_i >= 0:
            cuts.append(sizes[option_i]) # add option to cut
            l = l - sizes[option_i] # reduce length of rod
        else:
            break
    return memo_table[L], (cuts)