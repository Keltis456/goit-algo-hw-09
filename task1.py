def find_coins_greedy(amount: int) -> dict:
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    
    return result


if __name__ == "__main__":
    test_amounts = [113, 289, 1000, 7]
    
    for amount in test_amounts:
        result = find_coins_greedy(amount)
        total_coins = sum(result.values())
        print(f"Amount: {amount}")
        print(f"Coins: {result}")
        print(f"Total coins used: {total_coins}")
        print("-" * 30)

