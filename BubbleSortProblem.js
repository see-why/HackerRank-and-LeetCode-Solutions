//https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?isFullScreen=true

function countSwaps(a) {
    // Write your code here
    function swap(a, b, c) {
        let temp = a[b]
        a[b] = a[c]
        a[c] = temp        
    }
    
    let count = 0
    let n = a.length
    for (let i = 0; i < n; i++) {
    
        for (let j = 0; j < n-1; j++) {
            // Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]) {
                swap(a, j, j + 1);
                count++
            }
        }
    
    }
    
    console.log(`Array is sorted in ${count} swaps.`)
    console.log(`First Element: ${a[0]}`)
    console.log(`Last Element: ${a.pop()}`)

}
