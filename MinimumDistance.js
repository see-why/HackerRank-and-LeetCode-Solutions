//https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true

function minimumDistances(a) {
    // Write your code here
    let dict = {}
    let min_distance = Number.POSITIVE_INFINITY
    for (let i=0; i<a.length; i++){
        if(dict[a[i]]){
            let distance = i - dict[a[i]] + 1
            
            if(distance < min_distance){
                min_distance = distance
            }
            dict[a[i]] = i + 1
        }else {
            dict[a[i]] = i + 1
        }
    }
    
    min_distance = min_distance == Number.POSITIVE_INFINITY ? -1 : min_distance
    return min_distance
}
