//https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

function divisibleSumPairs(n, k, ar) {
    // Write your code here
    let count = 0;
    let sum = 0;
    ar.map((item, index) => {
        for (let i=index + 1; i < ar.length; i++){
           sum = item + ar[i] ;
           if( sum % k == 0){
               count++;
           } 
        }
    })
    return count;
}
