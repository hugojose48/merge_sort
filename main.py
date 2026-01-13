import random


def merge_sort(items):
    """
    Merge Sort implementation (in-place).
    It recursively splits the list into halves, sorts each half,
    and then merges them back into the original list.
    """
    # Base case: a list of length 0 or 1 is already sorted
    if len(items) > 1:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        # Debug output: show the current split
        print(left, "*" * 5, right)

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Pointers (indices) to traverse left and right sublists
        i = 0  # index for left
        j = 0  # index for right
        # Pointer (index) for the main list where we write merged values
        k = 0  # index for items

        # Merge the two sorted halves into the original list
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i += 1
            else:
                items[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining elements from left (if any)
        while i < len(left):
            items[k] = left[i]
            i += 1
            k += 1

        # Copy any remaining elements from right (if any)
        while j < len(right):
            items[k] = right[j]
            j += 1
            k += 1

        # Debug output: show the merge result at this recursion level
        print(f"left {left}, right {right}")
        print(f"items {items}")
        print("-" * 50)

    return items


if __name__ == "__main__":
    list_size = int(input("What size should the list be? "))

    # Generate a list of random integers between 0 and 100
    items = [random.randint(0, 100) for _ in range(list_size)]
    print(items)
    print("-" * 20)

    sorted_items = merge_sort(items)
    print(sorted_items)
