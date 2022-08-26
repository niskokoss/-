https://py.checkio.org/ru/mission/find-sequence/

from typing import List


def checkio(matrix: List[List[int]]) -> bool:
    print(matrix)
    number_v = 0
    number_g = 0
    number_d = 0
    N = len(matrix[0])
    for vertical in range(N):
        for horizon in range(N):
            for i in range(horizon + 1, N):
                if matrix[vertical][horizon] == matrix[i][horizon]:
                    number_v += 1
                else:
                    number_v = 0
                if matrix[vertical][horizon] == matrix[vertical][i]:
                    number_g += 1
                else:
                    number_g = 0
                try:
                    if matrix[vertical][horizon] == matrix[vertical + i][horizon + i]:
                        number_d += 1
                    else:
                        number_d = 0
                except IndexError:
                    number_d = 0
                print(number_d,number_v,number_g)
                if number_v >= 4 or number_g >= 4 or number_d >= 4:
                    print(matrix[vertical][horizon], matrix[vertical])
                    return True
    return False




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[1,5,6,3,7,3,2],[2,9,1,1,5,3,8],[3,3,3,1,1,8,9],[4,2,1,3,2,1,4],[1,4,5,7,1,3,6],[4,5,8,6,1,1,2],[3,7,1,5,7,4,7]]) == False
    assert checkio([[2,7,6,2,1,5,2,8,4,4],[8,7,5,8,9,2,8,9,5,5],[5,7,7,7,4,1,1,2,6,8],[4,6,6,3,2,7,6,6,5,1],[2,6,6,9,8,5,5,6,7,7],[9,4,1,9,1,3,7,2,3,1],[5,1,4,3,6,5,9,3,4,1],[6,5,5,1,7,7,8,2,1,1],[9,5,7,8,2,9,2,6,9,3],[8,2,5,7,3,7,3,8,6,2]])== False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    print('All Done! Time to check!')
