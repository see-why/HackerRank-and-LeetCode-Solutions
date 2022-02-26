//https://www.hackerrank.com/challenges/count-triplets-1/problem?isFullScreen=true

// Complete the countTriplets function below.
function countTriplets(arr, r) {
    let factors = new Map()
    let triplets = new Map()
    arr = arr.reverse()
    let count = 0
    for (let i=0; i<arr.length; i++){     
        if (triplets.has(arr[i] * r)){
            count += triplets.get(arr[i] * r)
        }
             
        if(factors.has(arr[i] * r)){
            let previous_value = triplets.has(arr[i]) ? triplets.get(arr[i]): 0
            triplets = triplets.set(arr[i], factors.get(arr[i] * r)+ previous_value)
        }
        
        factors = checkMap(factors, arr[i])
    }
    return count
}

const checkMap = (map, index) => {
     if(map.has(index)) {
            map.set(index, map.get(index) + 1)
        } else{
            map.set(index, 1)
        }
    return map
};
