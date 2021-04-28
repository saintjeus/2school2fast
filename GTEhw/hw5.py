#Question 1
# Given a list of potentially duplicate integers return a list of distinct integers sorted by their frequency in the original list.
# Any numbers that had the same number of duplicates should be returned in their natural sort order. Note that the input data is not sorted.
# Also, remember to take advantage of Python constructs like the sorted function.
# Ex:
# [] => []
# [2] => [2]
# [2, 2, 2, 2] => [2]
# [3, 3, 2, 2] => [2, 3]
# [3, 3, 2, 2, 3] => [3, 2]
# [-1, -3, 0, -3, 5, 5, 5] => [5, -3, -1, 0]
def condense_and_sort_list(lst):
    d = {}
    for i in lst:
        if i not in d:
            d[i] = 0
        d[i] += 1
    print("Dictionary:", d)
    #sort_d = sorted(d.items(), key=lambda kv:kv[1], reverse = True)
    d = sorted(d.items())
    sort_d = sorted(d, key=lambda d:d[1], reverse = True)
    result = []
    for item in sort_d:
         result.append(item[0])
    return result
    #print("Sorted dictionary by val: ", sort_d)

#print(condense_and_sort_list([1, 1, 2, 2, 3, 3,3 , 3, 4, 4,33]))
#print(condense_and_sort_list([3,3,2,2]))
#QUESTION 2
# Dr. Pichai has organized his class into pair programming groups. 
# The groups were supposed to have met twice and each student was 
# supposed to be the driver in one session and the navigator in another session.
# The students roles in each session were stored in tuples where the first item 
# is the driver's name and the second item is the navigator's name. For instance 
# in the tuple ("Tom", "Sally") Tom is the driver and Sally is the navigator.
# In this assignment you will be provided a list of tuples representing pair 
# programming sessions. You will create a function that returns a list of tuples 
# for sessions that still need to occur. For example, given the following sessions:
#   sessions = [("Tom", "Sally"), ("Sally", "Tom"), ("Bob", "Brenda")]
# You would return [('Brenda', 'Bob')] since Brenda has yet to be the driver in a session with Bob.
# You can assume:
#     All pairs have done at least one session, but no more than two sessions.
#     No two pairs have two people with the exact same names, though there might be some people with the same name in the class.
#     Names are case-sensitive.
def find_missing_programming_sessions(completed_sessions):
    d = {}
    for i in completed_sessions:
        if i[0] not in d:
            d[i[0]] = i[1]

    result = []
    for key in d.keys():
        temp = d[key]
        if temp in d:
            if d[temp] != key:
                #result.append(tuple(d[temp], key))
                result.append(tuple([d[temp], key]))
                #print(f"scenario 1: missing sesh: {d[temp]}, {key}")
        else:
            missing_sesh = tuple([temp, key])
            result.append(missing_sesh)
            #print(f"scenario 2: missing sesh: {temp}, {key}")
    return result
#print(find_missing_programming_sessions([ ("Tom", "Sally"), ("Sally", "Tom"), ("Bob", "Brenda")]))
# QUESTION 3
# Create a function that, given a list of unsorted integers,
# returns True if that list contains consecutive integers and 
# False if the list does not contain consecutive integers. 
# Duplicates in the input list indicate that the list does not contain consecutive integers.
# An empty input list is not considered consecutive.
#Solve this problem in O(n) time (no sorting!).
def is_consecutive(lst):
    dictionary = {}
    for i in lst:
        if i not in dictionary:
            dictionary[i]=0
        dictionary[i]+=1
    #print(dictionary)
    consec = True
    counter = 0
    for item in dictionary.keys():
        #print(f"item is {item} value is {dictionary[item]}")
        if dictionary[item] >= 2:
             return False
        elif item+1 in dictionary or item-1 in dictionary:
            consec = consec and True
        elif counter == 0 and item+1 not in dictionary:
            return False
        elif item+1 not in dictionary or item-1 not in dictionary:
            return False
        elif counter == len(dictionary)-1 and item-1 not in dictionary:
            return False
    return consec
#print(is_consecutive([-1,5,4,2,0,3,1]))
#print(is_consecutive([-1,0,0, 1]))
# print(is_consecutive([5,6]))
print(is_consecutive([534, 516, 513, 536, 504, 501, 521, 507, 512, 502, 523, 530, 538, 522, 503, 518, 526, 533, 508, 524, 517, 519, 527, 531, 529, 514, 532, 525, 520, 515, 510, 535, 511, 537, 505, 528, 509, 506]))
print(sorted([534, 516, 513, 536, 504, 501, 521, 507, 512, 502, 523, 530, 538, 522, 503, 518, 526, 533, 508, 524, 517, 519, 527, 531, 529, 514, 532, 525, 520, 515, 510, 535, 511, 537, 505, 528, 509, 506]))
#Question 5: multiple bags
def equivalent_bags(bags):
    d_bags = []

    for i in range(len(bags)):
        d_bags.append(dict_freqval(bags[i]))

    #print (d_bags)
    for i in d_bags:
        for key in i.keys():
            for j in d_bags:
                if key not in j:
                    return False
                if i[key] != j[key]:
                    return False
    return True
    
def dict_freqval(lst):
    d = {}
    for i in lst:
        if i not in d:
            d[i]=0
        d[i]+= 1
    return d
# bag1 = ["cherry", "lemon", "coconut", "cherry", "cherry", "coconut"]

# bag2 = ["coconut", "cherry", "cherry", "cherry", "lemon", "coconut"]

# bag3 = ["coconut", "cherry", "cherry", "cherry", "lemon", "coconut"]
# bags = [bag1, bag2, bag3]
# bag1 = ["cherry", "coconut", "coconut", "cherry", "cherry", "coconut"]

# bag2 = ["coconut", "cherry", "cherry", "cherry", "lemon", "coconut"]

# bag3 = ["coconut", "cherry", "cherry", "cherry", "lemon", "coconut"]
# bags = [bag1,bag2,bag3]
# print(equivalent_bags(bags))