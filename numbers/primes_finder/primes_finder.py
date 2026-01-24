
def find_all_primes(number: int) -> list[int]:
    primes = []
    if number <= 1:  # Sanity check.
        return primes

    # From 3 and so on, all primes are odd.
    current_prime = 2  # The only even prime is 2.

    while number > 1:
        if number % current_prime == 0:
            primes.append(current_prime)
            number //= current_prime
            continue

        if current_prime == 2:
            current_prime += 1

        else:
            current_prime += 2

        if current_prime > number ** 0.5 and number > 1:
            current_prime = number

    return primes
