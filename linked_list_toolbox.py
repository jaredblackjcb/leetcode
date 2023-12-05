from typing import Optional

class LinkedListToolbox:
    # Merge Sort a Linked List: https://leetcode.com/problems/sort-list/description/

    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None


    # Detect a cycle in a linked list
    def hasCycle(self, head: Optional[ListNode]):
        if not head:
            return False

        # Use two pointers technique w/ fast and slow
        slow = head
        fast = head.next

        while fast and fast.next:
            # A cycle exists if fast and slow pointers are ever the same ListNode object
            if fast == slow:
                return True
            fast == fast.next.next # 2 steps forward
            slow = slow.next # 1 step forward

        return False

    # Find the middle node using the 2 pointer fast/slow method (this is fine if you just need the val of the middle node)
    # This is using 0-based indexing.
    # For lists of size = 1, 2, 3, 4, and 5, the middle nodes are at index 0, 1, 1, 2, and 2, respectively.
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    # Find the middle node (represents the right side of the list)
    # Removes the pointer from slow.next to split the list into left and right halves (head, middle)
    def splitList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
        return middle

    # Delete node by setting the previousNode.next = previousNode.next.next, which skips over the node to delete
    # Now nothing is referencing the node to delete
    # Example: Delete middle node of linked list
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Return None for lists of length 0 or 1
        if not head or not head.next:
            return None
        # Use fast/slow pointer method to find the node before the middle node
        # starting fast 1 step ahead so slow will be previous node to the middle
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # The next node from the node before the middle should be the node after the middle
        slow.next = slow.next.next
        return head