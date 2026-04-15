def is_prime(num):
    """
    Determine if a number is prime.
    
    A number is prime if it is greater than 1 and has no divisors oth(er than 1 and itself.
    
    Args:
        num: The value to check (should be an integer)
    
    Returns:
        True if the number is prime, False otherwise.
    """
    if not isinstance(num, int) or num < 2:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    
    return True


def run_tests():
    """Execute comprehensive test cases for the is_prime function."""
    test_cases = [
        # Non-prime values
        (1, False),
        (0, False),
        (-5, False),
        (4, False),
        (6, False),
        (8, False),
        (9, False),
        (10, False),
        (15, False),
        (20, False),
        (25, False),
        (100, False),
        # Prime values
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
        (17, True),
        (19, True),
        (23, True),
        (29, True),
        (31, True),
        (37, True),
        (41, True),
        (43, True),
        (47, True),
        (97, True),
    ]
    
    passed = 0
    for num, expected in test_cases:
        result = is_prime(num)
        if result == expected:
            passed += 1
        else:
            print(f"FAIL: is_prime({num}) -> {result}, expected {expected}")
    
    print(f"Passed {passed}/{len(test_cases)} tests")


def display_primes(limit):
    """Display all prime numbers up to the given limit."""
    primes = [num for num in range(2, limit + 1) if is_prime(num)]
    print(f"Prime numbers up to {limit}: {primes}")


if __name__ == "__main__":
    print("=== Prime Number Checker ===\n")
    
    print("Running test suite...")
    run_tests()
    
    print("\nPrime numbers from 1 to 20:")
    for i in range(1, 21):
        if is_prime(i):
            print(i, end=" ")
    print("\n")
    
    display_primes(50)
