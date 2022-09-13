#ifndef _LEET_CODE_H_
#define _LEET_CODE_H_

#include "alg.h"

using namespace std;
class CLeetCode
{
public:
    CLeetCode()
    {
        log_i("leetcode","[CLeetCode] 算法题测试");
    }
    ~CLeetCode() {}

public:
    /**
     * @brief 哈希map的特性与操作 stl::unordered_map
     * @param nums
     * @param target
     * @return vector<int>
     */
    vector<int> twoSum(vector<int> &nums, int target)
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

    void test_twoSum(void)
    {
        // 1 两数之和
        vector<int> in = {9, 88, 11, 89, 0, 0, 7};
        vector<int> out = {1, 6};
        int target = 95;
        (twoSum(in, target) == out)
            ? (log_i("leetcode","[OK]twoSum"))
            : (log_i("leetcode","[ERROR]twoSum"));
    }

    // Definition for singly-linked list.
    struct ListNode
    {
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };

    /**
     * @brief 链表遍历，加法进位
     * @param l1
     * @param l2
     * @return ListNode*
     */
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *head = nullptr, *tail = nullptr;
        int c = 0;
        while (l1 || l2)
        {
            int n1 = l1 ? l1->val : 0;
            int n2 = l2 ? l2->val : 0;
            int sum = n1 + n2 + c;
            c = static_cast<int>(sum / 10); //隐式转换默认丢失小数部分 implicitly (automatically) convert
            if (nullptr == head)
            {
                head = tail = new ListNode(sum % 10);
            }
            else
            {
                tail->next = new ListNode(sum % 10);
                tail = tail->next;
            }
            if (l1)
                l1 = l1->next;
            if (l2)
                l2 = l2->next;
        }
        if (c > 0)
            tail->next = new ListNode(1);
        return head;
    }

    void test_addTwoNumbers(void)
    {
        // 1 两数之和
        ListNode l1_1(2), l1_2(4), l1_3(3);
        l1_1.next = &l1_2, l1_2.next = &l1_3;
        ListNode l2_1(5), l2_2(6), l2_3(4);
        l2_1.next = &l2_2, l2_2.next = &l2_3;
        ListNode *l = addTwoNumbers(&l1_1, &l2_1);
        ((l->val == 7) &&
         (l->next->val == 0) &&
         (l->next->next->val == 8))
            ? (log_i("leetcode","[OK]addTwoNumbers"))
            : (log_i("leetcode","[ERROR]addTwoNumbers"));
    }

    void test(void)
    {
        test_twoSum();
        test_addTwoNumbers();
    }

private:
};

#endif //_LEET_CODE_H_