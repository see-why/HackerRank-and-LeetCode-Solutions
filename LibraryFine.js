//https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true

function libraryFine(d1, m1, y1, d2, m2, y2) {
    // Write your code here
    let fine = 0;
    
    if (y1 > y2){
        fine += 10000
    } else if (y1 == y2){
        if (m1 == m2){
            if (d1 > d2){
                fine += 15 * (d1 -d2)
            }
        } else if (m1 > m2){
            fine += 500 * (m1 -m2)
        }
    }
    return fine
}
