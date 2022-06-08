def lengthOfLongestSubstring(s: str) -> int:
        cur = 0
        maxLenOfSub = 0
        length = len(s)
        while (cur < length-maxLenOfSub):
            charSet = set()
            for i in s[cur:]:
                if (i not in charSet):
                    charSet.add(i)
                else:
                    break
            # print(charSet)
            if len(charSet) > maxLenOfSub:
                maxLenOfSub = len(charSet)
            cur+=1

        return maxLenOfSub


if __name__ == '__main__':
    test1="abcabcbb"
    test2="bbbb"
    test3=""
    test4="pwwkew"
    print(lengthOfLongestSubstring(test1))
    print(lengthOfLongestSubstring(test2))
    print(lengthOfLongestSubstring(test3))
    print(lengthOfLongestSubstring(test4))
