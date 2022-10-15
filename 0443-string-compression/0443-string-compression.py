class Solution:
    def compress(self, chars: List[str]) -> int:
        start = index = 0
        while index<len(chars):
            chars[start] = chars[index]
            count = 1
            while index<len(chars)-1 and chars[index]==chars[index+1]:
                index += 1
                count += 1
            if count>1:
                for i in str(count):
                    start += 1
                    chars[start] = i
            index += 1
            start += 1
        return start