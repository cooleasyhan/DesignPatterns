
#%%
# import time

SLOW = 3
LIMIT = 5
WARNING = 'too bad, you picked the slow algorithm :('


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def all_unique_sort(s):
    tmp = sorted(s)
    for i, j in pairs(s):
        if i == j:
            return False
    return True


def all_unique_set(s):
    return len(set(s)) == len(s)


def all_unique(s, strategy):
    return strategy(s)


def main():
    strategies = [all_unique_set, all_unique_sort]

    for s in strategies:
        print(all_unique('abcdeg', s))
        print(all_unique('abccdega', s))


if __name__ == '__main__':
    main()
