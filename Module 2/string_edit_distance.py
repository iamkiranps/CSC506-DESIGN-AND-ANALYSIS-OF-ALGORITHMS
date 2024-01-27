"""
    Kiran Ponappan Sreekumari
    CSC506 – Design and Analysis of Algorithms
    Colorado State University - Global
    Dr. Dong Nguyen 
    January 25, 2024
    Module 2: Critical Thinking - Option #1: String Edit Distance Problem

"""
import sys
def string_edit_distance(word1, word2):
    m, n = len(word1), len(word2)

    # Create a matrix to store the edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the matrix with base cases
    for i in range(m + 1):
        dp[i][0] = i * 20  # Cost of deleting a letter

    for j in range(n + 1):
        dp[0][j] = j * 20  # Cost of inserting a letter

    # Fill the matrix using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost_copy = dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]) * 5  # Cost of copying or replacing a letter
            cost_delete = dp[i - 1][j] + 20  # Cost of deleting a letter
            cost_insert = dp[i][j - 1] + 20  # Cost of inserting a letter
            dp[i][j] = min(cost_copy, cost_delete, cost_insert)

    # The bottom-right cell of the matrix contains the final edit distance
    return dp[m][n]

#Input string
word1 = sys.argv[1]
word2 = sys.argv[2]
result = string_edit_distance(word1, word2)

print(f"The edit distance between '{word1}' and '{word2}' is {result}.")
