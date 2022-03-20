// https://www.hackerrank.com/challenges/the-love-letter-mystery/problem?isFullScreen=true

function theLoveLetterMystery(s) {
    // Write your code here
    let operations = 0;
    for (let i=0; i<s.length/2; i++){
        let char = s.charCodeAt(i)
        let alternate = s.charCodeAt(s.length - (1 + i))
        if(char != alternate) {
                operations+= Math.abs(char-alternate)
        }
    }
    
    return operations;
}

