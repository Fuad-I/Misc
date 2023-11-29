# A = [i for i in range(3, 0, -1)]
A = [5, 2]
B = [4, 1]
C = [3]

"""def move(n, source, auxiliary, target):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, target, auxiliary)

        target.append(source.pop())
        # solution.append(f'{target[-1]} -> ')

        print(A, B, C, '##############', sep='\n')

        # Move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, source, target)


# Initiate call from source A to target C with auxiliary B
move(6, A, B, C)"""


def move(lst, source, auxiliary, target):
    if len(lst) == 1:
        target.append(source.pop())
        print(A, B, C, '##############', sep='\n')
    else:
        l = len(lst) - 1
        move(lst[1:], source, target, auxiliary)
        target.append(source.pop())
        print(A, B, C, '##############', sep='\n')
        move(auxiliary[len(auxiliary) - l:], auxiliary, source, target)

# move(A, A, B, C)


def find(num, lst1, lst2, lst3):
    if num in lst1:
        return 0, lst1.index(num)
    elif num in lst2:
        return 1, lst2.index(num)
    else:
        return 2, lst3.index(num)


def solution(source, auxiliary, target):
    elements = list(sorted([item for item in source + auxiliary + target]))
    lst = [source, auxiliary, target]
    while elements:
        if elements[-1] in target:
            elements.pop()
        else:
            j = 0
            while j < len(elements) - 1:
                temp = [0, 1, 2]
                pos1 = find(elements[j], source, auxiliary, target)
                pos2 = find(elements[j + 1], source, auxiliary, target)
                if pos1[0] == pos2[0]:
                    j += 1
                else:
                    temp.remove(pos1[0])
                    temp.remove(pos2[0])
                    move(lst[pos1[0]][pos1[1]:], lst[pos1[0]], lst[temp[0]], lst[pos2[0]])
                    j += 1
            new_pos = find(elements[-1], source, auxiliary, target)
            new_temp = [0, 1]
            new_temp.remove(new_pos[0])
            move(lst[new_pos[0]][new_pos[1]:], lst[new_pos[0]], lst[new_temp[0]], target)


# solution(A, B, C)
