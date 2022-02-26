//https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true

function insertionSort1(n, arr) {
    // Write your code here
    let max = arr[n-1]
    for(let i=n-2; i>=0; i--){        
        if(arr[i] > max){
            arr[i+1] = arr[i]
            if (i == 0 && arr[i] > max){
                console.log(...arr)
                arr[0] = max
            }
        } else if (arr[i] < max) {
            arr[i+1] = max            
            console.log(...arr)
            break
        }
        console.log(...arr)
    }
}
