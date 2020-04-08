// 2Sum(Attemp 2).cpp : This file contains the 'main' function. Program execution begins and ends there.
//
// This is a problem that test on the use of data structure. 
// Summarizing the approach. 
// 1. Create a map, mapping the element to the index of that element in the array, call the map "M"
// for each element: e in M: 
//      If k - e in M:
//          return index of (k-e), index of M[e]
//      

#include <iostream>
#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    // a [i, j] such that nums[i] + nums[j] == target is true.
    vector<int> twoSum(vector<int>& nums, int target)
    {
        vector<int> res = *(new vector<int>());
        map<int, int> M = *(new map<int, int>());
        for (int I = 0; I < nums.size(); I++)
        {
            int n = nums[I];
            if (M.count(target - n) == 1)
            {
                res.push_back(I);
                res.push_back(M[target - n]);
                return res;
            }
            else
            {
                M[n] = I;
            }
        }
        return res;
    }
};

int main()
{
    cout << "Program Running!\n";
    
    int testArray[] = { 1,2,3,4,5,6,7,8,9,0 };
    
    int len = sizeof(testArray)/sizeof(testArray[0]);

    cout << "Len: " << len << endl;
    vector<int> testVec = *(new vector<int>(testArray, testArray + len)); // 
    
    Solution soln = Solution();
    vector<int> vec = soln.twoSum(testVec, 9);
    cout << "size of res: " << vec.size() << endl;
    if(vec.size() >= 2) cout << vec[0] << ", " << vec[1] << endl;
    
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
