def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst)
      and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        return -1

    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:

# Scenario 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Modified list 1:", result1)

# Scenario 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Modified list 2:", result2)
