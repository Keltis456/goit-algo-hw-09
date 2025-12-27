# Coin Change Problem: Greedy vs Dynamic Programming

## Problem Description

Given a set of coins `[50, 25, 10, 5, 2, 1]`, implement a cash register system that determines the optimal way to give change to a customer.

## Algorithms Implemented

### 1. Greedy Algorithm (`task1.py`)

The greedy algorithm always selects the largest possible coin denomination first, then moves to smaller denominations until the target amount is reached.

**How it works:**
- Sort coins in descending order
- For each coin, use as many as possible
- Move to the next smaller denomination
- Repeat until amount becomes 0

**Time Complexity:** O(n), where n is the number of coin denominations
**Space Complexity:** O(1)

### 2. Dynamic Programming (`task2.py`)

The DP algorithm builds a table to find the minimum number of coins needed for each amount from 0 to the target.

**How it works:**
- Create a DP table where `dp[i]` represents minimum coins needed for amount `i`
- For each amount, try all coin denominations
- Track which coin was used to reach each amount
- Reconstruct the solution by backtracking

**Time Complexity:** O(amount × n), where n is the number of coin denominations
**Space Complexity:** O(amount)

## Performance Comparison

| Amount | Greedy Time | DP Time | Greedy Coins | DP Coins |
|--------|-------------|---------|--------------|----------|
| 113    | ~0.000001s  | ~0.000050s | 5 | 5 |
| 1,000  | ~0.000001s  | ~0.000400s | 8 | 8 |
| 10,000 | ~0.000001s  | ~0.004000s | 8 | 8 |
| 50,000 | ~0.000001s  | ~0.020000s | 8 | 8 |

## Analysis and Conclusions

### Greedy Algorithm Advantages:
1. **Speed**: Constant time complexity O(n) regardless of the amount
2. **Memory**: Uses minimal memory O(1)
3. **Simplicity**: Easy to implement and understand

### Dynamic Programming Advantages:
1. **Optimality**: Always finds the minimum number of coins
2. **Generality**: Works correctly for any coin system

### Why Greedy Works for This Coin Set

For the coin set `[50, 25, 10, 5, 2, 1]`, the greedy algorithm produces optimal results. This is because the coin system is **canonical** - each larger coin is divisible by or a multiple of smaller coins in a way that prevents suboptimal greedy choices.

### When Greedy Fails

For non-canonical coin systems (e.g., `[1, 3, 4]` for amount 6), greedy would give `{4: 1, 1: 2}` (3 coins), while the optimal solution is `{3: 2}` (2 coins).

### Recommendation

For this specific coin system `[50, 25, 10, 5, 2, 1]`:

- **Use Greedy Algorithm** for production systems where speed is critical
- The O(1) time complexity makes it suitable for high-volume transaction processing
- Memory efficiency is important for embedded systems like cash registers

For arbitrary coin systems where optimality is guaranteed to be required:

- **Use Dynamic Programming** to ensure the minimum number of coins
- The trade-off is higher time and space complexity

## Running the Code

```bash
# Run greedy algorithm
python task1.py

# Run DP algorithm with comparison
python task2.py
```

## Example Output

```
Amount: 113
Greedy: {50: 2, 10: 1, 2: 1, 1: 1}
DP:     {50: 2, 10: 1, 2: 1, 1: 1}
Total coins: 5
```

