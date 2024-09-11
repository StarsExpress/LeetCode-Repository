
def distribute_candies(ratings: list[int]) -> int:  # LeetCode Q.135.
    total_ratings = len(ratings)
    distribution, total_candies = [1] * total_ratings, 0
    ratings2indices = dict()
    for idx, rating in enumerate(ratings):
        if rating not in ratings2indices.keys():
            ratings2indices.update({rating: []})
        ratings2indices[rating].append(idx)

    distinct_ratings = list(ratings2indices.keys())
    distinct_ratings.sort()
    # Lowest ratings all have one candy.
    total_candies += len(ratings2indices[distinct_ratings.pop(0)])
    for distinct_rating in distinct_ratings:
        for idx in ratings2indices[distinct_rating]:
            if idx > 0 and ratings[idx] > ratings[idx - 1]:
                distribution[idx] = max(distribution[idx], distribution[idx - 1] + 1)

            if idx < total_ratings - 1 and ratings[idx] > ratings[idx + 1]:
                distribution[idx] = max(distribution[idx], distribution[idx + 1] + 1)

            total_candies += distribution[idx]

    return total_candies
