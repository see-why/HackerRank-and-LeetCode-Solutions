//https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true


function queensAttack(n, k, r_q, c_q, obstacles) {
    // Write your code here
    let top = n - r_q
    let left = c_q -1
    let right = n - c_q
    let bottom = r_q - 1
    
    let top_left = Math.min(top, left)
    let top_right = Math.min(top, right)
    let bottom_left = Math.min(bottom, left)
    let bottom_right = Math.min(bottom, right)
    
    obstacles.forEach(([ x, y]) => {
        //top
        if(y === c_q && x > r_q){
            top = Math.min(top, x - r_q -1)
        }
        
        //left
        else if(x === r_q && y < c_q){
            left = Math.min(left, c_q - y - 1)
        }
        
        //right
        else if(x === r_q && y > c_q){
            right = Math.min(right,y - c_q - 1)
        }
        
        //bottom
        else if(y === c_q && x < r_q){
            bottom = Math.min(bottom,r_q - x - 1)
        }
        
        //top-left
        else if(x > r_q && y < c_q && x - r_q === c_q - y){
            top_left = Math.min(top_left, x - r_q - 1)
        }
        
        //top-right
        else if(x > r_q && y > c_q && x - r_q === y - c_q){
            top_right = Math.min(top_right,y - c_q - 1)
        }
        
        //bottom-left
        else if(x < r_q && y < c_q && r_q - x === c_q - y){
            bottom_left = Math.min(bottom_left, c_q - y - 1)
        }
        
        //bottom-right
        else if(x < r_q && y > c_q && r_q - x === y - c_q){
            bottom_right = Math.min(bottom_right,y - c_q - 1)
        }
    });
    
    return top + left + right + bottom + top_left + top_right + bottom_left + bottom_right;

}
