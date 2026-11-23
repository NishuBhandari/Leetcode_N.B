class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}
        count = 0

        left = 0
        ans = ""
        min_len = float("inf")

        for right in range(len(s)):

            c = s[right]

            if c in need:
                have[c] = have.get(c, 0) + 1

                if have[c] <= need[c]:
                    count += 1

            while count == len(t):

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left:right + 1]

                left_char = s[left]

                if left_char in need:
                    have[left_char] -= 1

                    if have[left_char] < need[left_char]:
                        count -= 1

                left += 1

        return ans