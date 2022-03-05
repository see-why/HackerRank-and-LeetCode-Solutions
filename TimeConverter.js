function timeConversion(s) {
    // Write your code here
    const timePeriod = s.substring(s.length - 2,s.length);
    const everthingElse = s.substring(2,s.length - 2);
    let hour = s.substring(0,2);
    
    hour = parseInt(hour);
    
    if (timePeriod == "AM" && hour == 12){
        hour = "00"
    }
    else if (timePeriod == "PM" && hour == 12){
        hour = "12"
    }
    else if(timePeriod == "PM"){
        hour += 12;
    }else if(timePeriod == "AM") {
        hour = '0'+ hour
    }
    
    return hour + everthingElse;
}
