//https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true

function sockMerchant(n, ar) {
    // Write your code here
    let count = 0;
    let checked_numbers = [];
    for (let item of ar){
        if (checked_numbers.includes(item) == false){
            let frequency = 0;
            ar.forEach((value) => value == item && frequency++);
            count += Math.floor(frequency/2);
        }
        checked_numbers.push(item);
        console.log(item)
    }
    return count;
}
