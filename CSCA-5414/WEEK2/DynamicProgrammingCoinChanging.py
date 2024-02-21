"""
# Dynamic Programming: Coin Changing Problem.

We are given a list of possible denominations $lst: [c_1, \ldots, c_k]$ and an amount $x$ for which we wish to make change.

Choose numbers of coins $n_1, \ldots, n_k$ of coins $c_1, \ldots, c_k$, respectively so that
  1. $n_1 c_1 + \ldots + n_k c_k = x$, i.e, we provide _exact_ change
  2. The number of coins $n_1 + \ldots + n_k$ is minimized.
  
"""

def min_coins(target, coins):
    if target == 0:
        return 0
    if target < 0:
        return 1000000
    coins_used = []
    memo_table = [0] * (target + 1)
    best_coins = [-1] * (target + 1)
    for i in range(1, target + 1):
        options = [(1 + memo_table[i-cn],cn) for cn in coins if (i - cn >= 0)]
        options.append((1000000, -1))
        memo_table[i], best_coins[i]  = min(options)
    target_left = target
    while target_left > 0:
        coins_used.append(best_coins[target_left])
        target_left = target_left - best_coins[target_left]
    assert target_left == 0
    return memo_table[target], coins_used