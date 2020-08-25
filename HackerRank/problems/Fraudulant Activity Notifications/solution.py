class MedianKeeper():
    """
        The range of all the integer data mustbe predefined. 
        All must be positive integers.
    """
    
    def __init__(self, maxIntVal):
        self._N = 0
        self._P = (0, 0)  # index, frequency pointer, fixed at n//2
        self._Arr = [0 for _ in range(maxIntVal)]
    
    def add(self, E):
        self._N += 1
        I, J, Arr = self._P[0], self._P[1], self._Arr
        Arr[E] += 1
        if self._N % 2 == 0:
            if J == Arr[I]:
                I += 1
                while Arr[I] == 0:
                    I += 1
                self._P = (I, 1)
            else: 
                self._P = (I, J + 1)
        return

    def remove(self, E):
        if self._Arr[E] == 0:
            raise RuntimeError
        self._N -= 1
        I, J, Arr = self._P[0], self.P[1], self._Arr
        Arr[E] -= 1
        if self._N % 2 == 1:
            if Arr[I] == 0:
                while Arr[I] == 0:
                    I -= 1
                self._P = (I, Arr[I])
            else:
                self._P = (I, J - 1)
        return

    def median(self):
        I, J = self._P
        Arr = self._Arr
        if Arr[I] == J:
            I += 1
            while Arr[I] == 0:
                I += 1
        if self._N % 2 == 1: 
            return Arr[I]

        return (Arr[I] + Arr[self._P[0]])/2

    
def main():
    Keeper = MedianKeeper(100)
    Keeper.add(3)
    Keeper.add(6)
    Keeper.add(9)
    Keeper.median()
    pass


if __name__ == "__main__":
    main()