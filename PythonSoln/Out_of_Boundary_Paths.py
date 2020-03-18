"""
Original Problem: https://leetcode.com/problems/out-of-boundary-paths/


There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent
cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times.
Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after
mod 109 + 7.


The problem rephrase:
    The ball moves in 4 directions, up down left right, one grid at a time.
    Find the number of paths less than N such that it gets out of the M by N grid.

    Note:
        This problem is very similar to Knight_probability_in_ChessBoard.


========================================================================================================================
+ Dynamic Programming and Solution
========================================================================================================================
    Tbl[i, j, k]:
        The number of paths that ends at i, j with exactly k moves.

    Tbl[i, j, k+1] += sum(
        Tbl[i-1, j-1, k],
        Tbl[i-1, j, k],
        Tbl[i+ 1, j, k ],
        Tbl[i, j+1, k]
    )

    For this problem we want a forward simulation, evolving the time step.

    for k in range(n):
     for each of the <nextentry> that the ball can go to:
        if it's still inside the grid: tbl[nextentry] += 1
        else:
            Increment the results

"""


def soln(m, n, N, i0, j0):
    tbl = [[0 for i in range(n)]for j in range(m)]
    tbl[i0][j0] = 1
    RecursiveTracking = []
    RecursiveTracking2 = []
    PathOutside = 0
    def outside(x,y):
        return x < 0 or x >= m or y < 0 or y >= n
    for K in range(N):
        newtbl = [[0 for i in range(n)]for j in range(m)]
        for I, J in [(I, J) for I in range(m) for J in range(n)]:
            if tbl[I][J] == 0:
                continue
            for dI, dJ in moves():
                if outside(I + dI, J + dJ):
                    PathOutside += tbl[I][J]
                else:
                    newtbl[I+dI][J+dJ] += tbl[I][J]
        RecursiveTracking.append(tbl)
        RecursiveTracking2.append(PathOutside%1000000007)
        tbl = newtbl

    return PathOutside%1000000007, RecursiveTracking, RecursiveTracking2


def moves():
    return [(0,1),(1,0),(-1,0),(0,-1)]

def brieftest():
    _, Solns, ObjVals = soln(4,4,20,0,0)

    MaxLen = 0

    for Table in Solns:
        for Row in Table:
            for N in Row:
                MaxLen = max(len(str(MaxLen)), N)

    for Table, ObjVals in zip(Solns, ObjVals):
        for Row in Table:
            for N in Row:
                print(str(N).ljust(MaxLen), end="|")
            print()
        print(f"Objecval: {ObjVals}\n")
    pass

if __name__ == "__main__":
    brieftest()
