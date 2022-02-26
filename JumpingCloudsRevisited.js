//https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true

function jumpingOnClouds(c, k) {
    let e = 100
    let n =  c.length
    let i = 0
    
    while (true) {
        e = c[(i+k) % n] == 1 ? e-2: e
        e -= 1   
        i = ((i+k) % n)
        if(i == 0) {
            break
        }
    }

    return e
}
