#Day 1
# Introductin to Binary search and complexity Analysis with Python

# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

# Ans:
# Sorted List -> [13, 11, 12, 7, 4, 3, 1, 0] e.g
# Positions ->   [  0   1   2  3  4  5  6  7 ]

# Example
# cards = [13, 11, 10, 7, 4, 3, 1, 0]
# query = 7
# output = 3

# The problem statement does not specify what to do if the list cards does not contain the number query.

# 1.) Read the problem statement again, carefully.
# 2.) Look through the examples provided with the problem.
# 3.) Ask the interviewer/platform for a clarification.
# 4.) Make a reasonable assumption, state it and move forward.

# Self made Test cases.
tests = []

# Test Case 1
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
})

# Test Case 2
tests.append({'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0})

# Test Case 3
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# Test Case 3
tests.append({'input': {'cards': [6], 'query': 6}, 'output': 0})

# Test Case 4
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

tests.append({
    'input': {
        'cards': [],
        'query': 3
    },
    'output': 7
})

# Linear Search (Brute force)

# 1.) Create a variable position with the value 0.
# 2.) Check whether the number at index position in card equals query.
# 3.) If it does, position is the answer and can be returned from the function
# 4.) If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
# 5.) If the number was not found, return -1.


def locate_card(cards, query):
  # Create a variable position with the value 0
  position = 0
  # Set up a loop for repetition
  while position < len(cards):
    # Check if the element at the current postion matche the query
    if cards[position] == query:
      #Answer found! Return and exit
      return position

    # Increament the position
    position += 1

    # Check if we have reached the end of the array
    if position == len(cards):
      # Number not found, Return -1
      return -1
    
  return "Empty List"


# Use this run_tests() function for all other test run cases to check pass and failed

import time

def run_tests():
    total_execution_time = 0
    passed_tests = 0
    failed_tests = 0

    for i, test in enumerate(tests, 1):
        input_data = test['input']
        expected_output = test['output']

        start_time = time.time()
        result = locate_card(**input_data)
        end_time = time.time()

        total_execution_time += end_time - start_time

        if result == expected_output:
            passed_tests += 1
            print(f'\033[92mTest case {i}: Passed (Execution Time: {end_time - start_time:.9f} seconds)\033[0m')
        else:
            failed_tests += 1
            print(f'\033[91mTest case {i}: Failed. Expected {expected_output}, got {result} (Execution Time: {end_time - start_time:.9f} seconds)\033[0m')

    print(f'\nTotal Execution Time for all test cases: {total_execution_time:.9f} seconds')
    print(f'Total Passed: \033[92m{passed_tests}\033[0m, Total Failed: \033[91m{failed_tests}\033[0m')

# Run the tests
run_tests()
