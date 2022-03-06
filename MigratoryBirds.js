//https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

function migratoryBirds(arr) {
    // Write your code here
    let count = 0;
    let value = 0;
    for(let item=1; item<=5; item++){
        let frequency = 0;        
        arr.forEach((val) => val == item && frequency++)
        if (frequency > count || (frequency == count && item < value)){
            count = frequency;
            value = item;
        }
    }
    return value;
}
