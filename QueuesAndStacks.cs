//https://www.hackerrank.com/challenges/30-queues-stacks/problem?isFullScreen=true

class Solution {
    //Write your code here
    public Stack<char> st {get; set;}
    public Queue<char> q {get; set;}
    
    Solution(){
        this.st = new Stack<char>();
        this.q = new Queue<char>();
    }
    
    public void pushCharacter(char c){
        st.Push(c);
    }
    
    public void enqueueCharacter(char c){
        q.Enqueue(c);
    }
    
    public char popCharacter(){
        return st.Pop();
    }
    
    public char dequeueCharacter(){
        return q.Dequeue();
    }
static void Main(String[] args) {
        // read the string s.
        string s = Console.ReadLine();
        
        // create the Solution class object p.
        Solution obj = new Solution();
        
        // push/enqueue all the characters of string s to stack.
        foreach (char c in s) {
            obj.pushCharacter(c);
            obj.enqueueCharacter(c);
        }
        
        bool isPalindrome = true;
        
        // pop the top character from stack.
        // dequeue the first character from queue.
        // compare both the characters.
        for (int i = 0; i < s.Length / 2; i++) {
            if (obj.popCharacter() != obj.dequeueCharacter()) {
                isPalindrome = false;
                
                break;
            }
        }
        
        // finally print whether string s is palindrome or not.
        if (isPalindrome) {
            Console.Write("The word, {0}, is a palindrome.", s);
        } else {
            Console.Write("The word, {0}, is not a palindrome.", s);
        }
    }
}
