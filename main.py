# Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just character at index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

# Example

# s=abc This is a valid string because frequencies are {a: 1, b: 1, c: 1}.

# s=abcc This is a valid string because we can remove one c and have 1 of each character in the remaining string.

# s=abccc This string is not valid as we can only remove 1 occurrence of c. That leaves character frequencies of {a: 1, b: 1, c: 2}.

# Function Description

# Complete the isValid function. isValid has the following parameter(s):

# string s: a string
# Returns

# string: either YES or NO
# Input Format

# A single string s.

# Note: DO NOT USE ANY EXTERNAL LIBRARIES - JUST DEFAULT PYTHON STRUCTURES

def isValid(string):
    """Capturing whether a string is valid or not according to criteria shown above.

    Args:
        string (string): The input string with only alphabet characters (e.g. abcc)

    Returns:
        string: YES or NO if the string is value or not respectively
    """
    # 1. Capture the default case of empty string
    if len(string) == 0:
        is_valid = 'No'

    # 2. Capture the default case of just a single character
    if len(string) == 1:
        is_valid = 'Yes'

    # 3. Capture scenario with multiple characters
    # 3.1 Capture the frequencies of each character in the string
    freq_dict = {}
    for char in string:
        if char not in freq_dict:
            freq_dict[char] = 1       # If character appears for the first time, create a key with its frequency
        else:
            freq_dict[char] += 1      # If charactes has been seen before, update tis frequency by one (1)

    # 3.2 Normalize the frequencies in the freq_dict to capture the absolute differences
    # Capture the min frequency present in the frequency dict
    freq_min = min(freq_dict.values())

    # Subtrack it from every single frequency for every single character using dict comprehension
    freq_dict_norm = [freq_char - freq_min for freq_char in freq_dict.values()]

    # 3.3 Capture all the different scenarios
    total_diffs = sum(freq_dict_norm)

    if total_diffs == 0:       # Means that all of the characters have the same frequency
        is_valid = 'Yes'
    elif total_diffs == 1:     # Means that there is only a single character that has a frequency higher than the others (expection scenario)
        is_valid = 'Yes'
    else:
        is_valid = 'No'        # Means that the frequencies difference is more than 2. Hence not a valid string

    return is_valid


