
def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    longest = 0

    for right, ch in enumerate(s):
        
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        
        seen[ch] = right
        longest = max(longest, right - left + 1)

    return longest
print(lengthOfLongestSubstring("abcabcdd"))


def generatePassword():
    random_password = "";

    for i in range(10):
        print(i);
        random_password += str(i)


    return random_password;

print(generatePassword());