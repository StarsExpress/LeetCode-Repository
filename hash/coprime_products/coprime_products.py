
def _find_primes(num: int) -> dict[int, int]:
    primes2counts: dict[int, int] = dict()  # Counts of all occurred primes.
    while num % 2 == 0:
        if 2 not in primes2counts.keys():
            primes2counts.update({2: 0})
        primes2counts[2] += 1
        num /= 2

    factor = 3  # Num must be odd now. Increment skips even elements.
    while factor * factor <= num:
        while num % factor == 0:
            if factor not in primes2counts.keys():
                primes2counts.update({factor: 0})
            primes2counts[factor] += 1
            num /= factor

        factor += 2

    if num > 2:  # When num is a prime greater than 2.
        primes2counts[num] = 1

    return primes2counts


def find_split_idx(nums: list[int]) -> int:  # LeetCode Q.2584.
    nums2primes: dict[int, dict[int, int]] = dict()
    prefix_primes: dict[int, int] = dict()
    suffix_primes: dict[int, int] = dict()

    for num in nums:
        if num not in nums2primes.keys():
            nums2primes[num] = _find_primes(num)

        for prime, count in nums2primes[num].items():
            if prime not in suffix_primes.keys():
                suffix_primes.update({prime: 0})
            suffix_primes[prime] += count

    common_primes: set[int] = set()
    for idx in range(len(nums) - 1):
        for prime, count in nums2primes[nums[idx]].items():
            if prime not in prefix_primes.keys():
                prefix_primes.update({prime: 0})
            prefix_primes[prime] += count
            common_primes.add(prime)

        for prime, count in nums2primes[nums[idx]].items():
            suffix_primes[prime] -= count
            if suffix_primes[prime] == 0:
                if prime in common_primes:
                    common_primes.remove(prime)

        if not common_primes:  # Current idx is the smallest idx to split.
            return idx

    return -1
