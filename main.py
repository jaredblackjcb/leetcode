# This is a sample Python script.
import heapq
import types
from typing import List, Optional
import re
import json
from collections import deque, defaultdict
from hashmap_toolbox import HashmapToolbox

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_ordered_configurations(config: str) -> List[str]:

    configs = config.split("|")
    pattern = "[0-9]{4}[A-Za-z0-9]{10}"
    output = [None] * len(configs)

    for c in configs:
        # Validate the config is in the correct format
        is_valid_pattern = re.fullmatch(pattern, c) is not None
        print(re.fullmatch(pattern, c))
        is_unique = c not in output
        if not (is_valid_pattern and is_unique):
            return ["Invalid configuration"]

        # get the index
        index = int(c[:4]) - 1
        # get the code
        code = c[4:]
        if output[index] is None and index >= 0:
            output[index] = code
        else:
            return ["Invalid configuration"]

    return output

def get_deployment_summary(deployments: str) -> List[int]:
    output = [0, 0, 0]
    print(json.loads(deployments))
    data = json.loads(deployments)

    deployment_id_pattern = "d-[A-Za-z0-9]{10}"
    for deployment in data['deployments']:
        id = deployment['deployment_id']
        status = deployment['status']
        # validate id
        # validate status

        print(deployment)
        print(deployment['test'])
        print(deployment['deployment_id'])
    return output

# get number of items enclosed by pipes
def numberOfItems(s, startIndices, endIndices):
    output = []
    pattern = "\|\*+"
    # print(f"s: {s}")
    # print(f"starts: {startIndices}")
    # print(f"ends: {endIndices}")

    for i in range(len(startIndices)):
        start = startIndices[i] - 1
        end = endIndices[i]
        # print(start, end)

        search_str = s[start:end]
        print(search_str)
        item_count = search_str.count('*')

        # Subtract 1 from item count until i run into a side
        while (search_str[start] == '*' or search_str[end] == '*') and (start < end):
            if search_str[start] == '*':
                start += 1
                item_count -= 1
            if search_str[end] == '*':
                end -= 1
                item_count -= 1

        # j = 0
        # if (len(search_str) > 0):
        #     while search_str[j] == '*':
        #         item_count -= 1
        #         j += 1

        #     k = len(search_str) - 1
        #     while search_str[k] == '*':
        #         item_count -= 1
        #         k -= 1
        # print(f"search_str: {search_str}")

        # compartments = re.findall(pattern, search_str)
        # Remove the last compartment if it doesn't get closed
        # if len(compartments) > 0 and search_str[-1] != '|':
        # compartments.pop()
        # print("last compartment removed")
        # print(f"compartments: {compartments}")
        # item_count = "".join(compartments).count('*')
        # print(f"item_count: {item_count}")
        output.append(item_count)

    return output

def count_enclosed_items(s):
    stack = []
    total_items = 0

    for i, char in enumerate(s):
        if char == '*':
            total_items += 1
        elif char == '|':
            if stack:
                last_wall = stack.pop()
                total_items += i - last_wall - 1

            stack.append(i)

    # Handle any remaining items in the last compartment
    if stack:
        total_items += len(s) - stack[-1] - 1

    return total_items

def minimalHeaviestSetA(arr):
    # Write your code here
    output = []
    a_weight = 0
    b_weight = sum(arr)

    # Sort the array
    arr.sort()
    print(arr)

    # While box a is lighter than box b, keep adding items
    i = len(arr) - 1
    while a_weight <= b_weight:
        item_weight = arr[i]
        output.append(item_weight)
        a_weight += item_weight
        b_weight -= item_weight
        i -= 1
    output.reverse()
    return output


def optimizedMinimalHeaviestSetA(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)

    a_weight = 0
    b_weight = sum(arr)
    output = []

    # Iterate through the sorted array
    for item_weight in arr:
        if a_weight <= b_weight:
            output.append(item_weight)
            a_weight += item_weight
            b_weight -= item_weight
        else:
            break

    return output

# stack, hash table
def isValidParentheses(s):
    # way to match values in pairs - hash table
    char_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for c in s:
        if c in char_map:
            if stack and char_map[c] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return len(stack) == 0

# stack, enumerate arr
def countItems(s):
    total_count = 0
    # Stack keeping track of wall indices
    stack = []

    # track the index of the last wall
    last_wall = None
    for index, char in enumerate(s):
        if char == '|':
            if stack:
                # add the difference between the last wall and the current index minus 1 to exclude the wall
                last_wall = stack.pop()
                total_count += index - last_wall - 1
            # Always add each wall index to the stack
            stack.append(index)

    return total_count


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def maxDepth(node: Node):
    if not node:
        return 0
    else:
        return max(maxDepth(node.left), maxDepth(node.right)) + 1

def subarraySum(nums, k):
    count = curr_sum = 0
    h = defaultdict(int)

    for num in nums:
        # current prefix sum
        curr_sum += num

        # situation 1:
        # continuous subarray starts
        # from the beginning of the array
        if curr_sum == k:
            count += 1

        # situation 2:
        # number of times the curr_sum − k has occurred already,
        # determines the number of times a subarray with sum k
        # has occurred up to the current index
        count += h[curr_sum - k]

        # add the current sum
        h[curr_sum] += 1

    return count

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    q = deque([root])
    while q:
        print(f"q:{q}")
        current = q.popleft()
        print(f"current: {current}")
        print(current.val)
        print(current.left)
        print(current.right)
        current.left, current.right = current.right, current.left
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)

    return root



class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RightTreeView:
    def getRightView(self, node):


class Solution:
    1   --> 1
   2  3 --> 3
  4     --> 4





if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)














    heap = [3,4,1,5,2]
    heapq.heapify(heap)
    i, j, = 0, len(heap) - 1
    while i < j:
        print(f"({heap[i]}, {heap[j]})")
        i += 1
        j -= 1

    # print(HashmapToolbox.getMaxKey({'A':1, 'B':2}))
    # print(HashmapToolbox.getMaxKey({'A':1, 'B':1}))

    # testArr = [1, -1, 1, -1]
    # targetSum = 0
    # print(subarraySum(testArr, targetSum))



    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    #
    # print(maxDepth(root))

    # Test Cases
    # test_cases = [
    #     ("***||****|**|***|**||*|**|*|||***", 15),
    #     ("*|*|*|*|*|*", 4),
    #     ("|||*|||||||||||||||||||||||*", 1),
    #     ("|||||||||||||||||||||||||||||", 0),
    #     ("|*|*|*", 2),
    #     ("**|||||***||*|||*||||", 5)
    # ]
    #
    # for s, expected_result in test_cases:
    #     result = countItems(s)
    #     assert result == expected_result, f"For input '{s}', expected {expected_result} but got {result}"
    #
    # print("All test cases passed!")

    # print(isValidParentheses("]"))

    # data = '{"deployments": [{"deployment_id": "d-123456abcd", "status": "Success"}, {"deployment_id": "d-098765efgh", "status": "Fail"}]}'
    # get_deployment_summary(data)
    # test_config = "0002f7c22e7904|000176a3a4d214|000305d29f4a4b"
    # print(get_ordered_configurations(test_config))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
