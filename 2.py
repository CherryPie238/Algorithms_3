def min_copy_time(n, x, y):
    if n <= 0:
        return 0

    first = min(x, y)

    left = 0
    right = (n - 1) * first

    while left < right:
        mid = (left + right) // 2

        copies = mid // x + mid // y

        if copies >= n - 1:
            right = mid
        else:
            left = mid + 1

    return first + left
