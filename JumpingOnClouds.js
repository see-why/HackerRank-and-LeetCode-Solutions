//https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true

function jumpingOnClouds(c) {
    // Write your code here
    let count = 0;
    const size = c.length;
    for(let i=0; i< size; i++){
        if(c[i] == 1){
            continue;
        } else {
            if(c[i] == c[i+2] && (i+2) < size){
                count++;
                i++;
            } 
            else if (c[i] == c[i+1] && (i+1) < size){
                count++;
            }
        }
        
    }
    return count;
}
