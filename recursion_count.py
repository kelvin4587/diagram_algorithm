def count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count(arr[1:])


if __name__ == '__main__':
    print(count([1, 2, 3, 9]))
