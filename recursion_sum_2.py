def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])


if __name__ == '__main__':
    print(sum([1, 2, 3, 9]))
