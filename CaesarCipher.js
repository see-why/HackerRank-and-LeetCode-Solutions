// https://www.hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=true

function caesarCipher(s, k) {
    // Write your code here
    let arr = []
    for (let i=0; i<s.length; i++){
        let code = s[i].charCodeAt(0);
        let newcode = ''
         if(65 <= code && code <= 90){
             if(code + k > 90){
               newcode = code + (k % 26)
               newcode = newcode > 90 ? 64 + (newcode-90) : newcode
             } else {
                 newcode = code + k;
             }
            arr[i] = String.fromCharCode(newcode);
        }
        else if(97 <= code && code <= 122){
            if(code + k > 122){
               newcode = code + (k % 26)
               newcode = newcode > 122 ? 96 + (newcode-122) : newcode                 
             } else {
                 newcode = code + k;
             }
            arr[i] = String.fromCharCode(newcode);
        }
        else{
           arr[i] = String.fromCharCode(code);
        }
    }
    
    return arr.join('')
}
