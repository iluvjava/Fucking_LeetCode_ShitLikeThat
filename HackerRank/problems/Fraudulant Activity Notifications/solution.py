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
        I, J, Arr = self._P[0], self._P[1], self._Arr
        self._N += 1
        Arr[E] += 1
        
        if self._N == 1:
            self._P = (E, 1)
            return
        
        if self._N % 2 == 1:
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
            if Arr[I] < J:
                while Arr[I] == 0:
                    I -= 1
                self._P = (I, Arr[I])
            else:
                self._P = (I, J - 1)
        return

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
        return (I + self._P[0])/2

    @property
    def arr(self):
        return self._Arr

    
def main():
    def Test1():
        Keeper = MedianKeeper(100)
        Keeper.add(3)
        print(Keeper.median())
        Keeper.add(6)
        print(Keeper.median())
        Keeper.add(9)
        print(Keeper.median())
        Keeper.add(9)
        print(Keeper.median())
        print(Keeper.arr)

    def Test2():
        pass

    Test1()



if __name__ == "__main__":
    main()