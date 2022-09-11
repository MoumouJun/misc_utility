#ifndef _LEET_CODE_H_
#define _LEET_CODE_H_

#include "alg.h"

using namespace std;
class CLeetCode
{
public:
    CLeetCode()
    {
        log_i("[CLeetCode] 算法题测试");
    }
    ~CLeetCode() {}

public:
    vector<int> twoSum(vector<int> &nums, int target);
    void test_twoSum(void);

    void test(void);

private:
};

#endif //_LEET_CODE_H_