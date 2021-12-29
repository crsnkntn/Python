# Question 2A from the Google Foobar challenge
#
# The problem is:
#
#       Given squares a and b, return the smallest number of moves to get from a to b on a chess board
#
#       The chess board squares are 0-63
#
#       Additional requirement: MUST BE FAST
from typing import List

def gen_moves(memo: List[List[bool]], dest: int, num_moves: int) -> int:
    for i, n in enumerate(memo[:]):
        if not n:
            continue
        for a, b in [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
            x = (i%8) + a 
            y = i + 8 * b
            if 0 > x or x > 7 or 0 > y  or y > 63:
                continue
            i_ = (i + a) + (8 * b)
            if i_ == dest:
                return num_moves
            memo[i_] = True

    return gen_moves(memo, dest, num_moves + 1)
   

def solution(src: int, dest: int) -> int:
    moves = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
    memo = [False] * 64
    memo[src] = True
    n = gen_moves(memo, dest, 1)
    return n


def main() -> None:
    print(solution(0, 1))


if __name__ == "__main__":
    main()