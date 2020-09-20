def solution(height):
    # use the stack to do the following: 
    # For each element in the array, find the index of the element that is immeidately larger than the current 
    # Element to the right side of the element. 

    def ImmdiateRightLarger():
        RightEqualOrLarger = [None]*len(height)
        MonotonicBars = []
        for I, H in enumerate(height):
            if not MonotonicBars or H < height[MonotonicBars[-1]]:
                MonotonicBars.append(I)
            else:
                while MonotonicBars and height[MonotonicBars[-1]] <= H:
                    J = MonotonicBars.pop()
                    RightEqualOrLarger[J] = I
        print("Right Equal or Lerger for each bar")
        print(RightEqualOrLarger)      
        return RightEqualOrLarger
    TrappingFromRight = ImmdiateRightLarger()

    return


def main():
    print(solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    pass


if __name__ == "__main__":
    main()