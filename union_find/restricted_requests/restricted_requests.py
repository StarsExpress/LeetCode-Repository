
class RestrictedFriendRequests:  # LeetCode Q.2076.
    def __init__(self):
        self.parents: list[int] = []
        self.forbidden: dict[int, set[int]] = {}

    def process_requests(
            self, n: int, restrictions: list[list[int]], requests: list[list[int]]
    ) -> list[bool]:
        self.parents.clear()  # Initialize each person's parent as self.
        self.parents = [person for person in range(n)]

        self.forbidden.clear()  # Each person's restricted people.
        self.forbidden.update(
            dict(
                zip([person for person in range(n)], [set() for _ in range(n)])
            )
        )

        for person_1, person_2 in restrictions:
            self.forbidden[person_1].add(person_2)
            self.forbidden[person_2].add(person_1)

        requests_results = []
        for person_1, person_2 in requests:
            parent_1 = self._find_parent(person_1)
            parent_2 = self._find_parent(person_2)
            request_success = True  # Default to True.

            for forbidden_person in self.forbidden[parent_1]:  # Test parent 1.
                if self._find_parent(forbidden_person) == parent_2:
                    request_success = False
                    break
            if request_success:  # Need to test parent 2.
                for forbidden_person in self.forbidden[parent_2]:
                    if self._find_parent(forbidden_person) == parent_1:
                        request_success = False
                        break

            requests_results.append(request_success)
            if request_success:
                self._union_people(parent_1, parent_2)

        return requests_results

    def _find_parent(self, person: int) -> int:
        parent = self.parents[person]
        return person if parent == person else self._find_parent(parent)

    def _union_people(self, person_1: int, person_2: int) -> None:
        parent_1 = self._find_parent(min(person_1, person_2))
        parent_2 = self._find_parent(max(person_1, person_2))
        if parent_1 != parent_2:
            self.parents[parent_2] = parent_1

            # Must merge parent 2's restricted people into parent 1's.
            self.forbidden[parent_1].update(self.forbidden[parent_2])
            del self.forbidden[parent_2]  # Clear unused memory.
