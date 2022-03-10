// https://www.hackerrank.com/challenges/weighted-uniform-string/problem?isFullScreen=true

function weightedUniformStrings(s, queries) {
    // Write your code here
    let a = 'a'.charCodeAt(0)
    let previous = s[0]
    let length = 0
    let weights = new Set()
    
    for(let i=0; i<s.length; i++){
        let value = (s.charCodeAt(i) - a) + 1;
        weights.add(value)
        if(s[i] == previous){
            length += 1            
            weights.add(length * value)           
        }else {
            length = 1
            previous = s[i]
        }
    }
    
    let response = []
    
    for(let i=0; i<queries.length; i++){
        if(weights.has(queries[i])){
            response.push("Yes")
        }else {
            response.push("No")
        }
    }
    
    return response
}
