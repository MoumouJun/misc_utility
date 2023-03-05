#ifndef _LEET_CODE_H_
#define _LEET_CODE_H_

#include "alg.h"

using namespace std;
class CLeetCode
{
public:
    CLeetCode()
    {
        log_i("leetcode", "[CLeetCode] 算法题测试");
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
            ? (log_i("leetcode", "[OK]%s", __FUNCTION__))
            : (log_e("leetcode", "[ERROR]%s", __FUNCTION__));
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
            ? (log_i("leetcode", "[OK]%s", __FUNCTION__))
            : (log_e("leetcode", "[ERROR]%s", __FUNCTION__));
    }

    /**
     * @brief 滑动窗口 unordered_set作为队列
     *
     * @param s
     * @return int
     */
    int lengthOfLongestSubstring(string s)
    {
        if (s.size() == 0)
            return 0;
        unordered_set<char> w;
        int max_ = 0, len = 0;
        for (int i = 0; i < s.size(); i++)
        {
            while (w.find(s[i]) != w.end())
            {
                w.erase(s[len]);
                len++;
            }
            max_ = max(max_, i - len + 1);
            w.insert(s[i]);
        }
        return max_;
    }
    void test_lengthOfLongestSubstring(void)
    {
        (lengthOfLongestSubstring("pwwkew") == 3)
            ? (log_i("leetcode", "[OK]%s", __FUNCTION__))
            : (log_e("leetcode", "[ERROR]%s", __FUNCTION__));
    }

    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        return 0.0;
    }

    void test_findMedianSortedArrays(void)
    {
        (lengthOfLongestSubstring("pwwkew") == 3)
            ? (log_i("leetcode", "[OK]%s", __FUNCTION__))
            : (log_e("leetcode", "[ERROR]%s", __FUNCTION__));
    }

    int expand(const string &s, int left, int right)
    {
        while (left >= 0 && right < s.size() && s[left] == s[right])
        {
            --left;
            ++right;
        }
        return (right - left - 2) / 2;
    }

    /**
     * @brief 马拉车算法
     *
     * @param s
     * @return string
     */
    string longestPalindrome(string s)
    {
        int start = 0, end = -1;
        string t = "#";
        for (char c : s)
        {
            t += c;
            t += '#';
        }
        t += '#';
        s = t;

        vector<int> arm_len;
        int right = -1, j = -1;
        for (int i = 0; i < s.size(); ++i)
        {
            int cur_arm_len;
            if (right >= i)
            {
                int i_sym = j * 2 - i;
                int min_arm_len = min(arm_len[i_sym], right - i);
                cur_arm_len = expand(s, i - min_arm_len, i + min_arm_len);
            }
            else
            {
                cur_arm_len = expand(s, i, i);
            }
            arm_len.push_back(cur_arm_len);
            if (i + cur_arm_len > right)
            {
                j = i;
                right = i + cur_arm_len;
            }
            if (cur_arm_len * 2 + 1 > end - start)
            {
                start = i - cur_arm_len;
                end = i + cur_arm_len;
            }
        }

        string ans;
        for (int i = start; i <= end; ++i)
        {
            if (s[i] != '#')
            {
                ans += s[i];
            }
        }
        return ans;
    }

    void test_longestPalindrome(void)
    {
        (longestPalindrome("babad") == "aba")
            ? (log_i("leetcode", "[OK]%s", __FUNCTION__))
            : (log_e("leetcode", "[ERROR]%s", __FUNCTION__));
    }
    void test(void)
    {
        test_twoSum();
        test_addTwoNumbers();
        test_lengthOfLongestSubstring();
        test_longestPalindrome();
    }

private:
};

#endif //_LEET_CODE_H_