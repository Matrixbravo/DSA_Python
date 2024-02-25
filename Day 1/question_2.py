# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
tests = []

# Test Case 1
tests.append({
    'input': {'nums': [1, 2, 3, 1]},
    'output': True
})

# Test Case 2
tests.append({
    'input': {'nums': [1, 2, 3, 4]},
    'output': False
})

# Test Case 3
tests.append({
    'input': {'nums': [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]},
    'output': True
})

# Additional Test Case (Edge Case)
tests.append({
    'input': {'nums': []},  # Empty array
    'output': False
})


# 1.) Sort the array so that any duplicate nnumber can be adjacent
# 2.) Create one hashset and add iterated numbers from array into the hashset
# 3.) Return True is exists else add into hashset
# 4.) Finally return False if array ended

class Solution(object):
    def containsDuplicate(nums):
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        

import time

def run_tests():
    total_execution_time = 0
    passed_tests = 0
    failed_tests = 0

    for i, test in enumerate(tests, 1):
        input_data = test['input']
        expected_output = test['output']

        start_time = time.time()
        result = Solution.containsDuplicate(**input_data)
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

