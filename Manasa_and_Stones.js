//https://www.hackerrank.com/challenges/manasa-and-stones/problem?isFullScreen=true


function stones(n, a, b) {
    // Write your code here
    let array_of_last_stones = []
    for (let i=0; i<n; i++){
        if (b > a){
             array_of_last_stones.push((b*i) + (a*(n-i-1)))
        } else {
            array_of_last_stones.push((a*i) + (b*(n-i-1)))
        }
       
    }
    return Array.from(new Set(array_of_last_stones))
}
