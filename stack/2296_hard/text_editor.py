from collections import deque


class TextEditor:  # LeetCode Q.2296.
    def __init__(self):
        self.cursor_left_chars = []  # Stack based. Chars at cursor's left.
        self.cursor_right_chars = deque()  # Queue based. Chars at cursor's right.

    def add_text(self, text: str) -> None:
        for char in text:
            self.cursor_left_chars.append(char)

    def delete_text(self, k: int) -> int:
        deletions = min(k, len(self.cursor_left_chars))
        for _ in range(deletions):
            self.cursor_left_chars.pop(-1)
        return deletions

    def move_cursor_left(self, k: int) -> str:
        while k > 0 and self.cursor_left_chars:
            char = self.cursor_left_chars.pop(-1)
            self.cursor_right_chars.appendleft(char)
            k -= 1

        str_min_idx = -min(10, len(self.cursor_left_chars))  # Backward idx.
        return "".join(self.cursor_left_chars[str_min_idx:])

    def move_cursor_right(self, k: int) -> str:
        while k > 0 and self.cursor_right_chars:
            char = self.cursor_right_chars.popleft()
            self.cursor_left_chars.append(char)
            k -= 1

        str_min_idx = -min(10, len(self.cursor_left_chars))  # Backward idx.
        return "".join(self.cursor_left_chars[str_min_idx:])
