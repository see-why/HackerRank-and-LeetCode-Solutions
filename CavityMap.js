//https://www.hackerrank.com/challenges/cavity-map/problem?isFullScreen=true

function cavityMap(grid) {
    // Write your code here
    let size = grid.length
   for(let index=0; index<size; index++) {   
        let row = Math.max(index-1, 0)
        let column = Math.min(index+1, size-1)     
        for(let i=0; i<size; i++){
            let current_depth = grid[index][i]           
            if ( current_depth > grid[row][i] && current_depth > grid[column][i] ){
                if (current_depth > grid[index][i-1] && current_depth > grid[index][i+1]){
                    let arr = Array.from(grid[index])
                    console.log(arr)
                    arr[i] = "X"
                    grid[index] = arr.join('')
                }
            }
        }
    }
    
    return grid
}
