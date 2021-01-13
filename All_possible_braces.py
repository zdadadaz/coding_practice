def dfs(cur,l,r, n, visited):
    if l == r and l == n and cur not in visited:
        visited.add(cur)
        print(cur)
        return 
    # add left
    if l < n:
        dfs(cur + '{', l+1, r, n, visited)
    if r < n and r < l:
        dfs(cur + '}', l, r+1, n, visited)

def print_all_braces(n):
    visited = set()
    cur = ''
    dfs(cur, 0, 0, n, visited)
    return list(visited)

print(print_all_braces(3))