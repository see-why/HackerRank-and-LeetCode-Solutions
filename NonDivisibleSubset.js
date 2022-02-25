//https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

function nonDivisibleSubset(k, s) {
    // Write your code here
    let dict = {}
    for (let i=0; i<=k; i++){
        dict[i] = 0
    }
    
    s.map((item) => {
        if(dict[item % k]){
            dict[item % k] += 1
        } else {
            dict[item % k] = 1
        }
    });
    
    let result = 0
    
    result += Math.min(dict[0],1);
    result = k % 2 == 0 ? result + Math.min(dict[k/2],1): result
    
    for (let i=1; i<Math.ceil(k/2); i++){
        if(i != k - i){
            result += Math.max(dict[i], dict[k - i])
        }
        
    }
     
    return result
}
