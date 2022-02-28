//https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true

function camelcase(s) {
    // Write your code here
    let pattern = /[A-Z]/g;
    return s.match(pattern) ? s.match(pattern).length + 1 : 1
}
