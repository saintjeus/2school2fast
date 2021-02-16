# QUESTION 1
# Given a list of positive integers, count how many prime numbers are in the list. A prime number is defined as an integer greater than 1 that cannot be written as a product of two integers that are not 1 or itself.
# Ex:
# [1,2,3] => 2
# [17] => 1
# [4,6,8,10] => 0
# [4,4,4,13,4,4,4] => 1

# QUESTION 2
# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE:
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false

# QUESTION 3
# Given a sorted list of integers, remove all duplicates such that each element appears only once. Maintain the order of the integers.
# Ex:
# starts like [1, 1, 2], ends like [1,2]
# starts like [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], ends like [0, 1, 2, 3, 4]
# Note: The problem requires to modify the input list and to not return anything.
# Note: Test Case 8 and Test Case 9 tests efficiency. If it fails try a different approach.

# QUESTION 4
# Given a list lst with non-negative integers where each represents the heights.
# Find two heights, which together form a container, such that the container contains the most water and return the area.
# Example:
# lst = [1, 8, 6, 2, 5, 4, 8, 3, 7] (same as diagram above) -> 7*7 = 49
# lst = [1, 1] -> 1*1 = 1
# lst = [4, 3, 2, 1, 4] -> 4*4 = 16
# lst = [1, 2, 1] -> 1*2 = 2

# QUESTION 5
# Given a list lst only made up of the integers 0 and 1, and positive integer k, return the length of the longest contigous sublist that contains only 1s given that you may change up to k values from 0 to 1.
# Example:
# lst = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2 outputs 6.
# Explanation: [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1] Longest sublist is underlined and bolded numbers were flipped from 0 to 1.
# lst = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3 outputs 10.
# Explanation: [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1] Longest sublist is underlined and bolded numbers were flipped from 0 to 1.

# QUESTION 6
# Given an NxN tic tac toe board with values ('', 'O', 'X'), 
# return integer 0 (Game not over), 1 (X wins), 2 (O wins),  or 3 (tie).
# A winner is declared if a full row, col, or full diagonal has either 
# all Os or Xs. You may assume any given board is in a valid state and N >= 3
# Example:
# board =
# [
#   ['X', 'X', 'X'],
#   ['O', 'O', 'X'],
#   ['O', 'X', 'O']
# ] -> 1 (X wins)
# board =
# [
#   ['', '', 'O'],
#   ['', 'X', ''],
#   ['', '', 'X']
# ] -> 0 (Game not over)
# board =
# [
#   ['', '', 'O', 'X'],
#   ['', 'X', '', 'O'],
#   ['', '', 'X', 'X']
# ] -> 0 (Game not over)