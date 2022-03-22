// https://www.hackerrank.com/challenges/anagram/problem?isFullScreen=true

def anagram(s):
    # Write your code here
    if len(s)%2: return -1
    l = len(s)//2
    a = collections.Counter(s[:l])
    b = collections.Counter(s[l:])
    return l-sum((a & b).values())

function anagram(s) {
    // Write your code here
    if(s.length % 2){
        return -1
    } else {
        let median = s.length/2;
        let first_string = s.substring(0,median);
        let other_string = s.substring(median,s.length);
        
        let result = 0
        
        for(let i=97; i<124; i++){
            let letter = String.fromCharCode(i);
            
            if(first_string.includes(letter) && other_string.includes(letter)){
                let pattern = new RegExp(letter, 'g')
                let count = Array.from(first_string.matchAll(pattern)).length;
                let counter = Array.from(other_string.matchAll(pattern)).length;
                result += count > counter ? counter : count;
            }
        }
        
        return median - result;
    }
    
}
