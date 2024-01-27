"""
    Kiran Ponappan Sreekumari
    CSC506 – Design and Analysis of Algorithms
    Colorado State University - Global
    Dr. Dong Nguyen 
    January 19, 2024
    Module 1: Critical Thinking - Option #2: Algorithms in Practice

"""
def next_larger_permutation(arrangement):
    arrangement = [int(i) for i in str(arrangement)]
    n = len(arrangement)
    
    # Step 1 - Find the first pair of adjacent digits 
    i = n - 1
    while i > 0 and arrangement[i] <= arrangement[i-1]:
        i = i - 1

    # Step 2 - Return no rearrangement
    if i == 0:
        return "No rearrangement possible"

    # Step 3 - Find the smallest digit 
    j = n - 1
    while arrangement[j] <= arrangement[i-1]:
        j = j - 1

    # Step 4 - Swap digits
    arrangement[i-1], arrangement[j] = arrangement[j], arrangement[i-1]

    # Step 5 - Reverse
    arrangement[i:] = reversed(arrangement[i:])

    # Step 6 - Convert list into number and return
    return int(''.join(str(i) for i in arrangement))

# Example usage
arrangement = input("Enter number : ")
result = next_larger_permutation(arrangement)

print(result)

