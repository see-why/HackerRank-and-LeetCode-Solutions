//https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

function hackerrankInString(s) {
    // Write your code here
    let pattern = /.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*/g
    return s.search(pattern) != -1 ? "YES" : "NO"

}
