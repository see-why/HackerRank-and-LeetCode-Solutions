// https://www.hackerrank.com/challenges/runningtime/problem?isFullScreen=true

function runningTime(arr) {
    // Write your code here
    let shifts = 0
    
     for(var j = 1; j < arr.length; j++) {
        var unsorted = arr[j];
        
        for(var i = j-1; i > -1; i--) {
            if(unsorted < arr[i]) {
                arr[i+1] = arr[i];
                arr[i] = unsorted;
                shifts++
            } else {
                arr[i+1] = unsorted;
                break;
            }
        }
    }
    return shifts
}
