
def solution():

class IntegerMedianKeeper():
    """
        The range of all the integer data mustbe predefined.
        All must be positive integers.
    """

    def __init__(self, maxIntVal):
        self._N = 0
        self._P = (0, 0)  # index, frequency pointer, fixed at n//2 if even, n//2 + 1 if odd
        # self._ElementToLeft = self._ElementToRight = 0  # the element the pointer is pointing at is not included.
        self._Arr = [0 for _ in range(maxIntVal + 1)]

    def add(self, E):
        I, J, Arr = self._P[0], self._P[1], self._Arr
        self._N += 1
        Arr[E] += 1
        # Edge case size == 1 ------------------------------------------------------------------------------------------
        if self._N == 1:
            self._P = (E, 1)
            return
        # Edge case size == 2
        if self._N == 2 and E < I:
            self.__move_left()
            return
        # Decide which direction to move the pointer -------------------------------------------------------------------
        if E >= I and self._N % 2 == 1:
            self.__move_right()
        elif E < I and self._N % 2 == 0:
            self.__move_left()


    def remove(self, E):
        if self._Arr[E] == 0:
            raise RuntimeError
        I, J, Arr = self._P[0], self._P[1], self._Arr
        self._Arr[E] -= 1
        # Decide where to move the pointer -----------------------------------------------------------------------------
        if E < I and self._N % 2 == 0:
            self.__move_right()
        elif E > I and self._N % 2 == 1:
            self.__move_left()
        elif E == I: # Edge case ---------------------------------------------------------------------------------------
            if J > Arr[I]:
                if self._N % 2 == 1:
                    self.__move_left()
                else:
                    self.__move_right()
        self._N -= 1


    def __move_left(self):
        """
            Find the immediate number on the left of
            current index that is not empty.
        :param toRight:
        :return:
        """
        I, J = self._P
        Arr = self._Arr
        if J - 1 >= 1:
            self._P = (I, J - 1)
        else:
            I -= 1
            while Arr[I] == 0:
                I -= 1
            self._P = (I, Arr[I])


    def __move_right(self):
        I, J = self._P
        Arr = self._Arr

        if J + 1 <= Arr[I]:
            self._P = (I, J + 1)
        else:
            I += 1
            while Arr[I] == 0:
                I += 1
            self._P = (I, 1)


    def median(self):
        I, J = self._P
        Arr = self._Arr
        if self._N % 2 == 0:
            if Arr[I] == J:
                I += 1
                while Arr[I] == 0:
                    I += 1
        if self._N % 2 == 1:
            return self._P[0]
        return (I + self._P[0]) / 2

    @property
    def arr(self):
        return self._Arr



if __name__ == "__main__":
    main()