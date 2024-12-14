#!/usr/bin/python3
"""Prime Game Solution"""


def isWinner(x, nums):
    """
    Returns the Name of the player that won the most rounds
    """
    # Function to generate primes using the Sieve of Eratosthenes
    def sieve(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    # Find the maximum n from all rounds
    max_n = max(nums)
    
    # Generate all primes up to the maximum n
    primes = sieve(max_n)

    # Function to simulate the game for a given n
    def simulate_game(n):
        # Create a list of booleans indicating if the number is still in the set
        is_prime_in_set = [True] * (n + 1)
        for p in primes:
            if p > n:
                break
            # Mark the multiples of the prime as removed
            for multiple in range(p, n + 1, p):
                is_prime_in_set[multiple] = False

        # Now simulate the game between Maria and Ben
        turn = 0  # 0 for Maria, 1 for Ben
        remaining_primes = [p for p in primes if p <= n and is_prime_in_set[p]]

        while remaining_primes:
            prime = remaining_primes.pop(0)  # Take the smallest available prime
            # Remove the prime and its multiples from the remaining primes
            remaining_primes = [p for p in remaining_primes if p % prime != 0]
            turn = 1 - turn  # Alternate the turn
        
        # If turn is 0 after the loop, it means it was Ben's turn and he couldn't play, so Maria wins
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0
    
    # Simulate each round and count wins
    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
