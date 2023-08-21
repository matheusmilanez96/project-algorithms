def merge_sort(string, start=0, end=None):
    if end is None:
        end = len(string)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(string, start, mid)
        merge_sort(string, mid, end)
        merge(string, start, mid, end)


def merge(string, start, mid, end):
    left = string[start:mid]
    right = string[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            string[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            string[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            string[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first_lower = first_string.lower()
    second_lower = second_string.lower()
    first_array = []
    for ch in first_lower:
        first_array.append(ch)
    merge_sort(first_array, 0, len(first_array))
    str1 = ""
    first_ordered = str1.join(first_array)

    second_array = []
    for ch in second_lower:
        second_array.append(ch)
    merge_sort(second_array, 0, len(second_array))
    str2 = ""
    second_ordered = str2.join(second_array)
    if (first_ordered == second_ordered and len(first_ordered) > 0):
        return (first_ordered, second_ordered, True)
    else:
        return (first_ordered, second_ordered, False)
