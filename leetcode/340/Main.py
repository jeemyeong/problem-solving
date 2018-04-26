class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        head_idx = 0
        tail_idx = 0
        length = len(s)
        hash_table = {}
        cnt = 0
        ret = 0
        while head_idx < length:
            head = s[head_idx]
            if not head in hash_table: hash_table[head] = 0
            if hash_table[head] == 0: cnt += 1
            hash_table[head] += 1
            while cnt > k:
                tail = s[tail_idx]
                hash_table[tail] -= 1
                if hash_table[tail] == 0: cnt -= 1
                tail_idx += 1
            ret = max(ret, head_idx - tail_idx + 1)
            head_idx += 1
        return ret


