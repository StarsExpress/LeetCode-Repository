from bisect import bisect_right


class MoviesRentingSystem:  # LeetCode Q.1912.
    def __init__(self, entries: list[list[int]]):
        # Each movie's prices and rent status at the shops offering it.
        # Format: (price, currently rented).
        self.movies_table: dict[int, dict[int, list[int | bool]]] = dict()

        # Each movie's sorted unrented copies list. Format: (price, shop).
        self.unrented_copies: dict[int, list[tuple[int, int]]] = dict()

        self.rented_copies: list[tuple[int, int, int]] = []  # Format: (price, shop, movie).

        for shop, movie, price in entries:
            if movie not in self.movies_table.keys():
                self.movies_table.update({movie: dict()})
                self.unrented_copies[movie] = []

            self.movies_table[movie][shop] = [price, False]

            idx = bisect_right(self.unrented_copies[movie], (price, shop))
            self.unrented_copies[movie].insert(idx, (price, shop))

    def search(self, movie: int) -> list[int]:
        if movie not in self.unrented_copies.keys():
            return []
        return [shop for _, shop in self.unrented_copies[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        if movie in self.movies_table.keys():
            if shop in self.movies_table[movie].keys():
                if not self.movies_table[movie][shop][1]:  # Currently unrented.
                    price = self.movies_table[movie][shop][0]

                    idx = bisect_right(self.unrented_copies[movie], (price, shop))
                    self.unrented_copies[movie].pop(idx - 1)
                    self.movies_table[movie][shop][1] = True  # Becomes rented.

                    idx = bisect_right(self.rented_copies, (price, shop, movie))
                    self.rented_copies.insert(idx, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        if movie in self.movies_table.keys():
            if shop in self.movies_table[movie].keys():
                if self.movies_table[movie][shop][1]:  # Currently rented.
                    price = self.movies_table[movie][shop][0]

                    idx = bisect_right(self.unrented_copies[movie], (price, shop))
                    self.unrented_copies[movie].insert(idx, (price, shop))
                    self.movies_table[movie][shop][1] = False  # Becomes unrented.

                    idx = bisect_right(self.rented_copies, (price, shop, movie))
                    self.rented_copies.pop(idx - 1)

    def report(self) -> list[list[int]]:
        return [[shop, movie] for _, shop, movie in self.rented_copies[:5]]
