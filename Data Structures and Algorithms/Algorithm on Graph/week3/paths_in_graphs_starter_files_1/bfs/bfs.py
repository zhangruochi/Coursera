#Uses python3

import sys
import queue

def distance(adj, s, t):
    if s == t:
        return -1

    level = 0
    my_queue = queue.Queue()
    my_queue.put((s,level))

    visited = set()

    while not my_queue.empty():
        cur,level = my_queue.get()
        if cur == t:
            return level

        for node in adj[cur]:
            if node not in visited:
                my_queue.put((node,level+1))
                visited.add(node)

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1

    print(distance(adj, s, t))
