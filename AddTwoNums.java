// You are given two non-empty linked lists representing two non-negative integers. 
// The digits are stored in reverse order and each of their nodes contain a single digit.
// Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.


// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8

 
 public ListNode listPlus(ListNode l1, ListNode l2) {
     if ( l1 == null ) {
         return l2;
     }
     if ( l2 == null ) {
         return l1;
     }

     // Constant space method -- You need to calculate the length!
     // l1 l2 get len. 
     // l1 for the longer one.
     // int len1 = 0;
     // int len2 = 0;
     // while(l1 != null){
     //     len1++;
     //     l1 = l1.next;
     // }
     // while(l2 != null){
     //     len2++;
     //     l2 = l2.next;
     // }
     // if(len2 > len1) {
     //    ListNode l3 = l1;
     //    l1 = l2;
     //    l2 = l3;
     // }
    
     ListNode newNode = new ListNode(0);
     newNode.next = l1;
     int carry = 0;
     
     // Smarter way to check if one of them are none!! Save while loop!
     while(l1 != null || l2 != null) {
         int cur = l1 != null ? l1.val : 0 + l2 != null? l2.val:0 + carry;
         carry = cur / 10;
         cur = cur % 10;
         l1.val =  cur;
         l1 = l1 !=null? l1.next : null;
         l2 = l2 != null ? l2.next: null;
     }
     
    //  while ( l != null ) {
    //      int cur = l.val + carry;
    //      carry = cur / 10;
    //      cur = cur % 10;
    //      tmp.next = new ListNode(cur);
    //      tmp = tmp.next;
    //      l = l.next;
    //  } 
    //  while ( l2 != null ) {
    //      int cur = l2.val + carry;
    //      carry = cur / 10;
    //      cur = cur % 10;
    //      tmp.next = new ListNode(cur);
    //      tmp = tmp.next;
    //      l2 = l2.next;
    //  } 
     
     // Don't remember carry at the last!
     if(carry == 1) {
         .next = new ListNode(1);
     }
     return newNode.next;
     
     
 }