from typing import List


class Sort:

    # Merge Sort Array
    def mergeSortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            # Break array in half
            leftArr = nums[:len(nums) // 2]
            rightArr = nums[len(nums) // 2:]

            # Recurse on each piece
            self.mergeSortArray(leftArr)
            self.mergeSortArray(rightArr)

            # merge the arrays back together in sorted order
            i, j, k = 0, 0, 0  # left idx pointers of left, right, and sorted arrays

            while i < len(leftArr) and j < len(rightArr):
                # left array smallest element less than right arr smallest element
                if leftArr[i] < rightArr[j]:
                    nums[k] = leftArr[i]
                    i += 1
                else:
                    nums[k] = rightArr[j]
                    j += 1
                k += 1

            if i < len(leftArr):
                for i in range(i, len(leftArr)):
                    # Add all the remaining elements in order
                    nums[k] = leftArr[i]
                    k += 1

            if j < len(rightArr):
                for j in range(j, len(rightArr)):
                    # Add all the remaining elements in order
                    nums[k] = rightArr[j]
                    k += 1

        return nums

    # refer to https://www.youtube.com/watch?v=9KBwdDEwal8 for explanation
    def quickSort(self, arr: List[int]) -> None:
        def sort(arr, left, right):
            if left < right:
                partitionPosition = partition(arr, left, right)
                sort(arr, left, partitionPosition - 1)
                sort(arr, partitionPosition + 1, right)

        def partition(arr, left, right):
            i , j = left, right
            pivot = arr[right]
            while i < j:
                while i < right and arr[i] < pivot:
                    i += 1
                while j > left and arr[j] >= pivot:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
            if arr[i] > pivot:
                arr[i], arr[right] = arr[right], arr[i]
            return i

        sort(arr, 0, len(arr - 1))


    def getMiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right
        return dummyHead.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # Recursively continue splitting the list in half
        mid = self.getMiddleNode(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the pieces back together
        return self.merge(left, right)