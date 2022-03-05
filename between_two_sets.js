function getTotalX(a, b) {
    // Write your code here
    let start = Math.max(...a);
    let end = Math.min(...b);
    
    let count = 0;
    
    for(let i = start; i <= end; i++){
        let arr_factors = a.filter((e) => i % e == 0);
        let arr_multiples = b.filter((e) => e % i == 0);
        
        if (arr_factors.length == a.length && arr_multiples.length == b.length) {
            count++;
        }
    }
    return count;
}
