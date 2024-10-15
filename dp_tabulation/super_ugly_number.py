
def find_nth_super_ugly_number(n: int, primes: list[int]) -> int:  # LeetCode Q.313 & 264.
    """
    Key: the next ugly number is a multiple of a prime and an existing ugly number.

    For each prime, track the existing ugly number that is
    likely to bring the next ugly number with the prime.
    """
    # Indices as values: use idx to locate the pairing ugly number in ugly numbers list.
    primes2ugly_numbers_indices = dict(zip(primes, [0] * len(primes)))

    next_ugly_number, next_ugly_number_primes = float("inf"), []
    ugly_numbers, total_ugly_numbers = [1], 1  # Base case.

    while total_ugly_numbers < n:
        for prime in primes:
            ugly_number = prime * ugly_numbers[primes2ugly_numbers_indices[prime]]
            if ugly_number < next_ugly_number:
                next_ugly_number = ugly_number
                next_ugly_number_primes.clear()

            if ugly_number == next_ugly_number:
                next_ugly_number_primes.append(prime)

        ugly_numbers.append(next_ugly_number)
        total_ugly_numbers += 1

        for prime in next_ugly_number_primes:
            primes2ugly_numbers_indices[prime] += 1

        next_ugly_number = float("inf")  # Reset for the next iteration.
        next_ugly_number_primes.clear()

    return ugly_numbers[-1]
