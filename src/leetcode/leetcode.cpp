#include "leetcode.h"

void CLeetCode::test(void)
{
    test_twoSum();
}

vector<int> CLeetCode::twoSum(vector<int> &nums, int target)
{
    unordered_map<int, int> hashtable;
    for (int i = 0; i < nums.size(); ++i)
    {
        auto it = hashtable.find(target - nums[i]);
        if (it != hashtable.end())
        {
            return {it->second, i};
        }
        hashtable[nums[i]] = i;
    }
    return {};
}


void CLeetCode::test_twoSum(void)
{
    // 1 两数之和
    vector<int> in = {9, 88, 11, 89, 0, 0, 7};
    vector<int> out = {1, 6};
    int target = 95;
    (twoSum(in, target) == out)
        ? (log_i("[OK]twoSum"))
        : (log_e("[ERROR]twoSum"));
}
