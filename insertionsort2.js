//https://www.hackerrank.com/challenges/insertionsort2/problem?isFullScreen=true

function insertionSort2(n, arr) {
    // Write your code here
     for(var j = 1; j < arr.length; j++) {
        var unsorted = arr[j];
        
        for(var i = j-1; i > -1; i--) {
            if(unsorted < arr[i]) {
                arr[i+1] = arr[i];
                arr[i] = unsorted;
            } else {
                arr[i+1] = unsorted;
                break;
            }
        }

        console.log(arr.join(' '));
    }

}
