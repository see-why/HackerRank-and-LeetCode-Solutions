//https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true


function equalizeArray(arr) {
    // Write your code here
    let dict = {}
    for(let i=0; i<arr.length; i++){
        if(dict[arr[i]]){
            dict[arr[i]] += 1
        } else {
            dict[arr[i]] = 1
        }
    }
    
    let result = Array.from(Object.values(dict))
    let max  = Math.max(...result)
    return result.reduce((total, b) => total + b) - max
}
