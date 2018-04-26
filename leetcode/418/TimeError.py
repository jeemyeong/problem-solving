class Solution:
    def next(self, sentence):
        self.idx += 1
        if self.idx < len(sentence) :
            return sentence[self.idx]
        else: 
            self.idx = 0
            self.cnt += 1
            return sentence[self.idx]

    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        self.idx = -1
        self.cnt = 0
        word = self.next(sentence)
        
        row = 0
        col = 0
        while row < rows and col < cols:
            if cols - col < len(word):
                col = 0
                row += 1
                continue
            col += len(word) + 1
            if col >= cols:
                col = 0
                row += 1
            word = self.next(sentence)
        return self.cnt
        

sentence = ["a", "bcd", "e"]
rows = 3
cols = 6

print(Solution().wordsTyping(sentence, rows, cols))