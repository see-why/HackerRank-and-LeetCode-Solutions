# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?isFullScreen=true


def has_cycle(head):
    if head is None or head.next is None:
        return False
    head.visited = True
    current = head
    while current.next is not None:
        current = current.next
        if current.visited:
            return True
    return False
