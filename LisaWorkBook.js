//https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true

function workbook(n, k, arr) {
    // Write your code here
    let page = 1
    let count = 0
    
    for(let i=0; i<arr.length; i++){
        for(let j=1; j<=arr[i]; j++){
            if (page == j){
                count++
            }
            
            if ((j % k == 0) && (j != arr[i])){
                page += 1
            }
        }
        page += 1
    }
    return count
}
