class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    JJ = ListNode(0, head)
    prev = JJ

    while head:
      while head.next and head.val == head.next.val:
        head = head.next
      if prev.next == head:
        prev = prev.next
      else:
        prev.next = head.next
      head = head.next

    return JJ.next