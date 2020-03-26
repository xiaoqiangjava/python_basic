#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 链表数据结构


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    @staticmethod
    def reverse_list(head):
        """
        链表反转
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        return pre

    @staticmethod
    def swap_paris(head):
        """
        链表交换相邻元素
        1->2->3->4
        2->1->4->3
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = None, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a

        return pre.next

    @staticmethod
    def has_cycle(head):
        """
        判断链表是否有环
        :param head: 头结点
        :return:
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True

        return False

    @staticmethod
    def has_cycle1(head):
        """
        通过判断元素是否已经遍历来确定是否有环
        :param head:
        :return:
        """
        list = []
        while head and head.next:
            head = head.next
            if list.count(head) == 1:
                return True
            list.append(head)

        return False
