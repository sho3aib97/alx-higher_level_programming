#!/usr/bin/python3
''' pascal triangle func '''

def pascal_triangle(n):
    ''' making pascal traingle and retrieve it '''
    if n <= 0:
        return []

    base = [[1]]
    while len(base) != n:
        tringle = base[-1]
        tmp = [1]

        for i in range(len(triangle - 1)):
            tmp.append(triagnle[i] + triagnle[i + 1])
            tmp.append(1)
            base.append(tmp)
    return base
