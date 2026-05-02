
class TextJustificator:  # LeetCode Q.68.
    def __init__(self) -> None:
        self.queue: list[str] = []

    def _form_sentence(self, chars_count: int, max_width: int, left_justify: bool) -> str:
        interval_spaces = ""
        intervals_count = len(self.queue) - 1
        modulo = 0

        if intervals_count > 0 and not left_justify:
            quotient = (max_width - chars_count) // intervals_count
            interval_spaces += " " * quotient

            modulo = (max_width - chars_count) % intervals_count

        sentence = ""

        for idx, word in enumerate(self.queue):
            sentence += word

            if idx < len(self.queue) - 1:  # Not the last word.
                if left_justify:
                    sentence += " "  # Left-justification.
                    continue

                sentence += interval_spaces  # Right-justification.
                if modulo > idx:
                    sentence += " "  # Need to pad extra space at left intervals.

        self.queue.clear()  # Reset for future usage.

        # Right end padding only runs for left-justification.
        sentence += " " * (max_width - len(sentence))
        return sentence

    def justify_text(self, words: list[str], max_width: int) -> list[str]:
        self.queue.clear()

        justified_sentences: list[str] = []
        chars_count = 0  # Characters only. Not counting interval spaces.

        for word in words:
            # Current sentence is finalized.
            if chars_count + len(self.queue) - 1 + len(word) + 1 > max_width:
                sentence = self._form_sentence(chars_count, max_width, False)
                justified_sentences.append(sentence)
                chars_count -= chars_count  # Reset for the next sentence.

            self.queue.append(word)
            chars_count += len(word)

        # Deal with last sentence. Last sentence must be left-justified.
        sentence = self._form_sentence(chars_count, max_width, True)
        justified_sentences.append(sentence)
        return justified_sentences
