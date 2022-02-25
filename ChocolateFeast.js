//https://www.hackerrank.com/challenges/chocolate-feast/problem?isFullScreen=true

function chocolateFeast(n, c, m) {
    // Write your code here
    let wrappers = Math.floor(n/c)
    let count = wrappers
    while (wrappers > 0){        
        let chocolates_from_wrappers = Math.floor(wrappers/m)
        count += chocolates_from_wrappers
        wrappers -= (chocolates_from_wrappers*m) 
        wrappers = chocolates_from_wrappers == 0 ? 0 : wrappers + chocolates_from_wrappers
    }
    
    return count
}
