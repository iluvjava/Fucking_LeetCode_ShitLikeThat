// 2Sum.cpp : This file contains the 'main' function. Program execution begins and ends there.
//=====================================
// This is a failed attempt, when I choose to use binary seach, the index information in the original 
// array will be lost, this is unwanted. 
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

inline bool comp(int& a, int& b)
{
    return a < b;
}

// l inclusive, h exclusive. 
/**
*   @param v
*   the vector.
*   @param n
*   the number to search
*   @param l
*   the lower bound inclusive
*   @param h
*   The upperbound inclusive. 
*/
int BinarySearch_1(vector<int>& v, int n, int l, int h)
{
    if (n < v[l] || n > v[h]) return -1; // out of range skip.  
    if (l == h) return (v[h] == n)? h : -1;
    if (l > h) return -1; // for logical closure. 
    if (h - l == 1)
    {
        if (v[h] == n)return h;
        else
            return (v[l] == n)? l : -1;
    }
    int mid = (l + h + 1) / 2;
    if (n == v[mid]) return mid;
    if (n < v[mid])
    {
        return BinarySearch_1(v, n, l, mid - 1);
    }
    if (n > v[mid])
    {
        return BinarySearch_1(v, n, mid + 1, h);
    }
    return -1; // for closure. 
}

void Sort(vector<int>& v)
{
    sort(v.begin(), v.end(), comp);
}

/**
* Precondition: Array is sorted. 
* This is a wrapper function. 
*
*/
int BinarySearch(vector<int>& v, int target)
{
    return BinarySearch_1(v, target, 0, v.size() - 1); 
}


class Solution {
    public:
        // a [i, j] such that nums[i] + nums[j] == target is true.
        vector<int> twoSum(vector<int>& nums, int target)
        {
            vector<int>* res = new vector<int>();
            Sort(nums);
            {
               
                for (int t = 0; t < nums.size(); t++)
                {
                    int J = BinarySearch(nums, target - nums[t]);
                    // Yo, they cannot be the same number, ok... Bin search only returns the first one it founds....
                    if (J != -1 && J != t)
                    {
                        res->push_back(t);
                        res->push_back(J);
                        return *res;
                    }
                }
            }
            return *res;
        }
};

// Runs against brute force with randomized tests. 
void CorrectnessTest()
{
    //bleh
}

int main()
{
    cout << "Ok, let's test some shit on this: \n";
    int arr[] = { 2, 7, 11, 15 };
    vector<int>* v = new vector<int>(arr, arr + 4); 

    cout << BinarySearch(*v, 2) << endl;
    cout << BinarySearch(*v, 7) << endl;
    cout << BinarySearch(*v, 11) << endl;
    cout << BinarySearch(*v, 15) << endl;
    cout << BinarySearch(*v, -1) << endl;
    cout << BinarySearch(*v, 18) << endl;

    Solution* soln = new Solution();
    vector<int> indices = soln->twoSum(*v, 9);

    if (indices.size() == 2)cout << indices[0] << ", " << indices[1] << endl;
    else cout << "Something is wrong" << endl;

    string halt;
    cin >> halt;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files
//   to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
