//https://www.hackerrank.com/challenges/fair-rations/problem?isFullScreen=true

function fairRations(B) {
    // Write your code here
    let count = 0
    let last_index = B.length - 1
    B.map((item, index) => {
        if(item % 2 != 0 && index != last_index){
            B[index] += 1
            B[index + 1] += 1
            count += 2
        }
    })
    
    return B[last_index] % 2 == 1 ? 'NO' : count
    
}
