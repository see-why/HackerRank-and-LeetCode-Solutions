//https://www.hackerrank.com/challenges/js10-bitwise/problem?isFullScreen=true

const getMaxLessThanK = (n,k) => {
    let max = 0
    for (let i= 1; i<=n ;i++){
        for(let j=i+1; j<=n ; j++){
            let bitwise_output = i&j
            max = bitwise_output > max && bitwise_output < k ? bitwise_output : max
        }
    }
    return max
};
