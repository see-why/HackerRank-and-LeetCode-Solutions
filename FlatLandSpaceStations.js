//https://www.hackerrank.com/challenges/flatland-space-stations/problem?isFullScreen=true

function flatlandSpaceStations(n, c) {
    let count = 0
    let min_array = []
    if (n == c.length){
        return count
    } else {
        for (let j =0; j<n; j++){
            if(c.includes(j) == false){
                let min_distance = n
                c.forEach((i) => {
                   let dist =  Math.abs(i-j)
                   min_distance = dist < min_distance ? dist : min_distance
                }) 
                min_array.push(min_distance)         
            }
            
        }       
    }

    return Math.max(...min_array)
}
