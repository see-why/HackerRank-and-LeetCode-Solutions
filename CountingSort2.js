// https://www.hackerrank.com/challenges/countingsort2/problem?isFullScreen=true

function countingSort(arr) {
    // Write your code here
    let array = new Array(100).fill(0);
        
        for (let i=0; i<arr.length; i++){
            array[arr[i]] += 1;
        }
    
    let result = []
        
         for (let i=0; i<array.length; i++){
            let all_values = new Array(array[i]).fill(i);
            result.push(all_values);
        }
        
    result = result.flat();
    return result;

}
