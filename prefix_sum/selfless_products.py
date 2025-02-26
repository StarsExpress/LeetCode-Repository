
def find_selfless_products(nums: list[int]) -> list[int]:  # LeetCode Q.238.
    prefix_products, suffix_products = [], []
    for num in nums:
        if not prefix_products:
            prefix_products.append(num)
            continue
        if prefix_products[-1] == 0:
            prefix_products.append(0)
            continue
        prefix_products.append(prefix_products[-1] * num)

    for num in nums[::-1]:  # Suffix products: backward iteration.
        if not suffix_products:
            suffix_products.append(num)
            continue
        if suffix_products[-1] == 0:
            suffix_products.append(0)
            continue
        suffix_products.append(suffix_products[-1] * num)
    suffix_products = suffix_products[::-1]  # Reverse to original indices order.

    selfless_products, total_nums = [], len(nums)
    for idx, num in enumerate(nums):
        if idx == total_nums - 1:
            selfless_products.append(prefix_products[-2])
            break
        if idx == 0:
            selfless_products.append(suffix_products[1])
            continue

        selfless_products.append(prefix_products[idx - 1] * suffix_products[idx + 1])

    return selfless_products
