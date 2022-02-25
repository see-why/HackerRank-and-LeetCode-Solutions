//https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true

function superReducedString(s) {
    // Write your code here
    for(let i=0; i<(s.length-1); i++){
        if (s[i] == s[i+1]){
            let str = s[i]+s[i]
            s = s.replace(str,'')
            s = s.trim()
            console.log(s)
            i = -1
        }
    }
    
    return !s ? "Empty String" : s.trim()
}
