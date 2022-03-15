// https://www.hackerrank.com/challenges/gem-stones/problem?isFullScreen=true

function gemstones(arr) {
    // Write your code here
    let dict = {}
    const alpha = Array.from(Array(26)).map((e, i) => i + 97);
    const alphabet = alpha.map((x) => String.fromCharCode(x));
    
     for(let j=0; j<alphabet.length; j++){
        dict[alphabet[j]] = -1 * arr.length;        
    }

    for(let i=0; i<arr.length; i++){
        let item = arr[i];
        for(let j=0; j<alphabet.length; j++){
            if(item.includes(alphabet[j])){
                dict[alphabet[j]] += 1;
            }          
        }
    }
    
    let count = 0;
    Object.values(dict).forEach((item) => {
        if(item === 0){
            count += 1;
        };
    });
    
    return count;
}
