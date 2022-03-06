function birthday(s, d, m) {
    // Write your code here
    let count = 0;
    s.map((item, index) => {
        let sum = item;
        for (let i=index+1; i < (index+m) ; i++ ){
            if (i < s.length){
                sum += s[i];
            }                
        }
        if (sum == d){
            count++;
        }
    })
    
    return count;

}
