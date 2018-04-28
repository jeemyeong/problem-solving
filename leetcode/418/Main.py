class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """

        joined_sentence = " ".join(sentence) + " "
        length = len(joined_sentence)
        start = 0
        for _ in range(rows):
            start += cols
            if joined_sentence[start % length] == " ":
                start += 1
            else:
                while start > 0 and joined_sentence[(start-1) % length] != " ":
                    start -= 1
        return start // length

sentence = ["hello","world"]
rows = 2
cols = 8

print(Solution().wordsTyping(sentence, rows, cols))