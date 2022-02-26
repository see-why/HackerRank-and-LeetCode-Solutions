//https://www.hackerrank.com/challenges/js10-date/problem?isFullScreen=true

function getDayName(dateString) {
    let dayName;
    // Write your code here
    let new_date = new Date(dateString)
    let date_array = new_date.toString().split(' ')
    
    if (date_array[0] == 'Wed'){
        dayName = 'Wednesday'
    } else if (date_array[0] == 'Sat') {
        dayName = 'Saturday'
    } else if (date_array[0] == 'Thu') {
        dayName = 'Thursday'
    } else {
        dayName = date_array[0] + 'day'
    }
    
    return dayName;
}
