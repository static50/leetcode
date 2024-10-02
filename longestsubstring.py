class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        substr = ""
        repeated_dict = dict()
        longest_repeat = 0
        current_length = 0

        for right in range(len(s)):
            current_char = s[right]

            if current_char in substr:
               if right > longest_repeat:
                  longest_repeat = right

               left = repeated_dict[current_char]
               substr = s[left:right]

            repeated_dict[current_char] = right

            if current_char not in substr:
                substr += current_char  # append the current character to the substring

            if len(substr) > current_length:
                current_length = len(substr)

        return current_length
