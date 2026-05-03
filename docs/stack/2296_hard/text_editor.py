from collections import deque


class TextEditor:  # LeetCode Q.2296.
    def __init__(self) -> None:
        self.cursor_left_side: deque[str] = deque([])
        self.cursor_right_side: deque[str] = deque([])

    def _slice_cursor_left_tail(self) -> str:        
        start_idx = max(0, len(self.cursor_left_side) - 10)

        text = ""
        for idx in range(start_idx, len(self.cursor_left_side)):
            text += self.cursor_left_side[idx]

        return text

    def add_text(self, text: str) -> None:
        self.cursor_left_side.extend(list(text))

    def delete_text(self, k: int) -> int:
        deletions_count = min(k, len(self.cursor_left_side))

        while k > 0 and self.cursor_left_side:
            self.cursor_left_side.pop()
            k -= 1
        
        return deletions_count

    def cursor_left(self, k: int) -> str:
        while k > 0 and self.cursor_left_side:
            char = self.cursor_left_side.pop()
            self.cursor_right_side.appendleft(char)
            k -= 1
        
        return self._slice_cursor_left_tail()

    def cursor_right(self, k: int) -> str:
        while k > 0 and self.cursor_right_side:
            char = self.cursor_right_side.popleft()
            self.cursor_left_side.append(char)
            k -= 1
        
        return self._slice_cursor_left_tail()
