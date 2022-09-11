#include "leetcode.h"

int main(int argc, char **argv)
{
    CTools tools;
    tools.start();

    // leetcode算法题测试
    CLeetCode lc;
    lc.test();

    tools.~CTools();
    return 0;
}
