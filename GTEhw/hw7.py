def permutationCoeff(n, k): 
  
    cache = [[0 for i in range(k + 1)]  for j in range(n + 1)] 
  
    # Calculate value of Permutation 
    # Coefficient in 
    # bottom up manner 
    for i in range(n + 1): 
        for j in range(min(i, k) + 1): 
  
            # Base cases 
            if (j == 0): 
                cache[i][j] = 1
  
            # Calculate value using  
            # previously stored values 
            else: 
                cache[i][j] = cache[i - 1][j] + ( 
                           j * cache[i - 1][j - 1]) 
  
            # This step is important  
            # as P(i, j) = 0 for j>i 
            if (j < k): 
                cache[i][j + 1] = 0
    return cache[n][k] 


# def countWays(n) :
#     res = [0] * (n + 2)
#     res[0] = 1
#     res[1] = 1
#     res[2] = 2
     
#     for i in range(3, n + 1) :
#         res[i] = res[i - 1] + res[i - 2] + res[i - 3]
     
#     return res[n]
# print(countWays(3))

def findStep( n) :
    if (n == 1 or n == 0) :
        return 1
    elif (n == 2) :
        return 2
     
    else :
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)
 
 
# Driver code
n = 4
print(findStep(n))