import time


def merge_sort(array):

    if len(array) <= 1:
        return array

    midpoint = int(len(array) / 2)

    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    return merge(left, right)


def merge(left, right):
    _result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            _result.append(left[left_pointer])
            left_pointer += 1

        elif right[right_pointer] < left[left_pointer]:
            _result.append(right[right_pointer])
            right_pointer += 1

    _result.extend(left[left_pointer:])
    _result.extend(right[right_pointer:])

    return _result


if __name__ == "__main__":
    _array = [5, 4, 3, 2, 1, 23, 64, 234, 65, 2346, 2345, 234, 4567345, 34, 34, 6, 3, 6, 3, 6, 435, 6, 3, 6, 128735,
              345, 236, 675, 48435, 34, 36456, 457, 35, 64]
    print(_array)
    start = time.perf_counter()
    result = merge_sort(_array)
    end = time.perf_counter()
    print(result)
    print(end - start)
