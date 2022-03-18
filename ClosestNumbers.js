// https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true

function closestNumbers(arr) {
    // Write your code here
    arr = arr.sort((a,b) => (a -b));
    let minDiff = arr[1] - arr[0];
    let elements = [];
    for(let i = 0; i < arr.length - 1; i++) {
        let diff = arr[i + 1] - arr[i];       
        
        if(diff < minDiff){
            elements = [];
            minDiff = diff;
        }
        
        if(diff == minDiff) {
            elements.push(arr[i]);
            elements.push(arr[i + 1]);
        }
    }
    elements = elements.sort((a, b) => a - b);
    return elements;

}

