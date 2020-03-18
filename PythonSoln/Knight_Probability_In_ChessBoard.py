"""
Original Link to problem: https://leetcode.com/problems/knight-probability-in-chessboard/

Statement of the problem:

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and
 columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction,
then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go
off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability
that the knight remains on the board after it has stopped moving.



========================================================================================================================
+ Background of the problem
========================================================================================================================
    This is a classial hitting time problem in markov chain, it's usually taking power of the transition matrix of the
    states and then see the probability of the absorbing states to determine the probability of staying on the board.

    However this is overkill and we are using dynamic programming instead, because it's probably going to be some kind
    of interview question here.


========================================================================================================================
+ A Dynamic Programming Approach to the problem
========================================================================================================================

    * if the knight is at i, j, where could it go in the next step?

        changes in coordinates:
        (2,1),   (1,2)
        (2,-1),  (1,-2)
        (-2,1),  (-1,2)
        (-2,-1), (-1,-2)
        Define this set of points: KnightMoves.

    * if the knight is at i, j currently, where was it one step before?

        takes the negative of all previously listed coordinates.

    * absorbing state:
        1. More than k moves.
        2. Out of chess board.

    * What are we looking at?
        The probability that the knight remains in the board.

    Assumption:
        Once of the knight is out of the board, then it remains there and never comes back.


========================================================================================================================
+ Solution to the problem
========================================================================================================================
    Input: N, K, I0, J0

    Create NxN table, each entry storing the probability of the night ending at the position after m steps.
    Tbl := The table we created.

    Create a variable, storing the probability of the knight got absorbed.

    Compute on the table for k times and use 1-ProbabilityOfAbosorbing to get the result.

    Initialization:
        Tbl[I0][J0] := 1
        OutofBoardProb: = 0
    for i in range(k):
        foreach entry in Tbl:
            Tbl[entry] += 1/8(Value in the previous entry where the knight could come from)
            if Tbl[entry] results out of the board: OutofBoardProb += sum of all entries that can move out of the board
            in the next step.

    return OutofBoardProb

"""



def soln(n, k, i0, j0):
    Tbl = [[0 for i in range(n)] for j in range(n)]
    Tbl[i0][j0] = 1
    OutOfChessBoard = 0
    Entries = [(I, J) for I in range(n) for J in range(n)]
    for K in range(k):
        NextTbl = [[0 for i in range(n)] for j in range(n)]
        for I, J in Entries:
            if Tbl[I][J] == 0:
                continue
            for DeltaI, DeltaJ in get_moves():
                if I + DeltaI < n and I + DeltaI >= 0 and J + DeltaJ < n and J + DeltaJ >= 0:
                    NextTbl[I + DeltaI][J + DeltaJ] += (1/8)*Tbl[I][J]
                else:
                    OutOfChessBoard += (1/8)*Tbl[I][J]
        Tbl = NextTbl
    return 1 - OutOfChessBoard


def get_moves():
    return [(2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2),(-2,-1),(-1,-2)]


def brief_test():
    print(soln(20, 2, 9, 9))
    print("Above solution should be 0. ")

    print(soln(20, 20, 9, 9))
    print("Above solution should be 0.5462. ")
    pass


if __name__ == "__main__":
    brief_test()