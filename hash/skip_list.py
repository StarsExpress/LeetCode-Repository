
class SkipList:  # LeetCode Q.1206.
    def __init__(self):
        self.numbers_table = dict()

    def search(self, target: int):
        try:
            self.numbers_table[target]

        except KeyError:
            return False

        return True

    def add(self, number: int):
        if number not in self.numbers_table.keys():
            self.numbers_table.update({number: 0})
        self.numbers_table[number] += 1

    def erase(self, number: int):
        try:
            self.numbers_table[number]

        except KeyError:
            return False

        self.numbers_table[number] -= 1
        if self.numbers_table[number] == 0:
            del self.numbers_table[number]
        return True
