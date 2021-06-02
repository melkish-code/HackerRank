#Find a string
def count_substring(string, sub_string):
    list1 = []
    m = len(string)
    n = len(sub_string)
    o = m - n + 1
    for i in range(o):
        list1.append(string[i:i + n])

    return (list1.count(sub_string))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)