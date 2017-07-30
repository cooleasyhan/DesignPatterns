#%%
from collections import defaultdict
graph = {
    'Frankfurt':    ['Mannheim', 'Wurzburg', 'Kassel'],
    'Mannheim': ['Karlsruhe'],
    'Karlsruhe':   ['Augsburg'],
    'Augsburg':  ['Munchen'],
    'Wurzburg':  ['Erfurt', 'Nurnberg'],
    'Nurnberg':  ['Stuttgart', 'Munchen'],
    'Kassel':     ['Munchen'],
    'Erfurt':      [],
    'Stuttgart':  [],
    'Munchen':  []
}


def print_path(path, start, end):
    tmp = list()
    tmp.append(end)
    while end != start:
        tmp.append(path[end])
        end = path[end]

    print(list(reversed(tmp)))


def bfs(graph, start, end):
    path = dict()
    marked = list()
    current_node = start
    marked.append(start)
    nodes = []
    while True:
        if not graph[current_node]:
            if nodes:
                current_node = nodes.pop()
            else:
                break
        current = graph[current_node].pop()
        if current not in marked:
            path[current] = current_node
            marked.append(current)
            if current == end:
                print(marked)
                print(path)
                print_path(path, start, end)
                return
            else:
                nodes.append(current)

        if len(graph[current_node]) == 0:
            if len(nodes) != 0:
                current_node = nodes.pop()
            else:
                break

    print(path)


# bfs(graph, 'Frankfurt', 'Munchen')
# bfs(graph, 'Frankfurt', 'Augsburg')


def bfs2(graph, start):
    if not graph[start] or start not in graph:
        return None, None
    visited, q, path = [], [start], {}
    while q:
        node = q.pop(0)
        for vertex in graph[node]:
            if vertex not in visited:
                visited.append(vertex)
                path[vertex] = node
                q.append(vertex)
    return visited, path


visited, path = bfs2(graph, 'Frankfurt')

print_path(path, 'Frankfurt', 'Stuttgart')
