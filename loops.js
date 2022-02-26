//https://www.hackerrank.com/challenges/js10-loops/problem?isFullScreen=true

function vowelsAndConsonants(s) {
     //   let re = /^(a|e|i|o|u).*\1$/ for words begining and ending with the same vowel
     /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts with 'Mr.', 'Mrs.', 'Ms.', 'Dr.', or 'Er.', 
     * followed by one or more letters.
      let re = /^(Mr\.|Mrs\.|Ms\.|Dr\.|Er.)\s?[A-Z|a-z]+$/
     */
   /*
     * Declare a RegExp object variable named 're'
     * It must match ALL occurrences of numbers in a string.
      let re = /[0-9]+/g
     */
   
    
     let pattern = /[aeiou]/
    for (let i=0; i<s.length; i++){
        if(pattern.test(s[i])){
            console.log(pattern.exec(s[i])[0])
        }
    }
    
    for (let i=0; i<s.length; i++){
        if(!pattern.test(s[i])){
           console.log(s[i])
        }
    }
}
