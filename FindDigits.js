//https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true

function findDigits(n) {
    // Write your code here
    let numbers = n.toString().split('\n');
    let count = 0;
  
    let divs = numbers.map((string) => {
        let factors = string.split('')
        factors.map((factor) => {
             if(n % parseInt(factor) == 0 ){
                count++
            }
        })       
    });
    return count;
}
