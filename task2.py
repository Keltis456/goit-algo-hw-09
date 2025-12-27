import time
from task1 import find_coins_greedy


def find_min_coins(amount: int) -> dict:
    coins = [50, 25, 10, 5, 2, 1]
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    parent = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    result = {}
    current = amount
    while current > 0:
        coin = parent[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin
    
    return result


def compare_algorithms():
    test_amounts = [113, 289, 1000, 5000, 10000, 50000]
    
    print("=" * 70)
    print("COMPARISON OF GREEDY AND DYNAMIC PROGRAMMING ALGORITHMS")
    print("=" * 70)
    
    for amount in test_amounts:
        print(f"\nAmount: {amount}")
        print("-" * 50)
        
        start = time.perf_counter()
        greedy_result = find_coins_greedy(amount)
        greedy_time = time.perf_counter() - start
        greedy_coins = sum(greedy_result.values())
        
        start = time.perf_counter()
        dp_result = find_min_coins(amount)
        dp_time = time.perf_counter() - start
        dp_coins = sum(dp_result.values())
        
        print(f"Greedy:  {greedy_result}")
        print(f"         Coins: {greedy_coins}, Time: {greedy_time:.6f}s")
        print(f"DP:      {dp_result}")
        print(f"         Coins: {dp_coins}, Time: {dp_time:.6f}s")
        
        if greedy_coins == dp_coins:
            print(f"Result:  Both algorithms use the same number of coins")
        else:
            print(f"Result:  DP uses {greedy_coins - dp_coins} fewer coins")


if __name__ == "__main__":
    print("Dynamic Programming Solution:")
    result = find_min_coins(113)
    print(f"Amount 113: {result}")
    print(f"Total coins: {sum(result.values())}")
    print()
    
    compare_algorithms()

