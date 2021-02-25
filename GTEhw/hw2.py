
# QUESTION 1
# Given a list of positive integers, count how many prime numbers are in the list. A prime number is defined as an integer greater than 1 that cannot be written as a product of two integers that are not 1 or itself.
# Ex:
# [1,2,3] => 2
# [17] => 1
# [4,6,8,10] => 0
# [4,4,4,13,4,4,4] => 1
def test(list):
    counter = 0 
    for num in list:
        for i in range(2, num+1):
            if num == i:
                counter += 1
            elif num % i == 0:
                break
                #print(num)
    return counter
#test([2,3,4,5,6,7,8,9,10])
#print(test([2,3,4,5,6,7,8,9,10]))
#print(test([1,2,3]))

# QUESTION 2
# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE:
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false
def isOneEditAway(str1, str2):
    i = 0
    j = 0
    edit_count = 0
    if len(str1)!= len(str2):
        longer = max(len(str1), len(str2))
        shorter = min(len(str1), len(str2))
        # print(f"longer is {longer} and shorter is {shorter}")
        if longer-1 != shorter:
            return False
        
    while i < len(str1) and j < len(str2):
        # print(f"i is {i}")
        # print(f"j is {j}")
        # print(f"edit count is {edit_count}")
        # if one of the pointers reached the end of the string before the other
        # if i == len(str1)-1 or j == len(str2)-1:
        #     edit_count += 1
        #     if edit_count > 1:
        #         return False
        if str1[i] != str2[j]:
            edit_count += 1
            if edit_count > 1:
                return False
            #if i + 1 >= len(str1) or j+1 >= len(str2):

            if str1[i+1] == str2[j]: #insert in str1 or removal in str2
                # i = i+1+1
                # j = j + 1
                i = i+1
            elif str1[i] == str2[j+1]: #insert in str2 or removal in str1
                # i = i+1
                # j = j+1+1
                j = j+1
            elif str1[i+1] == str2[j+1]:
                # i = i+1+1
                # j = j+1+1
                i += 1
                j += 1
            else:
                return False
        else: #str1[i] == str2[j]
            i += 1
            j += 1

    return True
# print(isOneEditAway("pale", "ple"))
# print(isOneEditAway("pales", "pale"))
# print(isOneEditAway("pale", "bale"))
# print(isOneEditAway("pale", "bae"))
# print(isOneEditAway("abcd", "dcba"))
# print (isOneEditAway("rale", "bales"))
# print (isOneEditAway("a", "b"))
# print (isOneEditAway("ab", "ac"))
# print (isOneEditAway("abcdefghijklmnopqrst", "abcdefghijklmnopqrsQ"))
# print (isOneEditAway("a", "ba"))
# print (isOneEditAway("ab", "acb"))
# print (isOneEditAway("abcde", "abkd"))
# print (isOneEditAway("abc", "axcd"))
# print (isOneEditAway("abc", "ax"))
# print (isOneEditAway("xyz", "xzw"))
# print (isOneEditAway("", ""))

# QUESTION 3
# Given a sorted list of integers, remove all duplicates such that each element appears only once. Maintain the order of the integers.
# Ex:
# starts like [1, 1, 2], ends like [1,2]
# starts like [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], ends like [0, 1, 2, 3, 4]
# Note: The problem requires to modify the input list and to not return anything.
# Note: Test Case 8 and Test Case 9 tests efficiency. If it fails try a different approach.
def remove_dupes(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    left = 0
    right = left + 1
    while True:
        print(f"left is {left}")
        print(f"right is {right}")
        
        if right < len(lst) - 1:
            if lst[left] == lst[right]:
                del lst[right]
                right = left + 1
            elif lst[left] != lst[right]:
                right = right + 1
        else:
            if right == len(lst)-1:
                if lst[left] == lst[right]:
                    del lst[right]
                    break
                left = left + 1
                right = left + 1
            elif left == len(lst) - 1:
                break
        

# a = [2, 2, 3, 3, 3]
# a = [-1, -1, 1, 1]
# c = [-3, -3, -3, -3, 2, 2, 2, 7, 7, 7, 7]
# remove_dupes(c)
# print(*c, sep=", ")

   


# QUESTION 4
# Given a list lst with non-negative integers where each represents the heights.
# Find two heights, which together form a container, such that the container contains the most water and return the area.
# Example:
# lst = [1, 8, 6, 2, 5, 4, 8, 3, 7] (same as diagram above) -> 7*7 = 49
# lst = [1, 1] -> 1*1 = 1
# lst = [4, 3, 2, 1, 4] -> 4*4 = 16
# lst = [1, 2, 1] -> 1*2 = 2
def most_water(lst):
    left = 0
    right = len(lst)-1
    max_area = -1
    while (left < right):
        area = min(lst[left], lst[right]) * (right - left)
        max_area = max(area, max_area)
        print(f"left is {left} right is {right} area is {area} max area is {max_area}")
        left += 1
        area = min(lst[left], lst[right]) * (right - left)
        max_area = max(area, max_area)
        print(f"left is {left} right is {right} area is {area} max area is {max_area}")
        right -= 1
    # left = 0
    # while (left < right):
    #     area = min(lst[left], lst[right]) * (right - left)
    #     max_area = max(area, max_area)
    #     print(f"left is {left} right is {right} area is {area} max area is {max_area}")
    #     right -= 1
    return max_area


# print(most_water([1,8,6,2,5,4,8,3,7]))
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
def tic_tac_toe(board):
    n = len(board)
    curr_player = ''
    for i in range(n):
        for j in range(n):
            if j == 0:
                curr_player = board[i][j]
            elif board[i][j] == curr_player:
                skip
            elif j==n:
                if curr_player == 'X':
                    return 1 # X wins
                if curr_player == 'O':
                    return 2 # O wins
            # board[i][j] goes by row
            
tic_tac_toe([['X', 'X', 'X'],['O', 'O', 'X'],['O', 'X', 'O']])