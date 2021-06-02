def minion_game(string):
    vowels = "AEIOU"
    l = len(string)
    stuart_pts = 0
    kevin_pts = 0
    n = 0
    for i in string:
        index = vowels.find(i)

        if index == -1:
            stuart_pts = stuart_pts + len(string) - n
            n = n + 1
        else:
            kevin_pts = kevin_pts + len(string) - n
            n = n + 1
    if stuart_pts > kevin_pts:
        print('Stuart', stuart_pts)
    elif stuart_pts < kevin_pts:
        print('Kevin', kevin_pts)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)