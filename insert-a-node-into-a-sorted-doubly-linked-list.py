# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_r=profile


def sortedInsert(llist, data):
    # Write your code here
    cur=llist
    node=DoublyLinkedListNode(data)
    if cur.data>data or cur.data==data:
        node.next=cur
        cur.prev=node
        llist=node
        return llist
    while cur.next:
        if (cur.data<data and cur.next.data>data) or cur.data==data:
            node.next=cur.next
            cur.next.prev=node
            node.prev=cur
            cur.next=node
            return llist
        cur=cur.next
    if cur.data<data or cur.data==data:
        node.prev=cur
        cur.next=node
        return llist
