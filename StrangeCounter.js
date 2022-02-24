//https://www.hackerrank.com/challenges/strange-code/problem?isFullScreen=true

function strangeCounter(t) {
    // Write your code here
    let n = 1
    let starting_cycle = 0
    while (starting_cycle < t) {
        starting_cycle = 3* Math.pow(2,n-1)
        n++
        if((starting_cycle - t) > 2){
             starting_cycle = 3 * Math.pow(2,n-3)
             break
        }
    }
    
    return starting_cycle - (t - (starting_cycle - 2))
}
