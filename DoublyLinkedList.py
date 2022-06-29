# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?isFullScreen=true

def reverse(head):
    # Write your code here
    if head == None or head.next == None:
        return head
    
    while True:
        temp = head.next
        head.next = head.prev
        head.prev = temp
        head = head.prev
        
        if head.next == None:
            break
    temp = head.next
    head.next = head.prev
    head.prev = temp
    return head
