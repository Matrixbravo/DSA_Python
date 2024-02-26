# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Test cases
tests = []

# Test Case 1
tests.append({
    'input': {'s': "anagram", 't': "nagaram"},
    'output': True
})

# Test Case 2
tests.append({
    'input': {'s': "rat", 't': "car"},
    'output': False
})

# Test Case 3
tests.append({
    'input': {'s': "listen", 't': "silent"},
    'output': True
})

# Test Case 4
tests.append({
    'input': {'s': "hello", 't': "world"},
    'output': False
})

# Additional Test Case (Edge Case)
tests.append({
    'input': {'s': "", 't': ""},  # Empty strings
    'output': True
})


# Solution

class Solution(object):
    def isAnagram(s, t):
        return sorted(s) == sorted(t)
    
        

# Run the tests function

import time

def run_tests():
    total_execution_time = 0
    passed_tests = 0
    failed_tests = 0

    for i, test in enumerate(tests, 1):
        input_data = test['input']
        expected_output = test['output']

        start_time = time.time()
        result = Solution.isAnagram(**input_data)
        end_time = time.time()

        total_execution_time += (end_time - start_time) * 1000  # Convert to milliseconds

        if result == expected_output:
            passed_tests += 1
            print(f'\033[92mTest case {i}: Passed (Execution Time: {(end_time - start_time) * 1000:.6f} ms)\033[0m')
        else:
            failed_tests += 1
            print(f'\033[91mTest case {i}: Failed. Expected {expected_output}, got {result} (Execution Time: {(end_time - start_time) * 1000:.6f} ms)\033[0m')

    print(f'\nTotal Execution Time for all test cases: {total_execution_time:.6f} ms')
    print(f'Total Passed: \033[92m{passed_tests}\033[0m, Total Failed: \033[91m{failed_tests}\033[0m')

# Run the tests
run_tests()
