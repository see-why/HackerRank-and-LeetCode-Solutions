// https://www.hackerrank.com/challenges/palindrome-index/problem?isFullScreen=true

function palindromeIndex(s) {
    // Write your code here 
    
    function isPalendrome(s, index){
        let result = false;
        let subString = s.substring(0, index) + s.substring(index+1);
        let reverseString = subString.split('').reverse().join('');
        
        if(subString == reverseString){
            result = true;
        }
        
        return result;
    }
      
    let index = -1
    if(s !== s.split('').reverse().join('')){
        for(let i=0; i<s.length/2; i++){
            let letter = s[i];
            let alternate_index = s.length - (i+1);
            let alternate_letter = s[alternate_index];
            
            if(letter != alternate_letter){
                let subString = s.substring(0, index) + s.substring(index+1);
                if(isPalendrome(s, i)){
                    index = i;
                } else if(isPalendrome(s, alternate_index)){
                    index = alternate_index;
                }
                break;
            }
        }
    }
  
    
    return index;
}
