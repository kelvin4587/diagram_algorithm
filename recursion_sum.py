def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        last_value=arr.pop()
        return last_value+sum(arr)


if __name__ == '__main__':
    print(sum([1,2,3,9]))

