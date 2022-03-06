//https://www.hackerrank.com/challenges/30-linked-list/problem?isFullScreen=true

this.insert=function(head,data){
          //complete this method
          if (head == undefined) {
              head = new Node(data);
          } else {
             if (head.next == undefined){
                 head.next = new Node(data);
             }
             else {
                 this.insert(head.next, data);
             }
          }
          return head
};
