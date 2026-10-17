
# class Solution(object):
#     def reverseWords(self, s):
#         words = s.split(' ')
#         reversed_words = [word[::-1] for word in words]
#         return ' '.join(reversed_words)



class Solution(object):
    def reverseWords(self, s):
        words = list(s)
        start = 0

        while start < len(words):
            end = start
            while end < len(words) and words[end] != " ":
                end += 1
            left = start
            right = end - 1
            while left < right:
                words[left], words[right] = words[right], words[left]
                left += 1
                right -= 1
            start = end + 1

        return "".join(words)


