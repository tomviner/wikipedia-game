from collections import deque

from fake_db import get_links


def find(source, destination):
    print source, '-->', destination
    current_level = 0
    queue = deque()
    visited = []

    if source == destination:
        return current_level
    else:
        current_level += 1
        queue.appendleft(source)

    while queue:
        print current_level, queue
        source = queue.pop()
        links = get_links(source)

        if links:
            for link in links:
                if link not in visited:
                    queue.appendleft(link)
            if destination in links:
                return current_level
            else:
                current_level += 1
                visited.append(links)

    print 'Not connected, sorry darlin'
    return -1

if __name__ == '__main__':
    print find('jesus', 'jesus')
    print find('italy', 'spaghetti')
    print find('italy', 'jesus')
    # this loops forever
    print find('italy', 'cat')
