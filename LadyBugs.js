//https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true

//https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true

function happyLadybugs(b) {
    // Write your code here
    let dict = {}
    for(let i=0; i<b.length; i++){
        if(dict[b[i]]){
            dict[b[i]] += 1
        } else {
            dict[b[i]] = 1
        }
    }
    
    let happy = true
    Object.keys(dict).map((key) => {
        if(key != "_" && dict[key] == 1){
            happy = false
        }
    })
    
    if(dict['_'] > 0 && happy == true){
        happy = true
    } else{
        let pair = 0
        for(let i=0; i<b.length-1; i++){ 
            if(b[i] == b[i+1]){
                pair++
            } else if(pair > 0){
                pair = 0
            }else {
                happy = false
            }
        }
    }
    
    return happy ? "YES" : "NO"
}
