//My solution to this Hackerank challenge...https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=true

function main() {

    let arr = Array(6);
    let array_of_sums = [];

    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }
    
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
    
    console.log(Math.max(...array_of_sums));
}
