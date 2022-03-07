//https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

function hourglassSum(arr) {
    // Write your code here
    let array_of_sums = [];
   for (let i= 0; i<6 ; i++){
         if ( (i + 2) < 6) {
            let length = arr[i].length;
            if ( (i + 2) < length){
                let nestedArray = arr[i];
                let secondNestedArray = arr[i+1];
                let thirdNestedArray = arr[i+2];                
                for (let k = 0; k < length; k++){
                    if (k+2 < length) {
                          let sum = nestedArray[k] + nestedArray[k+1] + nestedArray[k+2] + secondNestedArray[k+1] + thirdNestedArray[k] + thirdNestedArray[k+1] + thirdNestedArray[k+2];
                array_of_sums.push(sum);
                    }
                   
                }
               
            }
        }
    }
    
    return Math.max(...array_of_sums);
}
