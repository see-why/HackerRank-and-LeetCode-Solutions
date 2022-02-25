//https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true


function acmTeam(topic) {
    // Write your code here    
    function count_ones(str, str2) {
        let count = 0
       for(let i=0; i<str.length; i++){
          if(str[i] == 1) {
              count++
          } else if (str2[i] == 1){
              count++
          }
       }
        return count
    };
    
    let max = 0
    let teams = 0
    let max_index = topic.length - 1
    
    for (let i=0; i < max_index; i++){
        for(let j=i+1; j<=max_index; j++){
            let ones = count_ones(topic[i], topic[j])
            
            if (ones > max){
                teams = 0
                max = ones
            }
            
            if (ones == max){
                teams++
            }
            
        }
    }

    return [max, teams]
}
