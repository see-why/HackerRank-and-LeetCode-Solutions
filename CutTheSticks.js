//https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true

function cutTheSticks(arr) {
    // Write your code here
    let max = Math.max(...arr)
    let result = [arr.length]
    
    while (max > 0) {
        let count = 0
        let min = Math.min(...arr)
        arr = arr.filter((item) => {
            item -= min
            if (item != 0){
                count++
                return item 
            }            
        })
        console.log(arr)
        
        if(count > 0){
            result.push(count)
        }
       
        max = Math.max(...arr)
    }
    console.log(result)
    return result
}
