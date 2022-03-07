//https://www.hackerrank.com/challenges/30-queues-stacks/problem?isFullScreen=true

function Solution(){
  //Write your code here
    const st = [];
    const q = [];
    
    this.pushCharacter = (c) => {
        st.push(c);
    }
    
    this.enqueueCharacter = (c) => {
       q.push(c);
    }
    
    this.popCharacter = () => {
        return st.pop();
    }
    
    this.dequeueCharacter = () => {
        return q.shift();
    }
}
