from collections import deque

from fake_db import get_links

def find(source, destination):
    original_source = source
    print source, '-->', destination
    current_level = 0
    queue = deque()
    visited = []
    path = {}

    if source == destination:
        return current_level
    else:
        current_level += 1
        queue.appendleft(source)

    while queue:
        source = queue.pop()
        links = get_links(source)

        if links:
            for link in links:
                if link not in visited:
                    queue.appendleft(link)
                    path[link] = source
            if destination in links:
                page = destination
                print destination, '->',
                while True:
                    page = path[page]
                    print page, '->',
                    if page == original_source:
                        return current_level
            else:
                current_level += 1
                visited.append(links)

    print 'Not connected'
    return -1

if __name__ == '__main__':
    print find('jesus', 'jesus')
    print
    print find('italy', 'spaghetti')
    print
    print find('italy', 'jesus')
    print
    print find('italy', 'cat')
