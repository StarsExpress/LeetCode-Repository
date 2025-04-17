
class SkipList:  # LeetCode Q.1206.
    def __init__(self):
        self.nums2counts = dict()

    def search(self, target: int):
        if target not in self.nums2counts.keys():
            return False
        if self.nums2counts[target] == 0:
            return False

        return True

    def add(self, num: int):
        if num not in self.nums2counts.keys():
            self.nums2counts.update({num: 0})
        self.nums2counts[num] += 1

    def erase(self, num: int):
        if num not in self.nums2counts.keys():
            return False

        self.nums2counts[num] -= 1
        if self.nums2counts[num] == -1:
            self.nums2counts[num] += 1  # Go back to 0.
            return False
        return True
