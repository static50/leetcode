def lengthofLongestSubstring(s: str) -> int:
    left = 0 
    s = "abcbdefabc"
    substr = ""
    substrings = [] 
    repeated_dict = dict()
    longest_repeat = 0
    current_length = 0 

    for right in range(len(s)):
        current_char = s[right]  
        
        if current_char in repeated_dict: 
            if right > longest_repeat:
                longest_repeat = right
            
            left = longest_repeat + 1
            print(f"left: {left}")
            substr = s[left:right]


        repeated_dict[current_char] = right 
        substr += current_char # append the current character to the substring 
        
        if len(substr) > current_length:
            current_length = len(substr)

        print(current_length)
        
        print(substr)
        print(repeated_dict)
        

lengthofLongestSubstring("")

# for every character in string s
    # if the character is already in the dictionary 
        # and if the character value is longer than the last recorded
            # the longest is now that character value
            





# Notes:
# 








