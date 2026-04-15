# Prime Number Checker

## Overview

The **Prime Number Checker** is an efficient Python implementation for determining whether a given natural number is prime. This educational project demonstrates fundamental algorithmic thinking, number theory, and software testing practices.

---

## What is a Prime Number?

A **prime number** is a natural number that is:

- **Greater than 1**, and
- **Divisible only by 1 and itself** (no other divisors)

### Examples

| Number | Prime? | Reason |
|--------|--------|--------|
| 2      | ✓      | Only divisors are 1 and 2 |
| 7      | ✓      | Only divisors are 1 and 7 |
| 8      | ✗      | Divisible by 2 and 4 |
| 11     | ✓      | Only divisors are 1 and 11 |
| 15     | ✗      | Divisible by 3 and 5 |

---

## Core Function

### `is_prime(num)`

Determines whether a given number is prime.

**Signature:**
```python
def is_prime(num):
	"""
	Determine if a number is prime.
    
	Args:
		num: The value to check (should be an integer)
    
	Returns:
		True if the number is prime, False otherwise.
	"""
```

**Parameters:**
- `num` (int): The number to evaluate

**Returns:**
- `True` if `num` is prime
- `False` otherwise (including invalid inputs)

**Behavior:**
- Returns `False` for numbers less than 2 (including negative numbers and non-integers)
- Returns `True` if the number is prime
- Returns `False` if the number has divisors other than 1 and itself

---

## Algorithm Design

The implementation uses an **optimized divisibility check** approach:

1. **Early termination for small numbers:**
   - Numbers less than 2 are not prime
   - The number 2 is the only even prime

2. **Divisibility test:**
   - Check if the number is divisible by any odd number from 3 up to √num
   - If a divisor is found, return `False`
   - If no divisor is found, return `True`

3. **Efficiency:**
   - Only checks divisibility up to the **square root** of the number
   - Skips even divisors after checking 2
   - Time complexity: **O(√n)**

### Why Check Only Up to √num?

If a number `n` has a divisor greater than √n, it must also have a corresponding divisor less than √n. Therefore, checking up to √n is sufficient.

**Mathematical Proof:**
```
If a × b = n and a > √n, then b < √n
```

---

## Additional Functions

### `run_tests()`

Executes a comprehensive test suite with 28 test cases covering:
- Small prime numbers (2, 3, 5, 7, ...)
- Larger primes (97, 43, 41, ...)
- Non-prime values (1, 4, 6, 8, 9, ...)
- Edge cases (negative numbers, 0, 1)
- Invalid inputs

**Output Format:**
```
Passed X/Y tests
```

### `display_primes(limit)`

Displays all prime numbers up to and including the given limit.

**Example:**
```python
display_primes(25)
# Output: Prime numbers up to 25: [2, 3, 5, 7, 11, 13, 17, 19, 23]
```

---

## How to Run

### Execute the Script

Run the complete program with tests and demonstrations:

```bash
python Prime_Number_Checker.py
```

### Expected Output

```
=== Prime Number Checker ===

Running test suite...
Passed 28/28 tests

Prime numbers from 1 to 20:
2 3 5 7 11 13 17 19 

Prime numbers up to 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### Use in Your Own Code

```python
from Prime_Number_Checker import is_prime

# Check if 17 is prime
if is_prime(17):
	print("17 is prime!")

# Find all primes up to 100
primes = [n for n in range(1, 101) if is_prime(n)]
print(primes)
```

---

## Example Usage

| Call | Return | Explanation |
|------|--------|-------------|
| `is_prime(2)` | `True` | 2 is the smallest prime |
| `is_prime(7)` | `True` | 7 has no divisors except 1 and 7 |
| `is_prime(8)` | `False` | 8 = 2 × 4 (divisible by 2 and 4) |
| `is_prime(15)` | `False` | 15 = 3 × 5 (divisible by 3 and 5) |
| `is_prime(1)` | `False` | 1 is not considered prime (by definition) |
| `is_prime(-5)` | `False` | Negative numbers are not prime |
| `is_prime(97)` | `True` | 97 is prime |

---

## Project Structure

```
Prime_Number_Checker/
├── Prime_Number_Checker.py    # Main implementation with tests
- `README.md` - project documentation
```

---

## Key Concepts Demonstrated

✓ **Input Validation** – Handling invalid inputs gracefully  
✓ **Algorithm Optimization** – Using mathematical properties to improve efficiency  
✓ **Code Documentation** – Clear docstrings and comments  
✓ **Test-Driven Development** – Comprehensive test coverage  
✓ **Code Reusability** – Modular, function-based design  

---

## Learning Notes

- **Prime numbers are fundamental** in mathematics and computer science (cryptography, hashing, etc.)
- **Square root optimization** reduces time complexity from O(n) to O(√n)
- **Testing edge cases** (1, 2, negative numbers) is crucial for robust code
- **Avoiding redundant checks** (e.g., even divisors after 2) improves performance

---

## Performance Considerations

| Input Range | Max Iterations | Time |
|------------|----------------|------|
| 1 to 100   | ~10            | <1ms |
| 1 to 10,000 | ~100           | <1ms |
| 1 to 1,000,000 | ~1,000       | <5ms |

---

## Files

- **Prime_Number_Checker.py** – Complete implementation with optimized algorithm, input validation, test suite, and demonstration functions
- **README.md** – This documentation file

---

## Resources & Further Reading

- [Prime Numbers (Wikipedia)](https://en.wikipedia.org/wiki/Prime_number)
- [Miller–Rabin Primality Test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) – Advanced algorithm for large numbers
- [Python `math.isqrt()`](https://docs.python.org/3/library/math.html#math.isqrt) – For computing integer square roots

---

## License

This is educational code. Feel free to use, modify, and distribute for learning purposes.

---

**Happy Prime Checking!** 🎯


# Prime_Number_Checker
