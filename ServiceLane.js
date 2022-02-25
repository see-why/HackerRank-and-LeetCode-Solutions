//https://www.hackerrank.com/challenges/service-lane/problem?isFullScreen=true

function serviceLane(n, cases, width) {
    // Write your code here
    let result = []
    for (let i=0; i<cases.length; i++){
        let range = width.slice(cases[i][0], cases[i][1]+1)
        result.push(Math.min(...range))
    }
    return result
}
