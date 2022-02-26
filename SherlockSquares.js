//https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true

function squares(a, b) {
    // Write your code here
    let count = 0    
    let sq_root_a = parseInt(Math.sqrt(a))
    let sq_root_b = parseInt(Math.sqrt(b))
    
    count = sq_root_b - sq_root_a
    
    if((sq_root_a * sq_root_a) >= a){
        count++
    }
    
    
    return count
}
