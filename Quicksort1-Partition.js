// https://www.hackerrank.com/challenges/quicksort1/problem?isFullScreen=true

function quickSort(arr) {
    // Write your code here
    let pivot = arr.shift()
    let left_arr = []
    let right_arr = []
    
    for(let i=0; i<arr.length; i++){
        if(arr[i] <= pivot){
            left_arr.push(arr[i])
        }else {
            right_arr.push(arr[i])
        }
    }
    
    return left_arr.concat(pivot, right_arr)
}
