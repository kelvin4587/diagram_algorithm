def count_donw(i):
    if i <= 1:
        print(i)
        return
    else:
        count_donw(i - 1)
        print(i)


if __name__ == '__main__':
    count_donw(7)
