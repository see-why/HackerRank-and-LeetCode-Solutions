//https://www.hackerrank.com/challenges/30-regex-patterns/problem


function main() {
    const N = parseInt(readLine().trim(), 10);
    let pattern = /@gmail.com/
    const names = []

    for (let NItr = 0; NItr < N; NItr++) {
        const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

        const firstName = firstMultipleInput[0];

        const emailID = firstMultipleInput[1];
        
        if(pattern.test(emailID)) {
            names.push(firstName)
        }       
        
    }
    
    names.sort().forEach((item) => {
        console.log(item)
    })
}
