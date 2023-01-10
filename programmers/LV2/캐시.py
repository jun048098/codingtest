from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = deque()
    time = 0
    for c in cities:
        c = c.lower()
        if c not in cache:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(c)
            time += 5
        else:
            cache.remove(c)
            cache.append(c)
            time += 1

    return time