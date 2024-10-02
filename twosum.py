# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_list_len(self, l1):
        current = l1
        length = 0

        while current.next is not None:
            length += 1
            current = current.next 
        return length

    def help_pad_zeroes(self, LL, len_A, len_B):
        if len_A < len_B:
            current = LL

            for i in range(0, len_B):
                if i >= len_A:
                    current.next = ListNode(0)
                current = current.next

        return LL 

    def pad_zeroes(self, l1, l2):
        len_l1 = self.get_list_len(l1)
        len_l2 = self.get_list_len(l2)

        # will return the original list if need not be padded 
        
        l1 = self.help_pad_zeroes(l1, len_l1, len_l2)
        l2 = self.help_pad_zeroes(l2, len_l2, len_l1)

  
        return l1, l2
            

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result_node = ListNode() # dummy node
        current_node = result_node 
        
        result = 0
        carry = 0 
        
        l1, l2 = self.pad_zeroes(l1, l2) 

        while l1 is not None and l2 is not None:
            
            result = l1.val + l2.val + carry

            if carry > 0:
                carry = 0 
            
            l1 = l1.next
            l2 = l2.next

            carry = (int)(result / 10)  
            result = result % 10
            
            current_node.next = ListNode(result)   
            current_node = current_node.next

            result = 0  

        if carry != 0:
            current_node.next = ListNode(1)

        return result_node.next
        
        



        


            
        

