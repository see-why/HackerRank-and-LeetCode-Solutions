//https://www.hackerrank.com/challenges/frequency-queries/problem?isFullScreen=true

function freqQuery(queries) {    
    let value_counts = {}
    let frequency_map = {}
    let result = []
    
    queries.forEach(([type, value]) => {
        switch(type){
            case 1:
                if(frequency_map[value_counts[value]] && frequency_map [value_counts[value]] > 0){
                    frequency_map[value_counts[value]] -= 1
                }
                value_counts[value] = value_counts[value] ? value_counts[value] + 1 : 1
                 if(frequency_map[value_counts[value]]){
                    frequency_map[value_counts[value]] += 1
                } else{
                    frequency_map[value_counts[value]] = 1
                }
                break;
            case 2:
                 if(frequency_map[value_counts[value]] && frequency_map [value_counts[value]] > 0){
                    frequency_map[value_counts[value]] -= 1
                }
                 value_counts[value] = value_counts[value] ? value_counts[value] - 1 : 0
               if(frequency_map[value_counts[value]]){
                    frequency_map[value_counts[value]] += 1
                } else{
                    frequency_map[value_counts[value]] = 1
                }
                break;
            case 3:
                result.push(frequency_map[value] > 0 ? 1:0)
                break;
            default:
                break;
        }
    })
    
    return result

}
