def lengthofLongestSubstring(s: str) -> int:
    left = 0 
    s = "abcbdefabc"
    substr = ""
    substrings = [] 
    repeated_dict = dict()

    for right in range(len(s)):
        current_char = s[right]  

        # if string s has a character in substr 
        if current_char in substr: 
            # create a substring from the last repeated character to the current repeated character
            substr = s[left:right]  
            print(left)
            substrings.append(substr)      
            # find the closest equal element to s[right] and make sure we don't include it 
            substr = s[left:] 
            repeated_dict[current_char] = right  
            print(repeated_dict)
            left += 1 
        else:
            substr += current_char
              
        
    print(substrings) 
         

lengthofLongestSubstring("") 

