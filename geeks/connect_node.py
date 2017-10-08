import sys, collections
# import heapq

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

class Node(object):
    def __init__(self, value, head=None):
        self.value = value
        self.head = head
        self.left = None
        self.right = None
        self.nextRight = None

    def __str__(self):
        return "Node: {}".format(self.value)

# def get_next_right(node):
#     if node is None or node.head is None:
#         return None
#     if node.head.right != node:
#         return node.right
#     head_next_right = get_next_right(node.head)
#     if head_next_right is None or head_next_right.left is None:
#         return None
#     return head_next_right.left
    

def solve(n, nodes):
    nodes = nodes.split()
    tree = dict()
    tree[int(nodes[0])] = Node(int(nodes[0]))
    for i in range(0, 3*n, 3):
        head = tree[int(nodes[i])]
        node = Node(value=int(nodes[i+1]), head=head)
        tree[int(nodes[i+1])] = node
        direction = nodes[i+2]
        if direction == "L":
            head.left = node
        elif direction == "R":
            head.right = node

    # for i in tree:
    #     node = tree[i]
    #     if node.left is not None:
    #         node.left.nextRight = get_next_right(node.left)
    #     if node.right is not None:
    #         node.right.nextRight = get_next_right(node.right)

    q = collections.deque()
    q.append(tree[int(nodes[0])])
    ret1 = []
    while q:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            if cur is None:
                continue
            ret1.append(cur.value)
            q.append(cur.left)
            q.append(cur.right)
    stack = []
    stack.append(tree[int(nodes[0])])
    ret2 = []
    visited = [0]*1001
    while stack:
        cur = stack.pop()
        if cur is None:
            continue
        if visited[cur.value] is True:
            ret2.append(cur.value)
            continue
        visited[cur.value] = True
        stack.append(cur.right)
        stack.append(cur)
        stack.append(cur.left)
    return " ".join(map(str, ret1)) + "\n" + " ".join(map(str, ret2))

def main():
    t = I()
    for _ in range(t):
        n = I()
        nodes = S()
        print(solve(n, nodes))

main()
